def minion_game(string):
    # your code goes here
    index=[]
    for i in range(len(string)):
        if string[i]=='A' or string[i]=='E' or string[i]=='O' or string[i]=='I' or string[i]=='U':
            index.append(1)
        else:
            index.append(0)
    stuart=0
    kevin=0
    
    for i in range(len(index)):
        if(index[i]==0):
            stuart=stuart+len(index)-i
            
    for i in range(len(index)):
        if(index[i]==1):
            kevin=kevin+len(index)-i
            
    if(stuart>kevin):
      print ("Stuart "+str(stuart))
    elif stuart<kevin:
      print ("Kevin "+str(kevin))
    else:
      print ("Draw")
       