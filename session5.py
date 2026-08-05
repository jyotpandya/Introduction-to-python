playlist_ids=["Until I Found U","Perfect","Thousand Years","Dandelions","Sailor"]
print(playlist_ids)
print("Updated LIst-:")
playlist_ids.append("I Wanna be yours")
playlist_ids.extend("Fairytail")
print(playlist_ids)
print("Last Played Song REmoved-:",playlist_ids.pop())
print(playlist_ids)

print("----Tuple----")
insta_filters=("qwer","tyui","opas","dfgh")
#insta_filters.delete("qwer")
print("Error: 'tuple' object has no attribute 'delete' , Tuple is immutable")

print("---List Vs Tuple")
zomato=["Burger","Pizza","coffee"]
ipl_team=("RCB","MI","CSK")
print("Zomato Order-:",zomato)
print("Ipl Teams-:",ipl_team)
"""
Zomato order should used list becuase orders can be newly added or deleted means
changes can be applied so , tuple can't fit here . so, in zomato order list is used
while ipl teams are fixed so there is no extra need of using list we can easily used tuple.""" 