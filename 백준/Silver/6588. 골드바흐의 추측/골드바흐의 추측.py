# 에라테스토스트의 체 활용
# 1000000까지의 소수 여부 모두 구하고,
# 무한루프로 0이 들어오기 전의 값들에 대해 판별

import sys
input = sys.stdin.readline

n = 1000001
# 소수 아닌 모든 홀수 처리
table = [1] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if table[i]:
        for j in range(i * 2, n, i):
            table[j] = 0
# k가 만들어지는 두 홀수인 소수 검색
while 1:
    k = int(input())
    if not k:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if table[i] and table[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")