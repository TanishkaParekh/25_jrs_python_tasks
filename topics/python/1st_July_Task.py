# Numpy
# Q1: Given a 2D NumPy array A of shape (5, 5), subtract the mean of each row from every element in that row without using a loop.
# Q2: You have a NumPy array of integers from 1 to 1000. Return a new array containing only the numbers that are divisible by both 3 and 7 but not by 5.
# Q3: Create an 8x8 NumPy array with a chessboard pattern (alternating 0s and 1s), where the top-left element is 0.
import numpy as np
print("Answer 1")
A1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(A.shape)
A2 = np.array([[(np.mean(A,axis = 1))[0]],[(np.mean(A,axis = 1))[1]],[(np.mean(A,axis = 1))[2]],[(np.mean(A,axis = 1))[3]],[(np.mean(A,axis = 1))[4]]])
print(A1-A2)

print("Answer 2")
B1 = np.arange(0,1000,21)
B1 = B1[B1%5 != 0]
print(B1)
#or
B=np.arange(1,1000)
B1 = B[(B%7==0)&(B%3==0)&(B%5!=0)]
print(B1)

print("Answer 3")
C1 = np.zeros((8,1))
C2 = np.ones((8,1))
C=np.concatenate((C1,C2),axis=1)
C=np.concatenate((C,C),axis=1)
C=np.concatenate((C,C),axis=1)
print(C)

# Pandas (Create a DataFrame with the specified columns and perform the operations)
import pandas as pd
# Q1: Given a DataFrame df with columns: ["department", "employee", "salary"], normalize the salary within each department (i.e., for each department, subtract the mean and divide by the std of that department).
# Q2: Given a DataFrame with columns ["timestamp", "user_id", "action"], where timestamp is in string format, find the average number of actions per user per day.
# Q3: You have a DataFrame with columns: ["user_id", "product", "price", "quantity", "date"]. Calculate the total amount spent by each user on "Laptop" purchases only, and return the result as a new DataFrame with columns: ["user_id", "total_spent_on_laptops"].

