import traceback

number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")
a = 1
b = 2
var = "bigger" if a > b else "smaller"
print(var)
list_example = [
    "Pesho", "Gosho", "Tosho", 56, False, "Monika", "Kalina", "Nadejda", "Stoyan"
]
print(list_example[1])
print(list_example[-1])
print(list_example[-2])
print("Monika" in list_example)
print(len(list_example))
del list_example[2]
print("Elements are:")
""" Comment """


def printList(list):
    for el in list:
        print(el)


# printList(list_example)
temp = []
y = 0
for x in range(3, 6, 2):
    """
    Отначало y = 0,
    после 
    for(int i = 3 ;i <=6 ;i+=2){
    //1 итерация
     y+=3 ->  0+3 = 3  
    //2 итерация
     y+=5 -> y е било 3 и става 3+5 = 8
    }
    """
    y += x
    print(y)
    temp.append(x)
printList(temp)
# принтира  3 (8) 3  5
for element in list_example:
    if element == "Monika":
        print("Exists!")
        break
    else:
        print(("Current index is {0}".format(list_example.index(element))))
x = 1
while x <= 20:
    print(x)
    x += 1
dict = {
    "name": "Maya",
    3: "Peter",
    True: "Not exactly :)"
}
for el in dict:
    print(dict[el])
del dict[3]
for el in dict:
    print(dict[el])
map = {}
first = 45
second = "Kowalski"
try:
    first + second
except TypeError:
    # get the type error
    tr = traceback.format_exc()
    print(tr)
# unhandled exception handler
tuple = (1, "Cat", "Ivan", True)
print("{0} {1} {2}".format(tuple[0], tuple[1], tuple[2]))
