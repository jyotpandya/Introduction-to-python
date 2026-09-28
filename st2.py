playlist_stats = [120, 135, 150, 200, 120, 90, 200]
mean = sum(playlist_stats) / len(playlist_stats)
print("Mean =", mean)
delivery_times = [30, 25, 40, 35, 30, 45, 30]
delivery_times.sort()
n = len(delivery_times)
median = delivery_times[n // 2]
print("Median delivery time =", median)
def most_common_rating(ratings):
    return max(set(ratings), key=ratings.count)
ratings = [5, 4, 4, 3, 5, 4, 2, 4]
print("Most common rating =", most_common_rating(ratings))
import statistics
channel1 = [100, 120, 110, 105, 5000]
channel2 = [100, 110, 120, 115, 125]
channel3 = [50, 100, 150, 200, 250]
channels = [channel1, channel2, channel3]
for i in range(3):
    print("Channel", i + 1)
    print("Mean =", statistics.mean(channels[i]))
    print("Median =", statistics.median(channels[i]))
    print("Mode =", statistics.mode(channels[i]))
print("Channel 1 is most affected by the outlier 5000.")
import pandas as pd
data = pd.DataFrame({
    "runs": [45, 70, 20, 100, 55, 70, 80, 40, 60, 70]
})
print("Mean =", data["runs"].mean())
print("Median =", data["runs"].median())
print("Mode =", data["runs"].mode()[0])