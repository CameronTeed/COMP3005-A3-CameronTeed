#Cameron Teed 101227413
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=A3 user=postgres password=student")
# Create a new cursor
cur = conn.cursor()

# Gets all the students from the database
def getAllStudents():
    # Execute a select query
    cur.execute("SELECT * FROM Students")
    print(cur.fetchall())

# Adds a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    # Execute an insert query
    cur.execute("INSERT INTO Students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()

# Updates a students email
def updateStudentEmail(student_id, new_email):
    # Execute update query
    cur.execute("UPDATE Students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()

# Deletes a student from the database
def deleteStudent(student_id):
    # Execute delete query
    cur.execute("DELETE FROM Students WHERE student_id = %s", (student_id,))
    conn.commit()


if __name__ == "__main__":

    # Loops for input until user exits
    while(True):
        print("1. Add a student\n"
              "2. Update a student's email\n"
              "3. Delete a student\n"
              "4. Get all students\n"
              "5. Quit\n")
        
        choice = input("Enter your choice (number): ")
        if choice == "1":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            email = input("Enter the email: ")
            enrollment_date = input("Enter the enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "2":
            student_id = input("Enter the student ID: ")
            new_email = input("Enter the new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == "3":
            student_id = input("Enter the student ID: ")
            deleteStudent(student_id)
        elif choice == "4":
            getAllStudents()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

    # Close databasw
    cur.close()
    conn.close()


