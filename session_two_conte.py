from datetime import time

principle = 2333333
rate = 12.5
time = 2.5
simple_interest = (principle * rate * time)/100
print(simple_interest)

# Python functions
def my_function():
  print("Hello from a function")

my_function()

# Usage of parameters under python function
# Parameters are specified after the function name, inside the parentheses.
# You can add as many parameters as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Reuben")
my_function("Oluyali")
my_function("Omolo")

# using default parameter value
# Example one
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# Example two
def my_function(food = "Ugali|kuku"):
    print("I like eating " + food)
my_function("Pilau|beef")
my_function()
my_function("Kunde|Ugali")
my_function("Rice|beans")

# using of function to return a value
def my_function(p):
    return 7 * p
print(my_function(34))
print(my_function(23))
print(my_function(3))
print(my_function(5))
print(my_function(87))

# Python lambda
x = lambda a: a + 10
print(x(45))

p = lambda w, q, r: w + q + r
print(p(10, 12, 23))

# Using lambda  as an anonymous function
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(2)

print(mytripler(12))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(12))
# When bot of the functions are combined
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(12))
print(mytripler(12))

# Python Arrays
food = ["ugali", "rice", "chicken"]
# printing a specific item in a list
f = food[2]

print(f)
# counting of items in a list
x = len(food)
print(x)

# append function is used in adding an element to an array
atire = ["shoes", "Uniform", "socks", "sweater"]
atire.append("wind_breker")
print(atire)
# Use of pop() function in removal of array elements(used to pop out a decimal number)
atire.pop(1)
print(atire)
# remove function may also be used simultaneously as pop() function i.e.(used to remove letters)
atire.remove("sweater")
print(atire)

# Usage of various elements in python in a list to enable quick formatting
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# python classes and objects
class MyClass:
  x = 45
p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Oluyali", 19)
p2 = Person("Reuben", 22)
p3 = Person("Omolo", 135)
p4 = Person("Penalope", 18)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p3.name)
print(p3.age)
print(p4.name)
print(p4.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# python modules
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Reuben", 19)
p1.myfunc()

import mymodule

mymodule.greeting("penalope")
import mymodule

a = mymodule.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)


# python datetime
import datetime

x = datetime.datetime.now()

print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.time())
print(x.strftime("%A"))