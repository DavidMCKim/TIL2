# # 첫번째 풀이
# # >> 테스트 9~13 시간초과로 실패
# # 채점 결과
# # 정확성: 68.8
# # 합계: 68.8 / 100.0
# def solution(players, callings):
#     answer = []

#     for player in callings:
#         rank = players.index(player)
#         temp = players[rank-1]
#         players[rank-1] = players[rank]
#         players[rank] = temp

#     answer = players

#     return answer

# if __name__ == '__main__':
#     players  = ["mumu", "soe", "poe", "kai", "mine"]
#     callings = ["kai", "kai", "mine", "mine"]
#     answer = solution(players, callings)
#     print(answer)

# 두번째 풀이
# 첫번째 풀이 때,
# 리스트로만 풀어야한다는 생각에 dictionary 형태를 사용하지 않았었다.
def solution(players, callings):
    answer = []
    dict_players = {player:rank for rank,player in enumerate(players)}
    dict_rank = {rank:player for rank,player in enumerate(players)}
    for caller in callings:
        rank = dict_players[caller]
        dict_players[dict_rank[rank-1]], dict_players[dict_rank[rank]] = dict_players[dict_rank[rank]], dict_players[dict_rank[rank-1]]
        dict_rank[rank-1], dict_rank[rank] = dict_rank[rank], dict_rank[rank-1]
    
    answer = [player for player in dict_rank.values()]
    return answer

if __name__ == '__main__':
    players  = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    answer = solution(players, callings)
    print(answer)