#part i
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
num_rows = 5
print_pattern(num_rows)


#part ii
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

value = factorial(5)
print(f"The factorial of 5 is: {value}")



#part iii

def add_numbers(a, b):
    return a + b
value = add_numbers(3, 4)
print(f"The sum of 3 and 4 is: {value}")


# part iv
class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        

    def display_info(self):
        print(f"Car Information: {self.year} {self.brand} {self.color}")


#part v
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
       

    def display_info(self):
        print(f"Car Information: {self.year} {self.brand} ")
#instance
my_car = Car("Toyota", 2022)
my_car.display_info()
print(my_car)
