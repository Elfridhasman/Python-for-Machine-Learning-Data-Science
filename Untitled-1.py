number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in number:
    if(num % 3 == 0) & (num % 5 == 0):
        print("FizzBuzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print("No")  