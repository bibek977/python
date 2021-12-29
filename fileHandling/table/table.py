for i in range(2,8):
    with open(f"fileHandling/table/Multiplication_of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")

            if j!=10:
                f.write("\n")