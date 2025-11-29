import json

class StudentManager:
    def __init__(self):
        # ვქმნით კლასისთვის განკუთვნილ ცვლადს სადაც ჯეისონიდანაა ინფორმაცია წამოღებული
        with open("studentManager/studentList.json", "r", encoding = "utf-8") as f:
            self.__studentList = json.load(f)    
    
    def dataSaver(self):
        # ამ ფუნქციით ვანახლებთ ორიგინალურ ჯეისონის ფაილს
        with open("studentManager/studentList.json", "w", encoding = "utf-8") as f:
            json.dump(self.__studentList, f, indent = 4, ensure_ascii = False)
    
    def addStudent(self, newStudent):
        # ვამოწმებთ არის თუ არა სტუდენტი უკვე სიაში/აიდი გამოყენებულია თუ არა
        for eachPerson in self.__studentList:
            if newStudent.name == eachPerson["Student name"]:
                print("This student already exists in the list.")
                return
    
            if newStudent.id == eachPerson["ID"]:
                print("This ID is already taken in the list.")
                return
        
        # თუ არა, სტუდენტი ემატება
        self.__studentList.append({
            "ID": newStudent.id,
            "Student name": newStudent.name,
            "Student surname": newStudent.surname,
            "Grades" : newStudent.grade
        })
        self.dataSaver()
    
    def printStudents(self):
        # ზოგადად რასაც ვაკეთებთ ინფორმაციის წამოსაღებად
        for eachPerson in self.__studentList:
            print(f"The student with the ID of '{eachPerson["ID"]}' is called {eachPerson["Student name"]} {eachPerson["Student surname"]}.")
    
    def searchStudentById(self, newStudent):
        # ვამოწმებთ თოთეულ სტუდენტში აიდის.
        for eachPerson in self.__studentList:
            if newStudent.id == eachPerson["ID"]:
                print(f"The student with the id of {eachPerson["ID"]} is called {eachPerson["Student name"]} {eachPerson["Student surname"]}")
                return
            
        # თუ აიდი არ არსებობს
        print("No student found.")
    
    def checkStudentGrades(self):
        # გავდივართ თითოეულ სტუდენტს და ვპრინტავთ ყველაფერს ფაქტობრივად
        for eachPerson in self.__studentList:
            print(f"The student with the ID of '{eachPerson["ID"]}' is called {eachPerson["Student name"]} {eachPerson["Student surname"]} with the grades of: ", end = "")
            for eachGrade in eachPerson["Grades"]:
                print(eachGrade, end = ", ")
            print("")

# ვქმნით სტუდენტს
class Student:
    def __init__(self, id, name, surname, grade):
        self.id = id
        self.name = name
        self.surname = surname
        self.grade = grade

# ვააქტიურებეთ 'მენეჯერის' კლასს
manager = StudentManager()


while True:
    # შესაძლო ქმედებები
    print("1. Add a new student.")
    print("2. Show all students.")
    print("3. Search student by their ID.")
    print("4. Check student grades.")
    print("5. Quit the program.")

    # ქმედების აიდის ვალიდაცია
    try:
        action = int(input("Please choose an action: "))
    except ValueError:
        print("Please enter a valid action.")
        continue

    match action:
        case 1:
            # აიდის ვალიდაცია
            try:
                userId = int(input("ID: "))
            except ValueError:
                print("Please enter a valid action.")
                continue

            # მომხმარებელს შეყავს ინფორმაცია
            userName = input("Enter the name of the student: ")
            userSurname = input("Enter the surname of the student: ")
            userGrades = []

            # ქულების ვალიდაცია + შეყვანა
            while True:
                try:
                    eachGrade = int(input("Please input the grades (type '-1' to stop): "))
                except ValueError:
                    print("Please enter a valid grade.")
                    continue

                if eachGrade == -1:
                    break
                if eachGrade < -1 or eachGrade > 100:
                    print("You can't insert that grade.")
                    continue

                userGrades.append(eachGrade)
            
            # ვქმნით ახალ სტუდენტს და ვუშვებთ სტუდენტის დამამატებელ პროგრამას
            newStudent = Student(userId, userName, userSurname, userGrades)
            manager.addStudent(newStudent)

        case 2:
            # ვპრინტავთ სტუდენტებს
            manager.printStudents()

        case 3:
            # აიდის ვალიდაცია
            try:
                userId = int(input("ID: "))
            except ValueError:
                print("Please enter a valid action.")
                continue
            newStudent = Student(userId, None, None, None)
            manager.searchStudentById(newStudent)

        case 4:
            # პრინტავს მთლიანად ყველაფერს
            manager.checkStudentGrades()

        case 5:
            # გამოსვლა
            print("Thank you for using shalvaStudentClassroom.tm. Exiting program")
            break

        case _:
            print("Please chose a valid action")
            continue