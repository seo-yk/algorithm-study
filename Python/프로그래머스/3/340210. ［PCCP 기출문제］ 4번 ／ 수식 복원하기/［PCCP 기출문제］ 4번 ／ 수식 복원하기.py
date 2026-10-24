from collections import defaultdict

def solution(expressions):
    
    elist = []
    find_num = []
    answer = []
    for i in range(len(expressions)):
        elist.append(expressions[i].split(' '))
    
    max_num = 0
    for i in range(len(elist)):
        for j in range(len(elist[i])):
            if elist[i][j].isdigit():
                for k in range(len(elist[i][j])):
                    max_num = max(max_num, int(elist[i][j][k]))
                    
    def calculate(num, k):
        result = 0
        for i in range(len(str(num))):
            result += int(num[i]) * (k ** (len(num)-(i+1)))
        return result
    
    for i in range(max_num + 1, 10):
        flag = True
        for e in elist:
            if e[-1] != 'X':
                if e[1] == '+':
                    if (calculate(e[0], i) + calculate(e[2], i)) != calculate(e[4], i):
                        flag = False
                        break
                else:
                    if (calculate(e[0], i) - calculate(e[2], i)) != calculate(e[4], i):
                        flag = False
                        break
                
        if flag:
            find_num.append(i)
            
    def convert_to_base(n, k):
        if n == 0:
            return '0'

        digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []

        while n > 0:
            remainder = n % k
            result.append(digits[remainder])
            n //= k 

        return ''.join(reversed(result))
      
    for e in elist:
        if e[-1] == 'X':
            arr = e[:]
            rs = set()
            for fn in find_num:
                e0, e1, e2, e3, e4 = arr
                if e1 == '+':
                    rs.add(convert_to_base(calculate(e0, fn) + calculate(e2, fn), fn))
                    print(f"덧셈 === fn: {fn}, rs: {rs}")
                else:
                    rs.add(convert_to_base(calculate(e0, fn) - calculate(e2, fn), fn))
                    print(f"뺄셈 === fn: {fn}, rs: {rs}")
            
            if len(rs) == 1:
                arr[-1] = str(list(rs)[0])
            else:
                arr[-1] = '?'
            answer.append(' '.join(arr))
                
    return answer