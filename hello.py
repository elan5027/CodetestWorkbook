import itertools
import pandas as pd
import pprint

test1_dumy = ["ayaye", "ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
test3_dumy = [1, 3, 2, 4, 2, 1, 2, 3, 4, 5, 1, 2,
              3, 4, 4, 5, 3, 3, 2, 2, 3, 2, 2, 3, 4, 1]
test4_dumy = [[1, 4], [9, 2], [3, 8], [11, 6]]  # result 1
test4_dumy2 = [[3, 5], [4, 1], [2, 4], [5, 10]]
test5_dumy = [[0, 1], [2, 5], [3, 9]]
test5_dumy2 = [[-1, 1], [1, 3], [3, 9]]
test5_dumy3 = [[0, 5], [3, 9], [1, 10]]
test6_dumy = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
test6_dumy2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
test6_dumy3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [
    1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

test6_dumy4 = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]

# 프로그레머스 코테
# 파이썬3, 레벨0, 정답률 29%
# 옹알이 https://school.programmers.co.kr/learn/courses/30/lessons/120956


def test1(test):
    syllables = ["aya", "ye", "woo", "ma"]
    words = []
    answer = 0
    for length in range(1, 5):
        words.extend([''.join(x)
                     for x in itertools.permutations(syllables, length)])

    # answer = len(pd.Index(test).intersection(words))

    for s in test:
        if s in words:
            answer += 1
    return answer

# test1(test1_dumy)

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 85%
# 콜라츠 추측 https://school.programmers.co.kr/learn/courses/30/lessons/12943


def test2(num):
    answer = num
    cnt = 0
    while True:
        if answer == 1:
            break
        if answer % 2 == 0:
            answer = answer / 2
            cnt += 1

        elif answer == 1:
            break
        else:
            answer = answer * 3 + 1
            cnt += 1
        if answer == 1:
            break

    return cnt


# print(solution(1))

# 프로그레머스 코테
# 완전탐색 레벨1
# 모의고사 https://school.programmers.co.kr/learn/courses/30/lessons/42840
def test3(answers):
    answer = []
    player_1 = [1, 2, 3, 4, 5]
    player_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    player_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    rank = [0, 0, 0]
    for i, ans in enumerate(answers):
        if (player_1[i % len(player_1)] == ans):
            rank[0] += 1
        if (player_2[i % len(player_2)] == ans):
            rank[1] += 1
        if (player_3[i % len(player_3)] == ans):
            rank[2] += 1

    for i, rnk in enumerate(rank):
        if rnk == max(rank):
            answer.append(i+1)
    print(answer)
    return answer

# test_3 = test3(test3_dumy)


def test4(ans):
    arr = []
    for i in range(0, 3):
        for j in range(1+i, 4):
            x = ans[i][0]-ans[j][0]
            y = ans[i][1]-ans[j][1]
            arr.append(y/x)


print(test4(test4_dumy2))

# 프로그레머스 코테
# 파이썬3, 레벨0, 정답률 48%
# 평행 https://school.programmers.co.kr/learn/courses/30/lessons/120875


def test4_1(dots):
    arr = []
    for i in range(0, 3):
        for j in range(1+i, 4):
            x = dots[i][0]-dots[j][0]
            y = dots[i][1]-dots[j][1]
            arr.append(y/x)

    # test2 = set(arr)
    # if len(test2) == len(arr):
    #     answer = 0
    # else:
    #     answer = 1
    # return answer

# 테스트 케이스 12~17에러 발생.
# 원인 = 문제를 잘못 해석함
# 모든 케이스를 비교하고 그중에서 찾는 것으로 생각햇음 [ 6개의 케이스를 종류별로 대입비교 ]
# 6개의 케이스를 1:1 비교로 총 3가지만 비교하면 해결되는 문제. 해당 이유로 하단의 코드로 수정

    for i in range(0, 3):
        if arr[i] == arr[5-i]:
            answer = 1
            break
        else:
            answer = 0
    return answer

# print(test4(test4_dumy))

# 프로그레머스 코테
# 파이썬3, 레벨0, 정답률 54%
# 겹치는 선분의 길이   https://school.programmers.co.kr/learn/courses/30/lessons/120876


def test5(lines):
    answer = 0
    tmp = []
    for i in lines:
        for j in range(i[1]-i[0]):
            tmp.append(i[0]+j)
    answer = len([x for x in set(tmp) if tmp.count(x) >= 2])
    # 결과값에 answer 안에 속해있는 2개이상 중복된 값의 갯수 찾기
    return answer

# 선분 3개 평행 3개의 시작과 끝좌표
# [[start, end], [start, end], [start, end]]

# 2개 이상의 선분이 겹치는 부분의 길이를 반환.

# 겹치는 부분을 판단 해야함. start 시작부  제일 큰놈


# print(test5(test5_dumy))


# 프로그레머스 코테
# 파이썬3, 레벨0, 정답률 55%
# 안전지대  https://school.programmers.co.kr/learn/courses/30/lessons/120866
def test6(board):
    answer = 0
    bomb = []

    # 보드 공간 좌우 1칸씩 총 2칸 늘린 공간 만들기
    boardplus = [[""]*(len(board)+2) for i in range(len(board)+2)]

    for column in range(len(boardplus)):  # 세로값
        for row in range(len(boardplus)):  # 가로값
            if 1 <= column <= len(board) and 1 <= row <= len(board):
                boardplus[column][row] = board[column-1][row-1]
            else:
                boardplus[column][row] = 2

            if boardplus[column][row] == 1:
                bomb.append([column, row])
    # 기존에 값 복사 붙여넣기하고 추가된 구역은 2로 채워넣기.
    # 붙여넣은 값중에 진짜 폭탄이 있던 1의 위치를 x에 기억시키기.
    bomblen = (len(bomb))  # 폭탄의 갯수저장.
    for column in range(len(boardplus)):
        for row in range(len(boardplus)):
            if 1 <= column <= len(board) and 1 <= row <= len(board):
                for i in range(0, bomblen):
                    if bomb[i] == [column, row]:
                        for num in range(-1, 2):
                            boardplus[column+num][row+num] = 1
                            boardplus[column+num][row] = 1
                            boardplus[column][row+num] = 1
                            boardplus[column-num][row+num] = 1
            else:
                boardplus[column][row] = 2
    for i in boardplus:
        for j in range(0, len(boardplus)):
            if i[j] == 0:
                answer += 1
    return answer

# 폭탄이 위치한 상하좌우대각 모두 위험지역으로 분류
# 지뢰는 2차원배열 board에 1로 표시
# board 에는 지뢰1을 제외하면 0만으로 구성
# 지뢰가 매설된 지도가 매개변수로 주어질때 안전한 지억의 칸수를 반환.


# print(test6(test6_dumy2))
