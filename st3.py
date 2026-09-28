steps = [4500, 7000, 5000, 8000, 4000, 9000, 6000]
mean = sum(steps) / len(steps)
print("Mean =", mean)
squared_difference = []
for value in steps:
    difference = value - mean
    square = difference ** 2
    squared_difference.append(square)
    print(value, "-", mean, "=", difference, "Square =", square)
variance = sum(squared_difference) / len(steps)
print("Variance =", variance)
import statistics
def calculate_standard_deviation(scores):
    return round(statistics.stdev(scores), 2)
scores = [70, 75, 80, 85, 90]
print("Standard deviation =", calculate_standard_deviation(scores))
friend_a = [200, 200, 200, 200, 200]
friend_b = [100, 300, 150, 400, 50]
sd_a = statistics.stdev(friend_a)
sd_b = statistics.stdev(friend_b)
print("Friend A standard deviation =", sd_a)
print("Friend B standard deviation =", round(sd_b, 2))
print("Friend A has more consistent spending because its standard deviation is lower.")
salary = [28000, 29000, 27000, 60000, 26500, 27500]
variance = statistics.variance(salary)
standard_deviation = statistics.stdev(salary)
print("Variance =", variance)
print("Standard deviation =", round(standard_deviation, 2))
print("The high spread is mainly caused by the 60000 salary.")