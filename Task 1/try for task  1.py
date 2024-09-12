with open("d:/Visual studio code/input.txt", "r") as input_file:
    content = input_file.read().split()
    if len(content) < 2:
        raise ValueError("Input file must contain at least two integers.")
    a, b = map(int, content)

sum = a + b

with open("d:/Visual studio code/output.txt", "w") as output_file:
    output_file.write(str(sum))

