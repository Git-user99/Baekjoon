

def searchRoute(n, x, y, test_cases, cache) :
    if x == n-1 and y == n-1:
        return 1
    elif x >= n or y >= n:
        return 0
    if (x, y) in cache:  # 이미 계산된 경로라면 반환
        return cache[(x, y)]

    cache[(x, y)] = searchRoute(n, x + test_cases[x][y], y, test_cases, cache) or searchRoute(n, x, y + test_cases[x][y], test_cases, cache)

    return cache[(x, y)]


C = int(input().strip())  # 테스트 케이스 개수
result = []


for i in range(C):
    n = int(input().strip())  # 격자의 크기
    cache = {}
    test_cases = [list(map(int, input().split())) for _ in range(n)]
    result.append("YES" if searchRoute(n, 0, 0, test_cases, cache) else "NO")


print("\n".join(result))  # 한 번에 출력