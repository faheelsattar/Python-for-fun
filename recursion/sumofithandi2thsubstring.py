#the following problem is not yet completed

def sum(num:str,count:int,array:list,holder:str):
    if count+1 < len(num):
        summation= int (num[count])+ int (num[count+1])
        result= int(num[count+2])
        while result <summation:
            result+=1
        if checker(summation,result):
            array.append(num[count])
            print(array)
            count+=1
            return sum(num,count,array,'')         
    else:
        print(array)
        return
            

def checker(num1, num2):
    if num1 == num2:
        return True
    return False
    
sum("11235813",0,[],'')
"""
Input : "11235813"
Output : ["1", "1", "2", "3", "5", "8", "13"]

Input : "1111223"
Output : ["1", "11", "12", "23"]

Input : "1111213"
Output : ["11", "1", "12", "13"]

Input : "11121114"
Output : []
"""