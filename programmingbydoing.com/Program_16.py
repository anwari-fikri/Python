# Name, Age and Salary

import sys

print("Hello. What is your name?")
name = sys.stdin.readline()

print("Hi, " + name + "! How old are you?")
age = sys.stdin.readline()

print("So you're " + age + ", That's not old at all!")
print("How much do you make " + name + "?")
income = sys.stdin.readline()

print(income + "! I hope that's per hour not per year! LOL!")
