while True:
    g1 = float(input("Enter Grade1: "))
    g2 = float(input("Enter Grade2: "))
    g3 = float(input("Enter Grade3: "))
    g4 = float(input("Enter Grade4: "))
    g5 = float(input("Enter Grade5: "))
    T = [g1,g2,g3,g4,g5]
    print(f"Calculating Grades Statistics: '\033[34m{T}\033[0m'")
    print("\n")
    invalid = []
    min = 100
    max = 0
    avg = (g1+g2+g3+g4+g5)/5
    for grade in T:
        if grade < 0:
            invalid.append(grade)
        if grade < min:
            min = grade
        if grade > max:
            max = grade
    if len(invalid) == 0:
        print(f"Average: '\033[34m{avg}\033[0m'\nMaximum: '\033[34m{max}\033[0m'\nMinimum: '\033[34m{min}\033[0m'\n\n")
    else:
        print(f"Invalid Grades: '\033[31m{invalid}\033[0m'\n\n")