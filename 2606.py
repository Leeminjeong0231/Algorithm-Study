import sys

#컴퓨터의 개수
n = int(sys.stdin.readline())
#컴퓨터 쌍의 수(간선수)
c = int(sys.stdin.readline())

#컴퓨터의 수 = 노드의 수. 1번부터 이므로 맨 첫 번째 칸 비워두기~
computer = [[] for _ in range (n + 1)]

#연결된 컴퓨터 쌍 만들기
for _ in range(c):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)

visited_com = [False] * (n+1)

#dfs써야겟다
def dfs(n):
    visited_com[n] = True
    for i in computer[n]:
        if not visited_com[i]:
            dfs(i)


dfs(1)
infect = sum(visited_com) - 1
print(infect)