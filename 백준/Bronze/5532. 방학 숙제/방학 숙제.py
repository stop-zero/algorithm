L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

Days= L - max((A+C-1)//C, (B+D-1)//D)

print(Days)