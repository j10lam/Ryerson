Name: Jonathan Lam
Student ID: 500792483

Note: All intended features outlined in the assignment and shown in the exemplar work in my program including all bonus tasks.

The program Appointment Frame produces a GUI which allows the user to create, cancel, recall, and show appointments based on specific dates. Also allows the user to search for individuals in a contacts list. Furthermore, the user can access specific dates to view set appointments by using the monthView buttons show in a calendar format.

Main Text Area:
1. Shows all created appointments for current date

Date Subpanel:
1. Pressing arrow buttons increments/decrements current date by one day
2. Entering desired day, month and year and then pressing the show button displays all created appointments for desired date

Appointment Subpanel:
1. Entering desired Hour and Minute and then pressing the create button will create a new appointment under current date if available
	a. If desired time is not available - Displayed “CONFLICT!!” to Description sub-panel TextArea
2. Pressing cancel button deletes any appointment set at desired time if any.
3. Pressing recall button, the last appointment made is printed (calendar changes to date of appointment, hour & minute fields are filled again)

monthView Subpanel:
1. Shows the number of days in the current month in the form of buttons
2. Allows the user to press a button to change to a specific day in the month
3. Pressing << or >> , decrements or increments the month respectively
4. Current day button is highlighted in red
5. Any day of the month which has appointments set are highlighted in grey.
NOTE: for compatibility reasons: in Mac OS in order for the set background color to be filled completely, setBorderPainted(false) must be set for each ViewButton.

Contact Subpanel
1. Allows the user to enter partial information in the given fields to search for a contact in the contacts linked list
	a. If a Person contains information matching to filled fields, the rest of the fields in the sub panel are filled.
2. Uses manually filled or automatically filled (via. find button) textfields to create a Person and placed in appointment to be created

Description Subpanel
1. Allows user to enter descriptions for appointments
2. Shows any exception handling information if errors were to occur
	a. if hour or minutes is set out of typical bounds for a typical day (i.e.: if min = 61 -> Exception)
	b. if month, year is set outside of typical bounds (i.e.: if month > 12 -> Exception)
	c. if day set is outside max number of days for current month (i.e.: if mo = feb, day = 30 -> Exception)
	d. When reading contacts.txt exception is thrown when:
		i. if file cannot be read
		ii. if first line does not contain a valid integer
		iii. if the number of lines is not a multiple of 5
		iv. if last name or email of a person is blank.



Note: All intended features outlined in the assignment and shown in the exemplar work in my program including all bonus tasks.