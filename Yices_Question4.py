def writeLine(line, i):
    if i==1:
        f.write(str(line)+'\n')
    else:
        f.write(str(line)+" ")
def newVar(name, t):
    writeLine("("+str(name)+" "+str(t)+")", 0)
def manyVars(name, t, nr,NrStep): #Makes "nr" amount of variables of type "t" called "name1", "name2" ... "namenr"
    for i in range(1,nr+1):
        for j in range (0,NrStep+1):
            newVar(name+str(i)+str(j),t)
def OneStep(name,step,nr): # one transition: e.g. a12 ( a1 is variable and 2 is the step)
    writeLine("( or ",1)
    for var in range (2,nr):
        writeLine("( and ",0)
        writeLine("(= "+str(name)+str(var)+str(step)+" "+"(+ " + str(name)+str(var-1)+str(step-1) +" "+ str(name)+str(var+1)+str(step-1)+")) ",0)
        for j in [k for k in range (1,nr+1) if k!=var]:
            writeLine("(= "+str(name)+str(j)+str(step)+" "+ str(name)+str(j)+str(step-1)+" )",0)
        writeLine(")",1)
    writeLine(")",1)
def TRANs(name,NrSteps,nr):
    for i in range (1,NrSteps+1):
        OneStep(name,i,nr)

def startUp():
    writeLine("(benchmark "+filename,1)
    writeLine(":logic QF_UFLIA",1)
    writeLine("",1)
    writeLine("",1)
    writeLine("",1)
    writeLine(":extrafuns (",1)
def INITvar(name,nr):
    for i in range (1,nr+1):
        writeLine("(=  "+str(name)+str(i)+str(0) + " " + str(i)+" )",1)

filename="SMT_Question4.smt"
print "Start of writing"
NrSteps=10
NrOfVar=8
with open(filename, 'w') as f:
    startUp()
    #Enter any amount of NewVars here
    manyVars("a","Int",NrOfVar,NrSteps)
    #end of varialbes

    #Start of constraints
    writeLine("\n)",1)
    writeLine("", 1)
    writeLine(":formula (and", 1)

    # initial values
    INITvar("a",NrOfVar)
    # Transition
    TRANs("a",NrSteps,NrOfVar)
    # Uncomment either 4.a or 4.b to run
    #4.a
    #riteLine("(= a3"+str(NrSteps)+" "+"a7"+str(NrSteps) +")",1)
    #4.b
    writeLine("(= a3"+str(NrSteps)+" "+"a5"+str(NrSteps) +" "+"a7"+str(NrSteps) +")",1)

    # End of constraints
    writeLine("", 1)
    writeLine("))", 0)
    f.closed


