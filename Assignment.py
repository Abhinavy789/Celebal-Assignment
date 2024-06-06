#Create lower triangular, upper triangular and pyramid containing the "*" character.

def lower_triangular(n):
    for i in range(1, n + 1):
        print('*' * i)

def upper_triangular(n):
    for i in range(n, 0, -1):
        print('*' * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Get user input for the value of n
n = int(input("Enter the value of n: "))

print("Lower Triangular Pattern:")
lower_triangular(n)
print("\nUpper Triangular Pattern:")
upper_triangular(n)
print("\nPyramid Pattern:")
pyramid(n)
