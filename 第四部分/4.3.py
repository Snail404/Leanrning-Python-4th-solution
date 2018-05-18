def adder(*A):
    res = A[0]
    for i in A[1:]:
        res += i
    print(res)
    print(type(res))

adder({'a':'s'},{'w':'e'})

#第一次我传入的是字符串，返回的类型也是字符串
#传入不同类型参数时，会报错，因为不同类型根本加不了
#传入字典的时候，会报错，因为不支持，报错消息上写着的，你自己可以实验一下
