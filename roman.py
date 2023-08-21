def addTwoNumbers(l1, l2):
    i=0
    j=0
    x=0
    y=0
    l1.reverse()
    l2.reverse()
    while i < len(l1):
        x = x + (10**i * l1[i])
        i = i + 1

    while j < len(l2):
        y= y + (10**j * l2[j])
        j= j + 1

    z=x+y
    z= list(map(int, str(z)))
    z.reverse()
    return z
    



l1=[2,4,3]
l2=[5,6,4]
print(addTwoNumbers(l1,l2))