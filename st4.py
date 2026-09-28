import matplotlib.pyplot as plt
orders = [12, 15, 17, 14, 13, 16, 200, 18, 14, 15]
plt.plot(orders, marker="o")
plt.xlabel("Day")
plt.ylabel("Orders")
plt.title("Daily Swiggy Orders")
plt.show()
print("The data is right skewed because 200 is a very high value.")
import statistics
followers = [5, 7, 8, 8, 9, 10, 12, 15, 95]
mean = statistics.mean(followers)
median = statistics.median(followers)
print("Mean =", mean)
print("Median =", median)
print("Mean is higher than median.")
print("The data is right skewed because 95 pulls the mean upward.")
print("Example: YouTube video views")
print("Most videos receive a small or moderate number of views.")
print("A few viral videos can receive millions of views.")
print("These very high values create a long right tail.")
ratings = [3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(ratings, bins=5)
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Flipkart Product Ratings")
plt.show()
print("The distribution is left skewed because most ratings are high.")