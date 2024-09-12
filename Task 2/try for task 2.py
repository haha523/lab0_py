with open("d:/Visual studio code/input.txt", "r") as input_file:
    a, b = map(int, input_file.read().split())
sum = a + b**2
with open("d:/Visual studio code/output.txt", "w") as output_file:
    output_file.write(str(sum)) 
