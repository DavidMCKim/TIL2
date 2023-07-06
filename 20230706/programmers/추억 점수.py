# 첫번째 풀이
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(name, yearning, photo):
    answer = []
    dict_score_per_name = {name[idx]:yearning[idx] for idx in range(len(name))}
    for x in photo:
        score = 0
        for y in x:
            try:
                score += dict_score_per_name[y]
            except:
                pass
        answer.append(score)

    return answer# 첫번째 풀이