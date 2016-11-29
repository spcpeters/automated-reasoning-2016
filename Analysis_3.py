import os
def writeLine(line, i):
    if i==1:
        f.write(str(line)+'\n')
    else:
        f.write(str(line)+" ")
def makearray(content):
	for text in content:
		if len(text) >5:
			text=text.replace(")","")
			l=text.split()
			resultArray[l[1]]=l[2]
dest = 'filling here'
destp = 'filling here'    
openfile='output2.txt'

f= open(os.path.join(destp,openfile), 'r')
content=f.readlines()
content.sort()

resultArray={}
makearray(content)
with open(os.path.join(destp,dest), 'w') as f:
	writeLine("\t"+"startJob"+"\t"+"endJob",1)
	for i in range (1,13):
		writeLine(str(i),0)
		writeLine("\t"+str(resultArray["startJob"+str(i)]),0)
		writeLine("\t"+str(resultArray["endJob"+str(i)])+" ",1)


