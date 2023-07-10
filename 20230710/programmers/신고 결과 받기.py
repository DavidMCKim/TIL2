def solution(id_list, report, k):
    answer = []

    dict_declaration = {id:0 for id in id_list}
    dict_reporter = {id:0 for id in id_list}


    for ids in report:
        dict_declaration[ids.split(' ')[0]] += 1
        dict_declaration[ids.split(' ')[1]] += 1

    for ids in report:
        if dict_declaration[ids.split(' ')[0]] >= k:
            dict_reporter[id_list[idx]] += 1
        if dict_declaration[ids.split(' ')[1]] >= k:
            dict_reporter[id_list[idx]] += 1

    answer = [item for item in dict_declaration.values()]
    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report  = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k       = 2
    result  = [2,1,1,0]

    # id_list = ["con", "ryan"]
    # report  = ["ryan con", "ryan con", "ryan con", "ryan con"]
    # k       = 3
    # result  = [0,0]       

    answer = solution(id_list, report, k)
    print(answer)