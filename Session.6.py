insta_followers={"abc":1200,"def":3445,"tyu":9543,"fgh":9494}
print(insta_followers)
insta_followers["vor"]=1200
insta_followers["fgh"]=9349
insta_followers.pop("def")
print("Updated Dictionary-:",insta_followers)
print("---Zomato---")
z={"Burger":70,"Sandwich":80,"Panipuri":30,"dosa":210,"Pizza":250}
for key,value in z.items():
    if value>=200:
        print(key , ":" , value)
print("----Flipkart & Myntra----")
flipkart_users={"rahul", "priya", "amit", "neha", "rohit"}
myntra_users={"amit", "neha", "karan", "pooja", "rahul"}
common_users=flipkart_users.intersection(myntra_users)
print("Users on both platforms:")
print(common_users)
print("---Userdefined Function---")
def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)
playlist1 = {"Arijit Singh", "Taylor Swift", "Ed Sheeran"}
playlist2 = {"Ed Sheeran", "Shreya Ghoshal", "Armaan Malik"}
unique_artists = get_unique_artists(playlist1, playlist2)
print("Unique Artists:")
print(unique_artists)