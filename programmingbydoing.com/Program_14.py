# Asking Questions

import sys

print("How old are you?")
age = sys.stdin.readline()

print("How many feet tall are you?")
feet = sys.stdin.readline()

print("And how many inches?")
inch = sys.stdin.readline()

print("How much do you weigh?")
weight = sys.stdin.readline()

print("So you're " + str(age) + " years old, " + str(feet) + "'" + str(inch) + "\" tall and " + str(weight) + " heavy.")

# how to remove nextline from sys.stdin.readline() ??????????????
