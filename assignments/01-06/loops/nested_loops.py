# Nested loops, also known as inner loops or nested iterations, refer to the process of placing one loop inside another loop. The inner loop will iterate through its entire cycle for each iteration of the outer loop. 


# example  code

# multiplication table 
for outer in range(1,10):
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 10):
        print(f"{outer} * {inner} = {outer * inner}")
    print()