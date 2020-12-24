def compare_2_list(lst1, lst2): #互相比較lis內部的值，沒有的加進去
    for i in lst2:
        if i not in lst1:
            lst1.append(i)

    for i in lst1:
        if i not in lst2:
            lst2.append(i)
            
    lst2.sort() #排序list
    return lst2

lst1 = [1,2,3,4,5]
lst2 = [1,2,3]
print('原本list 1:', lst1)
print('原本list 2:', lst2)
lst1 = lst2 = compare_2_list(lst1, lst2)
print('合併後list 1:', lst1)
print('合併後list 2:', lst2)

lst1 = [1,2,3]
lst2 = [3,4,5]
print('原本list 1:', lst1)
print('原本list 2:', lst2)
lst1 = lst2 = compare_2_list(lst1, lst2)
print('合併後list 1:', lst1)
print('合併後list 2:', lst2)

lst1 = []
lst2 = [1,2,3]
print('原本list 1:', lst1)
print('原本list 2:', lst2)
lst1 = lst2 = compare_2_list(lst1, lst2)
print('合併後list 1:', lst1)
print('合併後list 2:', lst2)

lst1 = [4,5,6]
lst2 = []
print('原本list 1:', lst1)
print('原本list 2:', lst2)
lst1 = lst2 = compare_2_list(lst1, lst2)
print('合併後list 1:', lst1)
print('合併後list 2:', lst2)
