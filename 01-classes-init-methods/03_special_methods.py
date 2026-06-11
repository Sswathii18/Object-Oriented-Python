"""
03_special_methods.py
Special Methods (Dunder Methods) in Python Classes
"""

print("=" * 70)
print("PYTHON SPECIAL METHODS (DUNDER METHODS)")
print("=" * 70)

# ============================================================================
# 1. __str__ AND __repr__
# ============================================================================
print("\n1. __str__ AND __repr__")
print("-" * 70)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(f"str(): {str(person)}")
print(f"repr(): {repr(person)}")
print(f"In print: {person}")

# ============================================================================
# 2. __len__ AND __getitem__
# ============================================================================
print("\n\n2. __len__ AND __getitem__")
print("-" * 70)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        """Return number of songs."""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Access song by index."""
        return self.songs[index]
    
    def __repr__(self):
        return f"Playlist('{self.name}', {len(self)} songs)"

playlist = Playlist("My Mix")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

print(f"Playlist: {playlist}")
print(f"Length: {len(playlist)}")
print(f"First song: {playlist[0]}")
print(f"Second song: {playlist[1]}")
print(f"Last song: {playlist[-1]}")

# ============================================================================
# 3. __add__ AND OPERATOR OVERLOADING
# ============================================================================
print("\n\n3. __add__ AND OPERATOR OVERLOADING")
print("-" * 70)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")

# ============================================================================
# 4. __eq__ AND COMPARISON OPERATORS
# ============================================================================
print("\n\n4. __eq__ AND COMPARISON OPERATORS")
print("-" * 70)

class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self, other):
        """Check equality."""
        if isinstance(other, Money):
            return self.amount == other.amount
        return self.amount == other
    
    def __lt__(self, other):
        """Less than."""
        if isinstance(other, Money):
            return self.amount < other.amount
        return self.amount < other
    
    def __le__(self, other):
        """Less than or equal."""
        if isinstance(other, Money):
            return self.amount <= other.amount
        return self.amount <= other
    
    def __gt__(self, other):
        """Greater than."""
        if isinstance(other, Money):
            return self.amount > other.amount
        return self.amount > other
    
    def __str__(self):
        return f"${self.amount}"

m1 = Money(100)
m2 = Money(100)
m3 = Money(50)

print(f"m1 ({m1}) == m2 ({m2}): {m1 == m2}")
print(f"m1 ({m1}) == m3 ({m3}): {m1 == m3}")
print(f"m1 ({m1}) > m3 ({m3}): {m1 > m3}")
print(f"m3 ({m3}) < m1 ({m1}): {m3 < m1}")

# ============================================================================
# 5. __bool__ AND TRUTHINESS
# ============================================================================
print("\n\n5. __bool__ AND TRUTHINESS")
print("-" * 70)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def __bool__(self):
        """Account is True if it has positive balance."""
        return self.balance > 0
    
    def __str__(self):
        return f"Account (${self.balance})"

acc1 = BankAccount(100)
acc2 = BankAccount(0)
acc3 = BankAccount(-50)

print(f"{acc1} is {bool(acc1)}")
print(f"{acc2} is {bool(acc2)}")
print(f"{acc3} is {bool(acc3)}")

if acc1:
    print("Account 1 has money")
if not acc2:
    print("Account 2 is empty or negative")

# ============================================================================
# 6. __call__ - MAKING OBJECTS CALLABLE
# ============================================================================
print("\n\n6. __call__ - MAKING OBJECTS CALLABLE")
print("-" * 70)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Make instance callable like a function."""
        return x * self.factor
    
    def __repr__(self):
        return f"Multiplier({self.factor})"

multiply_by_2 = Multiplier(2)
multiply_by_5 = Multiplier(5)

print(f"multiply_by_2(10): {multiply_by_2(10)}")
print(f"multiply_by_5(10): {multiply_by_5(10)}")

# ============================================================================
# 7. __contains__ - IN OPERATOR
# ============================================================================
print("\n\n7. __contains__ - IN OPERATOR")
print("-" * 70)

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add_member(self, member):
        self.members.append(member)
    
    def __contains__(self, member):
        """Check if member is in team."""
        return member in self.members
    
    def __str__(self):
        return f"Team '{self.name}' with {len(self.members)} members"

team = Team("Developers")
team.add_member("Alice")
team.add_member("Bob")
team.add_member("Charlie")

print(team)
print(f"'Alice' in team: {'Alice' in team}")
print(f"'Diana' in team: {'Diana' in team}")

# ============================================================================
# 8. __iter__ AND __next__ - ITERATION
# ============================================================================
print("\n\n8. __iter__ AND __next__ - ITERATION")
print("-" * 70)

class Range:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """Return iterator object."""
        return self
    
    def __next__(self):
        """Get next value."""
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

print("Custom range (1, 5):")
for num in Range(1, 5):
    print(f"  {num}")

# ============================================================================
# 9. __enter__ AND __exit__ - CONTEXT MANAGERS
# ============================================================================
print("\n\n9. __enter__ AND __exit__ - CONTEXT MANAGERS")
print("-" * 70)

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        """Called when entering with block."""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block."""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False

# Using context manager (file will auto-close)
print("Using FileHandler context manager:")
with FileHandler("test.txt") as f:
    f.write("Hello, World!")
    print("File written")

# ============================================================================
# 10. PRACTICAL EXAMPLE: COMPLETE CLASS
# ============================================================================
print("\n\n10. PRACTICAL EXAMPLE: COMPLETE CLASS")
print("-" * 70)

class Card:
    """A playing card with rank and suit."""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False
    
    def __hash__(self):
        return hash((self.rank, self.suit))

class Deck:
    """A deck of playing cards."""
    
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def __contains__(self, card):
        return card in self.cards
    
    def __str__(self):
        return f"Deck of {len(self)} cards"
    
    def __repr__(self):
        return f"Deck({len(self)} cards)"

deck = Deck()
print(f"Deck: {deck}")
print(f"Number of cards: {len(deck)}")
print(f"First card: {deck[0]}")
print(f"Last card: {deck[-1]}")

ace_of_hearts = Card('A', 'Hearts')
print(f"Is Ace of Hearts in deck? {ace_of_hearts in deck}")

print("\n" + "=" * 70)
print("END OF SPECIAL METHODS TUTORIAL")
print("=" * 70)
