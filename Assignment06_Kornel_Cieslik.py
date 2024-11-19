# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Kornel Cieslik, 11/8/2024, Created Script
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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

menu_choice: str = ""
students: list = []
student_data: dict = {}

class FileProcessor:
    """
        Series of functions to work with JSON files.

        ChangeLog: (Who, When, What)
        Kornel Cieslik, 11/13/24, created the class
        """

    # This function exists to read the information from the json file from the student_data list
    @staticmethod
    def read_data_from_file(file_name: str, students: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

              ChangeLog: (Who, When, What)
              Kornel Cieslik,11.3.2024, function creation

              :parameter file_name: string name with the file to read from
              :parameter students: list of dictionary rows to be filled

              :return: list
              """

        try:
            with open(file_name, "r") as file:
                students = json.load(file)
                print(students)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a general non-specific error", e)
        return students


    @staticmethod
    def write_data_to_file(file_name: str, students: list):
        """ This function reads writes data the student_data list to the JSON file

                     ChangeLog: (Who, When, What)
                     Kornel Cieslik,11.3.2024, function creation

                     :parameter file_name: string name with the file to read from
                     :parameter student_data: list of dictionary rows to be filled

                     :return: list
                     """
        try:
            with open(file_name, "w") as file:
                json.dump(students, file)
            IO.output_student_courses(students = students)
        except TypeError as e:
            print("Please ensure that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        return students


class IO:
    """
           This class deals with the user inputs and the data outputs.

           ChangeLog: (Who, When, What)
           Kornel Cieslik, 11/13/24, created the class
           """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
                 This function outputs errors to the user

                 ChangeLog: (Who, When, What)
                 Kornel Cieslik, 11/13/24, created the class
             """
        print(message, end="\n\n")
        if error is not None:
            print("--- Technical Error Message ---")
            print(error, error.__doc__, type(error), sep = "\n")


    @staticmethod
    def output_menu(menu:str):
        """
                  This function prints out the menu to the user

                  ChangeLog: (Who, When, What)
                  Kornel Cieslik, 11/13/24, created the class
                  """
        # Present the menu of choices
        print(MENU)


    @staticmethod
    def input_menu_choice():
        """
                  This function provides prompts for the user to select menu options

                  ChangeLog: (Who, When, What)
                  Kornel Cieslik, 11/13/24, created the class
                  """
        while True: #while loop ensures that choice always is initialized with a user input value
            try:
                choice = input("Enter your menu choice number: ")
                if choice not in ("1", "2", "3", "4"): #strings
                    raise Exception("Please enter a value between 1 and 4")
                return choice
            except ValueError as e:
                IO.output_error_messages(e.__str__())


    @staticmethod
    def input_student_data(students: list):
        """
                  This function prompts the user for student information

                  ChangeLog: (Who, When, What)
                  Kornel Cieslik, 11/13/24, created the class
                  """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should only contain letter characters")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should only contain letter characters")
            course_name = input("Please enter the name of the course: ")

            #creating a dictionary for student information
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}

            #appending to student_data list
            student_data.append(student)
            print() #extra space for cleaner look
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            # Prints out various error messages depending on the error that occurs
        except ValueError as e:
            IO.output_error_messages("Please ensure that you are entering letter characters!")
        except Exception as e:
            IO.output_error_messages("Incorrect type of data!")
        return students

    @staticmethod
    def output_student_courses(students: list):
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# This will be the main body. Code below will be partitioned into functions to clean the code up
while True:

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()
    print()
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(students = students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, students = students)
        continue

    elif menu_choice == "4":
        print("Program Terminated...")
        break
    else:
        print("Please choose option 1, 2, or 3")



