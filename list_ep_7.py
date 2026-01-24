""" Write a Python program to extract a given number of randomly selected elements from a given list.
Original list:[1, 9, 2, 3, 7, 4, 5, 12] Selected 3 random numbers of the above list: [4, 9, 1]"""
from random import *
ls=list(map(int,input().split(",")))
n=int(input("no of random samples: "))
print(sample(ls,n))