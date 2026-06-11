"""
04_property_decorator.py
Using @property Decorator for Computed Attributes
"""

print("=" * 70)
print("PYTHON @property DECORATOR")
print("=" * 70)

# ============================================================================
# 1. SIMPLE PROPERTY - GETTER
# ============================================================================
print("\n1. SIMPLE PROPERTY - GETTER")
print("-" * 70)

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Convention: _ means "private"
    
    @property
    def radius(self):
        """Get the radius."""
        return self._radius
    
    @property
    def area(self):
        """Computed property - area is calculated."""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """Computed property - circumference is calculated."""
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# ============================================================================
# 2. PROPERTY WITH SETTER
# ============================================================================
print("\n\n2. PROPERTY WITH SETTER")
print("-" * 70)

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature with validation."""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature from Fahrenheit."""
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin."""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Set temperature from Kelvin."""
        if value < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        self._celsius = value - 273.15

temp = Temperature(20)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit:.2f}°F")
print(f"Kelvin: {temp.kelvin:.2f}K")

print("\nSetting Fahrenheit to 68°F...")
temp.fahrenheit = 68
print(f"Celsius: {temp.celsius:.2f}°C")
print(f"Fahrenheit: {temp.fahrenheit:.2f}°F")
print(f"Kelvin: {temp.kelvin:.2f}K")

# ============================================================================
# 3. PROPERTY WITH VALIDATION
# ============================================================================
print("\n\n3. PROPERTY WITH VALIDATION")
print("-" * 70)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value
    
    @property
    def is_adult(self):
        """Computed property - read-only."""
        return self._age >= 18

person = Person("Alice", 25)
print(f"Name: {person.name}, Age: {person.age}")
print(f"Is adult: {person.is_adult}")

print("\nChanging age to 16...")
person.age = 16
print(f"Is adult: {person.is_adult}")

print("\nTrying to set invalid age...")
try:
    person.age = 200
except ValueError as e:
    print(f"Error: {e}")

# ============================================================================
# 4. READ-ONLY PROPERTIES
# ============================================================================
print("\n\n4. READ-ONLY PROPERTIES")
print("-" * 70)

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        """Read-only property - no setter."""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Read-only property - no setter."""
        return 2 * (self._width + self._height)

rect = Rectangle(5, 3)
print(f"Rectangle: {rect.width}x{rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

print("\nChanging width to 10...")
rect.width = 10
print(f"Area: {rect.area}")

print("\nTrying to set area (should fail)...")
try:
    rect.area = 100
except AttributeError as e:
    print(f"Error: can't set attribute")

# ============================================================================
# 5. PROPERTY WITH DELETER
# ============================================================================
print("\n\n5. PROPERTY WITH DELETER")
print("-" * 70)

class BankAccount:
    def __init__(self, holder, balance):
        self._holder = holder
        self._balance = balance
        self._is_closed = False
    
    @property
    def balance(self):
        if self._is_closed:
            raise ValueError("Account is closed")
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    @balance.deleter
    def balance(self):
        """Close account by deleting balance."""
        print(f"Account for {self._holder} is being closed...")
        self._is_closed = True
        self._balance = 0

account = BankAccount("John", 1000)
print(f"Balance: ${account.balance}")

print("\nClosing account...")
del account.balance
print(f"Account closed: {account._is_closed}")

# ============================================================================
# 6. COMPUTED PROPERTIES
# ============================================================================
print("\n\n6. COMPUTED PROPERTIES")
print("-" * 70)

class Student:
    def __init__(self, name, math_score, english_score, science_score):
        self.name = name
        self.math_score = math_score
        self.english_score = english_score
        self.science_score = science_score
    
    @property
    def average_score(self):
        """Computed from other attributes."""
        total = self.math_score + self.english_score + self.science_score
        return total / 3
    
    @property
    def grade(self):
        """Computed from average."""
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'
    
    @property
    def is_passing(self):
        return self.average_score >= 60

student = Student("Alice", 85, 90, 88)
print(f"Student: {student.name}")
print(f"Math: {student.math_score}, English: {student.english_score}, Science: {student.science_score}")
print(f"Average: {student.average_score:.2f}")
print(f"Grade: {student.grade}")
print(f"Passing: {student.is_passing}")

# ============================================================================
# 7. PROPERTY CACHING
# ============================================================================
print("\n\n7. PROPERTY CACHING")
print("-" * 70)

class ExpensiveComputation:
    def __init__(self):
        self._result = None
        self._computed = False
    
    @property
    def result(self):
        """Compute expensive result only once."""
        if not self._computed:
            print("Computing expensive result...")
            import time
            # time.sleep(1)  # Simulate expensive operation
            self._result = sum(range(1000000))
            self._computed = True
        return self._result
    
    def clear_cache(self):
        """Clear cached result."""
        self._computed = False
        self._result = None

compute = ExpensiveComputation()
print("First access:")
print(compute.result)

print("\nSecond access (cached):")
print(compute.result)

# ============================================================================
# 8. PRACTICAL EXAMPLE: COMPLETE CLASS
# ============================================================================
print("\n\n8. PRACTICAL EXAMPLE: COMPLETE CLASS")
print("-" * 70)

class BankAccountFull:
    """Complete bank account with properties."""
    
    def __init__(self, holder, initial_balance=0):
        self._holder = holder
        self._balance = initial_balance
        self._transactions = []
    
    @property
    def holder(self):
        """Account holder name (read-only)."""
        return self._holder
    
    @property
    def balance(self):
        """Current balance."""
        return self._balance
    
    @property
    def transactions(self):
        """List of transactions (read-only)."""
        return self._transactions.copy()
    
    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(("deposit", amount))
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(("withdrawal", amount))
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    @property
    def total_deposited(self):
        """Sum of all deposits."""
        return sum(amount for trans_type, amount in self._transactions if trans_type == "deposit")
    
    @property
    def total_withdrawn(self):
        """Sum of all withdrawals."""
        return sum(amount for trans_type, amount in self._transactions if trans_type == "withdrawal")

account_full = BankAccountFull("Jane", 500)
print(f"Account holder: {account_full.holder}")
print(f"Initial balance: ${account_full.balance}")

print(f"\n{account_full.deposit(200)}")
print(f"{account_full.withdraw(100)}")
print(f"{account_full.deposit(150)}")

print(f"\nTotal deposited: ${account_full.total_deposited}")
print(f"Total withdrawn: ${account_full.total_withdrawn}")
print(f"Current balance: ${account_full.balance}")
print(f"Transactions: {account_full.transactions}")

print("\n" + "=" * 70)
print("END OF @property DECORATOR TUTORIAL")
print("=" * 70)
