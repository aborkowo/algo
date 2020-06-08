
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
        elif ((swap==True) and (i == ite or i == n)):
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


def pivot(A, begin, end):
    #select_pivot(A, begin, end)
    #next smaller element
    n = begin+1
    p = A[begin]
    s=''
    
    for i in range(begin+1, end):
        s+=f"<p>iteration: {i} </p>"
        s+="<table>\n"
        s+= iter_row(A[begin:end], i)
        if  A[i] < p :
            s+=num_row(A[begin:end],0, n, i, True)
            swap(A, i, n)
            n +=1
            s+=num_row(A[begin:end],0, n, i, False)
        else:
            s+=num_row(A[begin:end],0, n, i, False)
        s+=next_row(A[begin:end], n-begin)
        s+="</table>\n"

    s+=f"<p>finally </p>"
    s+="<table>\n"
    s+=iter_row(A[begin:end], i-begin)
    s+=num_row(A[begin:end],0, n-1, begin, True)
    swap(A, begin, n-1)
    s+=num_row(A[begin:end],n-1, n-1, begin, False)
    s+=next_row(A[begin:end], n-begin)
    s+="</table>\n"
    return n-1,s

html_header = ""
html_footer = ""

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
#test

header = """<!DOCTYPE html>
<html>
<head>
<style>
table {
 /* border: 2px solid black;
  margin-left: 10px;
  */
}
tr, {
  /* border: 1px solid black;*/
  text-align: left;
  padding: 8px;
  /*background-color: #2196F3;*/
}

td {
  /*background-color: #2196F3;*/
}

th, td {
  /* border: 1px solid black; */
  width: 50px

}
.pivot {
	background-color: lightblue;
}

.iter {
	background-color: orange;

}

.next {
	background-color: grey;

}

.swap {
	background-color: yellow;

}

.left {
	background-color: blue;

}
.clear {
	background-color: white;
}

</style>
</head>
<body>
<table>
"""

footer = """
</table>

</body>
</html>

"""

x = [11, 100, 20, 4 ,3, 2, 5, 5, 3, 15, 6 ]
def test():
#    s = iter_row(x, 4)
#    print(s)
#    s = num_row(x, 0, 3)
#    print(s)
#    s = num_row(x, 0, 3,5, True)
#    print(s)
#    s =next_row(x, 5)
#    print(s)
    s1 = header
    _, s = pivot(x, 0, len(x))
    s1 +=s
    s1+=footer
    
    print(s1)
    with open("pivot.html", "w") as f:
        f.write(s1)



        
                     
        
