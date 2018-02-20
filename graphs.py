import matplotlib.pyplot as plt
import numpy as np
import sys

n=input("Enter a named Entity: ")

if (n.lower()=="america"):
    pos=[35,45,20,45.2]
    neu=[45,45,70,31.9]
    neg=[20,10,10,22.9]
elif (n.lower()=="army"):
    pos=[15,15,0,46.3]
    neu=[70,55,100,45.9]
    neg=[15,30,0,7.8]
elif (n.lower()=="asian"):
    pos=[15,5,0,65.9]
    neu=[80,75,100,22.3]
    neg=[5,20,0,11.8]
elif (n.lower()=="florida"):
    pos=[10,35,10,40.6]
    neu=[85,55,80,37.7]
    neg=[5,10,10,21.7]
elif (n.lower()=="trump"):
    pos=[0,30,10,36.7]
    neu=[95,65,85,46.0]
    neg=[5,5,5,17.3]
else:
    print("Not a named entity")
    sys.exit()

figure,axis=plt.subplots()
ind=np.arange(3)
rect1=plt.bar(ind,[pos[0],neu[0],neg[0]],0.15,alpha=0.6,color='r',label='BBC News')
rect2=plt.bar(ind+0.15,[pos[1],neu[1],neg[1]],0.15,alpha=0.6,color='b',label='FOX News')
rect3=plt.bar(ind+0.3,[pos[2],neu[2],neg[2]],0.15,alpha=0.6,color='g',label='Various News sources')
rect4=plt.bar(ind+0.45,[pos[3],neu[3],neg[3]],0.15,alpha=0.6,color='y',label='Twitter')
plt.xlabel('SENTIMENT',fontsize=15)
plt.ylabel('No. of articles(%)',fontsize=15)
plt.title("Sentiment Analysis for "+n)
plt.xticks(ind+0.3,('Positive','Neutral','Negative'))
plt.legend()
plt.tight_layout()
plt.show()
