print("WELCOME TO CALCULATOR")
print("INTRUCTIONS:")
print("+ for Addition \n- for Substraction \n* for Multiplitaion \n/ for Division")
f = int(input("Enter the first number\n"))
s = int(input("Enter the second number\n"))
w = input("what operation do you want to do ?\n")
if w == "+":
    a = (f + s)
    print("the result is " + str(a))
elif w == "-":
    ss = (f - s)
    print("the result is " + str(ss))
elif w == "*":
    mm = (f * s)
    print("the result is " + str(mm))
elif w == "/":
    dd = (f / s)
    print("the result is " + str(dd))
print("THANKS FOR USING\nThis is made by Rahul")
