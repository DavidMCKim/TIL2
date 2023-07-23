def solution(babbling):
    answer = 0
    for babble in babbling:
        cnt = 0
        word = ''
        for b in babble:
            word += b
            if word in ['aya','ye','woo','ma']:
                word = ''
                cnt += 1
        if len(word) == 0 and cnt > 0:
            answer += 1
    return answer

