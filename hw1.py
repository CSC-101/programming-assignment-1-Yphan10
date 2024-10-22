import data
import math
# Write your functions for each part in the space below.

# Part 1
def vowel_count(s: str) -> int:
    #Returns the number of vowels in the input string s
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels) # Count and return the number of vowels

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    return [sublist for sublist in lst if len(sublist) == 2]  # Return sublists with exactly 2 elements

# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    return [sorted(sublist) if len(sublist) == 2 else sublist for sublist in lst] # Sort pairs, keep others unchanged

# Part 4
class Price:
    # Initialize a Price object with dollars and cents.
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents
    def __eq__(self, other):
        return (self.dollars == other.dollars) and (self.cents == other.cents)

def add_prices(p1: Price, p2: Price) -> Price:
    #Add two Price objects together.
    total_cents = p1.cents + p2.cents #add cents
    total_dollars = p1.dollars + p2.dollars + (total_cents // 100) # Add dollars and carry over cents
    return Price(dollars=total_dollars, cents=total_cents % 100) # Return new Price object

# Part 5
class Point:
    # Initialize a Point object with x and y coordinates.
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
class Rectangle:
    #Initialize a Rectangle object with top-left and bottom-right corners.
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

def rectangle_area(rect: Rectangle) -> int:
    #Calculate the area of a rectangle.
    width = rect.bottom_right.x - rect.top_left.x #calculate width
    height = rect.bottom_right.y - rect.top_left.y #calculate height
    return width * height

# Part 6
class Book:
    # Initialize a Book object with author and title.
    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title
    def __eq__(self, other):
        return (self.author == other.author) and (self.title == other.title)
def books_by_author(author: str, books: list[Book]) -> list[Book]:
    #A list of books written by the specified author.
    return [book for book in books if book.author == author] # Return books by the specified author

# Part 7
class Circle:
    #  Initialize a Circle object with a center point and radius.
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
def circle_bound(rect: Rectangle) -> Circle:
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2 # Calculate center x-coordinate
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2 # Calculate center y-coordinate
    radius = math.sqrt((rect.bottom_right.x - center_x) ** 2 + (rect.bottom_right.y - center_y) ** 2) #calculate radius
    return Circle(Point(center_x, center_y), radius)

# Part 8
class Employee:
    # Initialize an Employee object with a name and salary.
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees: # Check if the list is empty
        return []
    average_pay = sum(emp.salary for emp in employees)/ len(employees) # Calculate average salary
    return [emp.name for emp in employees if emp.salary < average_pay] # Return names of employees below average

