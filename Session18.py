print("---Task-1---")
import re
f = ['+91-9876543210']
y = re.findall(r'\d{10}', f[0])
print(y)
print("---Task-2---")
import re
def check_date(text):
    pattern = r'\d{2}/\d{2}/\d{4}'
    if re.search(pattern, text):
        return True
    else:
        return False
text = "My birthday is 27/08/2007"
print(check_date(text))
print("---Task-3--- ")
import re
text = "Products: Rs. 299, Rs. 1500, Rs. 450, Rs. 799 and Rs. 1200."
prices = re.findall(r'Rs\. (\d+)', text)
prices = [int(price) for price in prices]
print("Prices:", prices)
print("Total:", sum(prices))
print("---Task-4--- ")
import re
text = "Contact me at abc@gmail.com or xyz@yahoo.com for more information."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
modified_text = re.sub(pattern, '[hidden email]', text)
print(modified_text)
print("---Task-5--- ")
import re

with open("instagram_comments.txt", "r") as file:
    text = file.read()
pattern = r'@[A-Za-z0-9_]{3,}'
usernames = re.findall(pattern, text)
unique_usernames = set(usernames)
print("Unique Instagram usernames:")
for username in unique_usernames:
    print(username)