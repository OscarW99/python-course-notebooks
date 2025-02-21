# Chapter 4: Functions and Libraries

#* 1. Working with Built-in Functions
sequence_list = list("AGTC")
print(type(sequence_list))
for element in sequence_list:
    print(element)

#* 2. Functions vs Methods
# Function call
print(type("atcg"))
# Method call
print("atcg".upper())

#* 3. Processing Loop with range()
for i in range(1, 4):
    print(f"Processing sequence {i} of 3")
