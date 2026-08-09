print("----Spotify Music----")
s=int(input("Enter the time of music:"))
if s>=120:
    print("You are a true music fan!")
else:
    print ('Keep listening!')

print("----Zomato Order----")
z=int(input("Enter the amount of Zomato order:"))
if z>=300:
    print ('Eligible for free delivery')
else:
    print ('Delivery CHarges Apply')
print("----Flipkart Cart----")
z=int(input("Enter the Flipkart Total Cart:"))
if z>=2000:
    print ("You get 10% Discount")
elif z>=1000:
    print ("You get 5% Discount")

else:
     print ("No discount apply  ")
print("----Ipl Fantasy Points----")
points=int(input("Enter your Ipl Fantasy Team POINTS-:"))
if points>800:
    print("🏆Champions🏆")
else:
    if points>500:
        if points<800:
            print("Top Performer")
    else:
        print("Keep Trying")
