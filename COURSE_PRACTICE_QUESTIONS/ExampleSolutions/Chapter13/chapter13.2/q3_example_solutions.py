# Question 3 Example Solution
import sys

if len(sys.argv) < 2:
    sys.stderr.write("Error: Minimum gene length not provided.\n")
    sys.exit(1)
else:
    min_length = sys.argv[1]
    try:
        min_length = int(min_length)
        sys.stdout.write(f"Processing genes with minimum length: {min_length}\n")
    except ValueError:
        sys.stderr.write("Error: Provided minimum length is not an integer.\n")
        sys.exit(1)