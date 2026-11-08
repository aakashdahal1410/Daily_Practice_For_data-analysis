# Basic print

# def greet():
    # print("Hello")
# greet()


#ODD OR EVEN
def numb(n):
    if n%2==0:
        print("Number is even i.e",n)
    else:
        print("Number is Odd i.e",n)

n=int(input("Enter number"))
numb(n)





#factorial of user given number

# def fact(n):
#   if n==0 or n==1:
        # return 1
    # else:
        # return n*fact(n-1)

# n=int(input("Enter the number"))
# print("The factorial of given number is:",fact(n))



#Base and exponent 

# def pow(x,y):
    # if y==0:
        # return 1
    # else:
        # return x*pow(x,y-1)
# x=int(input("Enter the base"))
# y=int(input("Enter the exponents"))
# print("The value is",pow(x,y))