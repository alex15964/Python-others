try:
    def rom_to_num(num):
        if num == 'I':
            return 1
        elif num == 'V':
            return 5
        elif num == 'X':
            return 10
        elif num == 'L':
            return 50
        elif num == 'C':
            return 100
        elif num == 'D':
            return 500
        elif num == 'M':
            return 1000

    def num_to_rom(s, rom):
        ta = {'t3' : ['M', 'MM', 'MMM'], 't2' : ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], 't1' : ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], 't0' : ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']}
        return ta['t' + str(s)][rom - 1]

    while True:
        x = input()
        if x == '#':
            break
        lst = x.split(' ')
        anslst = []
        for strs in lst:
            sum = 0
            stra = 0
            while stra < len(strs):
                if (len(strs) > stra + 1) and rom_to_num(strs[stra+1]) > rom_to_num(strs[stra]):
                    sum += (rom_to_num(strs[stra+1]) - rom_to_num(strs[stra]))
                    stra += 2
                else:
                    sum += rom_to_num(strs[stra])
                    stra += 1
            anslst.append(sum)
        ans = abs(anslst[0] - anslst[1])
        if ans == 0:
            print('ZERO')
        else:
            rom = ''
            while ans / 10 > 1:
                rom += num_to_rom(len(str(ans))-1, int(ans /( 10 ** (len(str(ans))-1))))
                ans = ans % 10 ** (len(str(ans))-1)
            if ans != 0:
                rom += num_to_rom(len(str(ans))-1, int(ans / (10 ** (len(str(ans))-1))))
            print(rom)

except EOFError:
    pass