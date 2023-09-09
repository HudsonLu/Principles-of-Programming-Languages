from datetime import date

# Prints days left for my Birthday
today = date.today()
print("Today is", today)
my_bday = date(today.year, 5, 25) 
if my_bday < today: #my birthday has passed
    my_bday = my_bday.replace(  
        year=today.year + 1) #next year then
time_diff = my_bday - today
print(my_bday, "is", time_diff.days,
      "days from today")



