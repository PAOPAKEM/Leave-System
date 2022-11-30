import csv
import pandas as pd

oplist = ['0', '1', '2', '3', '4', '5', '6']
# ------------WrIte funCtion------------


def menu():
    print('''
MUICT Student Leave System
 1. print a list of students
 2. submit a leave request
 3. check leave with class date
 4. check leave with student ID
 5. check leave with student first name
 6. print leave summary
 0. exit\n''', end='')


# ------------ DEfiNe hOw eAch OptIon worKs.------------


def option1():
    df = pd.read_csv('students.csv')
    print(df.to_string(index=False))


def option2():  # LEaVe rEqueSt
    id = input('ID: ').strip()
    leave = input('Leave (S=Sick/B=Business/T=Travel/O=Others): ').upper()
    date = input('Class date (DD-MM-YYYY): ').strip()
    try:
        # aDd dAtA
        df1 = open('leave.csv')
        add = pd.DataFrame([[id, leave, date]], columns=[
                           'id', 'leave', 'date'])
        add.to_csv('leave.csv', mode='a', index=False, header=None)
        df1.close()
    except:
        # cReAte NEw fiLE
        add = pd.DataFrame([[id, leave, date]], columns=[
                           'id', 'leave', 'date'])
        add.to_csv('leave.csv', mode='a', index=False)
    # finally:
    #   a = pd.read_csv('leave.csv')
    #   print(a.to_string(index = False))


def option3():  # CHeck WitH datE
    date = input('Date (DD-MM-YYYY): ')
    df = pd.read_csv('leave.csv')
    stu_df = pd.read_csv('students.csv')
    c = 0
    stuid_index = 0
    for i in df['date']:  # CouNt
        if i == date:
            c += 1
    print(f"There are {c} students leave on {date}")
    for k in df[(df['date'] == date)].value_counts().to_dict().keys():
        stuid_index = 0  # reset
        for i in stu_df['id']:  # Find index
            # k[0] ==> student id
            if i != k[0]:
                stuid_index += 1
            else:
                break
        # k[1] ==> leave type
        if k[1] == 'S':
            print(
                f"(Sick) {k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}"
            )
        if k[1] == 'B':
            print(
                f"(Business) {k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}"
            )
        if k[1] == 'T':
            print(
                f"(Travel) {k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}"
            )
        if k[1] == 'O':
            print(
                f"(Other) {k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}"
            )


def option4():  # check with id
    id = input('ID: ')
    df = pd.read_csv('leave.csv')
    stu_df = pd.read_csv('students.csv')
    stuid_index = 0
    c = 0
    for k in df[(df['id'].astype(str) == id)].value_counts().to_dict().keys():
        stuid_index = 0  # reset
        # -------Find index---------
        for i in stu_df['id']:
            if i != k[0]:
                stuid_index += 1
            else:
                break
        # --------------------------
        if k[1] == 'S':
            print(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}: Sick Leave on {k[2]}"
            )
            c += 1
        elif k[1] == 'B':
            print(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}: Business Leave on {k[2]}"
            )
            c += 1
        elif k[1] == 'T':
            print(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}: Travel Leave on {k[2]}"
            )
            c += 1
        elif k[1] == 'O':
            print(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]}: Other Leave on {k[2]}"
            )
            c += 1
    if c == 0:
        print("There is no student leave record.")


def option5():
    fname = input('Firstname:')
    df = pd.read_csv('leave.csv')
    stu_df = pd.read_csv('students.csv')
    id_name_dict = {}
    for i in range(len(stu_df['id'])):
        if fname in (stu_df['fname'][i]):
            id_name_dict[stu_df['id'][i]] = (
                stu_df['fname'][i], stu_df['lname'][i])
    for i in range(len(df['id'])):
        for k, v in id_name_dict.items():
            if k == df['id'][i]:
                if df['leave'][i] == 'B':
                    print(
                        f"{k} {v[0]} {v[1]}: Business Leave on {df['date'][i]}")
                elif df['leave'][i] == 'S':
                    print(f"{k} {v[0]} {v[1]}: Sick Leave on {df['date'][i]}")
                elif df['leave'][i] == 'O':
                    print(f"{k} {v[0]} {v[1]}: Other Leave on {df['date'][i]}")
                elif df['leave'][i] == 'T':
                    print(
                        f"{k} {v[0]} {v[1]}: Travel Leave on {df['date'][i]}")


def option6():
    df = pd.read_csv('leave.csv')
    stu_df = pd.read_csv('students.csv')
    stuid_index = 0
    leave_summary = {'s': [], 'b': [], 't': [], 'o': []}
    for k in df.value_counts().to_dict().keys():
        stuid_index = 0  # reset
        for i in stu_df['id']:  # Find index
            if i != k[0]:
                stuid_index += 1
            else:
                break
        if k[1] == 'S':
            leave_summary['s'].append(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]} leave on {k[2]}"
            )
        elif k[1] == 'B':
            leave_summary['b'].append(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]} leave on {k[2]}"
            )
        elif k[1] == 'T':
            leave_summary['t'].append(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]} leave on {k[2]}"
            )
        elif k[1] == 'O':
            leave_summary['o'].append(
                f"{k[0]} {stu_df['fname'][stuid_index]} {stu_df['lname'][stuid_index]} leave on {k[2]}"
            )

    if leave_summary['s'] != []:  # check list not empty
        print('(Sick)')
        for i in leave_summary['s']:
            print(f'  {i}')
    if leave_summary['b'] != []:
        print('(Business)')
        for i in leave_summary['b']:
            print(f'  {i}')
    if leave_summary['t'] != []:
        print('(Travel)')
        for i in leave_summary['t']:
            print(f'  {i}')
    if leave_summary['o'] != []:
        print('(Other)')
        for i in leave_summary['o']:
            print(f'  {i}')


def main():
    menu()
    choice = input('Option: ')

    while True:
        if choice == '1':
            option1()
            menu()
            choice = input('Option: ')
        if choice == '2':
            option2()
            menu()
            choice = input('Option: ')
        if choice == '3':
            option3()
            menu()
            choice = input('Option: ')
        if choice == '4':
            option4()
            menu()
            choice = input('Option: ')
        if choice == '5':
            option5()
            menu()
            choice = input('Option: ')
        if choice == '6':
            option6()
            menu()
            choice = input('Option: ')
        if choice == '0':
            quit()
        else:
            while choice not in oplist:
                print('\n** Please Select Again **')
                menu()
                choice = input('Option: ')


main()
