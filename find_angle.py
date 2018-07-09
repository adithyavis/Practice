if __name__=='__main__':
    a=int(input())
    b=int(input())
    x=math.sqrt(a*a+(a*a+b*b)/4-a*math.hypot(a,b)*a/math.hypot(a,b))
    d=(x*x+b*b-(a*a+b*b)/4)/2/x/b
    c=math.acos (d)
    e=360*c/2/math.pi
    f=int(360*c/2/math.pi)
    if e>=f+0.5:
        e=f+1
    else:
        e=f
    print(e,chr(176),sep='')