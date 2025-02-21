# Chapter 11: Object-Orientated Programming

#* 1. Temperature Class with Dunder Methods
class Temperature:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()  # Ensure unit is uppercase for consistency

    def __str__(self):
        return f"{self.value}{self.unit}"

    def to_celsius(self):
        if self.unit == 'F':
            return (self.value - 32) * 5/9
        return self.value

    def to_fahrenheit(self):
        if self.unit == 'C':
            return (self.value * 9/5) + 32
        return self.value

    def __add__(self, other):
        if isinstance(other, Temperature):
            # Convert both to Celsius, add, then convert back to the original unit
            celsius_sum = self.to_celsius() + other.to_celsius()
            if self.unit == 'F':
                return Temperature(self.to_fahrenheit(), self.unit)
            return Temperature(celsius_sum, self.unit)
        raise TypeError("Can only add another Temperature object")

    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.to_celsius() == other.to_celsius()
        return False

# Example usage for Temperature class
temp_c = Temperature(25, 'C')
temp_f = Temperature(77, 'F')

print(f"Temperature in Celsius: {temp_c}")  # Demonstrates __str__
print(f"Temperature in Fahrenheit: {temp_f}")

# Addition of temperatures
sum_temp = temp_c + temp_f
print(f"Sum of temperatures in Celsius: {sum_temp}")  # Should be 50°C

# Equality check
print(f"Is 0°C equal to 32°F? {Temperature(0, 'C') == Temperature(32, 'F')}")  # True


#* 2. Genetic Marker Class with Dunder Methods
class GeneticMarker:
    def __init__(self, sequence, position):
        self.sequence = sequence
        self.position = position

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0 or key >= len(self.sequence):
                raise IndexError("Index out of range")
            return self.sequence[key]
        elif isinstance(key, slice):
            return self.sequence[key]
        raise TypeError("Invalid index type")

    def __eq__(self, other):
        if isinstance(other, GeneticMarker):
            return self.sequence == other.sequence and self.position == other.position
        return False

# Example usage for GeneticMarker class
marker1 = GeneticMarker("ATCG", 100)
marker2 = GeneticMarker("ATCG", 100)
marker3 = GeneticMarker("GCTA", 100)

# Length check
print(f"Length of marker1: {len(marker1)}")  # Demonstrates __len__

# Indexing
print(f"First base of marker1: {marker1[0]}")  # Demonstrates __getitem__
print(f"Slice of marker1: {marker1[1:3]}")

# Equality check
print(f"Is marker1 equal to marker2? {marker1 == marker2}")  # True
print(f"Is marker1 equal to marker3? {marker1 == marker3}")  # False

# Error handling for out of range index
try:
    print(marker1[4])  # Should raise IndexError
except IndexError as e:
    print(f"Index error: {e}")