"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data

from math import sqrt

# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # Purpose: computes the number of vowels in text
    # Input(s): text - a string for which we want to count the number of vowels
    # Output: returns an integer representing the number of vowels in text

    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # Purpose: returns a new list containing only the sublists with length equal to 2
    # Input(s): items - a list of lists of integers containing our input
    # Output: returns a list of lists of integers containing only the sublists with length equal to 2

    return [sublist for sublist in items if len(sublist) == 2]


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: returns a new list in which each sublist will have the same order, unless the sublist has 2 elements, in which case the order will be ascending
    # Input(s): ascending_pairs - a list of lists of integers containing our input
    # Output: returns a list of lists of integers containing the same order as the input, except for sublists with 2 elements, which will be in ascending order

    new_list = []

    for sublist in items:
        if len(sublist) == 2 and sublist[0] > sublist[1]:
            new_list.append([sublist[1], sublist[0]])
        else:
            new_list.append(sublist)

    return new_list


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Purpose: returns a new Price object representing the sum of the input Price objects
    # Input(s): first - a Price object representing the first price to be added, second - a Price object representing the second price to be added
    # Output: returns a Price object representing the sum of the input Price objects

    new_cents = (first.cents + second.cents) % 100
    new_dollars = first.dollars + second.dollars + (first.cents + second.cents) // 100
    return data.Price(new_dollars, new_cents)

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: computes the area of the input rectangle
    # Input(s): rectangle - a Rectangle object representing the rectangle for which we want to compute the area
    # Output: returns a float representing the area of the input rectangle

    return abs(rectangle.bottom_right.x - rectangle.top_left.x) * abs(rectangle.top_left.y - rectangle.bottom_right.y)


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: computes a list of books written by the specified author
    # Input(s): author - a string representing the author, books - a list of Book objects as input
    # Output: returns a list of Book objects written by the specified author

    my_books = []
    for book in books:
        for book_author in book.authors:
            if book_author == author:
                my_books.append(book)

    return my_books
            


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: computes the smallest circle that can enclose the rectangle
    # Input(s): rectangle - a Rectangle object as input
    # Output: returns a Circle object representing the smallest circle that can enclose the rectangle

    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    radius = sqrt(((rectangle.bottom_right.x - rectangle.top_left.x) ** 2) + ((rectangle.top_left.y - rectangle.bottom_right.y) ** 2)) / 2

    return data.Circle(data.Point(center_x, center_y), radius)

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: computes the average pay of employees and returns a list of names of employees who are payed below average
    # Input(s): employees - a list of Employee objects as input
    # Output: returns a list of strings representing the names of employees who are payed below average
    if len(employees) == 0:
        return []

    total_pay = 0
    for employee in employees:
        total_pay += employee.pay_rate
    average_pay = total_pay / len(employees)

    return [employee.name for employee in employees if employee.pay_rate < average_pay]
