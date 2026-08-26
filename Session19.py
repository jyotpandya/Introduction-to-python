print("---TAsk-1----")

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def play_preview(self):
        print(f'Playing 30-second preview of {self.title} by {self.artist}')
        
        

s = Song("Sajni", "Arijit Singh", 150)

print("Title:",s.title)
print("Artist:",s.artist)
print("Duration:",s.duration, "seconds")
s.play_preview()
class FoodOrder:
    def __init__(self, restaurant_name, items, price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.price = price
        self.total_price = sum(price)

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.price.append(item_price)
        self.total_price += item_price


x = FoodOrder("Sankalp", ["Idli", "Dosa"], [150, 120])

x.add_item("Uttapam", 70)
x.add_item("Coffee", 50)

print("Restaurant:", x.restaurant_name)
print("Items:", x.items)
print("Total:", x.total_price)
class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


s1 = Song("Sajni", "Arijit Singh")
s2 = Song("Kesariya", "Arijit Singh", 268)

print(s1.title, s1.artist, s1.duration)
print(s2.title, s2.artist, s2.duration)