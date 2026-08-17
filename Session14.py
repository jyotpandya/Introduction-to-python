print("----Task-1----")
with open("playlist.txt",'w') as f:
    f.write("Shape Of You.\n")
    f.write("Blinding Lights.\n")
    f.write("Levitating\n")
    f.write("Senorita\n")
print("----Task-2----")
with open("playlist.txt",'r') as fp:
    content=fp.read().upper()
    print(content)
print("----Task-3----")
import csv
with open('C:/Users/Jyot Pandya/Desktop/ipl_matches.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Match {row['match_id']}: Winner - {row['winner']}")
print("----TAsk-4----")
import json

with open("movies.json", "r") as file:
    movies = json.load(file)

for movie in movies:
    print("Title:", movie["title"])
    print("Rating:", movie["rating"])
    print()

print("---Task-5---")
from pathlib import Path
import json

file = Path("my_fav_apps.json")

if not file.exists():
    apps = [
        {"name": "Instagram", "category": "Social Media"},
        {"name": "Zomato", "category": "Food Delivery"},
        {"name": "Paytm", "category": "Payments"}
    ]

    with open(file, "w") as f:
        json.dump(apps, f, indent=4)

    print("File created successfully.")
else:
    print("File already exists.")