print(" LIST METHODS ")
fruits = ["Apple","Banana","Mango"]
fruits.append("Orange")
print("append:",fruits)
fruits.insert(1,"Grapes")
print("insert:",fruits)
fruits.remove("Banana")
print("remove:",fruits)
fruits.sort()
print("sort:",fruits)
fruits.reverse()
print("reverse:",fruits)
print("\n DICTIONARY METHODS ")
student = {
    "Name": "rutu",
    "Age": 20,
    "Course": "BCA"
}
print("keys():",student.keys())
print("values():",student.values())
print("items():",student.items())
student.update({"City":"Ahmedabad"})
print("update():",student)
removed =student.pop("Age")
print("pop():",removed)
print(student)
print("\nTUPLE METHODS ")
numbers = (10, 20, 30, 20, 40, 20)
print("count():", numbers.count(20))
print("index():", numbers.index(30))
tuple1 = (1, 2)
tuple2 = (3, 4)
print("Concatenation:", tuple1 + tuple2)
print("Repetition:", tuple1 * 3)
print("Length:", len(numbers))
print("\n SET METHODS ")
set1 = {1, 2, 3}
set1.add(4)
print("add():", set1)
set1.remove(2)
print("remove():", set1)
set1.update([5, 6])
print("update():", set1)
set2 = {3, 4, 7}
print("union():", set1.union(set2))
print("intersection():", set1.intersection(set2))
print("\n IF STATEMENT ")
num = 10
if num > 0:
    print("Positive Number")
print("\n IF ELSE ")
age = 18
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
print("\n IF ELIF ELSE ")
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
print("\n NESTED IF ELSE ")
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
print("\n BREAK EXAMPLE ")
for i in range(1, 11):
    if i == 6:
        break
    print(i)
print("\nCONTINUE EXAMPLE ")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("\n PASS EXAMPLE ")
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
print("\n INPUT METHOD ")
name = input("Enter your name: ")
print("Welcome,", name)
print("\n RANGE FUNCTION ")
for i in range(1,6):
    print(i)
print("\nLEN FUNCTION ")
text = "Python"
print("Length:", len(text))
print("\n TYPE FUNCTION ")
x = 100
print(type(x))
print("\n FOR LOOP ")
for i in range(5):
    print("Iteration:", i)
print("\n WHILE LOOP ")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
print("\nProgram Completed Successfully.")