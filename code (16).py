####################  FACTORIAL 
def factorial(n):
    if n==0 :
        return 1
    else:
        return n*factorial(n-1)
        
        
        
print(factorial(5))
 
 #######################################  FABINOCCI 
def fabinocci(n):
    if n==0:                #THESE ARE LIKE THE BASE CASES THAT ARE TO BE WRITTEN IN ORDER TO STOP THE 
        return 0         #RECURSIVE CALLS TO NEGATIVE CALLS
    if n==1:
        return 1
    
    return fabinocci(n-1)+fabinocci(n-2)           #LOGIC FOR THE fabinocci NUMBERS
        
print(fabinocci(5))