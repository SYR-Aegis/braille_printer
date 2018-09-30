import csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import matplotlib.pyplot as plt

f=open('D:/data/students-academic-performance-dataset/xAPI-Edu-Data.csv','r')
csvReader=csv.reader(f)

raw=[]
data=[]
label=[]

for row in csvReader:
    raw.append(row)

for i in range(1,len(raw)):
    data.append([int(raw[i][9])])

for i in range(1,len(raw)):
    for j in range(len(raw[i])):
        if j==10 or j==11 or j==12:
            data[i-1].append(int(raw[i][j]))

for i in range(1,len(raw)):
    if raw[i][-1] == 'H':
        label.append(2)
    elif raw[i][-1] == 'M':
        label.append(1)
    else:
        label.append(0)

testf=[]
trainf=[]
testl=[]
trainl=[]
cnt=0

for i in range(len(data)):
    if i<=400:
        trainf.append(data[i])
    else:
        testf.append(data[i])
        
for i in range(len(label)):
    if i<=400:
        trainl.append(label[i])
    else:
        testl.append(label[i])

x=np.array(trainf)
y=np.array(trainl)

clf=LinearDiscriminantAnalysis(n_components=2)
result=clf.fit(x,y).transform(x)
pred=clf.predict(testf)

for i in range(len(pred)):
    if pred[i]==testl[i]:
        cnt+=1
    else:
        pass
    
print(cnt/len(testl))

colors=['navy','turquoise','darkorange']
lw=2

plt.figure()
for color, i, tl in zip(colors, [0,1,2], ['0','1','2']):
    plt.scatter(result[y==i,0],result[y==i,1],alpha=.8,color=color,label=tl)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()

print(result[trainl==1])











