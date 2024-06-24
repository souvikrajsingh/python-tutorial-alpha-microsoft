# we will be taking a user choice and then will perform the actions that are said!

print('Enter 1. to add two numbers')
print("Enter 2. to subtract two numbers")
print("Enter 3. to multiply two numbers")
print("Enter 4. to divide two numbers");


#taking the user choice and saving it in the variable called "choice"
choice = int(input("Enter your choice please!"));


#we are using if-elif-else to check and perform the desired actions by the user depending on his choice

if(choice == 1): 
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2;
    print(result);
elif(choice == 2): 
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2;
    print(result);
elif(choice == 3):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2;
    print(result);
elif(choice == 4):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2;
    print(result);
else : 
    print("Invalid Input")
    
    

    