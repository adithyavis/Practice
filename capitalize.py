# Complete the solve function below.
def solve(s):
    list=s.split(' ')
    for i in range(len(list)):
            list[i]=list[i].capitalize()
    s=" "
    s=s.join(list)
    return s