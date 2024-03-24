def beauty(n):
    x=str(n)
    a=[i for i in x]
    for j in range(len(a)):
        if a[j-1]<a[j]:
            a[j-1],a[j]=a[j],a[j-1]
    return int(''.join(a))
if __name__=='__main__':
    n = int(input("enter any number: "))
    print(n)
    result=beauty(n)
    print(result)