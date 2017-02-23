from tkinter import *
import csv
from tkinter import filedialog
import string
from tkinter import messagebox
import random
#Comment: csv file has to be in this format: name, meld, OPTN, 1A status, 1B status
# add counter
# 6 hours parameter
# time frame assignment
# Decision time
# skip to next patient in the boundary region if the next highest meld score patient is too far away.
# decision to optimize the cureent system


class Simulator:
    def __init__(self):
        Window=Tk()
        Window.title("UNOS Liver Organ Transplant Simulator")
        self.var1 = StringVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.window1 = Frame(Window).grid()
        Label(self.window1, text="MELD score File").grid(row =0, column = 0)
        Label(self.window1, text="OPO region").grid(row=1,column=0,columnspan=2)
        Label(self.window1, text="Liver risk factor").grid(row=1,column=2,columnspan=2)
        
        Entry(self.window1, textvariable=self.var1, state="readonly").grid(row=0, column=1, columnspan=2)
        Entry(self.window1, textvariable=self.var2).grid(row=2,column=0,columnspan=2)
        Entry(self.window1, textvariable=self.var3).grid(row=2,column=2,columnspan=2)
        
        Button(self.window1, text="Select Patient Data", command=self.openDataClicked).grid(row=0, column=4)
        Button(self.window1, text="Calculate", command=self.Calc).grid(row=3,column=0,columnspan=4,sticky=W+E+N+S)

        OPORegion={}
        x=1
        for i in range(0,59):
            OPORegion[i]=x
            if x==11:
                x=1

        Window.mainloop()       
    def openDataClicked(self):
        self.fileName = filedialog.askopenfilename()
        self.var1.set(self.filename)

        self.Meld35 = {}
        for i in range(35,41):
            self.Meld35[i]=[]
        self.Meld1A = []
        self.Meld1B = []
        self.Meld15 = {}
        for i in range(15,35):
            self.Meld15[i]=[]
        self.Meld = {}
        for i in range(1,15):
            self.Meld15[i]=[]
        
        f=csv.reader(open(self.fileName,"r"),delimiter=",")
        for row in f:
            row = (row[0],int(row[1]),int(row[2]),row[3],row[4])
            if row[3].lower() == "true":
                self.Meld1A.append(row)
            elif row[4].lower() == "true":
                self.Meld1B.append(row)
            else:
                if row[1] >= 35:
                    self.Meld35[row[1]].append(row)
                elif row[1] >= 15:
                    self.Meld15[row[1]].append(row)
                else:
                    self.Meld[row[1]].append(row)
        self.Meld1A = sorted(self.Meld1A, key=lambda pt: pt[1], reverse=TRUE)
        self.Meld1B = sorted(self.Meld1B, key=lambda pt: pt[1], reverse=TRUE)
    def Calc(self):
        aListofPatient=[]
        region = self.var2.get()
        risk = self.var3.get()
        # 1A status in UNOS region
        for i in range(0,len(self.Meld1A)):
            if OPORegion[self.Meld1A[i][2]] == OPORegion[region] and riskCalc(self.Meld1A[i][1],risk):
                return self.Meld1A[i]
        for i in range(0,len(self.Meld1B)):
            if OPORegion[self.Meld1B[i][2]] == OPORegion[region] and riskCalc(self.Meld1A[i][1],risk):
                return self.Meld1B[i]
        # MeldScore 40 to 35 in region first then UNOS
        for i in range(40,34,-1):
            for j in range(0,len(self.Meld35[i])):
                if self.Meld35[i][j][2] == region and riskCalc(self.Meld35[i][j][1],risk):
                    return self.Meld35[i][j]
            for j in range(0,len(self.Meld35[i])):
                if OPORegion[self.Meld35[i][j][2]] == OPORegion[region] and riskCalc(self.Meld35[i][j][1],risk):
                    return self.Meld35[i][j]
        # MeldScore 15 to 35 in region first then UNOS
        for i in range(34,14,-1):
            for j in range(0,len(self.Meld15[i])):
                if self.Meld15[i][j][2] == region and riskCalc(self.Meld15[i][j][1],risk):
                    return self.Meld15[i][j]
            for j in range(0,len(self.Meld15[i])):
                if OPORegion[self.Meld15[i][j][2]] == OPORegion[region] and riskCalc(self.Meld15[i][j][1],risk):
                    return self.Meld15[i][j]
        # 1A status in nation
        for i in range(0,len(self.Meld1A)):
            if OPORegion[self.Meld1A[i][2]] != OPORegion[region] and riskCalc(self.Meld1A[i][1],risk):
                return self.Meld1A[i]
        for i in range(0,len(self.Meld1B)):
            if OPORegion[self.Meld1B[i][2]] != OPORegion[region] and riskCalc(self.Meld1A[i][1],risk):
                return self.Meld1B[i]
        # MeldScore 15 to 35 in Nation
        for i in range(34,14,-1):
            for j in range(0,len(self.Meld15[i])):
                if OPORegion[self.Meld15[i][j][2]] != OPORegion[region] and riskCalc(self.Meld15[i][j][1],risk):
                    return self.Meld15[i][j]
        # MeldScore less than 15
        for i in range(34,14,-1):
            for j in range(0,len(self.Meld15[i])):
                if self.Meld[i][j][2] == region and riskCalc(self.Meld[i][j][1],risk):
                    return self.Meld[i][j]
            for j in range(0,len(self.Meld15[i])):
                if OPORegion[self.Meld[i][j][2]] == OPORegion[region] and riskCalc(self.Meld[i][j][1],risk):
                    return self.Meld[i][j]
            for j in range(0,len(self.Meld15[i])):
                if OPORegion[self.Meld[i][j][2]] != OPORegion[region] and riskCalc(self.Meld[i][j][1],risk):
                    return self.Meld[i][j]
                    
    def riskCalc(self,meldScore,risk):
        #if risk is
        if random.random() >= (meldScore/40)*risk:
            return false
        else:
            return true

app=Simulator()
