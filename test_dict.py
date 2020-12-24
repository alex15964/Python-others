dic = {'a':[], 'b':[]}
for i in range(2):
    for j in range(2):
        dic['a'].append(i)
        dic['b'].append(j)
dic.clear()
print(dic)