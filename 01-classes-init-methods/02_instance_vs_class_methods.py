"""
02_instance_vs_class_methods.py
Understanding Instance, Class, and Static Methods
"""

print("=" * 70)
print("INSTANCE vs CLASS vs STATIC METHODS")
print("=" * 70)

# ============================================================================
# 1. INSTANCE METHODS
# ============================================================================
print("\n1. INSTANCE METHODS")
print("-" * 70)

class Dog:
    """A dog class with instance methods."""
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    # Instance method - uses self
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(f"Instance method call: {dog.bark()}")
print(f"Instance method call: {dog.get_info()}")

# ============================================================================
# 2. CLASS VARIABLES vs INSTANCE VARIABLES
# ============================================================================
print("\n\n2. CLASS VARIABLES vs INSTANCE VARIABLES")
print("-" * 70)

class Car:
    # Class variable - shared by all instances
    total_cars = 0
    
    def __init__(self, brand, model):
        # Instance variables - unique to each instance
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
    def get_info(self):
        return f"{self.brand} {self.model}"

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("BMW", "X5")

print(f"Car 1: {car1.get_info()}")
print(f"Car 2: {car2.get_info()}")
print(f"Car 3: {car3.get_info()}")
print(f"Total cars created: {Car.total_cars}")

# ============================================================================
# 3. CLASS METHODS - @classmethod
# ============================================================================
print("\n\n3. CLASS METHODS - @classmethod")
print("-" * 70)

class Student:
    # Class variable
    total_students = 0
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        Student.total_students += 1
    
    # Instance method
    def get_info(self):
        return f"{self.name} (ID: {self.student_id})"
    
    # Class method - uses cls parameter
    @classmethod
    def from_string(cls, student_str):
        """Create student from string format 'name,id'."""
        name, student_id = student_str.split(",")
        return cls(name, student_id)
    
    # Class method - get class information
    @classmethod
    def total_count(cls):
        return f"Total students: {cls.total_students}"

# Using instance method
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

print(f"Instance 1: {student1.get_info()}")
print(f"Instance 2: {student2.get_info()}")

# Using class method
student3 = Student.from_string("Charlie,S003")
print(f"Created from string: {student3.get_info()}")

# Using class method to get class info
print(f"Class info: {Student.total_count()}")

# ============================================================================
# 4. STATIC METHODS - @staticmethod
# ============================================================================
print("\n\n4. STATIC METHODS - @staticmethod")
print("-" * 70)

class MathHelper:
    """Math helper with static methods."""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathHelper.factorial(n - 1)

print(f"Add(5, 3): {MathHelper.add(5, 3)}")
print(f"Multiply(4, 7): {MathHelper.multiply(4, 7)}")
print(f"Is 10 even? {MathHelper.is_even(10)}")
print(f"Is 7 even? {MathHelper.is_even(7)}")
print(f"Factorial(5): {MathHelper.factorial(5)}")

# ============================================================================
# 5. COMPARING METHOD TYPES
# ============================================================================
print("\n\n5. COMPARING METHOD TYPES")
print("-" * 70)

class BankAccount:
    min_balance = 100  # Class variable
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    # Instance method - operates on instance data
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    # Instance method - uses instance data
    def get_balance(self):
        return self.balance
    
    # Class method - operates on class data
    @classmethod
    def change_min_balance(cls, new_min):
        cls.min_balance = new_min
        return f"Minimum balance changed to ${new_min}"
    
    # Static method - pure utility function
    @staticmethod
    def validate_amount(amount):
        return amount > 0

# Using instance methods
account = BankAccount("John", 500)
print(account.deposit(100))
print(f"Balance: ${account.get_balance()}")

# Using class method
print(BankAccount.change_min_balance(200))

# Using static method
print(f"Is 50 valid? {BankAccount.validate_amount(50)}")
print(f"Is -10 valid? {BankAccount.validate_amount(-10)}")

# ============================================================================
# 6. WHEN TO USE EACH METHOD TYPE
# ============================================================================
print("\n\n6. WHEN TO USE EACH METHOD TYPE")
print("-" * 70)

class DataProcessor:
    # Class variable for tracking
    processed_count = 0
    
    def __init__(self, data):
        self.data = data
        self.result = None
    
    # Instance method - processes this instance's data
    def process(self):
        """Process the data in this instance."""
        self.result = self.data.upper() if isinstance(self.data, str) else self.data
        DataProcessor.processed_count += 1
        return self.result
    
    # Class method - factory method
    @classmethod
    def from_list(cls, items):
        """Create processor from list items."""
        return cls(", ".join(items))
    
    # Class method - get class statistics
    @classmethod
    def get_stats(cls):
        return f"Total processed: {cls.processed_count}"
    
    # Static method - utility for validation
    @staticmethod
    def is_valid_data(data):
        return data is not None and len(str(data)) > 0

print("Creating processors...")
proc1 = DataProcessor("hello")
proc2 = DataProcessor.from_list(["python", "is", "awesome"])

print(f"Process 1: {proc1.process()}")
print(f"Process 2: {proc2.process()}")

print(f"Class stats: {DataProcessor.get_stats()}")
print(f"Is 'data' valid? {DataProcessor.is_valid_data('data')}")
print(f"Is '' valid? {DataProcessor.is_valid_data('')}")

# ============================================================================
# 7. CALLING METHODS DIFFERENT WAYS
# ============================================================================
print("\n\n7. CALLING METHODS DIFFERENT WAYS")
print("-" * 70)

class Example:
    def __init__(self, value):
        self.value = value
    
    def instance_method(self):
        return f"Instance method: {self.value}"
    
    @classmethod
    def class_method(cls):
        return "Class method called"
    
    @staticmethod
    def static_method():
        return "Static method called"

# Create instance
obj = Example(42)

# Instance methods - called on instance
print(obj.instance_method())

# Class methods - can be called on class or instance
print(Example.class_method())
print(obj.class_method())  # Also works on instance

# Static methods - can be called on class or instance
print(Example.static_method())
print(obj.static_method())  # Also works on instance

# ============================================================================
# 8. PRACTICAL EXAMPLE: BOOK CLASS
# ============================================================================
print("\n\n8. PRACTICAL EXAMPLE: BOOK CLASS")
print("-" * 70)

class Book:
    """Book class demonstrating all method types."""
    
    total_books = 0
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False
        Book.total_books += 1
    
    # Instance methods
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"'{self.title}' borrowed"
        return f"'{self.title}' is already borrowed"
    
    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"'{self.title}' returned"
        return f"'{self.title}' was not borrowed"
    
    # Class method - factory
    @classmethod
    def from_csv(cls, csv_line):
        """Create book from CSV: title,author,isbn"""
        title, author, isbn = csv_line.split(",")
        return cls(title, author, isbn)
    
    # Class method - statistics
    @classmethod
    def library_size(cls):
        return f"Total books in library: {cls.total_books}"
    
    # Static method - validation
    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()

print("Creating books...")
book1 = Book("Python Guide", "John Doe", "1234567890123")
book2 = Book("Web Dev", "Jane Smith", "9876543210123")
book3 = Book.from_csv("Data Science,Alice Brown,5555555555555")

print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")
print(f"Book 3: {book3.title} by {book3.author}")

print("\n" + Book.library_size())

print(f"\nIs '1234567890123' valid ISBN? {Book.is_valid_isbn('1234567890123')}")
print(f"Is '123' valid ISBN? {Book.is_valid_isbn('123')}")

print(f"\nBorrowing book 1...")
print(book1.borrow())
print(book1.borrow())  # Try again

print(f"\nReturning book 1...")
print(book1.return_book())

print("\n" + "=" * 70)
print("END OF INSTANCE vs CLASS vs STATIC METHODS TUTORIAL")
print("=" * 70)
