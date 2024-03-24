a=11
b=2
print("before swapping:\na={}\nb={}".format(a,b))
a=a^b
b=a^b
a=b^a
print("after swapping:\na={}\nb={}".format(a,b))