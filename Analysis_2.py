import os
import matplotlib.pyplot as plt
import matplotlib.colors as colors
def writeLine(line, i):
    if i==1:
        f.write(str(line)+'\n')
    else:
        f.write(str(line)+" ")
def makeDict(content):
	for text in content:
		if len(text) >5:
			text=text.replace(")","")
			text=text.replace("(","")
			text=text.replace("=","")
			l=text.split()
			if l[0][0]=="X" or l[0][0]=="Y" or l[0][0]=="r":
				resultDict[l[0]]=l[1]
dest = 'filling here'
destp = 'filling here'    
openfile='output2.txt'
rec=[(0,0),(4,5),(4,6),(5,20),(6,9),(6,10),(6,11),(7,8),(7,12),(10,10),(10,20),(4,3),(4,3)]
colors=['#6495ED','#EE82EE','#D8BFD8','#008080','#2E8B57','#BC8F8F','#CD853F','#DB7093','#9400D3','#6B8E23','#C71585','#C71585']
f= open(os.path.join(openfile), 'r')
content=f.readlines()
content.sort()

resultDict={}
makeDict(content)

rectangulars=[]
for i in range(1,13):
	if int(resultDict["r"+str(i)])==0:
		rectangulars.append((int(resultDict["X"+str(i)]),int(resultDict["Y"+str(i)]),rec[i][0],rec[i][1]))
	if int(resultDict["r"+str(i)])==1:
		rectangulars.append((int(resultDict["X"+str(i)]),int(resultDict["Y"+str(i)]),rec[i][1],rec[i][0]))

plt.axes()
plt.ylim([0,30])
plt.xlim([0,30])
for index,i in enumerate(rectangulars):
	print index,i
	rectangle = plt.Rectangle((i[0], i[1]), i[2], i[3], fc=colors[index],fill=True)
	plt.gca().add_patch(rectangle)
	plt.annotate((str(i[2]) + "x" + str(i[3])), xy=(i[0],i[1]))


#plt.axis('scaled')
plt.show()

print rectangulars

