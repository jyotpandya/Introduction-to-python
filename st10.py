import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(50, 10, 100)
plt.hist(data, bins=10)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Normal Distribution")
plt.show()
from scipy.stats import mode
steps = [
    5000, 5200, 4800, 5100, 5300,
    4900, 5000, 5100, 5200, 5000,
    4900, 5100, 5000, 5200, 4800,
    5100, 5000, 4900, 5200, 5100
]
mean = np.mean(steps)
median = np.median(steps)
mode_value = mode(steps, keepdims=True).mode[0]
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode_value)
print("Mean, median and mode are approximately close.")
scores = np.random.normal(70, 15, 200)
count = np.sum((scores >= 55) & (scores <= 85))
print("Players between 55 and 85 =", count)
print("Approximately 68 percent are expected within one standard deviation.")
print("Delivery times can sometimes follow an approximately normal distribution.")
print("Most deliveries may be close to the average delivery time.")
print("Fewer deliveries may take much less or much more time.")
print("Traffic and weather can cause the actual data to differ from normal.")