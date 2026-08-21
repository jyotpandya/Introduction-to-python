print("---Task-1---")
l=["Zomato", "Swiggy", "Domino's","Toing","Martinos"]
lo=iter(l)
print(next(lo))
print(next(lo))
print(next(lo))
print(next(lo))
print(next(lo))
print("---Task-2---")
def playlist_generator():
    w=["abc","zyx","ieie","kwij","iNnjw"]
    for i in w:
        yield i
io=playlist_generator()
print(next(io))
print(next(io))
print(next(io))
print(next(io))
print(next(io))
print("---Task-3---")
s=['Pizza', 'Burger', 'Fries', 'Coke']
for i in enumerate(s):
    print(i)
print("---Task-4---")
t=["RCB","GT","PBKS","DC"]
p=["18","14","10","9"]
for i,j in zip(t,p):
    print("Team-:",i,"Points-:",j)
print("---Task-5---")
def order_id_generator(start=1001):
    for i in range(start, 1000000):
        yield i
order = order_id_generator()
print(next(order))
print(next(order))
print(next(order))
print(next(order))
print(next(order))