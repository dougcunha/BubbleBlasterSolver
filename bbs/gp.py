### Genetic Programming System
### By Paras Chopra
### http://www.paraschopra.com
### email: paras1987 [at] gmail [dot] com
### email: paraschopra [at] paraschopra [dot] com

## Note: You may use this Genetic Programming module in any way you wish
## But please do not forget to give me the credit which I deserve


from random import *
from math import *
from pickle import *
#Global

import board
import heuristics

class Variables:
    def __init__(self,VarList=[]):
        self.VarDict={}
        for variable in VarList:
            self.VarDict[variable]=0 #initially alot each variable a zero value
        
    def GetVal(self,var):
        
        if type(var)==type("String"):
            
            if self.VarDict.has_key(var):    
                return self.VarDict[var]
            else:
                return 0
        else:
            return var
    def SetVal(self,var,val):
        if self.VarDict.has_key(var):
            self.VarDict[var]=val
            

    def __len__(self):
        return len(self.VarDict)

    def keys(self):
        return self.VarDict.keys()

# NodeTypes
# LF:Leaf e.g constant or a varibele i.e it comprises of CS and VR
# CS:Constant e.g 1,2,3 etc. ,
# VR: variables A,B,C ,etc. and
# FN: Function eg. ADD, SUB, etc.

class Node:
    NodeTypes = {"FN":0,"LF":1,"CS":2, "VR":3}

    def __init__(self,Value=None,Nodes=[],Type="FN",FuncName=None,Variables=None):
        if Value=="random":
            self.Value=random()
        else:
            self.Value=Value
        self.Nodes=Nodes
        self.NodeValues=[]
        self.Type=self.NodeTypes[Type]
        self.FuncName=FuncName
        self.Variables=Variables
        self.Size=1
        self.Depth=1
        self.NodeId=1
        
    def GetNode(self,nodeno):
        self.SetNodeId()
        RetVal=self.GetNodeTemp(nodeno)
        return RetVal

    def SetNodeId(self,curnumber=1):
        self.NodeId=curnumber
        if self.Nodes:
            for i in range(0,len(self.Nodes)):
                curnumber=self.Nodes[i].SetNodeId(curnumber+1)
        return curnumber

    def GetNodeTemp(self,nodeno):
        if nodeno==self.NodeId:
            return self
        if self.Nodes:
            for i in range(0,len(self.Nodes)):
                if self.Nodes[i].GetNodeTemp(nodeno)!=None:
                    return self.Nodes[i].GetNodeTemp(nodeno)
            
        return None

    def SetNode(self,nodeno,CopyNode):
        if nodeno==self.NodeId:
            self=CopyNode
            return 1
        if self.Nodes:
            for i in range(0,len(self.Nodes)):
                reval=self.Nodes[i].SetNode(nodeno,CopyNode)
                if reval==1:
                    self.Nodes[i]=CopyNode

        return None

    def RecalSize(self):
        self.Size=1
        if self.Nodes:
            for Unit in self.Nodes:
                self.Size+=Unit.RecalSize()
        return self.Size

    def ReInit(self):
        self.SetNodeId()
        self.ReCalculate()
        
    def ReCalculate(self):
        self.Size=1
        self.Depth=1
        largest_depth=1
        if self.Nodes:
            for Unit in self.Nodes:
                Unit.ReCalculate()
                if Unit.Depth > largest_depth:
                    largest_depth=Unit.Depth
                self.Size+=Unit.Size
            self.Depth+=largest_depth
    
    def Eval(self):
        self.NodeValues[:]=[]
        if self.Type==self.NodeTypes["VR"]:
            return self.Variables.GetVal(self.Value)
        elif self.Type== self.NodeTypes["CS"]:
            return self.Value
        else:
            for Unit in self.Nodes:
                    self.NodeValues.append(Unit.Eval())
            return self.FuncName(self.NodeValues)

    def PrintTree(self):
        self.DrawTree(1)

    def DrawTree(self,level):
        kIndentText = "|  "
        IndentText=""
        for n in range(1,level):
            IndentText = IndentText+kIndentText
        self.NodeValues[:]=[]
        if self.Type==self.NodeTypes["VR"]:
            print IndentText+"+--["+self.Value+"]"
        elif self.Type==self.NodeTypes["CS"]:
            print IndentText+"+--["+str(self.Value)+"]"
        else:
            print IndentText+"+--"+self.FuncName.__name__
            for i in range(0,len(self.Nodes)):
                self.Nodes[i].DrawTree(level+1)
            
        
class Program:
    NodeTypes = {"FN":0,"LF":1,"CS":2, "VR":3}

    def RandomTree(self,depth):
        if depth==1:
            NodeUse=self.NodeTypes["FN"]
        elif depth==self.MaxDepth:
            NodeUse=self.NodeTypes["LF"]
        else:
            NodeUse=randint(0,1)
        if NodeUse==self.NodeTypes["FN"]:
            childFuncList=[]
            FuncToUse=randint(0,len(self.FuncDict)-1)

            for i in range(0,self.FuncDict.values()[FuncToUse]):
                child=self.RandomTree(depth+1)
                if not child:
                    print "Error: Child is nonetype"
                    break
                childFuncList.append(child)
            return Node(None,childFuncList,"FN",self.FuncDict.keys()[FuncToUse],self.Variables)
        else:
            #there is 50/50 chance that leaf would be variable or constant
            if randint(0,1)==0:
                #leaf would be constant
                TermToUse=randint(0,len(self.TerminalList)-1)
                return Node(self.TerminalList[TermToUse],None,"CS",None,self.Variables)
            else:
                #leaf would be a variable
                VarToUse=randint(0,len(self.Variables)-1)
                return Node(self.Variables.VarDict.keys()[VarToUse],None,"VR",None,self.Variables)
            

    def __init__(self,FuncDict,TerminalList,Variable=[],MaxDepth=10):
        self.MaxDepth=MaxDepth
        self.FuncDict=FuncDict
        self.TerminalList=TerminalList
        self.Fitness=0
        self.Variables=Variables(Variable)
        self.Tree=self.RandomTree(1)
        self.Tree.ReInit()
        
    def EvalTree(self):
        return self.Tree.Eval()

    def PrintTree(self):
        self.Tree.PrintTree()

    def Depth(self):
        return self.Tree.Depth

    def Size(self):
        return self.Tree.Size

    def AssignFitness(self,Fitness):
        self.Fitness=Fitness

    def GetNode(self,nodeno):
        return self.Tree.GetNode(nodeno)

    def SetNode(self,CopyNode,NodeNo):
        self.Tree.SetNode(NodeNo,CopyNode)

    def RetCopy(self):
        return self

class Programs:

    def __init__(self,FuncDict,TerminalList,Variable,MaxDepth=10,Population=100,MaxGen=100,ReqFitness=99,CrossRate=0.9,MutRate=0.1,BirthRate=0.2,HighFitness=100):
        self.Progs=[]
        self.MaxGen=MaxGen
        self.Population=Population
        self.ReqFitness=ReqFitness
        self.CrossRate=CrossRate
        self.MutRate=MutRate
        self.MaxFitness=0
        self.MaxFitnessProg=None
        self.BirthRate=BirthRate
        self.HighFitness=HighFitness
        self.MaxDepth=MaxDepth
        for i in range(0,Population):
            self.Progs.append(Program(FuncDict,TerminalList,Variable,MaxDepth))

    def MainLoop(self):
        for i in range(0,1+self.MaxGen):
            print "Generation no:",i
            for j in range(0,self.Population):
                CurFitness=FitnessFunction(self.Progs[j])
                self.Progs[j].AssignFitness(CurFitness)
                if CurFitness>self.MaxFitness:
                    self.MaxFitness=CurFitness
                    self.MaxFitnessProg=self.Progs[j]
                if self.MaxFitness>=self.ReqFitness:
                    print "Solution found."
                    self.Progs[j].PrintTree()
                    print "The fitness value is:",FitnessFunction(self.Progs[j])
                    return self.Progs[j]
            if random()>=(1-self.CrossRate):
                self.CrossOver()
                pass
            if random()>=(1-self.MutRate):
                self.Mutation()
                pass
            ### If you want confirmation to continue after each generation uncomment the following

            #ans=raw_input("Do you wanna quit? (1==Yes,0==No)")
            #print ans,":",type(ans)
            #if ans=="1":
                #break
            
        self.MaxFitness=0
        i=0
        for Unit in self.Progs:
            if Unit.Fitness>self.MaxFitness:
                best=Unit
                self.MaxFitness=best.Fitness
                best_number=i
            i+=1
        print "The end of all the generations."
        print "The best solution found is Program number: "+str(best_number)
        best.PrintTree()
        print "The fitness value is:",FitnessFunction(best)
        return best



    def CrossOver(self):
        Children=[] #list of children
        totalfitness=0
        for j in range(0,self.Population):
            totalfitness+=self.Progs[j].Fitness
        total_children=int(self.BirthRate*(self.Population/2)) #always an even number

        # One loop produces 2 children, therefore half the loops
        for i in range(0,total_children): # Selecting two parents for each child
            normal_children=0
            while not normal_children: #While offsprings are not normal
                accufitness=0
                RandFit=randint(0,totalfitness)
                for j in range(0,self.Population):
                    accufitness+=self.Progs[j].Fitness # Selecting most fit tree as parent, this random method favours more fit trees than lesser ones

                    if accufitness>=RandFit:
                        Parent1=loads(dumps(self.Progs[j]))
                        Parent1No=j
                        Parent1Point=randint(1,Parent1.Size())
                        break

                RandFit=randint(0,totalfitness)
                accufitness=0
                for j in range(0,self.Population):
                    accufitness+=self.Progs[j].Fitness # Selecting most fit tree as parent, this random method favours more fit trees than lesser ones

                    if accufitness>=RandFit:
                        Parent2=loads(dumps(self.Progs[j]))
                        Parent2No=j
                        Parent2Point=randint(1,Parent2.Size())
                        break


                Child1=Parent1.Tree.GetNode(Parent1Point)
                Child2=Parent2.Tree.GetNode(Parent2Point)
                Parent1.SetNode(Child2,Parent1Point)
                Parent2.SetNode(Child1,Parent2Point)
                Parent1.Tree.ReInit()
                Parent2.Tree.ReInit()

                #We check here if the depth of child tree is greater than maxdepth
                # then the child (Parent1) is not fit to live

                if (Parent2.Depth()<= self.MaxDepth) and (Parent1.Depth()<= self.MaxDepth): 
                    normal_children=1 #Both are normal_children

            Children.append(Parent1)
            Children.append(Parent2)
            
        for i in range(0,len(Children)):
            RandFit=randint(0,totalfitness)
            accufitness=0
            for j in range(0,self.Population):
                accufitness+=(self.HighFitness-self.Progs[j].Fitness) #Replacing parent trees with child trees and least fit old trees with parent trees
                if accufitness>=RandFit:
                    self.Progs[j]=loads(dumps(Children[i]))
                    self.Progs[j].Tree.ReInit()
                    break

    def Mutation(self):
        individno=randint(0,self.Population-1)
        randpoint=randint(1,self.Progs[individno].Size())
        randProg=self.Progs[individno].RandomTree(self.Progs[individno].Depth()-int(self.Progs[individno].Size()/self.Progs[individno].Depth()))
        self.Progs[individno].SetNode (randpoint,randProg)
        self.Progs[individno].Tree.ReInit()

    def RetCopy(self):
        return self

    
def ADD(ValuesList):
    sumtotal=0
    for val in ValuesList:
        sumtotal=sumtotal+val
    return sumtotal

def SUB(ValuesList):
    return ValuesList[0]-ValuesList[1]

def MUL(ValuesList):
    return ValuesList[0]*ValuesList[1]

def DIV(ValuesList):
    if ValuesList[1]==0: #This is protected division i.e. if a number is divided by 0 the result is 1
        return 1
    return ValuesList[0]/ValuesList[1]

def COS(Value):
    return cos(Value[0])

def RANDINT(ValuesList): #return a random integer between ranges a,b
    if ValuesList[1]<ValuesList[0]:
        return randint(ValuesList[1],ValuesList[0])
    return randint(ValuesList[0],ValuesList[1])

def RANDOM(ValuesList):
    return random()

def X(ValuesList):
    return 100

def DummyFunc():
    pass

# You just need to modify this function to generate trees of your own choice
def FitnessFunction(Prog):

    #testing fitness on 10 different X and then averaging the result
    
    b = board.newboard(
    """
    4 2 2 2 1
    0 4 1 3 4
    0 4 0 3 4
    2 0 0 1 4
    3 4 0 4 2
    1 1 0 4 1
    """)
    max_fit = heuristics.sumOfUndropedBubbles(b)
    fitness = 0
    for i in range(1,5):
        Prog.Variables.SetVal("b",b) # Set the values of the variables
        retvalue=Prog.EvalTree()
        if (len(retvalue) == 2) and isinstance(retvalue[0], int) and isinstance(retvalue[1], int):
            board.touch(b, retvalue)
        fitness = heuristics.sumOfUndropedBubbles(b)
    
    score = (max_fit - fitness)
    if score == 0: 
        return 0
    else: 
        return int(((1 - (1.0 / score)) * 100))
    
def symbolic_regression(x):
    return(x*x+x+1)

def SELECTPLACE(ValuesList):
    d = None
    if isinstance(ValuesList[0], dict):
        d = ValuesList[0]
    if isinstance(ValuesList[1], dict):
        d = ValuesList[1]

    if d:
        if len(d) > 0:
            return choice(d.keys())
        else:
            return (0,0)       
        
    return (ValuesList[0], ValuesList[1])
    

### Problem Description
# We will try to evolve a tree for Symbolic Regression of a Quadratic Polynomial
# That is the fitness function x^2+x+1 in the range of -1 to 1


if __name__=="__main__":
    #pr=Programs({ADD:2,SUB:2,MUL:2,DIV:2},range(-1,2),["X"],10,50,100)
    # pr=Programs({ADD:2,SUB:2,MUL:2,DIV:2},["random"],["X"],5,100,100)
    pr=Programs({SELECTPLACE:2},range(0, 5),["b"],10,50,100)
    pr.MainLoop()
    wait=raw_input("Press any key to terminate....")

#### Sample Usage example
# prg = Programs({COS:1,RANDOM:0}, [1,2],["A","B"])

#### Syntax of the program
# pr=Programs(FuncDict,TerminalList,Variable,MaxDepth=10,Population=100,MaxGen=100,ReqFitness=99,CrossRate=0.9,MutRate=0.1,BirthRate=0.2,HighFitness=100)
# pr.MainLoop()

# pr=Prograns( {function1: no_of_arguments_of_function,...} , [list of leafs or constants], [list of variable names] )

### Description of arguments

# FuncDictis the dictionary of actual function names and the number of arguments it takes 
# TerminalList is the list of terminal constants possible in the tree e.g. [1,2,5,6] or range(5,11) or [1,2,"random"[]
# "random" in the Terminal List produces a number between 0 and 1 and e.g. 0.257522 or 0.444621
# Variable is a list of possible variables in the tree e.g. ["X","Y"] or ["A","B"]
# It is the responsibility of fitness function to supply values to the variables by using syntax:
# Prog.Variables.SetVal(Variable_Name,Variable_Value) e.g Prog.Variables.SetVal("X",10)
# MaxDepth is the maximum depth allowed for the initial trees
# Population is population in each generation. It starts from 0 to 99 i.e If u want 100 individuals then pass 99 as parameter
# MaxGen is the maximum number of generations until the evolution is aborted
# ReqFitness is the fitness level above which if any program is possesing fitness the program is terminated
# In the default case it is 99, i.e if any program has fitness greater than 99, the evolution is aborted and the candidate is termed as best
# CrossRate is the crossover rate, its default value is 0.9 i.e. the crossover is bound to happen 90% of time
# MutRate is the rate of mutation
# BirthRate is the number of new individuals produced per unit of population
# Its default value is 0.2 i.e if the population is 100 then 20 children will be produced per crossover operation
# HighFitness is the highest fitness attainable by the candidate, in default case it is 100
# MaxGen is maximum number of generations
# BirthRate is no of offsprings per 100 population e.g. if BirthRate is 2 and population of current population is 100 then in the next generation only 2 offsprings will be produced

#### Sample Usage example
# prg = Programs({COS:1,RANDOM:0}, [1,2],["A","B"])

#### To define functions of your own
# The functions used in the trees are real world python functions
# So of you want to add a new function such as power(a,b) i.e to calculate a^b
# use the following synatx

def POWER(ValuesList):
    ans=ValuesList[0]
    if ValuesList[1]<0:
        return 0
    for i in range(0,ValuesList[1]):
        ans=ans*ValuesList[0]
    return ans

# The fuctions which you will define will always contain only one argument which is ValuesList
# ValuesList is the list of values passed to the function
# In the present case of a^b ValuesList will contain values of a and b
# So ValuesList[0] will represent the first value i.e a
# and ValuesList[1] will represent the second value i.e b

# If your function takes three values then you will also use ValuesList[2]
# If your function does not takes any values such as RANDOM() then the list will be empty

# But observe that only one value can be returned from the function


### Note
# You may also use this module to create instancesof many GPs running simultaneously
# Or use it to run GP elsewhere in your program

