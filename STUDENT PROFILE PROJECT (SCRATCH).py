import os

students = {} #DATA BASE
def display():
    x = input("[1] Add New Student\n"         # DISPLAYS THE OPTIONS
              "[2] Display All Students\n"    # RETURNS A NUMBER BASED ON THE OPTIONS
              "[3] Edit Student\n"
              "[4] Delete All Students\n" #students.clear()
              "[5] Delete Single Student\n"
              "[0] Exit\n"
              "Enter Here: ")
    return int(x)

def new_student():                                      # RETURNS THE DETAILS AND KEY (STUDENT NUMBER)
    stud_num = ''
    details = ['','','','','']
    while not stud_num.isdigit():
        stud_num = input('Enter Student Number: ')
    details[0] = input('First Name: ')
    details[1] = input('Last Name: ')
    while not details[2].isdigit():
        details[2] = input('Year Level: ')
    details[3] = input('Course Taking: ')
    while not details[4].isdigit():
        details[4] = input('Age: ')
    return details, stud_num

def display_all(dict):
    for _ in dict.keys():                               #DISPLAYS ALL OF THE STUDENTS
        print(f'Student Number: {_}\n'
              f'First Name: {dict[_][0]}\n'
              f'Last Name: {dict[_][1]}\n'
              f'Year Level: {dict[_][2]}\n'
              f'Course: {dict[_][3]}\n'
              f'Age: {dict[_][4]}\n')

def edit_student(dict,stud_num):
    x = 0
    again = False
    while x not in range(1, 6):
        x = int(input("[1] Edit First Name\n"
                      "[2] Edit Last Name\n"
                      "[3] Edit Year Level\n"
                      "[4] Edit Course\n"
                      "[5] Edit Age\n"
                      "Enter Here: "))
    if x == 1:
        dict[stud_num][0] = input(f"Edit '{dict[stud_num][0]}' to: ")
    elif x == 2:
        dict[stud_num][1] = input(f"Edit '{dict[stud_num][1]}' to: ")
    elif x == 3:
        dict[stud_num][2] = input(f"Edit '{dict[stud_num][2]}' to: ")
    elif x == 4:
        dict[stud_num][3] = input(f"Edit '{dict[stud_num][3]}' to: ")
    elif x == 5:
        dict[stud_num][4] = input(f"Edit '{dict[stud_num][4]}' to: ")


    print(f'Student Number: {stud_num}\n'
          f'First Name: {dict[stud_num][0]}\n'
          f'Last Name: {dict[stud_num][1]}\n'
          f'Year Level: {dict[stud_num][2]}\n'
          f'Course: {dict[stud_num][3]}\n'
          f'Age: {dict[stud_num][4]}\n')

exit = True

while exit: # LOGIC

    user_input = display()
    os.system('cls')
    if user_input == 1:
        details, stud_num = new_student()
        students[stud_num] = details
    elif user_input == 2:
        display_all(students)
    elif user_input == 3:
        if len(students) == 0:
            print('Student list empty!')
            continue
        else:
            edit_stud = ''
            while edit_stud not in students.keys():
                edit_stud = input('Enter Student Number: ')
            edit_again = ''
            again = False
            while not again:
                edit_student(students, edit_stud)
                while edit_again not in 'YN':
                    edit_again = input('Edit Again? [Y/N]:\n')
                if edit_again.upper() == 'Y':
                    pass
                else:
                    again = True
    elif user_input == 4:
        students.clear()
        print('All students cleared!')
    elif user_input == 5:
        if len(students) == 0:
            print('No students in database.')
            continue
        stud_num_remov = ''
        while stud_num_remov not in students.keys():
            stud_num_remov = input('Enter Student Number:')
        del students[stud_num_remov]
    elif user_input == 0:
        exit = False

