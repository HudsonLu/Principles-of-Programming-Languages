import matplotlib
import matplotlib.pyplot as plt

names=['email attachments', 'malicious email', 'ransomware-phishing.', 'phishing messages 2016']
values=[66,49,21,30]
plt.figure(1,figsize=(10,10)) # set the size(width, height)
plt.subplot(131)
plt.bar(names, values)
plt.title('Percentage of attacks connected to malicious emails', loc='left')
plt.xticks(rotation=45, fontsize=7)
plt.savefig('barchart-rotatedLabels.png', dpi=300, bbox_inches='tight') #save in a .png file
plt.show()


