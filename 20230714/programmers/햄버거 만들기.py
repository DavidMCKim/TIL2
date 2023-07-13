def solution(ingredient):
    answer = 0
    burger = []
    for item in ingredient:
        burger.append(item)
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4):
                burger.pop()
    return answer

if __name__ == '__main__':
    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    a = solution(ingredient)
    print(a)
    print()