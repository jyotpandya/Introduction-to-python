print("---Task-1---")
def print_playlist_songs(songs):
    for i in songs:
        print(list(i))
print_playlist_songs(["Until I Found U","Perfect","Thousand Years","Dandelions","Sailor"])
print("---Task-2---")
def count_unread_messages(messages):
    # Count unread messages in current group
    total = messages.get("count", 0)

    # Recursively count messages in subgroups
    for subgroup in messages.get("subgroups", []):
        total += count_unread_messages(subgroup)

    return total
messages = {
    "count": 5,
    "subgroups": [
        {
            "count": 3,
            "subgroups": [
                {"count": 2},
                {"count": 4}
            ]
        },
        {
            "count": 6,
            "subgroups": [
                {"count": 1}
            ]
        }
    ]
}
print(count_unread_messages(messages))
print("---task-3---")
x = 'global'
def outer():
    x = 'outer'
"""def inner():
    nonlocal x # inner () x is not printing"""
x = 'inner'
#inner()
print('Inside outer:', x)#inner
outer()
print('Outside:', x)#inner
print("---Task-4---")
def format_number_short(n):
    if n < 1000:
        return n
    
    if n >= 1000000:
        return format_number_short(n / 1000) + "K"
    
    return str(n / 1000) + "K"

print(format_number_short(15000))