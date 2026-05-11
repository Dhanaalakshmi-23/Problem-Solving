#1. Reverse a number.
# sample input : 1234
# output : 4321

# sample input : -567
# output : -765

def reverseNumber(x):
    reversed_num = 0
    
    while x != 0:
        
        rem = int(x % 10)
        
        if x < 0 and rem > 0:
            rem -= 10
        
        x = int(x / 10)
        
        reversed_num = reversed_num * 10 + rem
    
    return reversed_num


print(reverseNumber(1234))
print(reverseNumber(-567))