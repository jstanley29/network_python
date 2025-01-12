# Lists

# OLD WAYS
data = ["eat", "sleep", "repeat"]
index = 0
for item in data:
    print(index, item)
    index += 1

data = ["A", "B", "C"]
line = 1
for item in data:
    print(line, item)
    line += 1

# SMART WAYS
data = ["eat", "sleep", "repeat"]
for index, item in enumerate(data):
    print(index, item)

data = ["A", "B", "C"]
for line, item in enumerate(data, 1):
    print(line, item)

# Dictionaries

data = {
    "111": "Apple",
    "222": "Orange",
    "333": "Pear"
}

# OLD WAY
for fruit_key in data:
    fruit = data[fruit_key]
    print(fruit_key, fruit)

# SMART WAY
for fruit_key, fruit in data.items():
    print(fruit_key, fruit)
