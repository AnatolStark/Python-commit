import csv

with open('students.csv','w') as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(['First name', 'Last name', 'Age'])
  csv_writer.writerow(['Jack', 'White', 24])
  csv_writer.writerow(['Jane', 'Black', 23])


def add_student(first_name, last_name, age):
    with open("students.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name, last_name, age])


add_student('Kevin', 'Shwarz', '22')

def print_students():
    with open("students.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for students_list in csv_reader: 
            print(students_list)


print_students()