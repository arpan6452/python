'''
Created on 09-Nov-2020

@author: arpaghos
'''

#Created a class called Bank

class bank:
    def _init_(self, IFSC_Code, bankname, branchname, loc):
        self.IFSC_Code = IFSC_Code
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc
        
    def getSavingAccountInfo(self):5
        return "IFSC_Code : " + self.IFSC_Code + " Bank Name: " + self.bankname + " Branch Name: " + self.branchname + " Location: " + self.loc
