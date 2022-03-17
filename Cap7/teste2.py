n = str(input()) 

def termos(n,c):
    n = list(n[::-1])
    m = []
    if c==1:
        for ma in n:
            m.append(int(ma))
        return m
    if c==0:
        for ma in n:
            m.append(int(ma)**b)
        return m

a = termos(n,1)
b = int((1+a.index(a[-1])))
d =list(termos(n,0))

'''
for x in range(len(a)):
print(a[x], end=f"^{b} + ")
'''


#print(d,'^',b,'=')
import math
ss = ""
for i in d:
    v = int(math.ceil(i**(1/len(d))))
    ss += str(v) + "^" + str(len(d)) + " + "
print(ss[:-3],"=")

if int(sum(d))==int(n):
    ss = ""
    for i in d:
        ss += str(i) + " + "
    ss = ss[:-3] + " = " + str(n)
    print (ss)
    print (f'{n} é um número de Armstrong de {b} ordem.')
else:
    ss = ""
    for i in d:
        ss += str(i) + " + "
    ss = ss[:-3] + " != " + str(n)
    print (ss)
    print (f'{n} não é um número de Armstrong de {b} ordem.')
