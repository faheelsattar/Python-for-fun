def fibonacci(value,prev,next):
    if value == 0:
        return 0
    elif next <=value:
       print(prev) 
       return fibonacci(value,next,prev+next) 
    else:
        return prev 
print('Fibonacci Sum= {}'.format(fibonacci(14,0,1)))