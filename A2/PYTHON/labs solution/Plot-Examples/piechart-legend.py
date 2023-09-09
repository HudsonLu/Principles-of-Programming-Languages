import matplotlib.pyplot as plt
import numpy as np

#pie chart
sizes = [22, 20, 13, 12, 10, 8, 6, 5, 2, 2]
labels = ["Phishing (22%)",
          "Malware (20%)",
          "Cyberattacks to disrupt (13%)",
          "Cyberattacks to steal money (12%)",
          "Fraud (10%)",
          "Cyberattacks to steal IP (8%)",
          "Spam (6%)",
          "Internal attacks (5%)",
          "Natural Disasters (2%)", "Espionage (2%)"]
plt.figure(1,figsize=(6,6)) # set the size(width, height)
patches, texts = plt.pie(sizes, startangle=100)
plt.legend(patches, labels,loc="best",
           title = "Top 10 biggest cyber threat to organisations")
plt.axis('equal')
plt.tight_layout()
plt.show()
