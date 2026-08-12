print('--TAsk-1--')
def calculate_final_price(price=1000, discount_rate=100):
    final_price=price-discount_rate
    print("Final Price-:",final_price)
calculate_final_price()
print("--TAsk-2--")
charges=0
def get_delivery_charge(amount, city='Ahmedabad'):
    c=input("ENter the City-:")
    if c=="Ahmedabad":
        print("Free Delivery")
        print("Your total Amount-:",amount)
    else:
        print("50 Rupees delivery charges applied")
        charges=amount+50
        print("Your total Amount-:",charges)
get_delivery_charge(1000)
print("---TAsk-3")

def format_price(price, currency='INR'):
    c=input("Enter the Currency-:")
    if c=='INR':
        print("₹500")
    elif c=='USD':
        print('$500')
format_price(500)

print("---TAsk-4")
def apply_coupon(price, coupon_code=None):
    coupon_code=input("Enter any Discount Coupon-:")
    if coupon_code=="Zomato10":
        dis_p=(price*10)/100
        f_p=price-dis_p
        print("Total Order Value with 10% Discount is-:",f_p)
    else:
        print("Total Order Value",price)
apply_coupon(1800)