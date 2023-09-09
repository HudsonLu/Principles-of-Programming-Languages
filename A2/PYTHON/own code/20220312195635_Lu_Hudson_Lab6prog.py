#Hudson Xingcheng Lu                2031140
#420-LCU Computer Programming
#S. Hilal , instructor

#Lab 6

#Part 1


bidders=input("list of the bidder names:")
bids=input("list of integers (bid):")

bidders_space = bidders.replace(","," ")
bidders_split = bidders_space.split()

y = bidders.split()
x = bids.split()

#print (y)
#print (x)

for i in range(len(x)):
    x[i] = int(x[i]), bidders_split[i]

    
L = sorted(x)



    
highest = L[-1]
second_highest = L[-2]

hi = " had the highest bid of $"
se = " had the second highest bid of $"
end = " pays this bid."
comma= ","


print (highest[1] + hi + str(highest[0]))
print (second_highest[1] + se + str(second_highest[0])+ comma +highest[1] + end)


#Part 2


x=input("Enter Student Record (Name, ID, program, and 5 grades separated by commas and no spaces):")

y=x.split()

Name_1 =' '.join(y[:2]) #Name
Name = Name_1[:-1]

ID_1 = y[2] #ID
ID = int(ID_1[:-1])


p = y[3] #program
p1= p.index(",")
program=p[:p1]

g=p[p1+1:]  #grades section
g1 = g.index(",")
g1_1 = float(g[:g1]) #grades
g2 = g.rindex(",")
g2_2 = float(g[g2+1:]) #grades
g3 = g[g1+1:g2]
g3_3 = g3.index(",") 
g3_3_3 = float(g3[:g3_3]) #grades
g4 = g3.rindex(",")
g4_4 = float(g3[g4+1:]) #grades
g5 = float(g3[g3_3+1:g4]) #grades


z = g1_1+g3_3_3+g5+g4_4+g2_2 #sum of grades

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

o = "["+"\""+Name+"\""+","+str(ID)+","+"\""+program+"\""+","+str(g1_1)+","+str(g3_3_3)+","+str(g5)+","+str(g4_4)+","+str(g2_2)+","+str(z)+","+"\'"+w+"\'"+"]"
print("Student list is", o)


#Part 3

message= """
\n\n\n
Part 3
\n
1. My answer is [0, 1, 2, 4, 5] IDLE >> [0, 1, 2, 4, 5]
2. My answer is [0, 1, 2, 4, 5, 6] IDLE >> [0, 1, 2, 3, 4, 5, 6]
3. My answer is [4, 6, 8, 10, 12, 14] IDLE >> [4, 6, 8, 10, 12, 14]
4. My answer is [11, 12, 13, 14] IDLE >> [11, 12, 13, 14]
5. My answer is [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] IDLE >> [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
6. My answer is [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0] IDLE >> [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
7. My answer is [-10, -9] IDLE >> [-10, -9]
8. My answer is [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10] IDLE >> [-19, -18, -17, -16, -15, -14, -13, -12, -11, -10]
9. My answer is [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6] IDLE >> [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
10. My answer is [-120, -119, -118, -117, -116] IDLE >> [-120, -119, -118, -117, -116]
11. My answer is [0, -1, -2, -3, -4] IDLE >> []
12. My answer is [0, -1, -2, -3, -4] IDLE >> [0, -1, -2, -3, -4]
13. My answer is [2, 6, 10, 14, 18, 22, 26, 30, 34, 38] IDLE >> [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
14. My answer is [25, 30, 35, 40, 45, 50, 55] IDLE >> [25, 30, 35, 40, 45, 50, 55]
15. My answer is [150, 175, 200, 225, 250, 275] IDLE >> [150, 175, 200, 225, 250, 275]
16. My answer is [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100] IDLE >> [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
17. My answer is [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0] IDLE >> [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]
18. My answer is [-10, -7, -4, -1] IDLE >> [-10, -7, -4, -1]
19. My answer is [-40, -35, -30, -25, -20, -15, -10] IDLE >> [-40, -35, -30, -25, -20, -15, -10]
20. My answer is [300, 250, 200, 150, 100, 50] IDLE >> [300, 250, 200, 150, 100, 50]
"""

print(message)




