#Hudson Xingcheng Lu           2031140
#420-LCU Computer Programming
#Monday Feb 21, 2022
#S. Hilal , instructor
#Assignment 1

   
#CONSTANT_VALUES

A_BASE_PRICE = 10 # Base price for plan A, in dollars.
A_FREE = 100 # Plan_A Number of free daytime minutes per month.
A_DAYTIME = 0.15 # Plan_A Cost of additional daytime minutes , in dollars.
A_EVENING = 0.20 # Plan_A Cost of evening minutes , in dollars.
A_WEEKEND = 0.25 # Plan_A Cost of weekend minutes , in dollars.

B_BASE_PRICE = 12 # Base price for plan B, in dollars.
B_FREE = 200 # Plan_B Number of free daytime minutes per month.
B_DAYTIME = 0.20 # Plan_B Cost of additional daytime minutes , in dollars.
B_EVENING = 0.25 # Plan_B Cost of evening minutes , in dollars.
B_WEEKEND = 0.30 # Plan_B Cost of weekend minutes , in cents.


C_BASE_PRICE = 12 # Base price for plan C, in dollars.
C_FREE = 250 # Plan_C Number of free daytime minutes per month.
C_DAYTIME = 0.30 # Plan_C Cost of additional daytime minutes , in dollars.
C_EVENING = 0.35 # Plan_C Cost of evening minutes , in dollars.
C_WEEKEND = 0.40 # Plan_C Cost of weekend minutes , in dollars.

D_BASE_PRICE = 15 # Base price for plan D, in dollars.
D_FREE = 0 # Plan_D Number of free daytime minutes per month.
D_DAYTIME = 39 # Plan_D Cost of additional daytime minutes , in dollars.
D_EVENING = 0 # Plan_D Cost of evening minutes , in dollars.
D_WEEKEND = 0 # Plan_D Cost of weekend minutes , in dollars.

#Start of my Cellphone Calculator1.
while True:
    print("""


    Program Menu
    Welcome to My Cellphone Calculator!
    1. Determine the Best Plan for my usage pattern and Display the average cost for all plans.
    2. Exit
    """)

    n = int(input("Enter your selected option :"))

    if n==2:
        break
    
    x = int(input("Number of daytime minutes?"))
    y = int(input("Number of evening minutes?"))
    z = int(input("Number of weekend minutes?"))

    #PLAN A

    if x > 100:
        firsta = abs(A_FREE - x) * (A_DAYTIME)
    elif x <= 100:
        firsta = 0
        
    seconda = (A_EVENING * y)
    thirda = (A_WEEKEND * z)
    totalA = A_BASE_PRICE + firsta + seconda + thirda



    #PLAN B
    if x > 200:
        firstb = abs(B_FREE - x) * (B_DAYTIME)

    elif x <= 200:
        firstb = 0


    secondb = (B_EVENING * y)
    thirdb = (B_WEEKEND * z)
    totalB = B_BASE_PRICE + firstb + secondb + thirdb


    #PLAN C
    if x > 250:
        firstc = abs(C_FREE - x) * (C_DAYTIME)

    elif x <= 250:
        firstc = 0


    secondc = (C_EVENING * y)
    thirdc = (C_WEEKEND * z)
    totalC = C_BASE_PRICE + firstc + secondc + thirdc



    #PLAN D
    if x > 0:
        x=1
    totalD = D_BASE_PRICE + (D_DAYTIME * x)


    print(str("Plan A costs")+" $"+str(totalA))
    print(str("Plan B costs")+" $"+str(totalB))
    print(str("Plan C costs")+" $"+str(totalC))
    print(str("Plan D costs")+" $"+str(totalD))

    #bestplan
    array = [[totalA, "plan A"] , [totalB, "plan B"], [totalC, "plan C"], [totalD, "plan D"]]
    array.sort()

    print("Choose "+str(array[0][1]))
    

    


 
