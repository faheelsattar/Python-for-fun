def orderLexicographic(value,count,holder):
    if count == len(value):
        return holder
    else:
        for index in range(0,len(value)):
            if value[count] < value[index]:
                holder+= value[count] + value[index]+','
            elif value[count] == value[index]:
                holder+=value[count]+','
            else:
                continue
        count+=1
        return orderLexicographic(value,count,holder)
print(orderLexicographic('abc',0,''))
"""
Input : abc
Output : a, ab, ac, b, bc, c
"""