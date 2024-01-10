
array=[1,2,3,4,5]
size=len(array)
for i in range(0,2*size):
    value=array[i%size]
    print(value)