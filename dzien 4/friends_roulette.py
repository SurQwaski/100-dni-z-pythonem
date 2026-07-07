import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Solution using random.randint

friends_count = len(friends)
drawn_friend = random.randint(0,friends_count)

print(friends[drawn_friend])

# Solution using random.choice

print(random.choice(friends))

