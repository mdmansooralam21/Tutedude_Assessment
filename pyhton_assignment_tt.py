'''

1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"

'''

marks_scored = int(input("Enter the marks scored: ")) # Taking user input and storing it as integer
print("\n")

if marks_scored >= 0 and marks_scored <= 100:
    if marks_scored >= 90:
        print("You have secured grade A!\n")
    elif marks_scored >= 80 and marks_scored <= 89:
        print("You have secured grade B!\n")
    elif marks_scored >= 70 and marks_scored <= 79:
        print("You have secured grade C!\n")
    elif marks_scored >= 60 and marks_scored <= 69:
        print("You have secured grade D!\n")
    elif marks_scored <= 60:
        print("You have secured grade F\n")
    
else:
    print("Please enter a valid marks [0-100]\n")

'''

2. Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student's grade.
Print all student grades.

'''

# A dictionary where the keys are student names and the values are their grades
marks_obtained = {
    'Abhay' : 'A',
    'Rohith' : 'A',
    'Mansoor' : 'B',
    'Muskaan' : 'B',
    'Avinash' : 'A',
    'Parwez' : 'B'
}

marks_obtained['Abhinav'] = 'B' # Add a new student and grade
marks_obtained['Mansoor'] = 'B' # Update an existing student's grade
print(marks_obtained) # Print all students grade


'''

3. Write to a File
Write a program to create a text file and write some content to it.

Using file functions like write and open.

'''

file_name = "first_file.txt"

with open("first_file.txt", 'w') as file:                           # This will create a new file named first_file.txt and open it in write mode and close it automatically after write operation completed
    file.write("This is the first line wriiten to the new file. \n")    # This will write the text into the file created

print("##################\n")
print(f"Successfully wrote the first line in the {file_name} and closed it automatically.\n")
print("##################\n")


'''

4. Read from a File
We used open in read mode and file.read to read and print to display.

'''

file_name = "first_file.txt"

f = open("first_file.txt", 'r')    # This will open the file in read mode
data = f.read()                    # This will read the content from the file
print("\n")
print(data)                        # This will print the content that was read 
print("\n")

f.close()                          # This will close the file at the end