# TheTrip.py , 0003 quiz
# written by badsaram

import sys
import math

class trip(object) :
    def __init__(self) :
        self.costs = []
        self.members = 4
        
    def isNumber(self, number) :
        try :
            float(number)
            return True
        except ValueError :
            return False

    def inputCost(self) :
        str = input("How many members ? ")
        if((str.isdigit() == False) or (str.isdecimal() == False)) :
            print("Not Digit or Not Decimal")
            return False
        
        self.members = int(str)
        if (self.members <= 0) :
            sys.exit()
        
        for i in range(0, self.members) :
            str = input("Cost ? ")
            if (self.isNumber(str) == False) :
                print("Not Number or Not Decimal")
                return False
            
            temp = float(str)
            if ((temp < 0.0) or (temp >= 10000.00)) :
                print("0 < cost < 10000")
                
            self.costs.append(float(str))
                
        return True
    
    def calcMinDelivery(self) :
        sum = 0.0
        avg = 0.0
        MinDelivery = 0.0
        
        for cost in self.costs :
            sum += cost
            
        avg = sum / self.members 
        
        for cost in self.costs :
            if (cost > avg) :
                temp = int((cost - avg) * 100) #floor under 0.00
                MinDelivery += (temp / 100)

        return MinDelivery
    
if __name__ == '__main__' :
    obj = trip()
    
    while (True) :
        if (obj.inputCost() == True) :
            print("$%.2f" % obj.calcMinDelivery())