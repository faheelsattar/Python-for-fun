def partitions(value ,array:list):
    if len(value) == 0:
        print(array)
        return
    else:
        holder=''
        for val in value:
            holder+=val
            if palindrome(holder):
                array.append(holder)
        value=value[1 : : ]
        partitions(value, array)
def palindrome(value):
    high=len(value)-1
    low=0
    while low < len(value):
        if value[low] == value[high]:
            if low == len(value)-1:
                return True
            low += 1
            high -= 1
        else:
            return False
partitions('nitin',[]) 

# input--> nitin
#output --> ['n', 'nitin', 'i', 'iti', 't', 'i', 'n']
