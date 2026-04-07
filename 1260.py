'''문제:그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, -> sort() 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.'''

'''입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.'''

'''출력: 첫째 줄에 DFS를 수행한 결과를 , 그 다음줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을
순서대로 출력하면 된다'''

import sys
from collections import deque

#주어질 N,M,V를 쪼개서 정수로 만들고 변수에 할당하기
n, m, v = map(int, sys.stdin.readline().split())

#정점의 개수만큼 탐색해야하므로 n+1만큼 반복해야함
graph = [[] for _ in range(n + 1)]

# 누가 누구랑 연결됐는지 정보 받기_다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
#m번동안 계속 새로운 a,b를 받아서 graph에 넣어줌
for _ in range (m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  #양방향

#작은 번호부터 가기로 했으니까 '정렬'
for i in range(1, n+1): #0은 안쓰니까 1부터 n+1
    graph[i].sort()

#DFS 함수
def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)

#BFS 함수 
def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        v = q.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True


visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(v)
print()
bfs(v)