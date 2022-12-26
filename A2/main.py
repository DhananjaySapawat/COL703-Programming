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
def addList(list1,list2):
    hp = []
    for i in list1:
        hp.append(i)
    hp.append(list2)
    return hp
def giveValue(formula,proof,c1,c2,n):
    a = (c1[-1] =='f') and formula[int(c1[:-1])-1] or (proof[int(c1[:-1])-1])[2:]
    b = (c2[-1] =='f') and formula[int(c2[:-1])-1] or (proof[int(c2[:-1])-1])[2:]
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
    return ourProof
def GiveProof(formula,proof,i,currentProofs):
    if(i==len(proof)):
        return currentProofs
    newCurrentProof = []
    c = (proof[i][0] == '??') and proof[i][1] or proof[i][0]
    if(len(currentProofs) == 0):
        for j in range(3,len(formula)+1):
            if(proof[i][0] == '??'):
                newCurrentProof.append([[str(j)+'f',c]+giveValue(formula,currentProofs,c,str(j)+'f',int(formula[1][2])+1)])
            else:
                newCurrentProof.append([[c,str(j)+'f']+giveValue(formula,currentProofs,c,str(j)+'f',int(formula[1][2])+1)])
    for k in range(len(currentProofs)):
        for j in range(3,len(formula)+1):
            p = currentProofs[k]
            if(proof[i][0] == '??'):
                tp = [str(j)+'f',c]+giveValue(formula,p,c,str(j)+'f',int(formula[1][2])+1)
                newCurrentProof.append(addList(p,tp))
            else:
                tp = [c,str(j)+'f']+giveValue(formula,p,c,str(j)+'f',int(formula[1][2])+1)
                newCurrentProof.append(addList(p,tp))
        for j in range(1,len(currentProofs[k])+1):
            p = currentProofs[k]
            if(proof[i][0] == '??'):
                tp = [str(j)+'p',c]+giveValue(formula,p,c,str(j)+'p',int(formula[1][2])+1)
                newCurrentProof.append(addList(p,tp))
            else:
                tp = [c,str(j)+'p']+giveValue(formula,p,c,str(j)+'p',int(formula[1][2])+1)
                newCurrentProof.append(addList(p,tp))               
    return GiveProof(formula,proof,i+1,newCurrentProof)
def count(dp1,dp2):
    a = 0 
    for i in dp1:
        a = a + i
    for i in dp2:
        a = a + i
    return a
def helpSort(e):
    return e[1]
def givelength(arr):
    arr = arr[1:]
    s = 0
    for i in arr:
        s = s + len(i)
    return s
def giveBestAnswer(AllAnswer):
    AllAnswer.sort(key=lambda x: x[1])
    return AllAnswer[0][0]
def solve(formulaFile,proofFile,outputFile):
    formula = GiveTextFileData(formulaFile)
    proof = GiveTextFileData(proofFile)
    OutPutProof = GiveProof(formula,proof,0,[])
    AllAnswer = []
    for i in OutPutProof:
        if(len(i[-1])==3):
            dp1 = (len(formula)+1)*[0]
            dp2 = (len(proof)+1)*[0]
            dp1[0] = dp1[0] + givelength(i)
            for c in i:
                if(c[0][-1] == 'f'):
                    dp1[int(c[0][:-1])] = -5
                else:
                    dp1[int(c[0][:-1])] = -5
                if(c[1][-1] == 'p'):
                    dp1[int(c[1][:-1])] = -5
                else:
                    dp1[int(c[1][:-1])] = -5
                if(c[0] == c[1]):
                    dp1[0] = 10
                if(c[0][-1] == 'p' and c[1][-1] == 'p'):
                    dp1[0] = dp1[0]+0.5
            AllAnswer.append([i,count(dp1,dp2)])
    BestAnswer = giveBestAnswer(AllAnswer)
    with open(outputFile, 'w') as f:
        for s in BestAnswer:
            f.write(' '.join(map(str, s)))
            #print(' '.join(map(str, s)))
            f.write('\n')
def main():
    if(len(sys.argv) < 2):
        print('please give name of Formula file')
        return 0
    if(len(sys.argv) < 3):
        print('please give name of Proof file')
        return 0
    if(len(sys.argv) < 4):
        print('please give name of Output file')
        return 0
    formulaFile = sys.argv[1] + '.txt'
    proofFile = sys.argv[2] + '.txt'
    outputFile = sys.argv[3] + '.txt'
    solve(formulaFile,proofFile,outputFile)


if __name__=="__main__":
    main()