/**
 * Name: Jonathan Lam
 * Student ID: 500792483
 */

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;


/**
 * The Appointment program creates a new appointment given date and description
 * In addition, it allows for the user to sort appointments by time and check for conflicts
 * @author Jonathan Lam (500792483)
 */
public class Appointment implements Comparable<Appointment>
{
	private Calendar date;
	private String description;
	private SimpleDateFormat sdf;
	private Person person;
	
	/**
	 * Appointment(year, month, day, hour, minute, desc, person) creates a new Appointment object
	 * @param year - year date of Appointment
	 * @param month - month date of Appointment
	 * @param day - day of month of Appointment
	 * @param hour - hour of Appointment
	 * @param minute - minute of Appointment
	 * @param desc - description of Appointment
	 * @param person - Person of Appointment 
	 */
	public Appointment(int year, int month, int day, int hour, int minute, String desc, Person person)
	{
		date = new GregorianCalendar(year,month,day,hour,minute);
		sdf = new SimpleDateFormat("H:mm ");
		description = desc;
		this.person = person;
	}
	
	/**
	 * getPerson() returns the person object
	 * @return person
	 */
	public Person getPerson()
	{
		return person;
	}
	
	/**
	 * getDescription() returns the appointment description
	 * @return description
	 */
	public String getDescription()
	{
		return description;
	}
	
	/**
	 * getDate() returns the date of type Calendar
	 * @return date of type Calendar for the Appointment
	 */
	public Calendar getDate()
	{
		return date;
	}
	
	/**
	 * toString() returns a formatted string
	 * @return the desired string output
	 */
	public String toString()
	{
		return (sdf.format(date.getTime()) + description);
	}
	
	/**
	 * occursOn(year, month, day, hour, min) checks to see if date matches given parameters
	 * @param year - year of date
	 * @param month - month of date
	 * @param day - day_of_month of date
	 * @param hour - hour of date
	 * @param min - minute of date
	 * @return a boolean: true if found or false if not found
	 */
	public boolean occursOn(int year, int month, int day, int hour, int min)
	{
		Calendar date = new GregorianCalendar(year, month, day, hour, min);
		return (this.date.equals(date));
	}
	
	/**
	 * compareTo(appt) compares this with another object of type Appointment
	 * @param appt - appointment object to compare
	 */
	public int compareTo(Appointment appt)
	{
		return date.compareTo(appt.date);
	}
}




