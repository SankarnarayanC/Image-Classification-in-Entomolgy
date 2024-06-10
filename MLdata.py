import numpy as np
import datetime 
import pandas as pd

#str = "3509780454540770473378215ABCDEFGHIJ A   0601242060624268R904974635+02932396148-00061978577-IND   ARV7586 ABCDE AB       53230483577965-"

class RecData2MLData:

    data = pd.DataFrame({"string length":[],"record type":[],"bank code":[],"branch code":[],"account code":[],"account type":[],"class code":[],"collateral code":[],"date difference":[],"tran code":[],"action code":[],"interest amount":[],"principal amount":[],"misc amount":[],"total amount":[],"target":[]})

    def __init__(self,strong):
        self.strong = strong
    
    def filehandle(self,st):
        file = open(st,"r+")
        lines = file.readlines()
        for l in lines[:20]:
            self.non_fraudulent(l)


    def non_fraudulent(self,string):
        target = 0
        str_len = len(string)
        rec_type = int(string[0:1]) #1
        bank_code = int(string[1:4]) #2
        branch_code = int(string[4:7]) #3
        acct_code = int((string[14:18])) #4
        acct_type = int(string[18:19]) #5
        class_code = int((string[19:21])) #6
        collateral_code = int(string[21:25]) #7
        diff_date = str((datetime.date(2024,int(string[40:42]),int(string[42:44])) - datetime.date(2024,int(string[47:49]),int(string[49:51])))).split()[0] #8
        tran_code = int(string[54:56]) #9
        action_code = ord(string[56:57]) #10
        interest_amount = float(string[57:64]) + float(string[64:66])/100
        if(string[66:67]=='-'):
            interest_amount = interest_amount*-1
        principal_amount = float(string[67:76]) + float(string[76:78])/100
        if(string[78:79]=='-'):
            principal_amount = principal_amount*-1
        misc_amount = float(string[79:88]) + float(string[88:90])/100
        if(string[90:91]=='-'):
            misc_amount = misc_amount*-1
        total_amount = float(string[120:132]) + float(string[132:134])/100
        if(string[134:135]=='-'):
            total_amount = total_amount*-1
 
        newrow = {"string length":str_len,"record type":rec_type,"bank code":bank_code,"branch code":branch_code,"account code":acct_code,"account type":acct_type,"class code":class_code,"collateral code":collateral_code,"date difference":diff_date,"tran code":tran_code,"action code":action_code,"interest amount":interest_amount,"principal amount":principal_amount,"misc amount":misc_amount,"total amount":total_amount,"target":target}
        self.data = self.data.append(newrow,ignore_index = True)
           

inst = RecData2MLData(3)
inst.filehandle(r"C:\Users\kartik\Desktop\VNIT\Intern-WellsFargo\2024-06-01")
print(inst.data)