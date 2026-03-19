# 주어진 무작위 그래프 입력에서
# 루트 노드, 8자 그래프, 막대그래프, 도넛그래프 개수 찾는 문제
# -> 모든 노드의 indegree, outdegree를 저장해두고, 모든 노드 순회하면서 특징점 나타날때마다 그래프 한개 발견하면됨
# 특징 찾는게 핵심, 다른 그래프의 노드, 같은 그래프 안의 노드와 중복되지 않는 유일한 조건을 잘 찾아봐야함

# 루트노드 특징 : 들어오는 간선이 하나도 없고 나가는 간선이 2개 이상
# 8자 그래프의 핵심 좌표 : 중앙교차점 : 들어오는 간선이 최소 2개이상이고 나가는간선도 2개이상
# 막대그래프의 핵심 좌표 : 맨 끝점 : 나가는 간선이 없음
# 도넛그래프 : 죄다 똑같아서 특징이 없음 -> 8자그래프 막대그래프 개수 다 세어놨으면 루트노드의 간선 하나 하나는 하나의 그래프를 가리키므로
# 루트노드 outdegree - (8자그래프 개수 + 막대그래프 개수) = 도넛그래프 개수


def solution(edges):
    node_detail = {}

    for u, v in edges:
        if u not in node_detail: node_detail[u] = [0,0]
        if v not in node_detail: node_detail[v] = [0,0]
        node_detail[u][1] += 1
        node_detail[v][0] += 1

    answer = [0, 0, 0, 0]

    root_outdegree = 0

    for node, detail in node_detail.items():
        indegree = detail[0]
        outdegree = detail[1]

        if outdegree >= 2 and indegree == 0:
            answer[0] = node
            root_outdegree = outdegree
        elif outdegree == 0:
            answer[2] += 1
        elif outdegree == 2 and indegree >= 2:
            answer[3] += 1

        answer[1] = root_outdegree - answer[2] - answer[3]

    return answer