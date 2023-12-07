#number 1, part i

import math

def calculate_area(radius):
    area = math.pi * radius**2
    return (area)
#testing for radius 5
radius = 5
area_of_circle = calculate_area(radius)
print(f"The area of a circle with radius  is: {area_of_circle}")


#part ii
def calculate_sum_of_naturals(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum_of_naturals(n - 1)
n = 4
sum_of_naturals = calculate_sum_of_naturals(n)
print(f"The sum of natural numbers up to {n} is: {sum_of_naturals}")

#part iii

numbers = [1, 3, 5, 7, 9]
numbers.append(10)
print("Updated list:", numbers)

#part iv

numbers = [2, 4, 6, 8, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)


#part v
student_info = {'name': 'alice', 'age': 20, 'grade': 'a'}
student_info['age'] = 25
student_info['city'] = 'New york'
print("Updated student information:", student_info)


#PART VI
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}
filtered_dict = {key: value for key, value in original_dict.items() if value > 5}
print("New dictionary with values greater than 5:", filtered_dict)
