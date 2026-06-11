# 01 - Classes, `__init__`, Instance vs Class Methods

## 📚 Overview

This section covers the fundamentals of object-oriented programming in Python, focusing on:
- Class definition and instantiation
- The `__init__` constructor method
- Instance variables and methods
- Class variables and methods
- Static methods
- Special methods and properties

## 🎯 Learning Objectives

After completing this section, you will understand:

✅ How to define classes and create objects
✅ How `__init__` works for initialization
✅ The difference between instance and class variables
✅ How to use instance, class, and static methods
✅ The role of `self` and `cls` parameters
✅ Special methods like `__str__` and `__repr__`
✅ Property decorators for computed attributes

## 📖 Key Concepts

### Class Definition
```python
class Dog:
    """A simple dog class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### Instance Variables vs Class Variables
```python
class Car:
    # Class variable (shared across all instances)
    total_cars = 0
    
    def __init__(self, brand):
        # Instance variables (unique per object)
        self.brand = brand
        Car.total_cars += 1
```

### Instance Methods
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):  # Instance method
        return f"Hello, I'm {self.name}"
```

### Class Methods
```python
class Student:
    total_students = 0
    
    @classmethod
    def from_file(cls, filepath):
        """Create student from file."""
        # Use cls instead of Student
        return cls("name")
```

### Static Methods
```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
```

### Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2
```

## 📁 Files in This Section

### 1. `01_class_basics.py`
Covers:
- Class definition and instantiation
- `__init__` constructor
- Instance variables
- Instance methods
- Object attributes
- `self` parameter

**Examples**: 15+ practical examples with output

### 2. `02_instance_vs_class_methods.py`
Covers:
- Instance methods
- Class methods (`@classmethod`)
- Static methods (`@staticmethod`)
- When to use each type
- `self` vs `cls` parameters
- Common patterns and use cases

**Examples**: 20+ method examples

### 3. `03_special_methods.py`
Covers:
- `__str__` and `__repr__`
- `__len__` and `__getitem__`
- `__add__` and operator overloading
- `__eq__` and comparison
- `__call__` and callable objects
- `__enter__` and `__exit__` (context managers)

**Examples**: 25+ special method examples

### 4. `04_property_decorator.py`
Covers:
- `@property` decorator
- Getters and setters
- Computed properties
- Validation with setters
- Read-only properties
- Property deletion

**Examples**: 15+ property examples

## 🚀 Getting Started

### Run the tutorials:
```bash
# Run in sequence
python 01_class_basics.py
python 02_instance_vs_class_methods.py
python 03_special_methods.py
python 04_property_decorator.py
```

## 💡 Key Takeaways

### `self` vs `cls`

| Aspect | Instance Method | Class Method | Static Method |
|--------|-----------------|--------------|---------------|
| First parameter | `self` | `cls` | None (no implicit) |
| Access | Instance data | Class data | None |
| Called on | Object instance | Class | Both (convention matters) |
| Use case | Normal operations | Constructors, utilities | Pure functions |

### When to Use Each

```python
class Example:
    class_var = "shared"
    
    def __init__(self, value):
        self.instance_var = value
    
    # Use for normal operations
    def instance_method(self):
        return self.instance_var
    
    # Use for alternative constructors
    @classmethod
    def from_string(cls, s):
        return cls(int(s))
    
    # Use for utility functions
    @staticmethod
    def is_valid(value):
        return isinstance(value, int)
```

## 📝 Exercises

### Exercise 1: Bank Account
Create a `BankAccount` class with:
- `__init__` that takes account holder name and initial balance
- Instance methods for deposit and withdrawal
- Class variable to track total accounts
- Class method to create account with zero balance
- Special method `__str__` for printing account info

### Exercise 2: Student Class
Create a `Student` class with:
- Instance variables for name, ID, grades
- Method to calculate average grade
- Class method to create from CSV line
- Static method to validate ID format
- Property for grade letter (A, B, C, etc.)

### Exercise 3: Temperature Converter
Create a `Temperature` class with:
- Private `_celsius` attribute
- Properties for celsius, fahrenheit, kelvin
- Setters that validate temperature
- Static method for conversion formulas

### Exercise 4: Rectangle Class
Create a `Rectangle` class with:
- Instance variables width and height
- Properties for area and perimeter
- Method to scale size
- Special methods for string representation
- Class variable to track total rectangles

## 🔍 Common Mistakes

### ❌ Forgetting `self`
```python
# Wrong
class Dog:
    def bark():
        print("Woof!")

# Right
class Dog:
    def bark(self):
        print("Woof!")
```

### ❌ Using class variable for instance data
```python
# Wrong - all instances share the same list
class Container:
    items = []  # DON'T do this

# Right - each instance has its own list
class Container:
    def __init__(self):
        self.items = []  # Do this
```

### ❌ Mutable default arguments
```python
# Wrong
class Config:
    def __init__(self, options={}):
        self.options = options  # Shared across instances

# Right
class Config:
    def __init__(self, options=None):
        self.options = options or {}
```

## 📚 Best Practices

1. **Use `__init__` for initialization**: Initialize all attributes here
2. **Name private attributes with `_`**: `self._private_var`
3. **Use properties for computed values**: Not methods that return fixed attributes
4. **Document with docstrings**: Explain what each method does
5. **Follow naming conventions**: Classes are PascalCase, methods are snake_case
6. **Use type hints**: Makes code clearer and enables IDE support

## 📖 Further Reading

- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Understanding `self`](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Properties in Python](https://www.datacamp.com/tutorial/property-decorator-python)
- [Special Methods (Dunder Methods)](https://docs.python.org/3/reference/datamodel.html)

## 🎓 Next Steps

After mastering this section:
1. Complete all exercises above
2. Modify examples and experiment
3. Move to **02-inheritance-encapsulation-polymorphism**
4. Apply these concepts in the sample projects

---

**Happy Learning!** 🐍
