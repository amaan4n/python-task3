##elif

time = 17

if time < 12:
    print("good morning")
elif time < 16:
    print("good afternoon")
elif time< 18:
    print("good evening")
elif time < 24:
    print("good night")
else:
    print("error")
#for loop

for temp in range(11):
    print(temp)

for temp in range(6,27):
    print(temp)

#even  no
for temp in range(0,100,2):
    print(temp)


#odd no
for temp in range(1,100,2):
    print(temp)


list =("bike","car","trucks","trains")
for temp in list:
    print(temp)
#

#while loop

number = 1


while number < 11:  #true
    print(number)
    number = number + 1
    
    
#FUCTIONS
#block of code whenever

def jeeva():
    print("hello world")
    print("hey")
def syed():
    print("hello syed")

def varsha():
    print("hello varsha")


syed()
varsha()
jeeva()

#
def func1():
    print("this is function 1")

def func2():
    print("this is function 2")

    func1()
    func2()

#
def addition(number1,number2):
    print("hello addition")
    print(number1)
    print(number2)

def subtraction(number3,number4):
    print("hello subs")
    print(number3)
    print(number4)
addition(5,2)
subtraction(6,9)
