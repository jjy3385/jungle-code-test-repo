import sys

input = sys.stdin.readline
# 테스트케이스
T = int(input().rstrip())
for _ in range(T):
    # 지원자 수
    N = int(input().rstrip())

    # 후보자 성적 (서류등수,면접등수) -> 서류등수 기준 오름차순 정렬
    C = sorted(
        [tuple(map(int, input().rstrip().split())) for _ in range(N)],
        key=lambda x: x[0],
    )
    
    cnt = 0
    min_interview_score = C[0][1]
    for i in range(1, N):
        if C[i][1] > min_interview_score:
            # 탈락
            cnt += 1
        else:
            min_interview_score = C[i][1]

    print(N - cnt)
