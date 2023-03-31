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


print(question22(["left", "right", "up", "right", "right"],	[11, 11]))
