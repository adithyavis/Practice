if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=sorted(arr,reverse=True)
    for num in arr:
        if num==arr[0]:
            continue
        else:
            print(num)
            break
            