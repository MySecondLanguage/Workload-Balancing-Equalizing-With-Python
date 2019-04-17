# Workload Equalizing System.

** I have written this program for my agentenine client **

The Requirement was:

A python script that arranges names over the calendar and assigns the names of the employees who are on duty with the following criteria:

• This is an on duty database that for every day has 3 names according to priority the first name will be the first to call the second name will have the second call and the third name will have the last call. Each employee is unique, therefore cannot repeat the same name on the same day.

• This project is to populate the database of the whole year with the names according to the criteria

• There are 3 categories of employees the X group employees the Y and Z.

• There are X employees that needs to have the highest priority therefore the will be working equally for the whole month, and each one of them have equal priority.

• There are Y employees that needs to work equally that has second priority and will be getting the first calls after each one of the X employees has finished their equally days of work

• There are Z employees that needs to be always on the second call or the third call and they will be getting their days of work equally over the month.

• There will be an option to put some of the X employees for the second call.

• Since the workload of the Y an Z cannot be the perfectly same the whole month (months of 28 days and months of 31 days), the script must be able to take into account how many days of work they have been working of the previous month and compensate this the following month.

• By the end of the year the days of work of each of the Y and Z must be approximately equal days regardless of the priority during the day.

The script must be able to load the database of the X Y and Z employees from a csv file, then will provide the option to put the X employees also in second call and the user must input the start date and the end date of the database to generate, and then output each month in a csv file with rows being the date and 3 columns with each one of the names.
