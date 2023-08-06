# def solution(dartResult):
#     answer = 0
#     pre_number = ''
#     now_number = ''
#     for i in dartResult:
#         if i.isnumeric():
#             now_number += i
#         elif i == 'S':
#             answer = int(now_number)**1
#             pre_number = now_number
#             now_number = ''
#         elif i == 'D':
#             answer = int(now_number)**2
#             pre_number = now_number
#             now_number = ''
#         elif i == 'T':
#             answer = int(now_number)**3
#             pre_number = now_number
#             now_number = ''
#         elif i == '*':
#             if pre_number != '':
#                 pre_number = int(pre_number) * 2
#                 now_number = int(now_number) * 2
#                 answer += pre_number
#                 answer += now_number
#             else:
#                 now_number = int(now_number) * 2
#                 answer += now_number
#         elif i == '#':
#             now_number = int(now_number) * -1
#             answer += now_number
#     return answer

def solution(dartResult):
    answer = 0
    number = ''
    score_list = []
    for i in dartResult:
        if i.isnumeric():
            number += i
        elif i == 'S':
            number = int(number)**1
            score_list.append(number)
            number = ''
        elif i == 'D':
            number = int(number)**2
            score_list.append(number)
            number = ''
        elif i == 'T':
            number = int(number)**3
            score_list.append(number)
            number = ''
        elif i == '*':
            if len(score_list) > 1:
                score_list[-2] = int(score_list[-2])*2
                score_list[-1] = int(score_list[-1])*2
            else:
                score_list[-1] = int(score_list[-1])*4
        elif i == '#':
            score_list[-1] = int(score_list[-1])*-1
    answer = sum(score_list)
    return answer

if __name__ == '__main__':
    dartResult = '1S2D*3T'
    temp = solution(dartResult)
    print(temp)