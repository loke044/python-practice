def sum(array):
    sum=0
    for i in array:
        sum+=i**2
    return sum

if __name__=='__main__':
    n=int(input("array_size: "))
    array=[]
    for i in range(n):
        array.append(int(input("enter values: ")))
    result=sum(array)
    print(result)