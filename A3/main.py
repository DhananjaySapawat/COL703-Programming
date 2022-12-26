import sys
from collections import defaultdict
# Do not change the name of the function. 
# Do not use global variables as we will run your code on multiple test cases.
# 
def GiveFormula(inputString):
    formula = inputString.split('\n')
    for i in range(2,len(formula)):
        formula[i] = [int(x) for x in formula[i].split(' ')]
    return formula
def CheckHorn(formula):
    for f in formula[2:]:
        a = 0
        for i in f:
            if(int(i)>0):
                a = a + 1
        if(a>1):
            return False
    return True
def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]
def CNF2(formula):
    form = "c 2-CNF formula which is sat iff input is renamable Horn \n"
    form = form + ''.join(formula[1][:-1]) 
    tempformula = []
    for f in formula[2:]:
        if(len(f)>3):
            for i in range(len(f)-1):
                for j in range(i+1,len(f)-1):
                    tempformula.append([f[i],f[j],0])
        elif(len(f) == 2 and int(f[0]) < 0):
            pass
        else:
            tempformula.append(f)
    tempformula = removeDuplicates(tempformula)
    form = form + str(len(tempformula)) + "\n" 
    for i in tempformula:
        form = form + ''.join([str(x)+" " for x in i]) 
        form = form[:-1]+ "\n"
    return form

def checkReName(formula,m,n,i):
    if(i>m):
        return [False,formula]
    if(CheckHorn(formula) == True):
        return [CheckHorn(formula),formula]
    c1 = checkReName(formula,m,n,i+1)
    Formula2 = []
    for l in range(len(formula)):
        Formula2.append(formula[l][0:])
    for j in range(2,n+2):
        for k in range(len(Formula2[j])):
            if(abs(formula[j][k]) == i):
                Formula2[j][k] = -1*Formula2[j][k]
    c2 = checkReName(Formula2,m,n,i+1)
    if(c1[0] == True):
        return c1
    return c2
def ChangeVar(ogFormula,newformula):
    ans = []
    for i in range(2,len(newformula)):
        for k in range(len(newformula[i])):
            if(ogFormula[i][k] != newformula[i][k]):
                ans.append(abs(ogFormula[i][k]))
    var = []
    [var.append(x) for x in ans if x not in var]
    var.sort()
    change = ""
    for i in var:
        change = change + str(i) + " "
    return change[:-1]
def solve(inputString, n):
    #
    # Write your code here
    formula = GiveFormula(inputString)
    if(n==1):
        if(CheckHorn(formula) == True):
            return "horn"
        else:
            return "not horn"
    elif(n==2):
        return CNF2(formula)
    elif(n==3):
        if(CheckHorn(formula) == True):
            return "already horn"
        if(checkReName(formula,int(formula[1].split(' ')[-2]),int(formula[1].split(' ')[-1]),1))[0]:
            return "renamable" 
        else:
            return "not renamable"
    elif(n==4):
        if(CheckHorn(formula) == True):
            return "already horn"
        ogFormula = []
        for i in range (len(formula)):
            ogFormula.append(formula[i][0:])
        bool , newformula = checkReName(formula,int(formula[1].split(' ')[-2]),int(formula[1].split(' ')[-1]),1)
        if(bool == False):
            return "not renamble"
        else:
            return ChangeVar(ogFormula,newformula)

# Main function: do NOT change this.
if __name__=="__main__":
    inputFile = sys.argv[1] + '.cnf'
    n = int(sys.argv[2])
    with open(inputFile, 'r') as f:
        inputString = f.read()
    print(solve(inputString, n))
