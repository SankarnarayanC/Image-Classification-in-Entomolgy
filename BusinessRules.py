import numpy as np
import pandas
import datetime

class DataLabeller():

    def __init__(self,var):
        self.var = var

    def labelldata(self,string):
        self.string = string
        return self.diffdate()
        
    def strlen3(self):
        if(len(self.string==136)):
            return 1
        else:
            return 0
        
    def rectype(self):
        if(int(self.string[0:1])==3):
            return 1
        else:
            return 0
        
    def bankcode(self):
        if(int(self.string[1:4])==601):
            return 1
        else:
            return 0
        
    def branchcode(self):
        if(int(self.string[4:7])>=500 and int(self.string[4:7])<600):
            return 1
        else:
            return 0
        
    def loanaccttype(self):
        if(int(self.string[14:18])):
            return 1
        else:
            return 0
        
    def accttype(self):
        if(int(self.string[18:19]) in []):
            return 1
        else:
            return 0
        
    def classcode(self):
        if(int(self.string[19:21])>=1 and int(self.string[19:21])<5):
            return 1
        else:
            return 0
        
    def collateralcode(self):
        if(int(self.string[21:25])>=2000 and int(self.string[21:25]) < 4000):
            return 1
        else:
            return 0
        
    def trancode(self):
        if(int(self.string[54:56])>=60 and int(self.string[54:56]) < 90):
            return 1
        else:
            return 0
    
    def actioncode(self):
        if(self.string[56:57] in ['A','R','P','I']):
            return 1
        else:
            return 0
        
    def interestamt(self):
        amt = float(self.string[57:64]) + float(self.string[64:66])/100
        if(amt>=0 and amt<=620830.00):
            return 1
        else:
            return 0
    
    def principalamt(self):
        amt = float(self.string[67:76]) + float(self.string[76:78])/100
        if(amt>=0 and amt<=4900000):
            return 1
        else:
            return 0
        
    def miscamt(self):
        amt = float(self.string[79:88]) + float(self.string[88:90])/100
        if(amt>=0 and amt<=100000):
            return 1
        else:
            return 0
    
    def totamt(self):
        amt = float(self.string[120:132]) + float(self.string[132:134])/100
        if(amt>=0 and amt<=5000000):
            return 1
        else:
            return 0
    
    def operator_id(self):
        for i in self.string[97:105]:
            if(i not in [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']):
                return 0
        return 1

    def diffdate(self):
        objpost = datetime.date(2024,int(self.string[40:42]),int(self.string[42:44]))
        objeff = datetime.date(2024,int(self.string[47:49]),int(self.string[49:51]))
        return int(str(objeff-objpost).split()[0])
    


         

string = "3509780454540770473378215ABCDEFGHIJ A   0601242060624268R904974635+02932396148-00061978577-IND   ARV7586 ABCDE AB       53230483577965-"

inst = DataLabeller(3)
print(inst.labelldata(string))







    

        



