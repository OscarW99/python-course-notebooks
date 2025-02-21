# Chapter 4: Functions and Libraries

#* 1. Power Calculation Function
def power(num, topwr):
    # Base case
    if topwr == 0:
        return 1
    # Recursive case
    else:
        return num * power(num, topwr - 1)
print(power(2, 3))
print(power(5, 0))
