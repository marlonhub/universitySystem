import mysql.connector as mysql
# import prettytable library
from prettytable import PrettyTable
db = mysql.connect(host="localhost", user="root", password="", database="college")
command_handler = db.cursor(buffered=True)

def student_info():
     while 1:
        print("")
        print("Student Menu")
        print("1. Register New Student")
        print("2. Delete Existing Student")
        print("3. View Existing Student")
        print("4. Edit Existing Student")
        print("5. Logout")

        user_option = input(str("Option: "))

        # Create User
        if user_option == "1":
            print("")
            print("Register New Student")
            firstname = input(str("Student First Name: " ))
            lastname = input(str("Student Last Name: " ))
            address = input(str("Student Address: " ))
            phoneNum = input(str("Student Phone #: " ))
            email = input(str("Student Email: " ))
            dateofbirth = input(str("Student DOB: " ))
            querys_vals = (firstname,lastname,address,phoneNum,email,dateofbirth)
            command_handler.execute("INSERT INTO student (firstname,lastname,address,phoneNum,email,dateofbirth) VALUES (%s,%s,%s,%s,%s,%s )", querys_vals)
            db.commit()
            print(firstname + " has been registered as a student!")
            
            # Delete User by id
        elif user_option == "2":
            print("")
            print("Delete Existing Student Account")
            student_id = input(str("Student ID : "))
            query_vals = (student_id,)
            command_handler.execute("DELETE FROM student WHERE id = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Student not found")
            else:
                print("Student with ID " + student_id + " has been deleted")

            

        # View user
        elif user_option == "3":
            print("")
            print("View Existing Student Account")
            
            # execute SQL query to retrieve all student information
            command_handler.execute("SELECT id, firstname, lastname, address, phoneNum, email, dateofbirth FROM student")
            result = command_handler.fetchall()
            
            if len(result) < 1:
                print("No students found")
            else:
                # create a PrettyTable object and set the field names
                table = PrettyTable()
                table.field_names = ["ID", "First Name", "Last Name", "Address", "Phone #", "Email", "DOB"]
                
                # add each row of data to the table
                for row in result:
                    table.add_row(row)
                    
                # print the table
                print(table)
        
        # Edit user
        elif user_option == "4":
            print("")
            print("Edit Existing Student")
            student_id = input(str("Student ID : "))
            query_vals = (student_id,)
            command_handler.execute("SELECT * FROM student WHERE id = %s", query_vals)
            result = command_handler.fetchone()
            if result is None:
                print("Student not found")
            else:
                print("Current Information:")
                print(f"ID: {result[0]}")
                print(f"First Name: {result[1]}")
                print(f"Last Name: {result[2]}")
                print(f"Address: {result[3]}")
                print(f"Phone #: {result[4]}")
                print(f"Email: {result[5]}")
                print(f"DOB: {result[6]}")

                # get new values from user
                firstname = input(str("New First Name (press enter to keep current value): "))
                lastname = input(str("New Last Name (press enter to keep current value): "))
                address = input(str("New Address (press enter to keep current value): "))
                phoneNum = input(str("New Phone # (press enter to keep current value): "))
                email = input(str("New Email (press enter to keep current value): "))
                dateofbirth = input(str("New DOB (press enter to keep current value): "))

                # build SQL query and execute
                update_vals = ()
                update_cols = []
                if firstname != "":
                    update_cols.append("firstname = %s")
                    update_vals += (firstname,)
                if lastname != "":
                    update_cols.append("lastname = %s")
                    update_vals += (lastname,)
                if address != "":
                    update_cols.append("address = %s")
                    update_vals += (address,)
                if phoneNum != "":
                    update_cols.append("phoneNum = %s")
                    update_vals += (phoneNum,)
                if email != "":
                    update_cols.append("email = %s")
                    update_vals += (email,)
                if dateofbirth != "":
                    update_cols.append("dateofbirth = %s")
                    update_vals += (dateofbirth,)
                if len(update_cols) > 0:
                    update_cols_str = ", ".join(update_cols)
                    update_vals += (student_id,)
                    command_handler.execute(f"UPDATE student SET {update_cols_str} WHERE id = %s", update_vals)
                    db.commit()
                    print("Student information updated!")
                else:
                    print("No changes made")

        #Logout
        elif user_option == "5":
            auth_admin()
def course_info():
     while 1:
        print("")
        print("Course Menu")
        print("1. Register New Course")
        print("2. View Existing Course")
        print("3. Delete Existing Course")
        print("4. Edit Existing Course")
        print("5. Logout")

        user_option = input(str("Option: "))

    # Create User
        if user_option == "1":
            print("")
            print("Register New Course")
            courseid = input(str("Course ID: " ))
            courseName = input(str("Course Name: " ))
            courseInstructor = input(str("Course Instructor: " ))
            sTime = input(str("Start Time: " ))
            eTime = input(str("EndT Time: " ))
            roomNum = input(str("Room #: " ))
            querys_vals = (courseid, courseName, courseInstructor, sTime, eTime, roomNum)
            command_handler.execute("INSERT INTO course (courseid, courseName, courseInstructor, sTime, eTime, roomNum) VALUES (%s,%s,%s,%s,%s,%s )", querys_vals)
            db.commit()
            print(courseName + " has been registered as a course!")

       # View user
        elif user_option == "2":
            print("")
            print("View Existing Courses")
            
            # execute SQL query to retrieve all student information
            command_handler.execute("SELECT courseid, courseName, courseInstructor, sTime, eTime, roomNum FROM course")
            result = command_handler.fetchall()
            
            if len(result) < 1:
                print("No courses found")
            else:
                # create a PrettyTable object and set the field names
                table = PrettyTable()
                table.field_names = ["courseid", "courseName", "courseInstructor", "sTime", "eTime", "roomNum"]
                
                # add each row of data to the table
                for row in result:
                    table.add_row(row)
                    
                # print the table
                print(table)

          # Delete User by id
        elif user_option == "3":
            print("")
            print("Delete Existing Course ")
            course_id = input(str("Course ID : "))
            query_vals = (course_id,)
            command_handler.execute("DELETE FROM course WHERE courseid = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Course not found")
            else:
                print("Course with ID " + course_id + " has been deleted")

         # Edit user
        elif user_option == "4":
            print("")
            print("Edit Existing Course")
            course_id = input(str("Course ID : "))
            query_vals = (course_id,)
            command_handler.execute("SELECT * FROM course WHERE courseid = %s", query_vals)
            result = command_handler.fetchone()
            if result is None:
                print("Course not found")
            else:
                print("Current Information:")
                print(f"CourseID: {result[0]}")
                print(f"Course Name: {result[1]}")
                print(f"Course Instructor: {result[2]}")
                print(f"Start Time: {result[3]}")
                print(f"End Time: {result[4]}")
                print(f"Room #: {result[5]}")
                

                # get new values from user
                courseid = input(str("New Course ID (press enter to keep current value): "))
                courseName = input(str("New Course Name (press enter to keep current value): "))
                courseInstructor = input(str("New Course Instructor (press enter to keep current value): "))
                sTime = input(str("New Start Time # (press enter to keep current value): "))
                eTime = input(str("New End Time (press enter to keep current value): "))
                roomNum = input(str("New Room # (press enter to keep current value): "))

                # build SQL query and execute
                update_vals = ()
                update_cols = []
                if courseid != "":
                    update_cols.append("courseid = %s")
                    update_vals += (courseid,)
                if courseName != "":
                    update_cols.append("courseName = %s")
                    update_vals += (courseName,)
                if courseInstructor != "":
                    update_cols.append("courseIntructor = %s")
                    update_vals += (courseInstructor,)
                if sTime != "":
                    update_cols.append("sTime = %s")
                    update_vals += (sTime,)
                if eTime != "":
                    update_cols.append("eTime = %s")
                    update_vals += (eTime,)
                if roomNum != "":
                    update_cols.append("roomNum = %s")
                    update_vals += (roomNum,)
                if len(update_cols) > 0:
                    update_cols_str = ", ".join(update_cols)
                    update_vals += (course_id,)
                    command_handler.execute(f"UPDATE course SET {update_cols_str} WHERE courseid = %s", update_vals)
                    db.commit()
                    print("Course information updated!")
                else:
                    print("No changes made")
        
        elif user_option == "5":
            auth_admin()

def enroll_info():
     while 1:
        print("")
        print("Enrollment Menu")
        print("1. Register Enrollment")
        print("2. View Existing Enrollment")
        print("3. Delete Existing Enrollment")
        print("4. Edit Existing Enrollment")
        print("5. Logout")

        user_option = input(str("Option: "))
    # Create Enrollment
        if user_option == "1":
            print("")
            print("Register New Enrollment")
        
            id = input(str("Student ID: "))
            courseid = input(str("Course ID: "))
            grade = input(str("Grade: "))

            # Check if student ID exists in the student table
            command_handler.execute("SELECT * FROM student WHERE id = %s", (id,))
            student_exists = command_handler.fetchone()

            # Check if course ID exists in the course table
            command_handler.execute("SELECT * FROM course WHERE courseid = %s", (courseid,))
            course_exists = command_handler.fetchone()

            if student_exists and course_exists:
                querys_vals = ( id, courseid, grade)
                command_handler.execute("INSERT INTO enrollment ( id, courseid, grade) VALUES (%s, %s, %s)", querys_vals)
                db.commit()
                print("Enrollment has been registered!")
            else:
                if not student_exists:
                    print("Student ID does not exist.")
                if not course_exists:
                    print("Course ID does not exist.")

         # View enrollment
        elif user_option == "2":
            print("")
            print("View Existing Enrollments")
            
            # execute SQL query to retrieve all student information
            command_handler.execute("SELECT enrollmentid, id, courseid, grade FROM enrollment")
            result = command_handler.fetchall()
            
            if len(result) < 1:
                print("No enrollment found")
            else:
                # create a PrettyTable object and set the field names
                table = PrettyTable()
                table.field_names = ["Enrollment ID", "Student ID", "Course ID", "Grade"]
                
                # add each row of data to the table
                for row in result:
                    table.add_row(row)
                    
                # print the table
                print(table)

         # Delete enrollment by id
        elif user_option == "3":
            print("")
            print("Delete Existing Enrollment ")
            enrollment_id = input(str("Enrollment ID : "))
            query_vals = (enrollment_id,)
            command_handler.execute("DELETE FROM enrollment WHERE enrollmentid = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Enrollment not found")
            else:
                print("Enrollment with ID " + enrollment_id + " has been deleted")
        
        # Edit existing enrollment
        elif user_option == "4":
            print("")
            print("Edit Existing Enrollment")

            enrollment_id = input(str("Enrollment ID: "))

            # Check if enrollment ID exists in the enrollment table
            command_handler.execute("SELECT * FROM enrollment WHERE enrollmentid = %s", (enrollment_id,))
            enrollment_exists = command_handler.fetchone()

            if enrollment_exists:
                print("Current Enrollment Details:")
                print("Student ID: " + str(enrollment_exists[1]))
                print("Course ID: " + str(enrollment_exists[2]))
                print("Grade: " + str(enrollment_exists[3]))

                print("\nEnter new details (leave blank to keep current value):")
                new_student_id = input(str("New Student ID: "))
                new_course_id = input(str("New Course ID: "))
                new_grade = input(str("New Grade: "))

                if new_student_id == '':
                    new_student_id = enrollment_exists[1]
                if new_course_id == '':
                    new_course_id = enrollment_exists[2]
                if new_grade == '':
                    new_grade = enrollment_exists[3]

                query_vals = (new_student_id, new_course_id, new_grade, enrollment_id)
                command_handler.execute("UPDATE enrollment SET id = %s, courseid = %s, grade = %s WHERE enrollmentid = %s", query_vals)
                db.commit()
                print("Enrollment has been updated!")

            else:
                print("Enrollment ID does not exist.")

        # Logout
        elif user_option == "5":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")
    
def schedule_info():
   print(" schedule info")



def department_info():
    while 1:
        print("")
        print("Department Menu")
        print("1. Register New Department")
        print("2. View Existing Department")
        print("3. Delete Existing Department")
        print("4. Edit Existing Department")
        print("5. Logout")

        user_option = input(str("Option: "))

    # Create department
        if user_option == "1":
            print("")
            print("Register New Department")
            departmentName = input(str("Department Name: " ))
            querys_vals = (departmentName, )
            command_handler.execute("INSERT INTO department (departmentName) VALUES (%s)", querys_vals)
            db.commit()
            print(departmentName + " has been registered as a department!")
    # View department
        elif user_option == "2":
            print("")
            print("View Existing Department")
            
            # execute SQL query to retrieve all student information
            command_handler.execute("SELECT departmentid, departmentName FROM department")
            result = command_handler.fetchall()
            
            if len(result) < 1:
                print("No departments found")
            else:
                # create a PrettyTable object and set the field names
                table = PrettyTable()
                table.field_names = ["Department ID", "Department Name"]
                
                # add each row of data to the table
                for row in result:
                    table.add_row(row)
                    
                # print the table
                print(table)

         # Delete department by id
        elif user_option == "3":
            print("")
            print("Delete Existing Department ")
            department_id = input(str("Department ID : "))
            query_vals = (department_id,)
            command_handler.execute("DELETE FROM department WHERE departmentid = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("Department not found")
            else:
                print("Department with ID " + department_id + " has been deleted")
         # Edit Department
        elif user_option == "4":
            print("")
            print("Edit Existing Department")
            department_id = input(str("Department ID : "))
            query_vals = (department_id,)
            command_handler.execute("SELECT * FROM department WHERE departmentid = %s", query_vals)
            result = command_handler.fetchone()
            if result is None:
                print("Department not found")
            else:
                print("Current Information:")
                print(f"Department Name: {result[0]}")
                
                

                # get new values from user
                departmentName = input(str("New department name (press enter to keep current value): "))
               

                # build SQL query and execute   
                update_vals = ()
                update_cols = []
                if departmentName != "":
                    update_cols.append("departmentName = %s")
                    update_vals += (departmentName,)
                if len(update_cols) > 0:
                    update_cols_str = ", ".join(update_cols)
                    update_vals += (department_id,)
                    command_handler.execute(f"UPDATE department SET {update_cols_str} WHERE departmentid = %s", update_vals)
                    db.commit()
                    print("Department information updated!")
                else:
                    print("No changes made")
        
        elif user_option == "5":
            auth_admin()
        

def prof_info():
    while 1:
        print("")
        print("Course Menu")
        print("1. Register New Professor")
        print("2. View Existing Professor")
        print("3. Delete Existing Professor")
        print("4. Edit Existing Professor")
        print("5. Logout")

        user_option = input(str("Option: "))

    # Create Professor
        if user_option == "1":
            print("")
            print("Register New Professor")
            departmentName = input(str(" Name: " ))
            querys_vals = (departmentName, )
            command_handler.execute("INSERT INTO department (departmentName) VALUES (%s)", querys_vals)
            db.commit()
            print(departmentName + " has been registered as a department!")







def student_portal():
    print("")
    print("Welcome Back!")
    print("1. Student Info")
    print("2. Course Info")
    print("3. Enrollment Info")
    print("4. Schedule Info")
    print("5. Department Info")
    print("6. Professor Info")


    try:
            user_option = input(str("Option: "))
    except:
            print("Error.")
    if user_option == "1":
            student_info()
    elif user_option == "2":
         print("Course Info")
         course_info()
    elif user_option == "3":
         enroll_info()
    elif user_option == "4":
         schedule_info()
    elif user_option == "5":
         department_info()
    elif user_option == "6":
        prof_info()
    else:
            print("No valid option was selected!")


def auth_admin():
    print("")
    print("Student Login")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == "user":
        if password == "pass":
            student_portal()
        else:
            print("Incorrect password!")
    else:
            print("Login details not recognized")



def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login in as a student")
        try:
            user_option = input(str("Option: "))
        except:
            print("Error.")
        if user_option == "1":
            auth_admin()
        
        else:
            print("No valid option was selected!")
       
main()