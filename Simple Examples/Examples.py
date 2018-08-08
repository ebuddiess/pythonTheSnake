# hello word in python
# print("Hello Word with python");
# ---------------------------------------------------------------------------
# name = "Puneet";
# print(name)
# working with strings------------------------------------------------------
# name = "Puneet";
# print(len(name));
# print(name[2]);
# print(name.replace("Puneet","Akshay"));
# --------------------------------------------------------------------------
# from math import  *
#
# number = 27.11;
# print(round(number))
# print(pow(number,2))
# print(max(2,33))
# print(floor(number))
# print(sqrt(16))
# ///////////////////////////TAKING INPUT ////////////////////////////
# name = input("Enter Your Name");
# age = input("Enter Your age");
# print(name+""+age)
#---------------------------- ARRAYS -------------------------------
#
# names = ["Puneet","Asif","Manish","Kunal"]
# age = [12,13,14,15]
# age.insert(0,90);
# age.remove(12)
# # names.extend(age)
# # print(names.count("Puneet"))
# names.reverse()
# print(names)
# ---------------------TUPLES -------------------------------
# # these are immutable and are final by nature and cant be change
# coords = (4,5,3)
# print(coords[0])
# ----------- FUNCTION --------------
#
# def calculate(value):
#     print(value[0])
#     print(value[1])
#
# names = ["Puneet","Asif"]
# calculate(names)
#

#--------------  RETURN STATEMENT -------------------
#
# def cube(num):
#     return num*num*num;
#
# print(cube(3))
# ------------------------------ Dictionarys -----------------
# months =  {
# "Jan" : "January"
# }
#
# print(months["Jan"])
# Loops ---------------------------------------------------------

# i=1
# while i<=1000:
#     print(i)
#     i=i+1
#----------------------------------
# name = "Puneet"
#
# for alphabet in name:
#     print(alphabet)
#
#
# def showvalue(value):
#     int(value)
#     values = {
#         1:"First Iteration",
#         2:"Second Iteration",
#         3:"Third Iteration",
#         4:"Fourth Iteration"
#     }
#     return  values[value]
#
# for index in range(1,5):
#     print(showvalue(index))
#
#

# --------------- LAMBDA ------------------
#
# x = lambda a,b:a+10+b;
# print(x(2,3))
#
# ---------------------- CLASSESS

# class Calculator:
#     first=0
#     second=0
#     result=0;
#     def getValue(self):
#         self.first = int(input("Enter First"));
#         self.second = int(input("Enter Second"));
#ss
#     def calculate(self):
#         self.result = self.first + self.second;
#     def show(self):
#         print(self.result)
#
#
# calc = Calculator()
# calc.getValue()
# calc.calculate()
# calc.show()
#

