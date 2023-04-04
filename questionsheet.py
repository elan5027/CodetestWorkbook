import math
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


# print(question07([2, 4]))


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


# print(question40(3, 20, 4))

# 최대공약수와 최소공배수
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


# 생각해낸 최대 함수
# 유클리드 호제법을 이용한 작성.
# 왜이렇게 쓰이는지 알려면 수학공식 봐야되고
#
# A=0 이면 GCD(0,B)=B  == GCD(A,B)=B
# B=0 이면 GCD(A,0)=A  == GCD(A,B)=A
# A를 A = B*Q+R
# GCD(A, B) = GCD(B, R)
#
# def gcd(a, b):
#     while b != 0:
#         r = a % b
#         a = b
#         b = r
#     return a
# B가 0일때까지 돌리며 B가 0이면 A,B의 최대공약수는 A가된다.
# 이를 축약하면 아래의 코드가 된다.
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# 해당 방법을 재귀를 통한 축약하면 아래의 모양이 된다.
# 아래의 모양으로 만들었다.
# https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def question41(n, m):
    def gcd(a, b):
        return gcd(b, a % b) if b else a
    return [gcd(n, m), n * m // gcd(n, m)]

# print(question41(7, 14))


def question42(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return int(answer, 3)


# print(question42(45))


# 에라토스테네스의 체 알고리즘은
# 1) 2부터 n까지의 모든 자연수 나열
# 2) 남은 수 중 처리하지 않은 가장 작은 수 i 탐색
# 3) 남은 수 중에서 i의 배수 제거(i 제외)
# 4) 2~3 과정 반복
# 의 과정으로 전개됩니다.
# 에라토스테네스의 체 간결 구현코드 참고.
# 효율성 차이 미쳣고.... 3000ms vs 300ms
def solution(n):
    num = set(range(2, n+1))  # 중복값 다제거.
    # 해당부분을 굳이 n+1로 잡을 필요가없다. **0.5 또는 //2 를 통해 절반으로 감소시켜도 된다.
    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

# 미친 개똑똑하다.
# range( 2*i  i값의 *2한 값 부터.
# n+1 한 값 까지의 범위를 가질것이다.
# i 만큼씩 떨어진 값을 만들꺼다. 즉
# set(range(4, 11, 2) ) 은 4, 6, 8, 10 을 만들고 해당 값을 num에서 제거한다.

# 최초의 num에는 2,3,4,5,6,7,8,9,10 이라는 값이 들어간다.
# 1회 반복시 num에는 2,3,5,7,9  남는다.
# 2회 반복시 set(range(6, 11, 3))은 6, 9 라는 값을 만들고 해당 값을 num에서 제거한다.
# 즉 2회 반복시 2,3,5,7 남는다
# 쭉 반복하여 값을 제거한다.
# 코드를 쭉 보았을대 반복문의 최대값을 어짜피 *2를 하여 절반으로 줄어드는데 n+1회까지 반복할 이유가 없는것 같다.
# 해당 부분을 (n+1)//2 로 나누어 테스트코드를 돌려보았는데 정상 작동하였다.


# print(solution(10))


def question43(n):
    # answer = 0

    # for i in range(2, n+1):
    #     is_prime = True
    #     for j in range(2, int(i**0.5)+1):
    #         if i % j == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         answer += 1
    # return answer

    def count_primes(n): return sum(
        all(n % i for i in range(2, int(n ** 0.5) + 1)) for n in range(2, n + 1))
    return count_primes(n)

# 예산 문제.


def question44(d, budget):
    answer = 0
    d.sort()
    for i in range(0, len(d)):
        if budget >= d[i]:
            answer += 1
            budget -= d[i]
    return answer


# print(question44([9, 2, 1, 3], 10))

def question45(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer += str(i)
    answer += '0'
    for i in range(1, len(food)):
        for j in range(food[len(food)-i]//2):
            answer += str(len(food)-i)

    return answer


# print(question45([1, 3, 4, 6]))


def question46(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i+m]) >= m:
            answer += (min(score[i:i+m])*m)

    return answer


# print(question46(3, 4, [1, 2, 3, 1, 2, 3, 1]))


def question47(number):
    answer = 0
    print(number)
    for i, num in enumerate(number):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                print(number[i], number[j], number[k])
                if (num+number[j]+number[k]) == 0:
                    answer += 1
                else:
                    continue
    return answer


# print(question47([-3, -2, -1, 0, 1, 2, 3]))


def question48(numbers, hand):
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

# print(question48([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
# print(question48([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))


def question49(survey, choices):

    # answer = ''
    # doc = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    # for key, value in zip(survey, choices):
    #     if key not in doc.keys():
    #         key = key[::-1]
    #         doc[key] -= value-4
    #     else:
    #         doc[key] += value-4

    # for key in doc.keys():
    #     if doc[key] >= 0:
    #         answer += key[1]
    #     elif doc[key] < 0:
    #         answer += key[0]
    # return answer

    choices_doc = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: -1,
        6: -2,
        7: -3
    }
    answer = ''
    doc = {
        "RT": 0,
        "CF": 0,
        "JM": 0,
        "AN": 0,
    }
    for i in range(0, len(survey)):
        if survey[i] not in doc.keys():
            survey[i] = survey[i][::-1]
            doc[survey[i]] += -choices_doc[choices[i]]
        else:
            doc[survey[i]] += choices_doc[choices[i]]

    print(doc)
    for key in doc.keys():
        if doc[key] < 0:
            answer += key[1]
        elif doc[key] >= 0:
            answer += key[0]
    return answer


# print(question49(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))


def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def is_prime_number2(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    # 수는 모두다 True -값이아니면.
    # [False, 2, 3, False,
    # [2,3,5,7,9]
    # 에라토스테네스의 체
    for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며

        if array[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n+1) if array[i]]
# cominations 함수 배우기.
# from itertools import combinations as cb
# 파이썬 for else 이건 몰랏다 ㄹㅇ.


def question50(nums):
    from itertools import combinations as cb
    answer = 0
    frime = is_prime_number2(2000)
    for c in cb(nums, 3):
        if sum(c) in frime:
            answer += 1

    # for i, _num in enumerate(nums):
    #     for j in range(i+1, len(nums)):
    #         for k in range(j+1, len(nums)):
    #             num = _num+nums[j]+nums[k]
    #             if is_prime_number(num):
    #                 answer += 1

    # for c in cb(nums, 3):
    #     if is_prime_number(sum(c)):
    #         answer += 1

    return answer


print(question50([1, 2, 3, 4]))


def question51(participant, completion):
    # answer = ''

    # for comp in completion:
    #     if comp in participant:
    #         participant.remove(comp)

    # return ''.join(participant)
    # 효율성테스트 통과를 위해 정렬한 이후 리스트내부를 검사하지 않고
    # 반복을 통해서 인덱스를 통한 검사로 변경하였다.
    # completion의 길이는 participant의 길이보다 1 작다는 구문상
    # 통과하지 못하는 사람은 1명이라는 결론을 가지고 문재를 재작성하였다.

    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# print(question51(["mislav", "stanko", "mislav", "ana"],
#      ["stanko", "ana", "mislav"]))


def question52(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    result = np.dot(arr1, arr2)
    return result.tolist()

# 넘파이 안쓰고 풀기 난이도 미쳣다.


def question52_type01(arr1, arr2):
    result = []

    for a1_row in arr1:
        row_result = []
        for a2_col in zip(*arr2):
            element_result = sum(a*b for a, b in zip(a1_row, a2_col))
            row_result.append(element_result)
        result.append(row_result)
    return result


# print(question52_type01([[1, 4], [3, 2], [4, 1]], [[3, 1], [2, 1]]))


def question53(new_id):
    import re
    new_id = str.lower(new_id)
    new_id = re.sub('[^0-9a-z\-\_\.]', '', new_id)
    # 처음 사용된 ^는 제외된것을 필터하겟다
    # [^ ] 괄호에 묶인경우는 제외된것 즉 Not '^x 는 문자의 시작부분 판단
    # 즉 ^0-9a-zㄱ-힗\-\_\. 이 부분은
    # 해당문자열에서는 0-9 (숫자) a-z (소문자) -,_,.(특수문자 3개)만을 허용하겟다.
    new_id = re.sub('[\^]', '', new_id)
    # 위 부분에서 사용된 ^가 필터가 되지않아 별도로 필터
    new_id = re.sub('\.{2,}', '.', new_id)
    # \. 문자가 2번이상 반복되면 필터하겟다 .으로
    # {2}는 2번 반복되면, {2,4} 2~4번반복되면 {2,} 2번이상 반복되면
    new_id = re.sub('^\.|\.$', '', new_id)
    # 시작이 .
    # | (or 또는)
    # . 으로 끝나면 빈값으로 바꾼다.

    if not new_id:
        new_id = 'a'
    # 비어있으면 a삽입
    if len(new_id) > 15:
        new_id = re.findall('.{1,15}', new_id)[0]
    # 문자열의 길이가 16 이상이면 findall() 1부터 15번째 까지 가져온다.
    # .x 는 임의의 문자 자릿수 표현 즉 어떤 문자던 1번부터 15번까지 가져온다는 의미.
    # 잘라낸 숫자는 리스트로 담기기때문에 15개가 담긴 0번 인덱스 가져온다.
    new_id = re.sub('^\.|\.$', '', new_id)
    # ^x 문자열의 시작은 x로 시작된다면
    # 해당에서 ^\. 은 문자열의 시작이 .이라면
    # x$ 문자열의 종료가 x라면
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    #문자열의 길이가 2이하인 경우에는 현재 문자열의 끝자리를 문자열의 길이가 3이 될만큼 반복하여 더해준다.
    return new_id


print(question53("asdasdasdasdas.a"))
