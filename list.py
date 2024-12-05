def match (w) :
    l=[]
    count=0
    for x in w:
        if x[0]== x[-1]:
            count=count+1
            l.append(x)
    print(count)
    print(l)
    

match([1231,"kaushik","codingal"])