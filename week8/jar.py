class Jar:
    def __init__(self, capacity=12):
        # Check if the capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        
        self._capacity = capacity
        self._size = 0  # Number of cookies in the jar, initially 0

    def __str__(self):
        # Return a string with 🍪 repeated 'size' times
        return "🍪" * self._size

    def deposit(self, n):
        # Check if depositing n cookies would exceed capacity
        if self._size + n > self._capacity:
            raise ValueError("Depositing would exceed the jar's capacity.")
        
        self._size += n  # Add n cookies to the jar

    def withdraw(self, n):
        # Check if there are enough cookies to withdraw
        if self._size < n:
            raise ValueError("Not enough cookies to withdraw.")
        
        self._size -= n  # Remove n cookies from the jar

    @property
    def capacity(self):
        return self._capacity  # Return the jar's capacity

    @property
    def size(self):
        return self._size  # Return the number of cookies in the jar
