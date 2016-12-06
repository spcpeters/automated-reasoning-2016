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
    writeLine(":logic QF_UFLRA",1)
    writeLine("",1)
    writeLine("",1)
    writeLine("",1)
    writeLine(":extrafuns (",1)

def newVar(name, t):
    writeLine("("+str(name)+" "+str(t)+")", 0)

def con(c, a, b, e="na", f="na", g="na", h="na",x="na",z="na"): #Extended function, can take 2-6 inputs
    if(e=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+")")
    elif(f=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" )")
    elif(g=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" "+str(f)+" )")
    elif(h=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" "+str(f)+" "+str(g)+" )")
    elif (x=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)+" )")
    elif (z=="na"):
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)+" "+str(x)+" )")
    else:
        return ("("+str(c)+" "+str(a)+" "+str(b)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)+" "+str(x)+" "+str(z)+" )")


def manyVars(name, t, nr): #Makes "nr" amount of variables of type "t" called "name1", "name2" ... "namenr"
    for i in range(1,nr+1):
        newVar(name+str(i),t)

def manyCons(c, a, b, nr): #Only works for binary for now...
    for i in range(1,nr+1):
        writeLine(con(c,str(a)+str(i),str(b)),1)

def setArrays(a, arr, nr, list):
    for i in range(1,nr+1):
        writeLine(con("=","("+str(a)+str(i)+" "+str(arr)+")",str(list[i-1])),0)
    f.write("\n")


#destp = 'E:\\yices\\bin\\'    
dest = 'assignment2_v2.smt'
rec=[(0,0),(4,5),(4,6),(5,20),(6,9),(6,10),(6,11),(7,8),(7,12),(10,10),(10,20),(4,3),(4,3)] #only take value from rec[1] - rec[12]
print "Start of writing"
with open(dest, 'w') as f:
    
    startUp()

    #Enter any amount of NewVars here

    manyVars("X", "Real", 12) #c11 and c12 are the power components
    manyVars("Y", "Real", 12)
    manyVars("W","Real Real",12) #They are arrays, W[0] = H[1] = given width; H[0] = W[1] = given height
    manyVars("H","Real Real",12)
    manyVars("r","Real",12)
    
    #End of variables

    writeLine("\n)",1)
    writeLine("", 1)
    writeLine(":formula (and", 1)

    #Enter any amount of constraints here
    '''
    #Set the sizes
    setArrays("W","0",12,[4, 4, 5, 6, 6, 6, 7, 7, 10, 10, 4, 4])
    setArrays("H","0",12,[5, 6, 20, 9, 10, 11, 8, 12, 10, 20, 3, 3])
    setArrays("W","1",12,[5, 6, 20, 9, 10, 11, 8, 12, 10, 20, 3, 3])
    setArrays("H","1",12,[4, 4, 5, 6, 6, 6, 7, 7, 10, 10, 4, 4])
    '''
    #Everything fits on the grid:
    #Forall comps: (0 <= X && X+w[r] <= 30 && 0 <= Y && Y+h[r] <= 30)
    for i in range(1,13): #For all components...
        
        #clearly identify value of [W 1] [W 0] [H 1] [H 0]
        writeLine(con("and",
        con("=","(W"+str(i)+" 0)",rec[i][0]),
        con("=","(W"+str(i)+" 1)",rec[i][1]),
        con("=","(H"+str(i)+" 0)",rec[i][1]),
        con("=","(H"+str(i)+" 1)",rec[i][0])
        ),1)
        

        writeLine(con("and", 
        con("<=",0,"X"+str(i)), #0 <= X
        con(">=",30,con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")")), #30 >= X+w
        con("<=",0,"Y"+str(i)), #0 <= Y
        con(">=",30,con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")")), #30 >= Y+h
        ),1) 
    #rotation is either 0 or 90 (180 and 270 are isomorphic)
        
        writeLine(con("or", #We're still looping over all components, so...
        con("=","r"+str(i),0), #r = 0 OR
        con("=","r"+str(i),1) #r = 1
        ),1)
        
    
        
    #No overlap:
    #Pretty much as described in the slides
    for i in range(1,13): #For all components...
        for j in range(1,13): #And every other component...
            if i!=j: #That is different... (This generates 132 constraints!)
                #i must be either to the left of j, to the right of j, above j, or underneath j
                writeLine(con("or",
                con("<=",con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")"),"X"+str(j)), #Xi + Wi <= Xj
                con("<=",con("+","X"+str(j),"(W"+str(j)+" r"+str(j)+")"),"X"+str(i)), #Xj + Wj <= Xi
                con("<=",con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")"),"Y"+str(j)), #Yi + Hi <= Yj
                con("<=",con("+","Y"+str(j),"(H"+str(j)+" r"+str(j)+")"),"Y"+str(i))  #Yj + Hj <= Yi
                ),1)
    
    #Centers of power must be at least 17 apart
    #IOW: Xa-Xb >=17 OR Xb-Xa >=17 OR Ya-Yb >=17 OR Yb-Ya >=17
    '''
    writeLine(con("or",
    con(">=",con("-","X11","X12"),17),
    con(">=",con("-","X12","X11"),17),
    con(">=",con("-","Y11","Y12"),17),
    con(">=",con("-","Y12","Y12"),17),
    ),1)
    '''
    writeLine(con("or",

    con(">=",con("-",con("ite","(= 0 r11)","(+ X11 2)", "(+ X11 1.5)"),con("ite","(= 0 r12)","(+ X12 2)", "(+ X12 1.5)")),17), 
    # X11 - X12 >=17 with if (r11 = 0) x11 + 2 else X11 + 1.5. If (r12 = 1)  X12 + 2, else X12 +1.5
    con(">=",con("-",con("ite","(= 0 r12)","(+ X12 2)", "(+ X12 1.5)"),con("ite","(= 0 r11)","(+ X11 2)", "(+ X11 1.5)")),17),

    con(">=",con("-",con("ite","(= 0 r11)","(+ Y11 1.5)", "(+ Y11 2)"),con("ite","(= 0 r12)","(+ Y12 1.5)", "(+ Y12 2)")),17),
    con(">=",con("-",con("ite","(= 0 r12)","(+ Y12 1.5)", "(+ Y12 2)"),con("ite","(= 0 r11)","(+ Y11 1.5)", "(+ Y11 2)")),17),
    ),1)

  
    
    #NOTE: We only check if their origin points at 17 apart. Is this a problem, considering they have constant size?

    #Every component must be adjacent to a power component
    for i in range(1,11): #For all non-power components...
        writeLine(con("or", #It needs to either...
        con("or",
        #Have it align horizontally with c11:
        con("and",
        con(">=",con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")"),"X11"), #Xi+Wi >= X11
        con(">=",con("+","X11","(W11 r11)"),"X"+str(i)), #X11+W11 >= Xi
        con("or", con("=",con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")"),"Y11"), con("=",con("+","Y11","(H11 r11)"),"Y"+str(i))) #(Yi+Hi+1==Y11 OR Y11+H11+1==Yi) 
        ),
        #Have it align vertically with c11: 
        con("and",
        con(">=",con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")"),"Y11"), #Yi+Hi >= Y11
        con(">=",con("+","Y11","(H11 r11)"),"Y"+str(i)), #Y11+H11 >= Yi
        con("or", con("=",con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")"),"X11"), con("=",con("+","X11","(W11 r11)"),"X"+str(i))) #(Xi+Wi+1==X11 OR X11+W11+1==Xi) 
        )), 
        #OR it could do the same things with c12....
        con("or",
        #Have it align horizontally with c12
                con("and",
        con(">=",con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")"),"X12"), #Xi+Wi >= X12
        con(">=",con("+","X12","(W12 r12)"),"X"+str(i)), #X12+W12 >= Xi
        con("or", con("=",con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")"),"Y12"), con("=",con("+","Y12","(H12 r12)"),"Y"+str(i))) #(Yi+Hi+1==Y12 OR Y12+H12+1==Yi) 
        ),
        #Have it align vertically with c12: 
        con("and",
        con(">=",con("+","Y"+str(i),"(H"+str(i)+" r"+str(i)+")"),"Y12"), #Yi+Hi >= Y12
        con(">=",con("+","Y12","(H12 r12)"),"Y"+str(i)), #Y12+H12 >= Yi
        con("or", con("=",con("+","X"+str(i),"(W"+str(i)+" r"+str(i)+")"),"X12"), con("=",con("+","X12","(W12 r12)"),"X"+str(i))) #(Xi+Wi+1==X12 OR X12+W12+1==Xi) 
        ), )
        ),1)
    

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
