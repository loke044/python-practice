def remove(s):
    char=[]
    prev=None
    for i in s:
        if prev!=i:
            char.append(i)
            prev=i
    return ''.join(char)

if __name__=='__main__':
    # s=input("enter_string: ")
    s="aabcddef"
    result=remove(s)
    print(result)
