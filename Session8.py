"""1.
Create a Python script that uses a for loop to print the names of 5 favorite food delivery 
apps (e.g., Zomato, Swiggy, etc.), one per line.
2.
Given a list of daily step counts for a week, use a while loop to find and print the first 
day when you crossed 10,000 steps.<br><br><em><strong>Hint:</strong> Loop through the list and stop as soon as you
 find a value greater than 10,000.</em>
3.
Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer 
than 6 characters, skipping the rest using the continue statement.
4.
You have a list of song durations (in seconds) from your Spotify playlist. 
Use a for loop with enumerate to print each song's position (starting from 1) and its duration in the format: 'Song 1: 210 seconds'.
5.
Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart,
 use a loop to sum the prices. If an item price is 0 (out of stock), skip it. Stop adding items if the running total crosses 
 ₹2000 using break, and print the final total.<br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>"""
print("----TAsk-1---")
r=["Zomato","Swiggy","Toing","jiomart","Minutes"]
for i in r:
    print(i)
print("----TAsk-2---")
L=[1200,3673,5000,3646,39393,1000,24353]
day=0
while day < len(L):
    if L[day] > 10000:
        print("First Day you Crossed 10000 Steps is -:",day + 1)
        break
    day+=1
print("----TAsk-3---")
def iplteams():
    ipl=["RoyalChallengersbenguluru","csk","MumbaiIndians","Kkr","Lucknow SG","GujaratTitans"]
    print("IPl Teams Whose NAmes Are Greater Than 6 letters-:")
    for i in ipl:
        if len(i)<6:
            continue
        

        print(i)
            
            
iplteams()

print("----TAsk-4----")
Song=["Song-1","Song-2","Song-3","Song-4"]
Time=["120","230","200","170"]
for i,(Song,Time) in enumerate(zip(Song,Time),start=1):
    print(Song,":",Time)

print("----Task-5----")
prices=[1102,292,382,4432]
total=0
for i in prices:
    
    if i==0:
        print("OUt OF STock")
        continue
    if total + i > 2000:
        print("Stop Adding items")
        break
    total+=i    
print("Total Cart-:",total)


     