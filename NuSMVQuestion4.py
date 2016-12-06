
def writeLine(line, i):
    if i==1:
        f.write(str(line)+'\n')
    else:
        f.write(str(line)+" ")
def startUp():
    writeLine("MODULE main",1)
    writeLine("VAR",1)
    writeLine("",1)
def newVar(name,value):
	writeLine(str(name) + " : " + str(value) + " ;",1)
def INITvar(name,nr):
	writeLine("INIT",1)
	for i in range (1,nr):
		writeLine(name+str(i) + " = " + str(i) + " & ",0)
	writeLine(name+str(nr) + " = " + str(nr),1)
def TRANS(name,nr):
	writeLine("TRANS",1)
	for i in range (2,nr):
		writeLine("(",0)
		writeLine("next("+str(name)+str(i)+")"+" = " + str(name)+str(i-1) + " + " + str(name)+str(i+1),0)
		for j in [ k for k in range (1,nr+1) if k!=i]:
			writeLine(" & next("+str(name)+str(j)+")"+" = " + str(name)+str(j),0)
		writeLine(")",0)
		if i!=nr-1:
			writeLine(" |",1)
		else:
			writeLine("",1)



filename="NuSMV_Question4.nusmv"
print "Start of writing"

with open(filename, 'w') as f:
	startUp()
	for i in range (1,9):
		newVar("a"+str(i),"1..100")
	INITvar("a",8)
	TRANS("a",8)
	#4.a
	#writeLine("LTLSPEC G !((a3 = a7))",1)
	#4.b
	writeLine("LTLSPEC G !((a3 = a5) & (a5 = a7))",1)

