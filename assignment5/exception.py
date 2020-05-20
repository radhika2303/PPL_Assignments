#1.NORMAL TRY-EXCEPT BLOCK IS IMPLEMENTED HERE

print("Exception 1: (try-except block)\n")

i = int(input("Enter 1st number :\n"))
j = int(input("Enter 2nd number :\n"))
try:
	k = i/j
	print(k)
except:
	print("You divided by 0")
	print("No error shown because the exception was handled")

#2.EXCEPTION FOR ZeroDivision Error

print("\nException 2: (ZeroDivision Error)\n")

a = int(input("Enter 1st value for division\n"))
b = int(input("Enter 1st value for division\n"))
try:
	print(a/b)
except ZeroDivisionError:
	print("A number cannot be divided by zero")

#3.EXCEPTION FOR HANDLING TYE-ERROR

print("\nException 3: (Type-Error)\n")

a = input("Enter 1st value for division\n")
b = int(input("Enter 1st value for division\n"))
try:
	print(a/b)
except TypeError:
	print("A string cannot be divided by integer. Convert string to integer in code while taking input")
	
#4.TRY WITH MULTIPLE EXCEPT

print("\nException 4: (Multiple Excepts)\n")

i = int(input("Enter 1st number :\n"))
j = int(input("Enter 2nd number :\n"))
try:
	print(i/j)
	print("Inside try ---  printed")
except TypeError:
    print("You added values of incompatible types")
except ZeroDivisionError:
    print("You divided by 0")
    
#5.If you don't know which type of exception to raise, then don't specify the exception name

print("\nException 5: (Using finally)\n")

print("Enter a filename you want to read\n")
a = input()
try:
	f = open(a, "r")
	m = f.read()
	print("This is the content of your file:")
	print(m)
except:
	print("Error : File not found.")
finally:
	print("Finally executes like a common print statement.It is executed always.\n")
	
#6.Deliberately raising an error using raise keyword

print("\nException 6: (Using raise)\n")

i = int(input("Enter 1st number :\n"))
j = int(input("Enter 2nd number :\n"))
try:
	if b==0:
		raise ZeroDivisionError
except:
	print("You divided by 0")
print("This is printed if no  error found\n")
	
print("\n----*----\n")
	

