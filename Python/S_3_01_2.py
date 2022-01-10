#入力
n = int(input())

answer = []
#√nまで調べる
limit = int(n ** 0.5)
for i in range(2, limit + 1):
    #各数で割れなくなるまで割る
    while n % i == 0:
        n /= i
        answer.append(i)

if n >= 2:
    answer.append(int(n))

print(*answer)
