print("---TAsk-1---")
Spotify=['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']
songs=list(map(lambda Spotify : Spotify.lower(),Spotify))
print(songs)

print("---TAsk-2---")
ratings=[4.2, 3.8, 4.5, 2.9, 3.5]
fil=list(filter(lambda ratings : ratings>4.0,ratings))
print(fil)

print("---TAsk-3---")
from functools import reduce
Flipkart=[499, 1299, 299, 799]
total_price=reduce(lambda x,y :x+y,Flipkart)
print(total_price)

print("---TAsk-4---")
follower_counts=[950, 1500, 25000, 1200000]
def format_followers(num):
    
    if num>=1000000:
        return f"{num/1000000}M"
    if num>=1000:
            return f"{num/1000}K"
    else:
         return num

l1=list(map(format_followers,follower_counts)) 
print((l1))
         
  
    


print("---TAsk-5---")
IPL_scores=[101, 98, 120, 77, 88]
y=list(filter(lambda x : x%2==0 ,IPL_scores))
print(y)