import numpy as np
import random


def question01(num1, num2):
    answer = num1 // num2
    print(answer)


def question02(array):
    answer_key = 0
    answer_value = 0
    count = {}
    for arr in array:
        count[arr] = array.count(arr)
    for key, value in count.items():
        if answer_value < value:
            answer_key = key
            answer_value = value
        elif answer_value == value == max(count.values()):
            return -1
    return answer_key


a = [1, 2, 3, 3, 3, 4]
b = [1, 1, 2, 2]
c = [1]
d = [0, 0, 0, 0]
# print(question02(b))


def question03(numbers):
    return [numbers[i]*2 for i in range(len(numbers))]


question03_data01 = [1, 2, 100, -99, 1, 2, 3]
question03_data02 = [1, 2, 3, 4, 5]
# print(question03(question03_data01))


def question04(numbers):
    for i in range(int(len(numbers)//2)):
        temp = numbers[i]
        numbers[i] = numbers[len(numbers)-i-1]
        numbers[len(numbers)-i-1] = temp
    return numbers


question04_data01 = [1, 2, 3, 4, 5]
question04_data02 = [1, 1, 1, 1, 1, 2]
question04_data03 = [1, 0, 1, 1, 1, 3, 5]
# print(question04(question04_data03))


def question05(my_string):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[len(my_string)-i-1]
    return answer


question05_data01 = "jaron"
# print(question05(question05_data01))


def question06(rsp):

    # Type01. 기본방법
    # answer = ''
    # for rsp_ in rsp:
    #     if '2' == rsp_:
    #         answer += '0'
    #     elif '0' == rsp_:
    #         answer += '5'
    #     else :
    #         answer += '2'
    # return answer

    # Type02. 딕셔너리 활용한 방법
    rsp_dic = {'0': '5', '2': '0', '5': '2'}
    answer = ''.join(rsp_dic[rsp_] for rsp_ in rsp)
    return answer

# print(question06("205"))


def question07(dot):
    # x가 음수면 2,3  y가 음수면 3,4
    # 둘다 음수면 3 둘다 양수면 1
    x, y = dot
    if x * y > 0:
        # x,y 둘다 음수 or 양수 경우의수 1 or 3
        # 둘중 하나라도 양수면 나머지도 양수니 x가 0 보다 크면
        # 1사분면 이다.
        return 1 if x > 0 else 3
    else:
        # 둘중 하나라도 음수인 경우 2,4
        # x가 양수라면 y는 음수이니 x가 양수면 4사분면
        return 4 if x > 0 else 2


# print(question07([2,4]))

def question08(numbers):
    numbers.sort()
    max_1 = numbers.pop()
    max_2 = numbers.pop()

    return max_1*max_2


question08_data01 = [1, 2, 3, 4, 5]
question08_data02 = [0, 31, 24, 10, 1, 9]
# print(question08(question08_data01))


def question09(my_string):
    answer = []
    for numcheck in my_string:
        if numcheck.isnumeric():
            answer.append(int(numcheck))
        answer.sort()
    return answer

# print(question09("hi12392"))


def question10(my_string):
    return ''.join(dict.fromkeys(my_string))


# print(question10('"We are the world'))


def question11(my_string):
    answer = ''
    # str.swapcase(my_string)
    for my_str in my_string:
        if my_str.islower():
            answer += str.upper(my_str)
        elif my_str.isupper():
            answer += str.lower(my_str)
        else:
            answer += my_str
    return answer


# question11("abCdEfghIJ")

def question12(my_string, num1, num2):
    answer = ''
    for i, my_str in enumerate(my_string):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_str

    # 방법2. 리스트화 시키고 쉽게 바꾸기.
    # answer = list(my_string)
    # answer[num1],answer[num2]  = my_string[num2], my_string[num1]
    # return ''.join(answer)

    return answer


# question12("I love you", 3, 6,)

def question13(s1, s2):
    answer = 0
    for _str in s1:
        if _str in s2:
            answer += 1
    return answer

# 방법2


def question13_solutuin02(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return len(s1.intersection(s2))


question13_dumy01 = ["n", "omg"], ["m", "dot"]
question13_dumy02 = ["a", "b", "c"], ["com", "b", "d", "p", "c"]
# question13(*question13_dumy02)
# print(question13_solutuin02(*question13_dumy02))


def question14(num, k):
    numlist = list(str(num))
    if str(k) in numlist:
        return numlist.index(str(k))+1
    else:
        return -1


# question14(29183, 1)


def question15(my_string):
    return ''.join(sorted(str.lower(my_string)))

# question15("Python")


def question16(array, height):
    array = sorted(array, reverse=True)
    for i, row in enumerate(array, start=0):
        if height < row:
            continue
        else:
            return i
    return len(array)


# print(question16([149, 180, 192, 170, 167], 0))

def question17(dots):
    # 1,4 * 1,2
    # * * * * *
    # 4 * 2 * *  1
    # * * * * *  0
    # 1 * 3 * *  -1
    # * * * * *
    # * * * * *
    # 1-2 + 1-1 = -1
    # 1-1 + 1-2 = -1 = 1
    x = []
    y = []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    return ((max(x)-min(x)) * (max(y)-min(y)))


test01 = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
test02 = [[1, 1], [2, 1], [2, 2], [1, 2]]
# print(question17(test01))


def question18(bin1, bin2):
    answer = (int(bin1, 2))+(int(bin2, 2))
    return bin(answer)[2:]


# print(question18("1001", "1111"))


def question19(num, total):
    answer = []
    average = total // num
    start_index = average - (num - 1) // 2
    end_index = average + (num + 2) // 2
    for i in range(start_index, end_index):
        answer.append(i)
    return answer


# print(question19(5, 15))
def question20(id_pw, db):
    for _db in db:
        if id_pw[0] == _db[0]:
            if id_pw[1] == _db[1]:
                return 'login'
            return "wrong pw"
    return "fail"


question20_data01 = ["meosseugi", "1234"], [
    ["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
question20_data02 = ["programmer01", "15789"],	[
    ["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
# print(question20(*question20_data02))


def question21(n, numlist):
    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer

# print(question21(3, [2, 100, 120, 600, 12, 12]))


def question22(num_list, n):
    answer = []
    for i in range(0, len(num_list)//2):
        temp = []
        index = 0
        if len(num_list) >= n-1:
            while (index != n):
                temp.append(num_list.pop(0))
                index += 1
        if temp:
            answer.append(temp)
    return answer

# print(question22([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))


def question22(keyinput, board):

    my_board = [0, 0]
    max_x = (board[0])//2
    max_y = (board[1])//2
    for key in keyinput:
        if 'left' == key and -max_x != my_board[0]:
            my_board[0] -= 1

        elif 'right' == key and max_x != my_board[0]:
            my_board[0] += 1

        elif 'up' == key and max_y != my_board[1]:
            my_board[1] += 1

        elif 'down' == key and - max_y != my_board[1]:
            my_board[1] -= 1

    return my_board


# print(question22(["left", "right", "up", "right", "right"],	[11, 11]))

def question23(numbers):
    answer = ''
    doc = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    start = 0
    end = 0
    for i in range(0, len(numbers)+1):
        if numbers[start:i] in doc:
            end = i
            answer += doc[numbers[start:end]]
            start = i
    return int(answer)


# print(question23("onetwothreefourfivesixseveneightnine"))

def question23(lines):
    answer = 0
    tmp = []
    for i in lines:
        for j in range(i[1]-i[0]):
            tmp.append(i[0]+j)
    tmp2 = []
    # 결과값에 answer 안에 속해있는 2개이상 중복된 값의 갯수 찾기
    for x in set(tmp):
        if tmp.count(x) >= 2:
            tmp2.append(x)
    return len(tmp2)


def question23_type02(lines):
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


# print(question23([[0, 5], [3, 9], [1, 10]]))

def question24(quiz):
    answer = []
    for q in quiz:
        tmp = q.split(' ')
        if tmp[1] == '-':
            if (int(tmp[0])-int(tmp[2])) == int(tmp[4]):
                answer.append('O')
            else:
                answer.append('X')
        elif tmp[1] == '+':
            if (int(tmp[0])+int(tmp[2])) == int(tmp[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer


def question24_type02(quiz):
    total = []
    for q in quiz:
        question, answer = q.split(' = ')
        x, op, z = question.split()
        if op == '+':
            result = 'O' if int(x) + int(z) == int(answer) else 'X'
            total.append(result)
        elif op == '-':
            result = 'O' if int(x) - int(z) == int(answer) else 'X'
            total.append(result)

    return total


# print(question24(["3 - 4 = -3", "5 + 6 = 11"]))

def question25(board):
    board = np.array(board)
    rows, cols = np.where(board == 1)

    for r, c in zip(rows, cols):
        if r-1 >= 0 and c-1 >= 0:
            board[r-1:r+2, c-1:c+2] = 1
        if c-1 < 0:
            board[r-1:r+2, c:c+2] = 1

    return len(board[board == 0])


def question25_type02(board):
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


def question25_type03(board):
    answer = 0
    bomb = []

    for i, boad in enumerate(board):
        for j in range(0, len(board)):
            if (boad[j] == 1):
                bomb.append([i, j])

    bomblen = (len(bomb))  # 폭탄의 갯수저장.
    for column in range(len(board)):
        for row in range(len(board)):
            for i in range(0, bomblen):
                if bomb[i] == [column, row]:
                    for num in range(-1, 2):
                        numCol = (column+num) if (column +
                                                  num) >= 0 and (column+num) < len(board) else column
                        numRow = (row+num) if (row+num) >= 0 and (row +
                                                                  num) < len(board) else row
                        onumCol = (column-num) if (column -
                                                   num) >= 0 and (column-num) < len(board)else column
                        board[numCol][row] = 2  # 위아래
                        board[numCol][numRow] = 3  # 좌상 우하
                        board[column][numRow] = 4  # 좌우
                        board[onumCol][numRow] = 5  # 좌하 우상

    for i in board:
        for j in range(0, len(board)):
            if (i[j] == 0):
                answer += 1
    return answer


# print(question25_type03([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
#      0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))


def question26(dots):
    arr = []
    answer = 0
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


# print(question26([[1, 4], [9, 2], [3, 8], [11, 6]]))


# 나중에 sort 안쓰고 재도전
def question27(strings, n):
    strings.sort()
    answer = []
    copy_strings = []
    for i in range(0, len(strings)):
        copy_strings.append(strings[i][n] + strings[i])
    copy_strings.sort()

    for i, string in enumerate(copy_strings):
        print(i, string[1:])
        answer.append(string[1:])
    return answer


dumy01 = [["sun", "bed", "car"], 1]
dumy02 = [["abce", "abcd", "cdx"], 2]
# print(question27(*dumy02))


def question28(n, arr1, arr2):
    answer = 0
    result = []
    for i in range(0, len(arr1)):
        result.append(bin(arr1[i] | arr2[i])[2:])

    for i in range(len(result)):
        if len(result[i]) < n:
            result[i] = '0' * (n - len(result[i])) + result[i]

        result[i] = result[i].replace('1', '#')
        result[i] = result[i].replace('0', ' ')

    return result


# print(question28(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

def question29(phone_number):
    answer = ''
#    answer = "".join("*" for x in range(0, len(phone_number))
#                     if x < (len(phone_number)-4) else phone_number[x])

    for i in range(0, len(phone_number)):
        if i < len(phone_number)-4:
            answer += '*'
        else:
            answer += phone_number[i]

    return answer


# print(question29("01033334444"))

def question30(a, b):
    answer = 0

    # Type 1
    # for i in range(min(a,b), max(a,b)+1):
    #     answer += i
    # return answer

    # Type 2
    return (abs(a-b)+1) * (a+b)//2


# print(question30(3, 5))


def question31(s):

    return True if s.isdigit() and len(s) in [4, 6] else False


# print(question31("a234"))

def question32(numbers):
    return sum(range(10)) - sum(numbers)


def question33(x, n):
    answer = []
    for xn in range(1, n+1):
        answer.append((x*xn))

    return answer


def question34(n):
    # str_x = str(n)
    # test = 0
    # for x1 in str_x:
    #     test += int(x1)
    # return n % test == 0
    return n % sum(int(x) for x in str(n)) == 0


# print(question34(11))


def question35(arr, divisor):
    # answer = []

    # for ar in arr:
    #     if ar % divisor == 0:
    #         answer.append(ar)
    # if len(answer) == 0:
    #     answer.append(-1)
    # answer.sort()
    # return answer

    return sorted([n for n in arr if n % divisor == 0]) or [-1]


# print(question35([3, 2, 6], 10))

def question36(arr1, arr2):

    answer = []
    for i, j in zip(arr1, arr2):
        result = []
        for z, x in zip(i, j):
            result.append(z+x)
        answer.append(result)

    # Tpye2
    # answer = [[z+x for z,x in zip(i,j)] for i,j in zip(arr1,arr2)]
    return answer


# print(question36([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


def question37(array, commands):
    answer = []
    # Commands[0] Start_index  : Index-1
    # Commands[1] End_index : Index
    # Commands[2] Return_index : index-1

    for com in commands:
        temp = sorted(array[com[0]-1:com[1]])
        answer.append(temp[com[2]-1])
    return answer


# print(question37([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


def question38(s):
    number_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                   'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for key, value in number_dict.items():
        s = s.replace(key, value)
    answer = int(s)
    return answer


# print(question38("2three45sixseven"))


def question39(num):
    answer = num
    cnt = 0
    while True:
        if answer % 2 == 0:
            answer = answer / 2
            cnt += 1
            if answer == 1:
                break
        elif answer == 1:
            break
        else:
            answer = answer * 3 + 1
            cnt += 1
        if answer == 1:
            break

    if cnt >= 500:
        cnt = -1
    return cnt

# print(question39(16))


def question40(price, money, count):

    # count 증가할수록 price 곱적용
    max_count = (count+1)*count//2*price
    return max_count-money if (max_count-money > 0) else 0

    return max(0, (count+1)*count//2*price-money)


#print(question40(3, 20, 4))


def question41(n):
    answer = 0
    return answer

def question42(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)

print(question42(45))