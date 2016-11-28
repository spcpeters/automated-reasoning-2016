######################################################
# To run this file, enter in command prompt:         #  
# .....\yices\bin\yices-smt -m test.smt > output.txt #
# Don't forget to change destp                       #
######################################################

def writeLine(line, i):
    if i==1:
        f.write(str(line)+'\n')
    else:
        f.write(str(line)+" ")

def startUp():
    writeLine("(benchmark "+dest,1)
    writeLine(":logic QF_UFLIA",1)
    writeLine("",1)
    writeLine("",1)
    writeLine("",1)
    writeLine(":extrafuns (",1)

def newVar(name, t):
    writeLine("("+str(name)+" "+str(t)+")", 0)

def constraint(c, a, b):
    return ("("+str(c)+" "+str(a)+" "+str(b)+")")

def manyVars(name, t, nr): #Makes "nr" amount of variables of type "t" called "name1", "name2" ... "namenr"
    for i in range(1,nr+1):
        newVar(name+str(i),t)

def manyCons(c, a, b, nr):
    for i in range(1,nr+1):
        writeLine(constraint(c,str(a)+str(i),str(b)),1)

def stackTrucks(nr):
    for i in range (1,nr+1):
        writeLine(constraint("<=", "(+ (* truckN"+str(i)+" 700) (* truckP"+str(i)+" 400) (* truckS"+str(i)+" 1000) (* truckC"+str(i)+" 2500) (* truckD"+str(i)+" 200))",8000),1)
        writeLine(constraint("<=", "(+ truckN"+str(i)+" truckP"+str(i)+" truckS"+str(i)+" truckC"+str(i)+" truckD"+str(i)+")",8),1)
    
def matLimit(nr, mat, lim):
    writeLine("(= (+",0)
    for i in range (1,nr+1):
        writeLine("truck"+str(mat)+str(i),0)
    writeLine(") "+str(lim)+")",1)
def notTogether(a,b,nr):
    for i in range (1,nr+1):
        #writeLine("( or (and (> " + str(a) + str(i) + " 0) (= " + str(b) +str(i) +" 0)) (and (> "+str(b)+str(i)+" 0) (= "+str(a) +str(i)+" 0)) (and (= "+str(b)+str(i)+" 0) (= "+str(a) +str(i)+" 0)) )", 1) 
        writeLine("( or (implies (> " + str(a) + str(i) + " 0) (= " + str(b) +str(i) +" 0)) (implies (> "+str(b)+str(i)+" 0) (= "+str(a) +str(i)+" 0)) )", 1) 


destp = 'E:\\yices\\bin\\'    
dest = 'test.smt'
x=3

print "Start of writing"
with open(destp+dest, 'w') as f:
    
    startUp()

    #Enter any amount of NewVars here
    manyVars("truckN", "Int", 8)
    manyVars("truckP", "Int", 8)
    manyVars("truckS", "Int", 8) 
    manyVars("truckC", "Int", 8)
    manyVars("truckD", "Int", 8)
    #End of variables

    writeLine("\n)",1)
    writeLine("", 1)
    writeLine(":formula (and", 1)

    #Enter any amount of constraints here
    stackTrucks(8) #Max weight can't go over a certain value, can only carry a certain amount of packets
    manyCons(">=","truckN",0,8) #Can't carry negative amounts
    manyCons(">=","truckP",0,8) 
    manyCons(">=","truckS",0,8) 
    manyCons(">=","truckC",0,8) 
    manyCons(">=","truckD",0,8) 
    matLimit(8,"N",4)
    matLimit(8,"S",8)
    matLimit(8,"C",10)
    matLimit(8,"D",20)
    manyCons("=","truckS",0,5) #Skipples need to be cooled; only three of the eight trucks have facility for cooling skipples.
    manyCons("<","truckN",2,8) #Nuzzles are very valuable: to distribute the risk of loss no two pallets of nuzzles may be in the same truck.
    
    #1.bthat prittles and crottles are an explosive combination
    #uncommment to enable 1.b --> max is 20
    notTogether("truckP","truckC",8)
    
    matLimit(8,"P",20) #Max needs to be determined. Experimental results show 22.
    #End of constraints

    writeLine("", 1)
    writeLine("))", 0)
    f.closed

print "End of writing. "

#with open(destp+dest, 'r') as f:
    #for line in f:
        #print line
    #f.closed

print "End of program"
