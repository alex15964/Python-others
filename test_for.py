ans = 1998
while ans / 10 > 1:
    print(len(str(ans))-1, int(ans / 10 ** (len(str(ans))-1)))
    ans = ans % 10 ** (len(str(ans))-1)
print(len(str(ans))-1, int(ans / 10 ** (len(str(ans))-1)))