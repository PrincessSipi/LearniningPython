def collatz(number):
    if number % 2 == 0:
        print(f"{number} // 2 = ")
        return number //2
    else:
        print(f"3 * {number} + 1 = ")
        return 3 * number + 1

try:
    number = int(input("Enter a number"))
    print("Collatz Sequence")
    print(number)
except:
    print("Enter a number")

while (number != 1):
    number = collatz(number)
    print(number)
print(number)  
    
