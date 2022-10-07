def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Choose one of them: ")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
choice = input("Enter Your Choice from a,b,c,d: ")
num1 = int(input("Enter Your Fist Number: "))
num2 = int(input("Enter Your Second Number: "))
if (choice == "a"):
    print(num1,"+",num2,"=",add(num1,num2))
elif (choice == "b"):
    print(num1,"-",num2,"=",sub(num1,num2))
elif (choice == "c"):
    print(num1,"*",num2,"=",mul(num1,num2))
elif (choice == "d"):
    print(num1,"/",num2,"=",div(num1,num2)) 
    
