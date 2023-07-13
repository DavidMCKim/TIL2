def solution(s):
    answer = 0    
    cnt1 = 0 
    cnt2 = 0
    str = ""
    for i in s:
        if cnt1 == cnt2:
            cnt1 +=1
            x = i
            answer +=1
        elif i == x:
            cnt1 +=1
        else:
            cnt2 +=1
    return answer

if __name__ == '__main__':
    s = 'aaabbaccccabba'
    print(solution(s))