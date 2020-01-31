def possiblities(set:list, k:int, holder):
    if k==0:
        print(holder)
    else:
        newholder=''
        for index in range(0,len(set)):
           newholder=holder+ set[index]
           possiblities(set, k-1, newholder) 

possiblities(['a','b','c'],2,'')

"""
input --> ['a','b','c'],2,''
output--> aa,ab,ac,ba,bb,bc,ca,cb,cc
"""