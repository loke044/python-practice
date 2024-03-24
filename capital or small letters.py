def find(s):
    small=0
    capital=0
    for i in s:
        if i.islower():
            small+=1
        if i.isupper():
            capital+=1
    if small<capital:
        return 1
    elif small>capital:
        return 2
    else:
        return 0

if __name__=='__main__':
    s="aaBBK"
    result=find(s)
    print(result)