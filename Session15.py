print("---TAsk-1---")
def get_song_duration_per_minute():
    try:
        total_duration=int(input("Enter total playlist duration (minutes): "))
        number_of_songs=int(input("Enter number of songs: "))
        a=total_duration/number_of_songs
        print("Average duration per song:", a, "minutes")
    except ZeroDivisionError:
        print("There are 0 songs in your Spotify playlist.")
    finally:
        print("Calculation completed.")
get_song_duration_per_minute()
        
print("---TAsk-2---")
def calculator():
    try:
        total_cart_amount=int(input("Enter total cart amount: "))
        item_count=int(input("Enter total item count: "))
        b=total_cart_amount/item_count
    except ZeroDivisionError:
        print("There is no items in cart")
    finally:
        print("Thank you for visiting flipkart")
calculator()

print("---TAsk-3---")
class NoOffersApplied(Exception):
    pass


def Paytm_cashback_calculator():
    try:
        total_spend = int(input("Enter total spend: "))
        number_of_offers = int(input("Enter number of offers: "))
        if number_of_offers == 0:
            raise NoOffersApplied
        average = total_spend / number_of_offers
        print("Average cashback per offer:", average)
    except NoOffersApplied:
        print("Error: No offers were applied. Cashback cannot be calculated.")
Paytm_cashback_calculator()
print("---TAsk-3---")
def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    finally:
        print('Thank you for using the calculator')
print(calculate_average_rating(500, 0))

print("---TAsk-4---")
def safe_divide_for_zomato(bill_amount,number_of_people):
    try:
        cal=bill_amount/number_of_people
    except ZeroDivisionError:
        print("Total Bill")
    else:
        
        print(f"Success! The result is {cal}")
    finally:
        print("Split calculation done")
safe_divide_for_zomato(1000,2)