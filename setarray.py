if __name__ == '__main__':
    List = []
    n = int(input())
    for i in range(n):
        work = input().split(' ')
        if work[0] == 'append':
            List.append(int(work[1]))
        elif work[0] == 'print':
            print(List)
        elif work[0] == 'insert':
            List.insert(int(work[1]), int(work[2]))
        elif work[0] == 'remove':
            List.remove(int(work[1]))
        elif work[0] == 'sort':
            List.sort()
        elif work[0] == 'pop':
            List.pop()
        elif work[0] == 'reverse':
            List.reverse()
            print(List)