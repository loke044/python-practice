A="THE CAT"
B=""
C=0
for j in range(len(A)):
    for i in range(C, len(A)):
        B = B + A[i]
        print(B)
    C += 1
    B=""
