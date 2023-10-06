def max_subarray_average(n,k):
    '''You are given an integer array nums consisting of n elements, and an integer k.

        Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
        Any answer with a calculation error less than 10-5 will be accepted.'''


    msum=float('-inf')
    csum=0
    if len(n)==1:
        return float(n[0])
    elif len(n)==0:
        return 0

    for i in range(k):
        csum+=n[i]
    for i in range(k,len(n)):
        csum=csum-n[i-k] + n[i]
        msum=max(csum,msum)
    return msum/k
print(max_subarray_average( [5], 1))

