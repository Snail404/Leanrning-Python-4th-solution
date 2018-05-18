def f1(a,b): print(a,b)             #普通按顺序匹配，很常用 第二次调用关键词匹配，在有特别需求的配置环境时候经常使用
def f2(a,*b): print(a,b)            #收集参数，用于不知道使用者会使用多少个参数的情况中

def f3(a,**b): print(a,b)           #第一个参数正常匹配，第二第三属于字典被第三个参数收集起来，也是用于特殊场合

def f4(a,*b,**c): print(a,b,c)      #跟上面差不多，不过多了个收集元组的*，两者的区别是一个*，一个是两个*

def f5(a,b=2,c=3): print(a,b,c)     #只输入了一个参数，后面两个就按照默认参数，很简单，用于有些数据用即可以让使用者定制，又可以默认，可以一个函数的循环次数

def f6(a,b=2,*c): print(a,b,c)      #这个确实没想到，只输入了一个参数以后，C竟然产生了一个空列表，没有报错，确属预料之外
                                    #第二次调用属于了两个参数，由于第三个参数是属于收集型的参数，它自动的产生了一个元组，我想其意思跟上一个测试差不多



#最后两个问题，混合匹配这种事情已经重复过很多次，看写代码的人怎么利用，这种事情很主观，我也没写过几次代码，在此我也不好评论
#由于没啥经验，这里说不出它的适用情况，大概就是用在写着很复杂的函数上面吧
