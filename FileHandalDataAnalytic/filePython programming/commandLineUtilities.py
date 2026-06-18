import argparse

# Create parser
parse = argparse.ArgumentParser(description="Simple Calculator")

# Positional arguments
parse.add_argument("num1", type=int, help="First number")
parse.add_argument("num2", type=int, help="Second number")
parse.add_argument("operation", choices=['add', 'sub', 'mul', 'div'], help="Operation to perform")

# Parse arguments
args = parse.parse_args()

# Display all args (optional)
print(args)

# Calculator Logic
if args.operation == "add":
    print(f"Total answer is: {args.num1 + args.num2}")

elif args.operation == "sub":
    print(f"Total answer is: {args.num1 - args.num2}")

elif args.operation == "mul":
    print(f"Total answer is: {args.num1 * args.num2}")

elif args.operation == "div":
    if args.num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Total answer is: {args.num1 / args.num2}")
