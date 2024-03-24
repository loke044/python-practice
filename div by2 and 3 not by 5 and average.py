def average(array):
    sum = 0
    count=0
    for i in array:
        if i%2==0 and i%3==0 and i%5!=0:
            sum+=i
            count+=1
    print(sum)
    print(count)
    average=sum/count
    return average

if __name__=='__main__':
    array=[]
    array_count=int(input("arr_count: "))
    for i in range(array_count):
        array.append(int(input("enter values: ")))
    result=average(array)
    print(result)