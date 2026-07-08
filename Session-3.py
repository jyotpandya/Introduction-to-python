age = 20
height = 170.5
name = "Jyot"
spotify = True

print(age)
print(type(age))

print(height)
print(type(height))

print(name)
print(type(name))

print(spotify)
print(type(spotify))
prices = ["199.99", "49", "350.75"]

total = 0

for i in prices:
    total = total + float(i)

print("Total =", total)

score = input("Enter your score: ")

score = int(score)

if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")

is_premium = "True"

result = (is_premium == "True")

print(result)
print(type(result))