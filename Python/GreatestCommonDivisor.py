n = int(input())
numbers = input().split(' ')

answer = 1
for i in range(0, n):
    p = int(numbers[i])
    q = answer
    
    if i == 0:
        answer = p
        continue

    if p > q:
        p, q = q, p
        

    while q % p != 0:
        q = q % p
        p, q = q, p

    answer = p

print(answer)


