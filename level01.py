import re
import itertools
import pandas as pd
import pprint
import numpy as np
import math

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


# print(test02(*test02_dumy01))
test03_dumy01_key = ["ABACD", "BCEFD"]
test03_dumy01_tag = ["ABCD", "AABB"]
test03_dumy02_key = ["AA"]
test03_dumy02_tag = ["B"]
test03_dumy03_ket = ["AGZ", "BSSS"]
test03_dumy03_tag = ["ASA", "BGZ"]


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 대충만든자판  https://school.programmers.co.kr/learn/courses/30/lessons/160586
def test03(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for tar in target:
            min_index = [x.find(tar)+1 for x in keymap if x.find(tar)+1 != 0]
            # 찾아라 keymap에서 target의 1번째부터 돌려가면서 단, 누르는 행위는 0번이아닌 1번부터 표기되기 때문에 1을 더해준다.
            # 같은 문자가 찾아지면 몇번째인지 판단하여 반환해 준다 행이 여러개인경우 [x, y, z] 의 형식으로 받는다.
            if not min_index:  # 받아온 값이 없을경우 즉, 내용이 없는 경우 -1을 대입한다.
                count = -1
                break  # 1개라도 이미 없는것을 확인 햇기때문에 종료한다 이후의 문자가 존재하면 다른 문자가 삽입되기 때문
                # 문제에서 완성할수 없는 문자라면 -1값을 요청햇다.
            else:
                # min_index에 값이 들어가 있다면 안의 숫자중 가장 작은값을 count함수에 더해준다.
                count += min(min_index)
        # targets의 n번쨰 색인이 끝나는 지점이며 이때, answer에 n번째에 count의 값이 들어간다.
        answer.append(count)
        # 만약 없는 값이 1개라도 있었다면 -1이 들어가고 answer를 리턴한다.
    return answer


# print(test03(test03_dumy01_key, test03_dumy01_tag))


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 짝수와 홀수  https://school.programmers.co.kr/learn/courses/30/lessons/12937
tset03_dumy01 = 3
tset03_dumy02 = 4


def test04(num):
    answer = ''
    answer = 'Even' if num % 2 == 0 else 'Odd'
    return answer


# test04(tset03_dumy01)


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 약수의 합  https://school.programmers.co.kr/learn/courses/30/lessons/12928

def test05(n):
    answer = 0
    for x in range(1, n+1):
        if n % x == 0:
            answer += x
    return answer


# print(test05(12))


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 자릿수 더하기  https://school.programmers.co.kr/learn/courses/30/lessons/12931

def test06(n):
    answer = 0
    arr = str(n)
    print(arr)
    for ar in arr:
        answer += int(ar)

    return answer

# test06(987)

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 자릿수 더하기  https://school.programmers.co.kr/learn/courses/30/lessons/12944


def test07(arr):
    answer = 0
    count = 0
    for ar in arr:
        count += ar
    answer = (count/len(arr))
    return answer


# test07([1, 2, 3, 4])

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# x만큼 간격이 있는 n개의 숫자 https://school.programmers.co.kr/learn/courses/30/lessons/12954

def test08(x, n):
    answer = []
    for xn in range(1, n+1):
        answer.append((x*xn))

    return answer

# test08(2, 5)

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 자연수 뒤집어 배열로 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/12932


def test09(n):
    tmp = str(n)
    answer = []
    for t in tmp:
        answer.insert(0, int(t))
    return answer


# test09(12345)


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 정수 제곱근 판별  https://school.programmers.co.kr/learn/courses/30/lessons/12934
# math.sqrt 를 사용안하고 알고리즘을 해결보자는 취지에서 구현.

def test10(n):
    answer = n ** 0.5
    if int(answer) % (answer):
        return -1
    return (answer+1) ** 2


def test10_1(n):
    value = str(math.sqrt(n))
    check = len(value[value.find(".")+1:])
    if (check == 1):
        return pow(int(math.sqrt(n))+1, 2)
    else:
        return -1


# print(test10_1(121))
# print(test10(121))


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 문자열 내 p와 y의 개수  https://school.programmers.co.kr/learn/courses/30/lessons/12916

def test10(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 나머지가 1이 되는 수 찾기  https://school.programmers.co.kr/learn/courses/30/lessons/87389

def test11(n):
    answer = 0
    for x in range(1, n+1):
        if n % x == 1:
            answer = x
            break
    print(answer)
    return answer

# test11(11)


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 정수 내림차순으로 배치하기  https://school.programmers.co.kr/learn/courses/30/lessons/12933

def test12(n):

    # answer = 0
    # arr = sorted(str(n), reverse=True)
    # arr.sort(reverse=True)
    # for ar in arr:
    #     answer = (answer+ar)*10
    # answer /= 10
    answer = int("".join(sorted(str(n), reverse=True)))
    return answer


# test12(118372)


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 문자열을 정수로 바꾸기  https://school.programmers.co.kr/learn/courses/30/lessons/12925
def test13(s):
    return int("".join(s))


# test13("-1234")

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# 없는 숫자 더하기  https://school.programmers.co.kr/learn/courses/30/lessons/86051

def test14(numbers):
    answer = 0
    temp = []
    isval = True
    for num in numbers:
        temp.append(num)
    temp.sort()
    for i in range(0, 10):
        for j in temp:
            if i == j:
                isval = False
                break
            else:
                isval = True
        if isval:
            answer += i
    return answer


def test14_1(x): return sum(range(10)) - sum(x)
# 1~10까지 더한값에서 들어온 x의 값들의 합을 빼면 없는 값의 합만큼이 남는다.

# print(test14_1([5, 8, 4, 0, 6, 7, 9]))


# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def test15(s):
    number_list = ['zero', 'one', 'two', 'three',
                   'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, 10):
        s = re.sub(number_list[i], str(i), s)

    number_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                   'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for key, value in number_dict.items():
        s = s.replace(key, value)

    answer = int(s)
    return answer


test15_dumy01 = "one4seveneight"
test15_dumy02 = "23four5six7"
test15_dumy03 = "2three45sixseven"
test15_dumy04 = "123"

# test15(test15_dumy01)

# 프로그레머스 코테
# 파이썬3, 레벨1, 정답률 %


def test16(numbers):
    answer = []
    for n, i in enumerate(numbers):
        for m, j in enumerate(numbers):
            if n != m:
                answer.append(i+j)

    answer = [*set(answer)]
    print(answer)
    answer = sorted(answer)
    print(answer)
    return sorted(answer)


# test16([77, 88, 55, 2, 1, 33, 3, 4, 1])

def test17(lottos, win_nums):
    count = 0
    for num in win_nums:
        if num in lottos:
            count += 1
    rank = {'6': 1, '5': 2, '4': 3, '3': 4, '2': 5, '0': 6, '1': 6}
    min_lotto = str(count)
    max_lotto = str(count+lottos.count(0))
    for key, value in rank.items():
        if max_lotto == key:
            max_lotto = value

        if min_lotto == key:
            min_lotto = value

    return [max_lotto, min_lotto]

#    rank2 = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 0: 6, 1: 6}
#    test1 = [rank2[len(set(lottos) & set(win_nums)) + lottos.count(0)],
#             rank2[len(set(lottos) & set(win_nums))]]


test17_dumy01 = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
test17_dumy02 = [0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]
test17_dumy03 = [45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]
# test17(*test17_dumy01)

# [카카오 인턴] 키패드 누르기 https://school.programmers.co.kr/learn/courses/30/lessons/67256


def test18(numbers, hand):
    phon = {1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2),
            '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    answer = ""
    curr_left = '*'
    curr_right = '#'
    current = 0
    for num in numbers:
        if num in left:
            curr_left = num
            answer += "L"
        elif num in right:
            curr_right = num
            answer += "R"
        else:
            current = phon[num]
            l_hand = phon[curr_left]
            r_hand = phon[curr_right]
            l_value = abs(l_hand[0]-current[0]) + abs(l_hand[1]-current[1])
            r_value = abs(r_hand[0]-current[0]) + abs(r_hand[1]-current[1])

            if l_value > r_value:
                answer += "R"
                curr_right = num
            elif l_value == r_value:
                if hand == "left":
                    answer += "L"
                    curr_left = num
                else:
                    answer += "R"
                    curr_right = num
            else:
                answer += "L"
                curr_left = num
    return answer

# 1,4,7, 입력 왼손
# 3,6,9 입력 오른손
# 2,5,8,0 입력은 현재키패드에서 가까운곳 = 즉 움직인위치 현위치를 기억해야한다.
# 거리가 같다면 입력된 Hand의 방향이 우선.


test18_dumy01 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
test18_dumy02 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"
test18_dumy03 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"

# test18(*test18_dumy02)


# 3진법 뒤집기 https://school.programmers.co.kr/learn/courses/30/lessons/68935
def test19(n):
    answer = ''
    while n > 0:
        # n, mod = divmod(n, 3)
        # answer += str(mod)
        answer += str(n % 3)
        n = n // 3
    print(1 % 3)
    print(answer)
    return int(answer, 3)
# 자연수 n에 대하여 3진법상에서 앞뒤로 뒤집은후 10진법으로 바꾼후 리턴.
# 3진법은 0,1,2로 이루어진다. 즉 만약 45라면 3에 제곱근만큼 가능한한 빼준다. 즉 3^3 27을 빼면 45-27 18 더이상 못빼니 3^2 = 9 18-9= 9 한번더 되니 3^2 = 9- = 0 해당 값은 1200 이된다.
# 진법 번환 이론 : 값에 N을 나누어주고 나머지값을 남긴다 Ex) 45를 3진법으로  45/3 몫 15 나머지 0  15/3 몫 5 나머지 0  5/3 몫 1 나머지 2 == 값 1 나머지 2 이전의 나머지 0, 0 45의 3진법은 1200
# 파이썬에서 몫을 구할때는 // 나머지를 구할떄는 % 사용.
# 식에따라 나머지값을 문자로 더해준다. 1을 3으로 나누면 나머지는 1이 되기때문에 자연스럽게 마지막 1,2는 나머지값으로 들어간다.

# 0000 0
# 0010 3
# 0100 9
# 1000 27

# test19(45)


def test20(sizes):

    # 1번 가장먼저 떠올린 방법
    answer = 0
    rows = [0, 0]
    for size in sizes:
        size = sorted(size)
        for i in range(0, 2):
            rows[i] = max(rows[i], size[i])
    answer = rows[0]*rows[1]

    # 2번 먼저 떠올린 방법에서 sizes 에 x,y 값이 있다는것을 깨닳고 변경한것.
    width = 0
    hight = 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        width = max(width, w)
        hight = max(hight, h)

    # 3번 위 2개 방법을 구현후 다른사람이  작성한 코드 중 가장 인상깊었던 것.
    row = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    print(row, row2)
    # 1. 내부의 값 W, H 중 큰값 중에 가장 큰값을 구한다.
    # 2. 내부의 값 W, H 중 작은값 중에 가장 큰값을 구한다.
    # 그 둘을 곱하여 준다. 무지막지하게 신박햇다.
    return answer
#
# 입력값은 [가로,세로] 의 형태를 지닌다.
# 최소값을 구해야된다 명함의 가로 세로를 작은순으로 정렬하면 가장 작은 상자의 크기로 정렬이 될 것이다.
# 반복을 돌면서 가장 작은값을 찾아보자.


test20_dumy01 = [[60, 50], [30, 70], [60, 30], [80, 40]]
test20_dumy02 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
test20_dumy03 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

# test20(test20_dumy01)
