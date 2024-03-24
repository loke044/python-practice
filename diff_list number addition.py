def sum(array):
    sum=0
    for i in array:
        if i%2==0:
            sum+=(-1)*i
        else:
            sum+=i
    return sum

if __name__=='__main__':
    n=int(input("enter array size: "))
    array=[]
    for i in range(n):
        array.append(int(input("enter elements: ")))
    result=sum(array)
    print(result)