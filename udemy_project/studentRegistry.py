class GradeLog:

    gradeDict = {'Jeff':[87,90,88],'Alex':[77,81,82]}
    #path = 'G:\programs\py_git\scripts\udemy_project\studentData.txt'

    def addStudent():
        name = input('Student Name: ')
        grade = input('Grade: ')
        print('Adding grade...')
        if name not in GradeLog.gradeDict:
            GradeLog.gradeDict[name] = [int(grade)]
        else:
            GradeLog.gradeDict[name].append(int(grade))
        print(GradeLog.gradeDict)

    def removeStudent():
        name = input('Student name: ')
        print('Removing student...')
        if name in GradeLog.gradeDict:
            del GradeLog.gradeDict[name]
            print(GradeLog.gradeDict)
        else:
            print(name,'is not present in the system log. Please check the name')

    def getAverage():
        from statistics import mean
        name = input('Student name: ')
        print('Computing average...')
        if name in GradeLog.gradeDict:
            grades = GradeLog.gradeDict[name]
            mean_grade = mean(grades)
            print('Average grade:',mean_grade)
        else:
            print(name,'is not present in the system log. Please check the name')


def main():
    active = True
    while active:
        print('[1] - Enter Grades')
        print('[2] - Remove Student')
        print('[3] - Student Average Grade')
        print('[4] - Exit')
        choice = input('What do you want to do today? Enter a number: ')
        if choice == '1':
            #GradeLog.getData()
            GradeLog.addStudent()
            print()
        elif choice == '2':
            #GradeLog.getData()
            GradeLog.removeStudent()
            print()
        elif choice == '3':
            #GradeLog.getData()
            GradeLog.getAverage()
            print()
        elif choice == '4':
            active = False
            print('Exiting the application...')
        else:
            print(choice,'is invalid. Please select a valid option')

admins = {'Python':'9999','User2':'Pass2'}
v_username = input('Username: ')
v_password = input('Password: ')
if v_username in admins:
    if v_password == admins[v_username]:
        print('Welcome,',v_username)
        main()
    else:
        print('Invalid Password.\nExiting the application')
else:
    print('The username does not exit.\nExiting the application')

    
    
                  
                  
