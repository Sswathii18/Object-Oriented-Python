"""
01_class_basics.py
Fundamentals of Classes and __init__ in Python
"""

print("=" * 70)
print("PYTHON CLASSES - BASICS")
print("=" * 70)

# ============================================================================
# 1. SIMPLE CLASS DEFINITION
# ============================================================================
print("\n1. SIMPLE CLASS DEFINITION")
print("-" * 70)

class Dog:
    """A simple dog class."""
    pass

# Creating an instance
my_dog = Dog()
print(f"Created an instance: {my_dog}")
print(f"Type: {type(my_dog)}")

# ============================================================================
# 2. __init__ CONSTRUCTOR METHOD
# ============================================================================
print("\n\n2. __init__ CONSTRUCTOR METHOD")
print("-" * 70)

class Cat:
    """A cat with name and age."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Whiskers", 3)
print(f"Cat created: {cat1.name}, Age: {cat1.age}")

cat2 = Cat("Mittens", 5)
print(f"Cat created: {cat2.name}, Age: {cat2.age}")

# ============================================================================
# 3. INSTANCE VARIABLES
# ============================================================================
print("\n\n3. INSTANCE VARIABLES")
print("-" * 70)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = "2024-01-01"

person1 = Person("Alice", "alice@example.com")
person2 = Person("Bob", "bob@example.com")

print(f"Person 1: {person1.name}, {person1.email}")
print(f"Person 2: {person2.name}, {person2.email}")

# Each instance has separate attributes
print(f"Modifying person1.name...")
person1.name = "Alice Smith"
print(f"Person 1 name: {person1.name}")
print(f"Person 2 name: {person2.name} (unchanged)")

# ============================================================================
# 4. INSTANCE METHODS
# ============================================================================
print("\n\n4. INSTANCE METHODS")
print("-" * 70)

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into account."""
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds"
    
    def get_balance(self):
        """Get current balance."""
        return self.balance

account = BankAccount("John", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.get_balance()}")

# ============================================================================
# 5. ATTRIBUTES CREATED OUTSIDE __init__
# ============================================================================
print("\n\n5. ATTRIBUTES CREATED OUTSIDE __init__")
print("-" * 70)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999.99)
print(f"Product: {product.name}, Price: ${product.price}")

# Add new attribute dynamically
product.stock = 50
print(f"Stock: {product.stock}")

product.discount = 0.1  # 10% discount
print(f"Discount: {product.discount * 100}%")
print(f"Final price: ${product.price * (1 - product.discount)}")

# ============================================================================
# 6. DEFAULT VALUES IN __init__
# ============================================================================
print("\n\n6. DEFAULT VALUES IN __init__")
print("-" * 70)

class Car:
    def __init__(self, brand, model, year=2024):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry")  # Uses default year
car2 = Car("Honda", "Civic", 2020)  # Custom year

print(f"Car 1: {car1.brand} {car1.model} ({car1.year})")
print(f"Car 2: {car2.brand} {car2.model} ({car2.year})")

# ============================================================================
# 7. MULTIPLE INSTANCES, INDEPENDENT STATE
# ============================================================================
print("\n\n7. MULTIPLE INSTANCES, INDEPENDENT STATE")
print("-" * 70)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(92)

student2.add_grade(78)
student2.add_grade(82)

print(f"{student1.name}: Average = {student1.average():.2f}")
print(f"{student2.name}: Average = {student2.average():.2f}")

# ============================================================================
# 8. self PARAMETER
# ============================================================================
print("\n\n8. self PARAMETER")
print("-" * 70)

class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, x):
        self.value += x
        return self.value
    
    def multiply(self, x):
        self.value *= x
        return self.value
    
    def reset(self):
        self.value = 0

calc = Calculator(10)
print(f"Initial: {calc.value}")
print(f"After add(5): {calc.add(5)}")
print(f"After multiply(2): {calc.multiply(2)}")
print(f"After reset(): {calc.reset()}")

# ============================================================================
# 9. TYPE HINTS IN __init__
# ============================================================================
print("\n\n9. TYPE HINTS IN __init__")
print("-" * 70)

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

rect = Rectangle(5.0, 3.0)
print(f"Rectangle: {rect.width} x {rect.height}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# ============================================================================
# 10. DOCSTRINGS
# ============================================================================
print("\n\n10. DOCSTRINGS")
print("-" * 70)

class Temperature:
    """Represents a temperature value in Celsius."""
    
    def __init__(self, celsius: float):
        """Initialize with temperature in Celsius.
        
        Args:
            celsius: Temperature value in Celsius
        """
        self.celsius = celsius
    
    def to_fahrenheit(self) -> float:
        """Convert temperature to Fahrenheit.
        
        Returns:
            Temperature in Fahrenheit
        """
        return self.celsius * 9/5 + 32
    
    def to_kelvin(self) -> float:
        """Convert temperature to Kelvin.
        
        Returns:
            Temperature in Kelvin
        """
        return self.celsius + 273.15

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.to_fahrenheit()}°F")
print(f"Kelvin: {temp.to_kelvin()}K")

print(f"\nDocstring: {Temperature.__doc__}")
print(f"Method docstring: {Temperature.to_fahrenheit.__doc__}")

# ============================================================================
# 11. PRIVATE ATTRIBUTES (CONVENTION)
# ============================================================================
print("\n\n11. PRIVATE ATTRIBUTES (CONVENTION)")
print("-" * 70)

class BankAccount2:
    def __init__(self, holder, initial_balance=0):
        self.holder = holder
        self._balance = initial_balance  # Convention: _ means private
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def get_balance(self):
        return self._balance

account2 = BankAccount2("Jane", 500)
print(f"Account holder: {account2.holder}")
print(f"Balance: ${account2.get_balance()}")
account2.deposit(200)
print(f"After deposit: ${account2.get_balance()}")

# ============================================================================
# 12. PRACTICAL EXAMPLE: BOOK CLASS
# ============================================================================
print("\n\n12. PRACTICAL EXAMPLE: BOOK CLASS")
print("-" * 70)

class Book:
    """Represents a book with title, author, and ISBN."""
    
    def __init__(self, title: str, author: str, isbn: str, year: int = 2024):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False
    
    def borrow(self) -> str:
        if self.is_borrowed:
            return f"'{self.title}' is already borrowed"
        self.is_borrowed = True
        return f"'{self.title}' borrowed successfully"
    
    def return_book(self) -> str:
        if not self.is_borrowed:
            return f"'{self.title}' was not borrowed"
        self.is_borrowed = False
        return f"'{self.title}' returned successfully"
    
    def get_info(self) -> str:
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({self.year}) - {status}"

book1 = Book("Python 101", "John Doe", "978-1234567890", 2023)
book2 = Book("Web Dev", "Jane Smith", "978-0987654321")

print(book1.get_info())
print(book2.get_info())

print("\nBorrowing books...")
print(book1.borrow())
print(book1.get_info())
print(book1.borrow())  # Try to borrow again

print("\nReturning book...")
print(book1.return_book())
print(book1.get_info())

print("\n" + "=" * 70)
print("END OF CLASS BASICS TUTORIAL")
print("=" * 70)
