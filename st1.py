actions = [
    ("Instagram", "Number of likes", "Numerical"),
    ("Instagram", "Post type", "Categorical"),
    ("Zomato", "Order amount", "Numerical"),
    ("Zomato", "Food category", "Categorical"),
    ("Flipkart", "Product rating", "Numerical")
]
for action in actions:
    print(action)
music_data = ['Pop', 'Rock', 'Jazz', 'Hip-Hop', 'Pop', 'Rock', 'Jazz', 'Pop']
print("Data:", music_data)
print("Type: Categorical")
print("Reason: The data contains music genres, which are categories and not numerical values.")
likes = [100, 150, 200, 250, 300]
average_likes = sum(likes) / len(likes)
print("Average likes:", average_likes)
print("Statistics can help identify the average engagement and improve content recommendations.")
mean = 100
median = 80
mode = "Pop"
print("Mean: Average number of song plays =", mean)
print("Median: Middle value of song plays =", median)
print("Mode: Most frequently played genre =", mode)