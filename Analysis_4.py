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
			text=text.replace("(","")
			text=text.replace("=","")
			l=text.split()
			resultArray[l[0]]=l[1]
  
openfile='output4.txt'
destp='Analysis_4.txt'

f= open(openfile, 'r')
content=f.readlines()
content.sort()

resultArray={}
makearray(content)
with open(destp, 'w') as f:
	writeLine("a(ij) with a(i) is the variable and j is the step j(th)")
	for j in range (1,9):
		for i in range (0,len(resultArray)/8):
		#writeLine("Step: "+str(i),1)
		
			writeLine("a"+str(j)+str(i)+"="+str(resultArray["a"+str(j)+str(i)])+"\t",0)
		writeLine("",1)