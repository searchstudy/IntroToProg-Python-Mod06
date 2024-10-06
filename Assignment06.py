# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: Using constants, variables, print statements to display msgs
# about student registration with functions and classes.
# Max Mikos, Sept25, 2024, Created Script
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# store data in json
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ""  # Hold the choice made by the user
students: list = []  # a table of student data

csv_data: str = ""  # Holds combined string data separated by a comma.
json_data: str = ""  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.

student_data: dict = {}  # one row of student data
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    I'm using the provided starter assignment code for assignment 6 and 7 to guide me.
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            student_data.extend(json.load(file))
            file.close()
        except Exception as e:
            IO.output_error_messages(message = "Error: There was a problem with reading the file.", error = e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be written to the file

        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data = student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program.\n"
            IO.output_error_messages(message = message, error = e)
        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        :return: None
        """
        print() # Adding extra space to make it look nicer.
        print(menu)
        print() # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("What would you like to do?\n Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4!")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod 
    def output_student_courses(student_data: list):
        """ This function displays the student and course names to the user

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 51) #prints 51 hyphens ---
        for student in student_data:
            print(f"Student {student['FirstName']} "
                  f"{student['LastName']} is enrolled in {student['CourseName']}")
        print("-" * 51)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The First name should not contain numbers or be empty!")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The Last name should not contain numbers or be empty!")
            student_course_name = input("Please enter the name of the course: ")
            if not student_course_name.strip():
                raise ValueError("The Course name should not be empty!")

            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": student_course_name}
            student_data.append(student)
            
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {student_course_name}.")
        except ValueError as e:
            IO.output_error_messages(message = "One of the values was the correct type of data!", error = e)
        except Exception as e:
            IO.output_error_messages(message = "Error: There was a problem with your entered data.", error = e)
        return student_data


# Extract the data from file into the students list from above
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")

    students = json.load(file)

    file.close()
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in a json format.")
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
finally:
    if file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Please enter your choice number here: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")

            json.dump(students, file) #w/ dump() function, app writes contents of the students variable to the file 
            # closing the file after dump()
            file.close()
            
            print("\nThe following data was saved to file!\n")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if not file.closed:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended! \nYou may close this window.")

