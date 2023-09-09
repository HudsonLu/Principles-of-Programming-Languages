# Hudson Xingcheng Lu              2031140

#420-LCU Computer Programming, Section #00002
# S. Hilal, instructor
# Assignment 2


menu="""

Welcome to the Simple Class Calculator. Here’s the list of available options: 
1- Enter a student record (Name, ID, program, and 5 grades separate by commas, no spaces). 
2- Display the full class data sorted in alphabetical order based on name. 
3- Calculate and Display the class descriptive statistics. 
4- Display the record of a given student 
5- Display the list of student names below class average. 
6- Exit 
Enter your selected option :"""


option = 1
while option !=6:
    option = int(input(menu))
    if option == 1:
        record_input=input("Enter Student Record (Name, ID, program, and 5 grades separated by commas and no spaces):")
        IDs = []
        student_list=record_input.split(",")
#Lea Smith, 12345, HH,20,24.5,10,9.5,28
#Bob Green, 23456, HP,22.5,24.5,10,8,21      
        IDs1 = student_list[1]
        IDs2 = IDs1[1:]
        students=[]

        IDs = []


        while len(student_list)==8 :
            if len(IDs2) != 5 :
                print('ID must have 5 digits. Record rejected.')
                break
            for u in range(len(students)-1) :
                if student_list[1].count(students[u][1])>1:
                    print('Duplicate ID number. Record rejected.')
                    break
            if len(student_list) !=8 :
                print('Record Incomplete, Record rejected.')
                break
            else:
                print('Record Accepted.')
                student_ID = student_list[1]
                student_ID1 = int(student_ID[1:])
                student_program = student_list[2]
                student_program1 = student_program[1:]
                
                grades = student_list[3:]
                for i in range(len(grades)):
                    grades[i] = float(grades[i])

                z = grades[0]+grades[1]+grades[2]+grades[3]+grades[4]
                y = z
                if (y >= 87):
                    w= "A"

                elif (75 <= y <= 86):
                    w="B"
                    
                elif (70 <= y <= 79):
                    w="C"
                    
                elif (65 <= y <= 74):
                    w="D"
                    
                elif (y < 65):
                    w="F"
                student_list[1]= student_ID1
                student_list[2]= student_program1
                student_list[3:] = grades
                student_list.append(z)
                student_list.append(w)
                students.insert(1, student_list)
                break
           
        students.insert(0, student_list) #Limit to 8
        students.insert(1, student_list)
        students.insert(1, student_list)
        students.insert(1, student_list)
        students.insert(1, student_list)
        students.insert(1, student_list)
        students.insert(1, student_list)
        

                
                       
  
# student_list[0]
# student_ID1
# student_program1
# grades
# z
# w
      
    elif option == 2:
        q = students[:]
        q.sort()
        print(q)


        
    elif option == 3:
       print('Number of students entered:', len(students))
       
       sum1 = 0
       for u in range(len(students)-1):
           avg = students[u][-2]
           sum1 = sum1 + avg

       avg1 = sum1/(len(students)-1)


       print('Class average based on total grade', avg1
)
       
       test1sum = 0
       for u in range(len(students)-1):
           test1avg = students[u][3]
           test1sum = test1sum + test1avg
       test1avg = test1sum/(len(students)-1)

       test2sum = 0
       for u in range(len(students)-1):
           test2avg = students[u][4]
           test2sum = test2sum + test2avg
       test2avg = test2sum/(len(students)-1)

       assignment1sum = 0
       for u in range(len(students)-1):
           assignment1avg = students[u][5]
           assignment1sum = assignment1sum + assignment1avg
       assignment1avg = assignment1sum/(len(students)-1)

       assignment2sum = 0
       for u in range(len(students)-1):
           assignment2avg = students[u][5]
           assignment2sum = assignment2sum + assignment2avg
       assignment2avg = assignment2sum/(len(students)-1)

       projectsum = 0      
       for u in range(len(students)-1):
           projectavg = students[u][6]
           projectsum = projectsum + projectavg
       projectavg = projectsum/(len(students)-1)
       
       print(' Average grade for each test, each assignment and the project:', test1avg, test1avg, assignment1sum, assignment2sum, projectavg)

       
       for u in range(len(students)-1):
           letters = students[u][-1]
           A = letters.count('A')
           B = letters.count('B')
           C = letters.count('C')
           D = letters.count('D')
           F = letters.count('F')

       
       print('Letter Grade distribution (how many of each letter grade):',A, 'A ',B, 'B  ', C, 'C  ', D,'D   ', F, 'F  ') 


    elif option == 4:
        student_ID = input("Enter the ID of a student:")
        for u in range(len(students)):
            ID = students[u][1]
            if ID == student_ID:
                IDallo = students[u]
        print('Name:', students[u][0], '       ID:', students[u][1]),
        print('Test Grades:', students[u][3], students[u][4],' Assignment Grades:', students[u][5], students[u][6], '  Project Grade:', students[u][7])                          
        print('Total Grade:', students[u][-2],'      Letter Grade:', students[u][-1] )
        


        
    elif option == 5:
        sum1 = 0
        for u in range(len(students)-1):
            avg = students[u][-2]
            sum1 = sum1 + avg

        avg1 = sum1/(len(students)-1)

        if not avg < avg1:      
                print('Name:', students[u][0], '    ID:', students[u][1],'    Total Grade:', students[u][-2],'    Letter Grade:', students[u][-1] )
        for u in range(len(students)-1):
            if avg > avg1:      
                print('Name:', students[u][0], '    ID:', students[u][1],'    Total Grade:', students[u][-2],'    Letter Grade:', students[u][-1] )
        
    elif option == 6:
         print("Exit")

