import time
class Student() :
    """
    This a class to create Students objects.
    """
    def __init__ (self,student_number,student_name,student_phone,student_family,student_family_phone) :
        self.student_number = student_number
        self.student_name = student_name
        self.student_phone = student_phone
        self.student_family = student_family
        self.student_family_phone = student_family_phone
        
    def studentsave(self) : 
        """
        this methot does save inside the studentfile.
        """
        with open("students.txt", "a", encoding="utf-8") as studentfile:
            studentfile.write(self.student_number+ "," +self.student_name+ "," +self.student_phone+ "," +self.student_family+ "," +self.student_family_phone+"\n")
    def showinformation(self): #This methot shows student information
        print(f"Student Number : {self.student_number}\nStudent Name : {self.student_name}\nStudent Phone : {self.student_phone}\nStudent Family : {self.student_family}\nStudent Family Phone : {self.student_family_phone}")
    def changestudentphonenumber (self,new_phone) : #ChangeStudentPhoneNumber
        print(f"Old number is {self.student_phone}")
        self.student_phone = new_phone
        print("Update succesful".center(50,"*"))
    def changefamilyphonenumber (self,new_phone): #ChangeFamilyNumber
        print(f"Old number is {self.student_phone}")
        self.student_family_phone = new_phone
        print("Update succesful".center(50,"*"))
    def turnstudentphonenumber (self): #We need this methot for reach to student phone number information
        return self.student_phone
    def turnfamilyphonenumber (self) : #We need this methot for reach to family student phone number information
        return self.student_family_phone
    def deletestudent(self):
        """
        delete student
        """
        del(self)
def checkstudentnumber (student_number) :
    if len (student_number) != 4 :
        raise IndexError ("Student number must 4 digits.")
def checkphonenumber (phonenumber) :
    if len (phonenumber) != 10 :
        raise IndexError ("Phone number must 10 digits.")


print("Welcome to the Students enrollment program")
 # This part compare ID and password with Teacher.txt information.
while True :
    teacher_ID = input("Enter your Teacher ID : ")
    teacher_password = input("Enter Your Password : ")
    """
    Txt files information is as follow  : ID,name,surname,password
    """
    with open("teacher.txt","r",encoding="utf-8") as teacherfile : 
        teachers_id = []
        teachers_password = []
        teachers_name = []
        teacher_dic = {}
        teachers_name_dic = {}
        for point in teacherfile : #Seperate all information
            point = point[:-1]
            point = point.split(",")
            teachers_id.append(point[0])
            teachers_password.append(point[3])
            names = point[1]+" "+point[2]
            names = names.title()
            teachers_name.append(names)
        index = 0
        while index < len(teachers_id) : #Check ID and Password
            teacher_dic[teachers_id[index]] = teachers_password[index]
            index += 1
        index = 0
        while index < len(teachers_id) :
            teachers_name_dic[teachers_id[index]] = teachers_name[index]
            index += 1
        try :
            if teacher_dic[teacher_ID] == teacher_password :

                print(f"Welcome {teachers_name_dic[teacher_ID]}".center(50,"*"))
                break
            elif teacher_dic[teacher_ID] != teacher_password :
                print("Wrong Password")
        except KeyError :
            print("Wrong ID or Password")
            continue

while True :
    print("1-Student Add\n2-Student Show\n3-Exit")
    print("Please select option..")
    choice = input ("Your Choice : ")
    if choice == "1" :
        print("Student Add".center(50,"*"))
        while True : #Takes all new student information
            student_number = input("Please Enter Student Number : ")
            try :
                checkstudentnumber(student_number)
                break
            except IndexError as Err :
                print(Err)
                continue
        student_name = input("Please Enter Student Name And Surname : ")
        student_name = student_name.title()
        while True :
            student_phone = input("Please Enter Student Phone ")
            try :
                checkphonenumber(student_phone)
                break
            except IndexError as Err :
                print(Err)
                continue
        student_family = input("Please Enter Member of Family Name : ")
        student_family = student_family.title()
        while True :
            student_family_phone = input("Please Enter Member of Family's Number : ")
            try :
                checkphonenumber(student_family_phone)
                break
            except IndexError as Err :
                print(Err)
                continue
        choice2 = input("İf you want to save the student press 's'\nİf you want to re-enter information press  : ")
        if choice2 == "s" :
            student_number = Student (student_number,student_name,student_phone,student_family,student_family_phone) #created object in Student class
            student_number.studentsave() # saving in student.txt file
            print("Student Added on the system".center(50,"*"))
        else :
            print("Incorrect option")
    elif choice == "2" :
        while True :
            student_number_see = input("Enter the student number you want to process : ")
            with open("students.txt", "r", encoding="utf-8") as studentsshow:
                reachtotheobject = {} # All students going inside dic for reach with str
                studentlist = studentsshow.readlines()
                for i in studentlist:
                    i = i[:-1]
                    i = i.split(",")
                    reachtotheobject[i[0]] = Student(i[0], i[1], i[2], i[3], i[4]) #all students creates object and going inside dic.
                if student_number_see in reachtotheobject.keys():           #Do we have the student we want to process ?
                    break
                elif student_number_see not in reachtotheobject.keys():
                    print(f"We dont have {student_number_see} ")
        while True:
            print("1-Show Student Information\n2-Update Student\n3-Delete Student\nGo to back with ANY button")
            choice3 = input("Choice : ")
            if choice3 == "1" :
                print("*"*50)
                reachtotheobject[student_number_see].showinformation() #Now we will reach the student we want to process with this method.
                print("*"*50)
            elif choice3 == "2" :
                print("1-Student Phone\n2-Student Family Phone Number\nGo to back with ANY button")
                choice4 = input("What do you want to change : ")
                if choice4 == "1" :
                    while True :
                        new_phone_number = input("Write a new phone number : ")
                        try :
                            checkphonenumber(new_phone_number)
                            break
                        except IndexError as Err :
                            print(Err)
                            continue

                    with open("students.txt","r",encoding="utf-8") as studentfile : # This block deletes old student lines from txt file and adds new student line with new phone number
                        studentlines = studentfile.readlines()
                        counter = 0
                        s = ""
                        print(studentlines)
                        for k in studentlines :
                            k = k[:-1]
                            if k[:4] == student_number_see :
                                s = k.replace(reachtotheobject[student_number_see].turnstudentphonenumber(),new_phone_number)
                                break
                            counter +=1
                        studentlines.append(s)
                        studentlines.append("\n")
                        del studentlines[counter]
                    with open ("students.txt","w",encoding="utf-8") as newstudentfile :
                        for wrr in studentlines:
                            newstudentfile.write(wrr)
                        reachtotheobject[student_number_see].changestudentphonenumber(new_phone_number)
                elif choice4 == "2" : # This block deletes old student lines from txt file and adds new student line with new family phone number
                    while True :
                        new_phone_number = input("Write a new phone number : ")
                        try :
                            checkphonenumber(new_phone_number)
                            break
                        except IndexError as Err :
                            print(Err)
                            continue

                    with open("students.txt","r",encoding="utf-8") as studentfile :
                        studentlines = studentfile.readlines()
                        counter = 0
                        s = ""
                        for k in studentlines :
                            k = k[:-1]
                            if k[:4] == student_number_see :
                                s = k.replace(reachtotheobject[student_number_see].turnfamilyphonenumber(),new_phone_number)
                                break
                            counter +=1
                        studentlines.append(s)
                        studentlines.append("\n")

                        del studentlines[counter]


                    with open ("students.txt","w",encoding="utf-8") as newstudentfile :
                        for wrr in studentlines:
                            newstudentfile.write(wrr)

                        reachtotheobject[student_number_see].changefamilyphonenumber(new_phone_number)
            elif choice3 == "3" :
                print(reachtotheobject[student_number_see].showinformation() ," is deleting...")
                time.sleep(1)
                del reachtotheobject[student_number_see]
                with open("students.txt", "r", encoding="utf-8") as studentfile:
                    studentlines = studentfile.readlines()
                    counter = 0
                    for k in studentlines:
                        k = k[:-1]
                        if k[:4] == student_number_see:
                            break
                        counter += 1
                    del studentlines[counter]
                with open("students.txt", "w", encoding="utf-8") as newstudentfile:
                    for wrr in studentlines:
                        newstudentfile.write(wrr)
                print("DELETED.")
            else :
                break
    elif choice == "3" :
        print("Thank You For Using")
        break

