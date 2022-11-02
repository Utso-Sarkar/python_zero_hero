for i in range(10000):
    a=int(input("\npress 1 for sub:\n press 2 for add \n press 3 for div\npress 4 for gun\npress 5 for modulus\npress 6 for gor\npress 7 for Rectangle area count\n press 7 for :\npress 8 for calender\n\n\n Enter your choice ="))
    
    if a == 1:
        b=int(input())
        c=int(input())
        d=b-c
        print(d)

    elif a == 2:
        e=int(input())
        f=int(input())
        g=e+f
        print(g)
    elif a == 3:
        h=int(input())
        i=int(input())
        j=h/i
        print(j)
    elif a == 4:
        k=int(input())
        l=int(input())
        m=k*l
        print(m)
    elif a == 5:
        n=int(input())
        o=int(input())
        p=n%o
        print(p)
    elif a == 6:
        q=int(input())
        r=int(input())
        s=(q+r)/2
        print(s)
    
    elif a == 4:
        t=int(input())
        u=int(input())
        v=t*u
        print(v) 
    elif a == 7:
        w=int(input())
        x=int(input())
        y=3.1416*w*x
        print(y)
    elif a == 8:
        import calendar
        ki=int(input())
        li=int(input())
        #month=int(input())
        mo=calendar.month(ki,li)
        print(mo)
   

    else:
        a<7
        print("Hihi kam hobe na !")
    





