def qsort(A):
    qsort_r(A, 0, len(A))
    #print(f"A: {A}")

def qsort_r(A, begin, end):
    if (begin +1)>= end:
        return
    p = pivot(A, begin, end)
    #print(f"p: {p-begin}, pivoted:{A[begin:end]}")
    qsort_r(A, begin, p)
    qsort_r(A,p+1, end)
    
def pivot(A, begin, end):
    select_pivot(A, begin, end)
    #next smaller element
    n = begin+1
    p = A[begin]

    for i in range(begin+1, end):
        if  A[i] < p :
            swap(A, i, n)
            n +=1
    swap(A, begin, n-1)
    return n-1

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
# selects pivot element and sets pivot element at index begin
# there are several techniques choosing pivot element
# Todo: make this an option for the algorithm
# default pivot selection doesn't do anything
def select_pivot(A, begin, end):
    pass
