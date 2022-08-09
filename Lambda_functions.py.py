#creating a list of integers between 5.5 and 20.5
i = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#printing even numbers in the list
even_no = list(filter(lambda x: (x % 2 == 0), i))
print("Even numbers in the list: ", even_no) 

#printing odd numbers in the list
odd_no = list(filter(lambda x: (x % 2 != 0), i))
print("Odd numbers in the list: ", odd_no) 

#counting the even numbers in the list
even_count = len(list(filter(lambda x: (x%2 == 0) , i)))
print("Even numbers available in the list: ", even_count)

#counting the odd numbers in the list
odd_count = len(list(filter(lambda x: (x%1 == 0) , i)))
print("Odd numbers available in the list: ", odd_count)

#printing the squares of the list
square = list(map(lambda x: (x**2), i))
print(square)

#printing the cube of the list
cube = list(map(lambda x: (x**3), i))
print(cube)