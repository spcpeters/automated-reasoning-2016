######################################################
# To run this file, enter in command prompt:         #  
# .....\yices\bin\yices-smt -m test.smt > output.txt #
# Don't forget to change destp                       #
######################################################
import os
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

def manyVars(name, t, nr): #Makes "nr" amount of variables of type "t" called "name1", "name2" ... "namenr"
    for i in range(1,nr+1):
        newVar(name+str(i),t)
def runningtime(start,end,nr):
    for i in range(1,nr+1):
        writeLine("(=  "+str(end)+str(i)+ " (+ " +str(start) + str(i) +" " + str(i+5)+" ))",1)
def startGreaterThanZero(start,nr):
    for i in range(1,nr+1):
        writeLine("(>=  "+str(start)+str(i)+ " 0 )",1)
def beforeAfter(start,end):
    writeLine("(>= "+str(start) + " " + str(end)+" )",1)

def noOverlap(startA,endA,startB,endB,startC,endC):
    #A=Job5, B=Job10, C=Job7 ---> should start 5 and 10 before 7
    writeLine("( or (>= " + str(startA) + "  " + str(endB) +") (>= " + str(startB) + "  " + str(endA) +" ))",1)
    writeLine("( or (>= " + str(startC) + "  " + str(endA) +" ) (>= " + str(startA) + "  " + str(endC) +"))",1)
    writeLine("( or (>= " + str(startC) + "  " + str(endB) +" ) (>= " + str(startB) + "  " + str(endC) +") )",1)
   # writeLine("(>= " + str(startC) + "  " + str(endA) +" )",1)
    #writeLine("(>= " + str(startC) + "  " + str(endB) +" )",1)
      



destp = 'filling here'    
dest = 'filling here'
print "Start of writing"
with open(os.path.join(destp,dest), 'w') as f:

    startUp()

    #Enter any amount of NewVars here
    manyVars("startJob", "Int", 12)
    manyVars("endJob","Int",12)
    #end of varialbes

    writeLine("\n)",1)
    writeLine("", 1)
    writeLine(":formula (and", 1)

    # running time Job(i) = i + 5
    runningtime("startJob","endJob",12)
    # start time must >=0
    startGreaterThanZero("startJob",12)
    # End before start
    beforeAfter("startJob3","endJob1")
    beforeAfter("startJob3","endJob2")
    beforeAfter("startJob5","endJob3")
    beforeAfter("startJob5","endJob4")
    beforeAfter("startJob7","endJob3")
    beforeAfter("startJob7","endJob4")
    beforeAfter("startJob7","endJob6")
    #job 8 may not start early than job 5
    beforeAfter("startJob5","startJob8")

    beforeAfter("startJob9","endJob5")
    beforeAfter("startJob9","endJob8")
    beforeAfter("startJob11","endJob10")
    beforeAfter("startJob12","endJob9")
    beforeAfter("startJob12","endJob11")

    #job 5,7 and 10 can run at the same time ( should start job 5,10 before job 7 because 5,10 have dependency)
    noOverlap("startJob5","endJob5","startJob10","endJob10","startJob7","endJob7")

    # job 6 runs within duration of job 12
    beforeAfter("startJob6","startJob12")
    beforeAfter("endJob12","endJob6")
    writeLine("", 1)
    writeLine("))", 0)
    f.closed

print "End of writing. "
print "End of program"



  
