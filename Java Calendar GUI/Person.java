/**
 * Name: Jonathan Lam
 * ID: 500792483
 *
 */

import java.util.Comparator;


/**
 * This Class creates a Person object with contact information,
 * retrieves contact information, and compares arguments with 
 * other Person objects 
 * @author Jonathan Lam (500792483)
 */
public class Person implements Comparable<Person>
{
	private String lastName;
	private String firstName;
	private String telephone;
	private String address;
	private String email;
	
	/**
	 * Person(last, first, tel, address, email) constructs a Person object
	 * @param last - Last Name of individual
	 * @param first - First Name of individual
	 * @param tel - Telephone of individual
	 * @param address - Address of individual
	 * @param email - Email of individual
	 */
	public Person(String last, String first, String tel, String address, String email)
	{
		lastName = last;
		firstName = first;
		telephone = tel;
		this.address = address;
		this.email = email;
	}
	
	/**
	 * getInfo(choice) returns information corresponding to choice
	 * @param choice - designates which information is required
	 * @return one of (lastName, firstName, telephone, address, or email)
	 */
	public String getInfo(int choice)
	{
		if (choice == 0) {return lastName;}
		else if (choice == 1) {return firstName;}
		else if (choice == 2) {return telephone;}
		else if (choice == 3) {return address;}
		else {return email;}
	}
	
	/**
	 * toString() returns formatted string
	 * @return String
	 */
	public String toString()
	{
		return "Contact Information";
	}
	
	/**
	 * compareTo(other) compares lastName or firstName
	 * of this with other
	 * @param other - another Person object
	 * @return an integer (one of: -1, 0, 1)
	 */
	public int compareTo(Person other)
	{
		int result = (lastName).compareTo(other.lastName);
		if (result == 0)
		{
			result = (firstName).compareTo(other.firstName);
		}
		return result;
	}
	
	/**
	 * EmailComparator, which extends Comparator is used to compare
	 * the private instance variable: email, corresponding to two
	 * Person objects 
	*/
	public class EmailComparator implements Comparator<Person>
	{
		@Override
		
		/**
		 * compare(one, two) compares the email argument of 
		 * two Person Objects
		 * @param one - Person one
		 * @param two - Person two
		 * @return an integer corresponding to either: less than, equal to,
		 * or greater than
		 */
		public int compare(Person one, Person two)
		{
			return (one.email).compareTo(two.email);
		}
	}
	
	/**
	 * TelComparator, which extends Comparator is used to compare
	 * the private instance variable: telephone, corresponding to two
	 * Person objects 
	*/
	public class TelComparator implements Comparator<Person>
	{
		@Override
		/**
		 * compare(one, two) compares the telephone argument of 
		 * two Person Objects
		 * @param one - Person one
		 * @param two - Person two
		 * @return an integer corresponding to either: less than, equal to,
		 * or greater than
		 */
		public int compare(Person one, Person two)
		{
			return (one.telephone).compareTo(two.telephone);
		}
	}
}




