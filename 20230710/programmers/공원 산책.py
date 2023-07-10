# 첫번째 풀이
def solution(park, routes):
    answer = []
    lat, lon = 0, 0
    
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y].upper == 'S':
                lat = x
                lon = y
                break
        
        for route in routes:
            x = lat
            y = lon

            rocation, count = route.split(' ')
            for round in range(int(count)):
                if rocation == 'N' and y != 0 and park[y-1][x] != 'X':
                    y -= 1
                    if round == int(count)-1:
                        y = y
                elif rocation == 'S' and y != len(park)-1 and park[y+1][x] != 'X':
                    y += 1
                    if round == int(count)-1:
                        y = y
                elif rocation == 'W' and x != 0 and park[y][x-1] != 'X':                        
                    x -= 1
                    if round == int(count)-1:
                        x = x                                          
                elif rocation == 'E' and x != len(park[0])-1 and park[y][x+1] != 'X':
                    x += 1
                    if round == int(count)-1:
                        x = x
    answer.append(y)
    answer.append(x)
    return answer

if __name__ == '__main__':
    park   = ["SOO","OOO","OOO"]
    routes = ["E 2","S 2","W 1"]
    result = [2,1]

    # park   : ["SOO","OXX","OOO"]
    # routes : ["E 2","S 2","W 1"]	
    # result : [0,1]

    # park   : ["OSO","OOO","OXO","OOO"]
    # routes : ["E 2","S 3","W 1"]	
    # result : [0,0]    
    answer = solution(park, routes)
    print(answer)