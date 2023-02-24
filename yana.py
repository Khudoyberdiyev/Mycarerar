def myResult(a:list,b:list)->tuple:
    return a+b,a-b,a*b
numbers1=[6,5,3,9]
numbers2=[0,1,7,7]
Result=map(myResult,numbers1,numbers2)
print(list(tuple(Result)))