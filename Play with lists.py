L = [4,5,1,2,9,7,10,8]
print("oringinal List :",L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum =",count)
print("average = ", avg)
L.sort()

print("Smallest element is:", L[0])
print("Largest elememt is:", L[-1])

print("Maximun value is:",max(L))
print("Minimum value is:",min(L))