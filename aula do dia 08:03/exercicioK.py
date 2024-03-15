q = 1
g=0
while q <= 64:
    i=1 
    g=(2**q)-1
    s=0
    while i<=g:
        s+=i
        i+=1
    print("O somatório de {} grão(s) é {}".format(g, s))
    q+=1