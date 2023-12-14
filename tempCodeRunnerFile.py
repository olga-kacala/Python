start = 1
end = 100

def perfectNum(start, end):
    list = []

    for i in range(1, n):
        if n%i ==0:
            sum +=i
            if sum == i:
                list.append(i)
    return list

print(perfectNum(start, end))