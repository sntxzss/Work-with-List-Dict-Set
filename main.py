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

numbers = [1, 2, 2, 3, 4, 4, 5]
print(numbers)
print(set(numbers))

tasks = []
def add_task():
 task = tasks.append(input("Enter your task: "))
 return task
add_task()
print(tasks)

def delete_task():
 delete = tasks.remove(input("Enter task you wanna delete: "))
 return delete
delete_task()
print(tasks)

def add_task():
 task = tasks.append(input("Enter your task: "))
 return task
add_task()
print(tasks)

def find_task():
 find = input("Enter task you want to find: ")
 print(find in tasks)
find_task()
print(tasks)