''' 1)
Write a Python program to filter a list of integers using Lambda.

Expected output:
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
'''
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter even integers
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))

# filter odd integers
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

# print output
print("even_numbers = ", even_numbers)
print("odd_numbers = ", odd_numbers)

''' 2)
Create a list of days that have exactly 6 characters using a lambda function on the list below. 
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# filter by 6 using lambda
six_chars = list(filter(lambda day:len(day) == 6, weekdays))

print("The days with 6 characters are: ", six_chars)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

Expected output
['red', 'green', 'blue', 'white']

'''

words = ['orange', 'red', 'green', 'blue', 'white', 'black']

remove_words = ['orange', 'black']

# filter and remove
filtered_words = list(filter(lambda word: word not in remove_words, words))

print(filtered_words)

''' 4) 
You are given a list of temperatures in Celsius: [0, 12, 34, 25, -5]. Use map() and a lambda function to convert each temperature to Fahrenheit.

Expected output: [32.0, 53.6, 93.2, 77.0, 23.0]

'''

cel = [0, 12, 34, 25, -5]

# using map and lambda to convert to Fahrenheit
# formula: (celsius * 9/5) + 32
fahrenheit = list(map(lambda c: (c * 9/5) + 32, cel))

print(fahrenheit)


''' 5) Use map() with a lambda function to calculate the final price for each item in the card after applying a 10% discount.
'''

cart = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Phone', 'price': 800},
    {'name': 'Tablet', 'price': 300},
    {'name': 'Monitor', 'price': 150}
]

# using map and lambda to apply a 10% discount
discounted_cart = list(map(lambda item: {'name': item['name'], 'price': round(item['price'] * 0.9, 2)}, cart))

print(discounted_cart)


''' 6)
Write a lambda function that takes two arguments x and y and returns:

    "x is greater" if x > y
    "y is greater" if y > x
    "Equal" if x == y

 '''

compare = lambda x, y: "x is greater" if x > y else ("y is greater" if y > x else "Equal")

print(compare(5, 3))  # Output: 'x is greater'
print(compare(3, 7))  # Output: 'y is greater'
print(compare(4, 4))  # Output: 'Equal'




''' 7)
Write a lambda function to sort the list by the length of each string.
Expected Output: ['C', 'Java', 'Ruby', 'Python', 'JavaScript']


'''
languages = ['Python', 'Java', 'C', 'Ruby', 'JavaScript']

# using sorted() with lambda to sort by length
sorted_languages = sorted(languages, key = lambda x: len(x))

print(sorted_languages)


''' 8)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Using sorted() with lambda to sort by the second element
sorted_scores = sorted(original_scores, key = lambda x: x[1])

print(sorted_scores)






''' 9)
Given a dictionary of student names and their scores, use a lambda function to increase each score by 5:

Expected output:
curved scores = {'Alice': 90, 'Bob': 92, 'Charlie': 83}

'''

students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
curved_scores = {name: (lambda score: score + 5)(score) for name, score in students.items()}

print("Curved scores:", curved_scores)











#CHALLENGE QUESTION (Not required)!!
''' 10)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

#str1 = "Hello8world"
#str1 = "HELLO"
#str1= "hello"