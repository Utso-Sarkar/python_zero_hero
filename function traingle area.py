def traingle():
    import math
    a=10
    b=25
    c=10
    if (a+b)>c and(a+c)>b and (b+c)>a:
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("area :",area)
    else:
        print("traingle is not possible")
traingle()
