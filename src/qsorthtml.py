
# numbers row, highlight current element
# highlight pivot element

# highlight position of next smallest element

def iter_row(A, ite):
    s = '<tr>\n'
    for i,a in enumerate(A):
        cl = '' if (i != ite) else 'iter'
        it = '' if (i != ite) else i
        s += f'<td class=\"{cl}" > {it} </td>\n'
    s+= '</tr>\n'
    return s

def num_row(A, p, n, ite = 0, swap = False):
    s = '<tr>\n'
    for i,a in enumerate(A):
        cl = ''
        if (i == p):
            cl = 'pivot'
        elif i< n:
            cl ='left'
        elif swap and (i == ite or i == n):
            cl = 'swap'

        s+= f'<td class="{cl}"> {a} </td>\n'
    s+= '</tr>\n'
    return s

def next_row(A, n):
    s = '<tr>\n'
    for i,a in enumerate(A):
        cl = '' if (i != n) else 'next'
        it = '' if (i != n) else i
        s += f'<td class=\"{cl}" > {it} </td>\n'
    s+= '</tr>\n'
    return s


#test

x = [1, 100, 20, 4 ,3, 2, 5, 5, 3]
def test():
    s = iter_row(x, 4)
    print(s)
    s = num_row(x, 0, 3)
    print(s)
    s = num_row(x, 0, 3,5, True)
    print(s)
    s =next_row(x, 5)
    print(s)




        
                     
        
