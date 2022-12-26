import sys
def GiveTextFileData(file):
    with open(file,'r') as f:
        fileData = f.readlines()
    for i in range(len(fileData)):
        fileData[i] = fileData[i].strip().split()
    return fileData
def checkTwoArray(array1,array2):
    array1.sort()
    array2.sort()
    return array1==array2 and True or False
def check(p,formula,proof,n):
    a = (p[0][-1] =='f') and formula[int(p[0][:-1])-1] or (proof[int(p[0][:-1])-1])[2:]
    b = (p[1][-1] =='f') and formula[int(p[1][:-1])-1] or (proof[int(p[1][:-1])-1])[2:]
    dp1 = [0]*n 
    dp2 = [0]*n 
    for i in a:
        if(int(i)>=0):
            dp1[int(i)] += 1
        else:
            dp2[-int(i)] += 1
    for i in b:
        if(int(i)>=0):
            dp1[int(i)] += 1
        else:
            dp2[-int(i)] += 1
    ourProof = []
    for i in range(1,n):
        if (dp1[i] > 0 and dp2[i]==0):
            ourProof.append(i)
        elif(dp1[i]==0 and dp2[i]>0):
            ourProof.append(-i)
    ourProof.append(0)
    pro = list(map(int,p[2:]))
    return checkTwoArray(ourProof,pro)
def CheckProof(formula,proof):
    for p in proof:
        if(check(p,formula,proof,int(formula[1][2])+1) == False):
            return False
    return True

def main():
    if(len(sys.argv) < 2):
        print('please give name of Formula file')
        return 0
    if(len(sys.argv) < 3):
        print('please give name of Proof file')
        return 0
    formulaFile = sys.argv[1]
    proofFile = sys.argv[2]
    formula = GiveTextFileData(formulaFile+'.txt')
    proof = GiveTextFileData(proofFile+'.txt')
    if(int(proof[-1][2]) != 0):
        print("incorrect")
        return 0
    print(CheckProof(formula,proof) and "correct" or "incorrect")


if __name__=="__main__":
    main()