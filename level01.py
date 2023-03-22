import itertools
import pandas as pd
import pprint
import numpy as np


test01_dumy01 = [".#...", "..#..", "...#."]
test01_dumy02 = ["..........", ".....#....",
                 "......##..", "...##.....", "....#....."]
test01_dumy03 = [".##...##.", "#..#.#..#", "#...#...#",
                 ".#.....#.", "..#...#..", "...#.#...", "....#...."]
test01_dumy04 = ["..", "#."]

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 32%
# 바탕화면 정리  https://school.programmers.co.kr/learn/courses/30/lessons/161990


def test01(wallpaper):
    answer = []
    wall = []
    for arr in (wallpaper):
        wall.append([arr[i:i+1] for i in range(0, len(arr), 1)])

    wall = np.array(wall)
    print(wall)
    rows, cols = np.where(wall == '#')
    wall[min(rows):max(rows)+1, min(cols):max(cols)+1] = '#'
    print(wall)

    rows, cols = np.where(wall == '#')
    print(rows, cols)
    tmp = int(min(rows)), int(min(cols)), int(max(rows)+1), int(max(cols)+1)
    answer.append(tmp)
    answer = list(itertools.chain(*answer))
    return answer


# print(test01(test01_dumy04))


test02_dumy01 = [8, 4, [2, 3, 6]]
test02_dumy02 = [5, 4, [1, 3]]
test02_dumy03 = [4, 1, [1, 2, 3, 4]]

# n은 벽의수 m은 룰러의 길이, section은 칠해야되는구역번호

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 32%
# 덧칠하기  https://school.programmers.co.kr/learn/courses/30/lessons/161989
def test02(n, m, section):
    answer = 0
    idx = 0
    for sec in section:
        if sec > idx:
            answer += 1
            idx = sec + m - 1
            print("현제 섹션 : ", sec)
            print("룰러의 길이 : ", m)
            print("현제 칠해진 섹션의 마지막 : ", (sec + m - 1))

    return answer
# 그리디 알고리즘
# 현제 색션에 룰러의 길이인 m 값을더하고 1을 빼면
# m값에 -1을 하는 이유는 현재 공간부터 칠해야 하기 때문.
# 마지막으로 칠해진 섹션의 인덱스값이 된다.
# 해당값보다 현제 섹션의 값이 크면 현제 섹션은 안 칠해진 공간으로 판단하고 룰러의 길이 -1 만큼 칠단다.

#print(test02(*test02_dumy01))



