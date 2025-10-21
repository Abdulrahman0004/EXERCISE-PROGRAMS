import numpy as np

#Example 1:
arr1 = np.arange(10)
print(arr1)
print(arr1[5])
print(arr1[-2])

#Example 2:
Scores = np.array(['86', '98', '100', '65', '75'])
print(Scores)
print("The second student score is: ", Scores[1])

#Example 3:
grocery_list = np.array(['carrot', 'beetroot', 'brinjal', 'banana', 'mango', 'potato', 'apple'])
print(grocery_list)
print(grocery_list[5])

#Example 4:
student_score = np.array([[99, 87, 63], [100, 98, 78], [95, 100, 96]])
print(student_score)
print("Student3 score in 2nd subject is :", student_score[2, -2])

#Example 5:
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1[2] + arr1[3])

#Example 6:
arr1 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("\n", arr1)
print(arr1[0, 1, -3])


