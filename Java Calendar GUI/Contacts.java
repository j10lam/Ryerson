/**
 * Name: Jonathan Lam
 * ID: 500792483
 *
 */

import java.util.LinkedList;
import java.util.Collections;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


/**
 * The Contacts class creates a LinkedList which holds Person objects and allows
 * the user to find a Person in the list that was created from a text file containing
 * contact information 
 * @author Jonathan Lam (500792483)
 */
public class Contacts 
{
	private LinkedList<Person> list;
	
	/**
	 * Contacts() constructs a Contacts object
	 */
	public Contacts()
	{
		list = new LinkedList<Person>();
	}
	
	/**
	 * findPerson(last, first, tel, address, email) finds object in list which contains
	 * given arguments
	 * @param last - last name of possible person
	 * @param first - first name of possible person
	 * @param tel - telephone of possible person
	 * @param address - address of possible person
	 * @param email - email of possible person
	 * @return a Person if found, else null
	 */
	public Person findPerson(String last, String first, String tel, String address, String email)
	{
		Person person = new Person(last, first, tel, address, email);
		int index = 0;
		
		for (Person p : list)
		{
			if ((!last.isEmpty()) && (!first.isEmpty()))
			{
				index = Collections.binarySearch(list, person);
			}
			else if (!tel.isEmpty())
			{
				index = Collections.binarySearch(list, person, p.new TelComparator());
			}
			else
			{
				index = Collections.binarySearch(list, person, p.new EmailComparator());
			}
		}
		
		if (index >= 0)
		{
			return list.get(index);
		}
		return null;
	}
	
	/**
	 * readContactsFile() creates Person objects from file and adds onto list
	 * if no exceptions are thrown
	 * @throws FileNotFoundException
	 */
	public void readContactsFile() throws FileNotFoundException
	{
		File file = new File("contacts.txt");
		Scanner in = new Scanner(file);
		int count = 0;
		
		in.nextInt();
		in.nextLine();
		while (in.hasNextLine())
		{
			count++;
			in.nextLine();
		}
		in.close();

		if (count % 5 != 0)
		{
			throw new IllegalArgumentException("Indivisible by 5");
		}
	
		in = new Scanner(file);
		in.nextLine();
		while (in.hasNextLine())
		{
			String last = in.nextLine();
			String first = in.nextLine();
			String tel = in.nextLine();
			String address = in.nextLine();
			String email = in.nextLine();
			
			list.add(new Person(last, first, tel, address, email));
			
			if (last.isEmpty() || email.isEmpty())
			{
				in.close();
				list.clear();
				throw new IllegalArgumentException("Empty");
			}
		}
		
		in.close();
		Collections.sort(list);
	}
}


