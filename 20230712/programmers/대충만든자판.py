def solution(keymap, targets):
    keyCnt = {}
    for keys in keymap:
        for index, key in enumerate(keys):
            if key not in keyCnt:
                keyCnt[key] = index+1
            else:
                keyCnt[key] = min(keyCnt[key], index+1)

    answer = []
    for target in targets:
        Cnt = 0
        for t in target:
            if t not in keyCnt:
                Cnt = -1
                break
            Cnt += keyCnt[t]
        answer.append(Cnt)

    return answer

if __name__ == '__main__':
    keymap = ["ABACD", "BCEFD"]	
    targets = 	["ABCD","AABB"]	
    result = solution(keymap, targets)
    print()
