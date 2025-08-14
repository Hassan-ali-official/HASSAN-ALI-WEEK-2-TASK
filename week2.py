#  Store 5 student names & print each.


students = ["Ali", "Hassan", "Sara", "Ayesha", "Bilal"]
for name in students:
    print(name)


# . Reverse list without reverse().


students = ["Ali", "Hassan", "Sara", "Ayesha", "Bilal"]
reversed_students = students[::-1]
print(reversed_students)



# . Store 3 coordinates & unpack.


coords = (10, 20, 30)
x, y, z = coords
print(x, y, z)



#. Swap vars using tuple assignment.


a, b = 5, 10
a, b = b, a
print(a, b)



# Remove duplicates from list.


nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)



# Find intersection of two sets.


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1 & set2
print(intersection)



#. Student record CRUD in dict.


student = {'name': 'Hassan', 'age': 22, 'grade': 'A'}
student['subject'] = 'Math'  # Create
print(student)               # Read
student['grade'] = 'A+'      # Update
del student['subject']       # Delete
print(student)



#. Count word frequency in sentence.


sentence = "python is fun and python is powerful"
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)



#. Write calc(a,b,op).


def calc(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else None
    else: return None

print(calc(5, 3, '+'))
print(calc(5, 3, '-'))
print(calc(5, 3, '*'))
print(calc(5, 0, '/'))



#. Write factorial(n) recursive.


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n-1)

print(factorial(5))


#. Use random & datetime in script.


import random
from datetime import datetime

print(random.randint(1, 100))
print(datetime.now())



#. Create math_utils module & import.


# math_utils.py
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else None

# main.py
import math_utils
print(math_utils.add(2, 3))
print(math_utils.sub(7, 4))
print(math_utils.mul(3, 5))
print(math_utils.div(10, 2))
print(math_utils.div(10, 0))



#. Safe int input loop.

while True:
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
        break
    except ValueError:
        print("Invalid input, please try again.")


# File open with error message.

try:
    with open("file.txt", "r") as f:
        data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found.")



# Phonebook App: CRUD contacts dict <-> JSON file storage

import json

def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as f:
        json.dump(contacts, f)

def add_contact(contacts, name, phone):
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact '{name}' saved.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

contacts = load_contacts()
add_contact(contacts, "Hassan", "12345")
add_contact(contacts, "Ali", "98765")
view_contacts(contacts)
delete_contact(contacts, "Ali")
view_contacts(contacts)


