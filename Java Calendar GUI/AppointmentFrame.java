/**
 * Name: Jonathan Lam
 * Student ID: 500792483
 */

import java.text.SimpleDateFormat;

import java.io.FileNotFoundException;

import java.util.Calendar;
import java.util.Collections;
import java.util.GregorianCalendar;
import java.util.InputMismatchException;
import java.util.Stack;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JScrollPane;
import javax.swing.BorderFactory;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;

/**
 * The AppointmentFrame program creates a GUI which allows the user to create, view, recall,
 * and cancel appointments
 * In addition, the monthView panel allows the user to view appointments on different days of
 * the month
 * Further, the program lets the user find contact information using partially filled in information
 * if present in the Contacts list.
 * @author Jonathan Lam (500792483)
 */
@SuppressWarnings("serial")
public class AppointmentFrame extends JFrame 
{
	private JPanel controlPanel;
	private JLabel date;
	private JTextArea text;
	private JLabel currMonth;
	private SimpleDateFormat sdf;
	private SimpleDateFormat sdfmonth;
	private Calendar today;
	private Calendar previous;
	private ActionListener listener;
	private Contacts contacts;
	private Stack<Appointment> stack;
	private ArrayList<Appointment> appointments;
	
	//datePanel
	private JButton left;
	private JButton right;
	private JButton show;
	private JTextField day;
	private JTextField month;
	private JTextField year;
	
	//appointmentPanel
	private JButton create;
	private JButton cancel;
	private JButton recall;
	private JTextField hour;
	private JTextField minute;
	
	//calendarPanel
	private ArrayList<ViewButton> buttons;
	private JPanel monthView;
	private JButton prev;
	private JButton next;
	
	//contactPanel
	private JButton find;
	private JButton clear;
	private JTextField last;
	private JTextField first;
	private JTextField tel;
	private JTextField email;
	private JTextField address;
	
	//descriptionPanel
	private JTextArea description;

	/**
	 * AppointmentFrame() constructs an Appointment Frame object
	 */
	public AppointmentFrame() 
	{
		sdf = new SimpleDateFormat("EEE, MMM dd, yyyy");
		sdfmonth = new SimpleDateFormat("MMM");
		today = new GregorianCalendar();
		previous = (Calendar) today.clone();
		contacts = new Contacts();
		stack = new Stack<Appointment>();
		appointments = new ArrayList<Appointment>();
		
		setSize(1000,800);
		createComponents();
		loadContacts();
	}
	
	/**
	 * createComponents() creates various components and adds
	 * it to the frame
	 */
	public void createComponents()
	{
		controlPanel = new JPanel();
		monthView = new JPanel();
		text = new JTextArea(50,200);
		JScrollPane scroll = new JScrollPane(text);
		listener = new ButtonListener();
		
		monthView.setLayout(new GridLayout(0,7));
		controlPanel.setLayout(new GridLayout(3,2));
		
		controlPanel.add(scroll); 
		calendarPanel();	
		controlPanel.add(monthView);
		datePanel(); 
		contactPanel();
		appointmentPanel(); 
		descPanel();
		headerPanel();
		add(controlPanel, BorderLayout.CENTER);
	}
	
	/**
	 * headerPanel() creates the formatted dates to be shown
	 * at the top of the program
	 * In addition, creates two buttons to change monthView monthView
	 */
	public void headerPanel()
	{
		JPanel labels = new JPanel();
		JPanel calendarHeader = new JPanel();
		date = new JLabel(sdf.format(today.getTime()));
		currMonth = new JLabel(sdfmonth.format(today.getTime()), SwingConstants.CENTER);
		prev = new JButton("<<");
		next = new JButton(">>");
		
		labels.setLayout(new GridLayout(1,2));
		calendarHeader.setLayout(new BorderLayout());
		prev.addActionListener(listener);
		next.addActionListener(listener);
		
		calendarHeader.add(prev, BorderLayout.WEST);
		calendarHeader.add(currMonth, BorderLayout.CENTER);
		calendarHeader.add(next, BorderLayout.EAST);
		labels.add(date);
		labels.add(calendarHeader);
		add(labels, BorderLayout.NORTH);
	}

	/**
	 * datePanel() creates the date sub panel of controlPanel
	 */
	public void datePanel()
	{
		JPanel panel = new JPanel();
		JPanel top = new JPanel();
		JPanel middle = new JPanel();
		JPanel bottom = new JPanel();
		
		left = new JButton("<");
		right = new JButton(">");
		show = new JButton("Show");
		
		JLabel day = new JLabel("Day");
		JLabel month = new JLabel("Month");
		JLabel year = new JLabel("Year");
		
		this.day = new JTextField(2);
		this.month = new JTextField(2);
		this.year = new JTextField(4);
		
		left.addActionListener(listener);
		right.addActionListener(listener);
		show.addActionListener(listener);
		
		panel.setLayout(new GridLayout(3,1));
		panel.setBorder(BorderFactory.createTitledBorder("Date"));

		top.add(left);
		top.add(right);
		middle.add(day);
		middle.add(this.day);
		middle.add(month);
		middle.add(this.month);
		middle.add(year);
		middle.add(this.year);
		bottom.add(show);
		panel.add(top);
		panel.add(middle);
		panel.add(bottom);
		controlPanel.add(panel);
	}
	
	/**
	 * appointmentPanel() creates the appointment sub panel of controlPanel
	 */
	public void appointmentPanel()
	{
		JPanel panel = new JPanel();
		JPanel top = new JPanel();
		JPanel bottom = new JPanel();
		
		create = new JButton("CREATE");
		cancel = new JButton("CANCEL");
		recall = new JButton("RECALL");
		
		JLabel hour = new JLabel("Hour");
		JLabel minute = new JLabel("Minute");
		
		this.hour = new JTextField(4);
		this.minute = new JTextField(4);
		
		create.addActionListener(listener);
		cancel.addActionListener(listener);
		recall.addActionListener(listener);
		
		panel.setLayout(new GridLayout(2,1));
		panel.setBorder(BorderFactory.createTitledBorder("Appointment"));
		
		top.add(hour);
		top.add(this.hour);
		top.add(minute);
		top.add(this.minute);
		bottom.add(create);
		bottom.add(cancel);
		bottom.add(recall);
		panel.add(top);
		panel.add(bottom);
		controlPanel.add(panel);
	}
	
	/**
	 * calendarPanel() creates the monthView sub panel of controlPanel
	 */
	public void calendarPanel()
	{
		buttons = new ArrayList<ViewButton>();
		Calendar firstDay = (Calendar) today.clone();
		String[] days = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};	
		
		firstDay.set(Calendar.DAY_OF_MONTH, 1);
		
		int num_days = firstDay.getActualMaximum(Calendar.DAY_OF_MONTH);
		int offset = firstDay.get(Calendar.DAY_OF_WEEK) - 1;
		
		for (String day : days)
		{
			monthView.add(new JLabel(day));
		}
		
		for (int o = 0; o < offset; o++)
		{
			monthView.add(new JLabel(""));
		}
		
		for (int n = 1; n <= num_days; n++)
		{
			ViewButton button = new ViewButton(n);
			buttons.add(button);
			monthView.add(button);
		}
		
		setColors();
		
	}

	/**
	 * contactPanel() creates the contact sub panel of controlPanel
	 */
	public void contactPanel()
	{
		JPanel panel = new JPanel();
		JPanel buttons = new JPanel();
		JPanel top = new JPanel();
		JPanel bottom = new JPanel();
		
		find = new JButton("Find");
		clear = new JButton("Clear");
		
		JLabel last = new JLabel("Last Name");
		JLabel first = new JLabel("First Name");
		JLabel tel = new JLabel("tel");
		JLabel email = new JLabel("email");
		JLabel address = new JLabel("address");
		
		this.last = new JTextField(8);
		this.first = new JTextField(8);
		this.tel = new JTextField(8);
		this.email = new JTextField(8);
		this.address = new JTextField(8);
		
		find.addActionListener(listener);
		clear.addActionListener(listener);
		
		panel.setLayout(new BorderLayout());
		top.setLayout(new GridLayout(4,2));
		bottom.setLayout(new GridLayout(3,1));
		panel.setBorder(BorderFactory.createTitledBorder("Contact"));
		
		top.add(last);
		top.add(first);
		top.add(this.last);
		top.add(this.first);
		top.add(tel);
		top.add(email);
		top.add(this.tel);
		top.add(this.email);

		bottom.add(address);
		bottom.add(this.address);
		bottom.add(buttons);
		buttons.add(find);
		buttons.add(clear);
		panel.add(top, BorderLayout.NORTH);
		panel.add(bottom, BorderLayout.CENTER);
		controlPanel.add(panel);
	}
	
	/**
	 * descPanel() creates the description TextArea of controlPanel
	 */
	public void descPanel()
	{
		JPanel panel = new JPanel();
		description = new JTextArea(5,25);
		
		panel.setBorder(BorderFactory.createTitledBorder("Description"));
		
		panel.add(description, BorderLayout.NORTH);
		controlPanel.add(panel);
	}

	/**
	 * updateComponents() updates certain components in the frame
	 * such as: changing labels for date, changing monthView, etc.
	 */
	public void updateComponents()
	{
		Collections.sort(appointments);
		currMonth.setText(sdfmonth.format(today.getTime()));
		date.setText(sdf.format(today.getTime()));
		
		if ((previous.get(Calendar.MONTH) != today.get(Calendar.MONTH)) || 
				(previous.get(Calendar.YEAR) != today.get(Calendar.YEAR)))
		{
			previous = (Calendar) today.clone();
			monthView.removeAll();
			calendarPanel();
			monthView.repaint();
		}
		
		setColors();
		printAppointments();
	}

	/**
	 * setColor() sets the JButton background colors in monthView sub panel
	 * Current day JButton is set to red
	 * Any day of the month with appointments is set to grey
	 */
	public void setColors()
	{
		int prevDay = previous.get(Calendar.DAY_OF_MONTH);
		int currDay = today.get(Calendar.DAY_OF_MONTH);
		
		for (Appointment a : appointments)
		{
			int day = a.getDate().get(Calendar.DAY_OF_MONTH);
			int month = a.getDate().get(Calendar.MONTH);
			ViewButton b = buttons.get(day - 1);
			
			if (month == today.get(Calendar.MONTH))
			{
				b.setGray();					
			}
			else
			{
				b.resetColor();
			}
		}
		
		if ((buttons.get(prevDay - 1)).getBackground() != Color.LIGHT_GRAY)
		{
			(buttons.get(prevDay - 1)).resetColor();
		}
		(buttons.get(currDay - 1)).setRed();
	}
	
	/**
	 * clearFields() clears all JTextFields in Action and Description sub-panels
	 */
	public void clearFields()
	{
		hour.setText("");
		minute.setText("");
		description.setText("");
	}
	
	/**
	 * printAppointment() outputs to JTextArea all appointments that match current date
	 */
	public void printAppointments() 
	{
		text.setText("");
		String temp = "";
		for (Appointment a : appointments)
		{
		
			if ((a.getDate().get(Calendar.YEAR) == today.get(Calendar.YEAR))
			&& (a.getDate().get(Calendar.MONTH) == today.get(Calendar.MONTH))
			&& (a.getDate().get(Calendar.DAY_OF_MONTH) == today.get(Calendar.DAY_OF_MONTH)))
			{
				if (!a.getPerson().getInfo(1).isEmpty() && !a.getPerson().getInfo(0).isEmpty())
				{
					temp = a.getPerson().getInfo(1) + " " + a.getPerson().getInfo(0) + " " + a.getPerson().getInfo(2) + " " + a.getPerson().getInfo(4);
					temp.replaceAll("\\s+", " ");
					if (!temp.trim().isEmpty())
					{
						temp = " WITH: " + temp;
					}
				}
				
				text.append(a.toString() + temp + "\n");
				text.append("\n");
			}
		}
	}
	
	/**
	 * findAppointment(y, mo, d, h, m)
	 * returns an appointment if any that matches given parameters
	 * @param y year of date
	 * @param mo month of date
	 * @param d day_of_month of date
	 * @param h hour of date 
	 * @param m minute of date
	 * @return object of type Appointment if found otherwise, null
	 */
	public Appointment findAppointment(int y, int mo, int d, int h, int m)
	{
		Appointment appt = null;
		
		for (Appointment a : appointments)
		{
			if (a.occursOn(y, mo, d, h, m)) 
			{
				appt = a;
				break;
			}
		}
		return appt;
	}
	
	/**
	 * createAppointment(y, mo, d, h, m, appt, person)
	 * creates a new appointment if no existing appointments at specified date
	 * and refreshes JTextArea with new appointments
	 * otherwise outputs to description panel - "CONFLICT!!"
	 * @param y year of date
	 * @param mo month of date
	 * @param d day_of_month of date
	 * @param h hour of date
	 * @param m minute of date
	 * @param appt output of findAppointment
	 */
	public void createAppointment(int y, int mo, int d, int h, int m, Appointment appt, Person person)
	{
		if (appt == null) 
		{
			Appointment a = new Appointment(y, mo, d, h, m, description.getText(), person);
			stack.push(a); 
			appointments.add(a);
			clearFields();
		}
		else
		{
			description.setText("CONFLICT!!");
		}
	}
	
	/**
	 * cancelAppointment(appt) removes existing appointment if any
	 * @param appt output of findAppointment 
	 */
	
	public void cancelAppointment(Appointment appt)
	{
		if (appt != null)
		{
			appointments.remove(appt);
			stack.remove(appt);

			text.setText("");
		}
		clearFields();
	}
	
	/**
	 * loadContacts() scans file and adds Persons to a LinkedList
	 */
	public void loadContacts()
	{
		try
		{
			contacts.readContactsFile();
		}
		catch(FileNotFoundException e)
		{
			description.setText("No file found");
		}
		catch(InputMismatchException e)
		{
			description.setText("Not a valid integer");
		}
		catch(IllegalArgumentException e)
		{
			description.setText(e.getMessage());
		}
	}
		
	/**
	 * changeDate() changes the current calendar date info using
	 * information from the given fields if no exceptions are found
	 */
	public void changeDate()
	{
		int yf = Integer.parseInt(year.getText());
		int mf = Integer.parseInt(month.getText()) - 1;
		int df = Integer.parseInt(day.getText());
		
		try
		{
			if (yf >= today.getActualMinimum(Calendar.YEAR))
			{
				today.set(Calendar.YEAR, yf);
			}
			else
			{
				throw new IllegalArgumentException("Invalid Year Entry");
			}
			
			if (mf >= 0 && mf < 12)
			{
				today.set(Calendar.MONTH, mf);
			}
			else
			{
				throw new IllegalArgumentException("Invalid Month Entry");
			}
			
			if (df >= 1 && df <= today.getActualMaximum(Calendar.DAY_OF_MONTH))
			{
				today.set(Calendar.DAY_OF_MONTH, df);
			}
			else
			{
				throw new IllegalArgumentException("Invalid Day Entry");
			}
			description.setText("");
		}
		catch (IllegalArgumentException exception)
		{
			today = (Calendar) previous.clone();
			description.setText(exception.getMessage());
		}
	}
	
/**
 * 	The ButtonListener class provides information on what each specific button
 *  that implements ButterListener should do when pressed
 */
private class ButtonListener implements ActionListener
	{
		/**
		 * actionPerformed(event) performs a series of operations depending on
		 * which JButton object was activated
		 * @param event - type of event
		 */
		public void actionPerformed(ActionEvent event)
		{
			Object src = event.getSource();
			Person person;
			Appointment appt;
			
			previous = (Calendar) today.clone();

			String l = last.getText();
			String f = first.getText();
			String t = tel.getText();
			String a = address.getText();
			String e = email.getText();
									
			if (src == left)
			{
				today.add(Calendar.DAY_OF_MONTH, -1);
			}
			else if (src == right)
			{
				today.add(Calendar.DAY_OF_MONTH, +1);
			}
			else if (src == show)
			{
				changeDate();
			}
			else if (src == find)
			{
				person = contacts.findPerson(l, f, t, a, e);
				
				if (person != null)
				{
					last.setText(person.getInfo(0));
					first.setText(person.getInfo(1));
					tel.setText(person.getInfo(2));
					address.setText(person.getInfo(3));
					email.setText(person.getInfo(4));
				}
			}
			else if (src == clear)
			{
				last.setText("");
				first.setText("");
				tel.setText("");
				address.setText("");
				email.setText("");
			}
			else if (src == recall)
			{
				appt = stack.peek();
				today.setTime(appt.getDate().getTime());
				hour.setText(Integer.toString(today.get(Calendar.HOUR_OF_DAY)));
				minute.setText(Integer.toString(today.get(Calendar.MINUTE)));
				description.setText(appt.getDescription());
			}
			else if (src == prev)
			{
				today.add(Calendar.MONTH, -1);
				today.set(Calendar.DAY_OF_MONTH, 1);
			}
			else if (src == next)
			{
				today.add(Calendar.MONTH, +1);
				today.set(Calendar.DAY_OF_MONTH, 1);
			}
			else
			{
				int y = today.get(Calendar.YEAR);
				int m = today.get(Calendar.MONTH);
				int d = today.get(Calendar.DAY_OF_MONTH);
				
				try
				{
					int h = Integer.parseInt(hour.getText());
					int min = (minute.getText().isEmpty()) ? 0 : Integer.parseInt(minute.getText());
					
					if (!(h >= 0 && h <= 23) || !(min >=0 && min <= 59))
					{
						throw new IllegalArgumentException("Invalid time given");
					}
					
					appt = findAppointment(y, m, d, h, min);
					
					if (src == create)
					{
						person = new Person(l, f, t, a, e);
						createAppointment(y, m, d, h, min, appt, person);
					}
					else
					{
						cancelAppointment(appt);
					}
				}
				catch (IllegalArgumentException exception)
				{
					description.setText(exception.getMessage());
				}
			}
			updateComponents();
		}
	}


/**
 * The ViewButton extends JButton and creates buttons specific to
 * the monthView panel
 */
private class ViewButton extends JButton implements ActionListener
	{
		private int day;
		private Color color;
		
		/**
		 * ViewButton(day) constructs a new ViewButton object
		 * @param day - day of the month
		 */
		public ViewButton(int day)
		{
			this.day = day;
			
			setText(Integer.toString(day));
			addActionListener(this);
			setOpaque(true);
			setBorderPainted(true);
		}
		
		/**
		 * setRed() sets the background of ViewButton to Red
		 */
		public void setRed()
		{
			setBackground(Color.RED);
		}
		
		/**
		 * setGray() sets the background of ViewButton to Gray
		 */
		public void setGray()
		{
			setBackground(Color.LIGHT_GRAY);
		}
		
		/**
		 * resetColor() resets the background of ViewButton
		 */
		public void resetColor()
		{
			setBackground(color);
		}
		
		/**
		 * actionPerformed(event) changes the current day depending
		 * on which ViewButton was activated
		 * @param event - type of event
		 */
		public void actionPerformed(ActionEvent event)
		{
			previous = (Calendar) today.clone();
			
			today.set(Calendar.DAY_OF_MONTH, this.day);
			updateComponents();
		}
	}

}

