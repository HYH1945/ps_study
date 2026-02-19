def solution(info, n, m):
    # A가 다 뒤집어쓴 후, B가 본인이 갈 수 있는 내에서 A흔적을 최대로 줄인걸 계산
    #dp[j] = B가 j만큼 훔쳤을 때(누적 흔적이 j일때) 줄일 수 있는 A 흔적의 최댓값
    dp = [-1] * m
    dp[0] = 0
    total_a_trace = 0
    for item in info:
        total_a_trace += item[0]

    for trace_a, trace_b in info:
        for j in range(m-1, trace_b-1, -1):
            if dp[j-trace_b] != -1:
                dp[j] = max(dp[j], dp[j-trace_b] + trace_a)

    max_discount = max(dp)

    final_a_trace = total_a_trace - max_discount

    if max_discount != -1 and final_a_trace < n:
        return final_a_trace
    else:
        return -1
