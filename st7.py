import matplotlib.pyplot as plt
hours = [1, 2, 2.5, 3, 4, 4.5, 5]
posts = [1, 2, 2, 3, 4, 5, 6]
plt.scatter(hours, posts)
plt.xlabel("Instagram Hours")
plt.ylabel("Posts Made")
plt.title("Instagram Usage vs Posts")
plt.show()
print("The relationship shows positive correlation.")
import numpy as np
zomato = [5, 8, 6, 10, 7, 9]
swiggy = [4, 7, 5, 9, 6, 8]
correlation = np.corrcoef(zomato, swiggy)[0, 1]
print("Correlation coefficient =", correlation)
if correlation > 0:
    print("Positive correlation")
elif correlation < 0:
    print("Negative correlation")
else:
    print("Zero correlation")
print("YouTube videos watched and study hours may have negative correlation.")
print("If video watching increases, available study time may decrease.")
print("Therefore, one variable may increase while the other decreases.")
spotify_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [95, 91, 88, 84, 80, 76, 72, 68, 63, 60]
plt.scatter(spotify_hours, marks)
plt.xlabel("Time Spent on Spotify")
plt.ylabel("Test Marks")
plt.title("Spotify Time vs Test Marks")
plt.show()
print("The data shows strong negative correlation.")