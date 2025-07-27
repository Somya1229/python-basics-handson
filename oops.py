"""
OOPS Concepts in Python
Demonstrates:
1. Class Variables vs Instance Variables
2. Constructor (__init__)
3. Inheritance
4. Method Overriding
5. Basic Practical Examples (Car and Animal classes)
"""

# =========================================
# Car Class Example
# =========================================

class Cars:
    # Class variable (shared by all instances)
    wheel = 4

    def __init__(self, model, name, year):
        # Instance variables (unique to each object)
        self.model = model
        self.name = name
        self.year = year

    def drive(self):
        """Method to display driving action"""
        print(f"{self.model} is driving")


# =========================================
# Animal Class (Base Class)
# =========================================

class Animal:
    alive = True  # Class variable
    can_eat = True

    def eat(self, name):
        """Method to describe eating behavior"""
        self.name = name
        print(f"The {self.name} can eat")


# =========================================
# Bird Class (Inherited from Animal)
# =========================================

class Birds(Animal):
    def fly(self, name):
        """Method to describe flying behavior"""
        self.name = name
        print(f"The {self.name} can fly")


# =========================================
# Fibonacci Function Example
# =========================================

def fibonacci(n):
    """
    Print Fibonacci sequence up to n terms
    Example: fibonacci(5) -> 0 1 1 2 3
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # Newline after sequence


# =========================================
# Demo Execution (Will only run when file executed directly)
# =========================================
if __name__ == "__main__":
    # Car Example
    car1 = Cars("Audi", "Q5", "2022")
    car2 = Cars("Ford", "Mustang", "2021")

    car1.drive()
    car2.drive()

    # Bird Example (Inheritance)
    bird = Birds()
    bird.eat("Elephant")
    bird.fly("Hawk")

    # Fibonacci Example
    print("Fibonacci (5 terms):")
    fibonacci(5)

    print("Fibonacci (10 terms):")
    fibonacci(10)
