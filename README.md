# 🏛️ Object-Oriented Python

A comprehensive guide to mastering Object-Oriented Programming (OOP) in Python with 4 major topics, 15+ tutorial files, and 10 challenging real-world projects.

## 📚 What You'll Learn

This repository covers advanced OOP concepts that are essential for professional Python development:

### 1️⃣ **Classes, `__init__`, Instance vs Class Methods**
- Class fundamentals and object creation
- Constructor (`__init__`) and object initialization
- Instance variables and methods
- Class variables and methods
- Static methods
- `self` and `cls` parameters

### 2️⃣ **Inheritance, Encapsulation, Polymorphism**
- Single and multiple inheritance
- Method resolution order (MRO)
- `super()` function
- Private, protected, and public attributes
- Data hiding and encapsulation
- Duck typing and polymorphism
- Abstract base classes (ABC)

### 3️⃣ **Dataclasses**
- Introduction to dataclasses
- Field definitions and defaults
- Post-init processing
- Frozen dataclasses
- Comparing and hashing dataclasses
- Evolution and compatibility

### 4️⃣ **Pydantic Models**
- Introduction to Pydantic
- Field validation
- Custom validators
- Config classes
- Model inheritance
- JSON schema generation
- Integration with FastAPI/LLM frameworks

## 📁 Repository Structure

```
Object-Oriented-Python/
├── README.md
├── SAMPLE_PROJECTS.md
│
├── 01-classes-init-methods/
│   ├── README.md
│   ├── 01_class_basics.py
│   ├── 02_instance_vs_class_methods.py
│   ├── 03_special_methods.py
│   └── 04_property_decorator.py
│
├── 02-inheritance-encapsulation-polymorphism/
│   ├── README.md
│   ├── 01_inheritance_basics.py
│   ├── 02_multiple_inheritance.py
│   ├── 03_encapsulation.py
│   ├── 04_polymorphism.py
│   └── 05_abstract_classes.py
│
├── 03-dataclasses/
│   ├── README.md
│   ├── 01_dataclass_basics.py
│   ├── 02_dataclass_advanced.py
│   └── 03_dataclass_patterns.py
│
└── 04-pydantic-models/
    ├── README.md
    ├── 01_pydantic_basics.py
    ├── 02_validation_validators.py
    ├── 03_pydantic_advanced.py
    └── 04_pydantic_real_world.py
```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sswathii18/Object-Oriented-Python.git
   cd Object-Oriented-Python
   ```

2. **Run tutorial files**
   ```bash
   # Topic 1: Classes and Methods
   python 01-classes-init-methods/01_class_basics.py
   
   # Topic 2: Inheritance and Polymorphism
   python 02-inheritance-encapsulation-polymorphism/01_inheritance_basics.py
   
   # Topic 3: Dataclasses
   python 03-dataclasses/01_dataclass_basics.py
   
   # Topic 4: Pydantic Models
   python 04-pydantic-models/01_pydantic_basics.py
   ```

3. **Explore sample projects**
   See `SAMPLE_PROJECTS.md` for 10 challenging projects

## 📖 Topics Overview

### Topic 1: Classes, `__init__`, Instance vs Class Methods
**Files**: 4 tutorial files with 50+ examples
- Class definition and instantiation
- Constructor and initialization
- Instance, class, and static methods
- Special methods (`__str__`, `__repr__`, `__len__`)
- Property decorator and computed properties

### Topic 2: Inheritance, Encapsulation, Polymorphism
**Files**: 5 tutorial files with 60+ examples
- Single and multiple inheritance
- Method resolution order (MRO)
- Protected and private attributes
- Encapsulation best practices
- Polymorphism and method overriding
- Abstract base classes

### Topic 3: Dataclasses
**Files**: 3 tutorial files with 40+ examples
- Simplified class definition
- Automatic `__init__`, `__repr__`, `__eq__`
- Field configuration
- Post-init processing
- Frozen dataclasses

### Topic 4: Pydantic Models
**Files**: 4 tutorial files with 50+ examples
- Data validation
- Type checking
- Custom validators
- Config and settings
- JSON schema generation
- Integration with ML/AI frameworks

## 🏆 Sample Projects Overview

This repository includes **10 challenging real-world projects**:

1. **Banking System** - Multi-level inheritance, encapsulation
2. **E-Commerce Platform** - Complex object relationships
3. **Game Development** - Polymorphism and design patterns
4. **AI Chat Bot** - Pydantic for tool schemas (LLM integration)
5. **Data Pipeline** - Abstract classes and composition
6. **Configuration Manager** - Dataclasses and validation
7. **ORM (Database Layer)** - Advanced OOP patterns
8. **File System** - Inheritance and polymorphism
9. **Event Management** - Observer pattern with OOP
10. **Microservices API** - Pydantic models with FastAPI

See `SAMPLE_PROJECTS.md` for detailed descriptions and code structure.

## 💻 Prerequisites

- Python 3.8+
- Basic Python knowledge (from Core-Python repo recommended)
- Understanding of functions and data structures
- Text editor or IDE (VS Code, PyCharm, etc.)

## 📦 Dependencies

For Pydantic projects:
```bash
pip install pydantic>=2.0
pip install fastapi uvicorn  # For API projects
```

## ✨ Features

✅ **15+ Tutorial Files** with detailed explanations
✅ **100+ Code Examples** covering all OOP concepts
✅ **10 Real-World Projects** with varying difficulty
✅ **Best Practices** for professional development
✅ **Design Patterns** (Singleton, Factory, Observer, etc.)
✅ **Performance Considerations** throughout
✅ **Common Pitfalls** highlighted with solutions
✅ **Extensive Exercises** for hands-on learning

## 📚 Resources

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Dataclasses PEP 557](https://www.python.org/dev/peps/pep-0557/)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)
- [Real Python - OOP](https://realpython.com/python-oop/)

## 🔗 Related Repositories

- [Core-Python](https://github.com/Sswathii18/Core-Python) - Fundamentals

## 🎓 How to Use This Repository

1. **For Learning**: Start with Topic 1, read README, run examples
2. **For Reference**: Jump to specific topics as needed
3. **For Projects**: Pick a project and implement it
4. **For Teaching**: Use files and projects for classroom/training
5. **For Interview Prep**: Focus on concepts and sample projects

## 💡 Tips for Success

- Run every example and modify it
- Implement all exercises
- Build at least 3 of the 10 projects
- Use type hints in your code
- Write docstrings for all classes
- Test your code thoroughly
- Understand SOLID principles

---

**Happy Learning!** 🐍✨

Start with `01-classes-init-methods/README.md`
