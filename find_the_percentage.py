if __name__ == '__main__':
    nestlist=[]
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s=[name,score]
        nestlist.append(s)
    def Fn(s):
      return s[-1]
    nestlist =sorted(nestlist,key=Fn)
    s=[]
    sk=[]
    
    for n in nestlist:
        if n[1]==nestlist[0][1]:
            continue
        else:
            sk.append(n)
            
    for n in sk:
        if n[1]==sk[0][1]:
            s.append(n[0])
        else:
            break
            
    s=sorted(s)
    for sn in s:
     print(sn)