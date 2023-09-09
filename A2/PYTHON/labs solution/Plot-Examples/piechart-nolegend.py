#Statistics on Banking Fraud that occurred in India circa 2016
import matplotlib
import matplotlib.pyplot as pl

fraud = ("Internet banking/ATM fraud",
         "Credit/Debit card fraud", "Identity Fraud",
         "Collusion between employees and conumers",
         "Funds transfer fraud", "Bribery and corruption", "Others")
colors = ["blue", 'yellow', 'green', 'orange', 'red', 'purple', 'grey']
sizes = [24,18,17,15,13,7,6]
pl.pie(sizes, labels=fraud, colors=colors, startangle=90, autopct='%1.1f%%')
pl.axis('equal')
pl.title('Statistics on Banking Fraud from India circa 2016')
pl.show()
