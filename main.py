fruits = ["яблуко", "банан"]
fruits.append("Apelsyn")
print(fruits)

colors = ["червоний", "зелений", "синій", "зелений"]
colors.remove("зелений")
print(colors)

items = ["ручка", "олівець", "зошит"]
items.pop()
print(items)

animals = ["кіт", "пес", "папуга"]
print("пес" in animals)
print("слон" in animals)  

user = {"name": "Олександр", "age": 25, "city": "Київ"}
print(user.get("name"))
keys = user.keys()
print(list(keys))

values = user.values()
print(list(values))

print(list(user.items()))