def calculate_probability(event_count, total_outcomes):
    return event_count / total_outcomes
probability = calculate_probability(1, 2)
print("Probability of Heads =", probability)
import random
six_count = 0
for i in range(100):
    dice = random.randint(1, 6)
    if dice == 6:
        six_count += 1
probability = six_count / 100
print("Number of 6s =", six_count)
print("Experimental probability =", probability)
genres = [
    "pop", "rock", "pop", "hiphop", "pop",
    "jazz", "rock", "pop", "hiphop", "pop",
    "rock", "jazz", "pop", "rock", "pop",
    "hiphop", "jazz", "pop", "rock", "pop"
]
pop_count = genres.count("pop")
total = len(genres)
probability = pop_count / total
print("Probability of Pop =", probability)
def both_probability(food_users, dessert_users):
    food_users = set(food_users)
    dessert_users = set(dessert_users)
    both = food_users.intersection(dessert_users)
    total_users = food_users.union(dessert_users)
    return len(both) / len(total_users)
food = ["u1", "u2", "u3", "u4"]
dessert = ["u2", "u3", "u5"]
print("Probability of both =", both_probability(food, dessert))
phone_users = ["u1", "u2", "u3", "u4", "u5"]
headphone_users = ["u2", "u3", "u6"]
both = set(phone_users).intersection(set(headphone_users))
probability = len(both) / len(phone_users)
print("P(Headphones | Phone) =", probability)