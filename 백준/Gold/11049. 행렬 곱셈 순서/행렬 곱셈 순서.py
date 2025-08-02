import sys

input = sys.stdin.readline

# 행렬의 개수
N = int(input().rstrip())
# 행렬의 크기r,c
M = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

# dp[2] = 5 * 3 * 2 = 30
# dp[2] 도 사실 의미는 없어보이지만 이 값을 dp[3]에서 사용하고 있음
# dp[3] => (AB)C => (5 * 3 * 2) => (5 , 2) 행렬이 생성됨 => 5 * 2 * 6 = 60 , 따라서 30 + 60 = 90
# dp[3] => A(BC) => A * (3 * 2 * 6) => 36 , A * (3 , 6) => 5 * 3 * 6 = 90, 따라서 36 + 90 = 126
# 둘의 min 값은 90

# dp[i][j] 를 i인덱스 행렬부터 j인덱스 행렬까지 곱할 때의 최소 연산수로 정의
# 이렇게 정의하면 우리가 구하는 답은 dp[0][N-1] 여기에 있게 됨

INF = 2**31
dp = [[INF] * N for _ in range(N)]


# 자기자신을 곱하는 최소 연산수는 0
for i in range(N):
    dp[i][i] = 0

# 가장 바깥쪽 반복문은 행렬구간의 길이를 늘려감
for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j], dp[i][k] + dp[k + 1][j] + (M[i][0] * M[k][1] * M[j][1])
            )
        # print(dp)


# print(matrix)

# for i in range(N):
#     for j in range(N):
#         print(dp[i][j], end=" ")
#     print()


print(dp[0][N - 1])
