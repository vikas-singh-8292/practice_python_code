print("Enter num 1")
num1= int(input())
print("Enter num 2")
num2 =int(input())
try:
    print("The sum of these number is :",
          num1+num2)
except Exception as e:
    print(e)
print("This line is very important")
try:
   print("Hellow")
# except NameError:
#     print("Variable x is not define")
except:
    print("Somthing else went wrong")
else:
    print("Nothing Went Wrong")

# Finally

try:
    print(x)
except:
    print("Somethin Went to Wrong")
finally:
    print("The Try Exception is Finished")
