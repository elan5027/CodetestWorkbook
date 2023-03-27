def test01(n):
    answer = []
    strn = (str(n)[::-1])
    for i in range(0, len(strn)):
        answer.append(int(strn[i]))
    print(answer)


# test01(1012345)


def test02(number):
    answer = 0
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i]+number[j]+number[k] == 0:
                    answer += 1

    return answer


test02_dumy1 = [-2, 3, 0, 2, -5]
test02_dumy2 = [-3, -2, -1, 0, 1, 2, 3]
test02_dumy3 = [-1, 1, -1, 1]

# test02(test02_dumy2)


def test03(s):
    answer = []
    zero_count = 0
    binery = 0
    while (len(s) > 1):
        zero_count += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        binery += 1
    answer.append(binery)
    answer.append(zero_count)
    return answer


# test03("110010101001")

def test04(s):
    st = list(map(int, s.split(' ')))

    return str(min(st))+" "+str(max(st))


test04_dumy01 = "1 2 3 4"
test04_dumy02 = "-1 -2 -3 -4"
# print(test04(test04_dumy02))


def test05(s):
    answer = []
    a = ' '.join(map(lambda s: s[0].upper() +
                     s[1:].lower() if s else s, s.split(' ')))

    st = s.split(' ')
    for x in st:
        if x:
            answer += [x[0].upper()+x[1:].lower()]

        else:
            answer += [x]
    answer = ' '.join(map(str, answer))
    print("Lambda : ", a)
    print("Generic : ", answer)


test05_dumy01 = "3people aaa 3a  unFollowed w  9 me"
test05_dumy02 = "a a a a a a a a a a "
# test05(" hello word")


def test06(s):
    answer = ''
    for word in s.split(' '):
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    print(answer)
    return answer[:-1]


# print(test06("  tRy hello  WORLD   "))

def test07(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B, reverse=True)
    print(a, b)
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
# 가장 작은 경우의수는 A의 최소값 * B의 최대값 , 중간값, A의 최대값 * B의 최소값이므로 정렬과 역정렬을 하여
# 순서대로 곱해주면 최소곱이 나온다.


# test07([1, 4, 2], [5, 4, 4])

def test08(s):
    start = '('
    end = ')'
    count = 0
    for i in s:
        if i == start:
            count += 1
        elif i == end:
            count -= 1
        if count < 0:
            return False
    return count == 0
    # 괄호가 열렷으면 닫쳐야된다. 현제 문자가 무었인지 판단하고
    # 열린 갯수를 카운팅한다. 열리면 +1 닫히면 -1  카운트가 0보다 작아지면 닫힘의 잘못사용 false 리턴
    # 열린갯수와 닫힌갯수가 같으면 True 아니면 False
    # 처음이 )면 false 마지막이 ( 면 false 처음에 닫히면 -1이 됨으로 false 리턴 마지막이 열리면 1이됨으로 False 리턴

# print(test08("()()"))


def test09(n):
    answer = 0
    for i in range(1, n+1):
        notCount = 1
        maxcount = int(n/i)
        temp = 0
        for j in range(i, n+1):
            temp += j
            if notCount > maxcount:
                break
            if temp > n:
                break
            if temp == n:
                answer += 1
    print(answer)
    # for i in range(1, n+1):
    #     maxcount = int(n/i)

    #     find = False
    #     num = i
    #     sum = 0
    #     interCount = 1
    #     while num <= n:
    #         if interCount > maxcount:
    #             break
    #         sum += num

    #         if sum == n:
    #             find = True
    #             break

    #         num += 1
    #         interCount += 1
    #     if find:
    #         answer += 1

    return answer


# n을 연속한 자연수들로 표현.
# 15= 1+2+3+4+5 / 4+5+6 / 7+8 / 15
# 등차가 1인 수열  !! 최대 시행횟수는 최대값 / 현재값 만큼이다.
# 반복횟수마다 시행횟수 카운트를 증가시키고 시행횟수가 최대 시행횟수가 도달하면 없다고 판단하고 break한다.
# test09(9)

def test10(n):
    n2_one = bin(n).count('1')

    while 1:
        n += 1
        if n2_one == bin(n).count('1'):
            print(n)
            return n

# n의 다음큰숫자는 n보다 크다.
# n의 다음 큰숫자와 n은 2진 변환 시 1의 갯수가 같다. count 1
# n의 다음 큰 숫자는 조건 1,2를 만족하는 수중 가장 작다.

# 다풀고 찾아본 다른사람 코드중 인상깊은 코드
    # n_bin = bin(n)[2:]
    # add_len = 0
    # for i in range(len(n_bin)):
    #     if n_bin[-(i + 1)] == '1':
    #         add_len = i
    #         break
    # add = '1' + '0' * add_len
    # target = bin(n + int(add, 2))[2:]
    # slide_len_1 = n_bin.count('1') - target.count('1')
    # if slide_len_1 == 0:
    #     return int(target, 2)
    # return int(target[:-slide_len_1] + '1' * slide_len_1, 2)
# test10(78)


def test11(n):
    pabo_a = 1
    pabo_b = 1
    if n <= 2:
        pabo_a = 1
    for i in range(1, n):
        pabo_a, pabo_b = pabo_b, pabo_b+pabo_a
        print(i, " : ", pabo_a, pabo_b)
    num = 1234567
    return pabo_a % num
# 파보나치 수열은 F(0) = 0 / F(1) = 1 일때 1이상의 n에 대하여 F(n) = F(n-1)+ F(n-2)가 적용되는 수이다.
# Ex. F(2) = F(0) + F(1) = 0 + 1 = 1
#    F(3) = F(1) + F(2) = 1 + 1 = 2


# 재귀식 표현.
def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

# 메모이제이션을 활용한 재귀식 방법
# 데이터 연산량을 줄여준다. 반복 사용되는 재귀함수들의 데이터들을 일괄적으로 memo 리스트에 모아두고 재사용.


def fib2(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fib2(n-1) + fib2(n-2))
    return memo[n]


memo = [0, 1]


# pabo = []
# pabo.append(fib1(5))
# print(pabo)


def test12(s):
    answer = -1
    st = []
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                st += s[:i]+s[j:]
                print("CH : ", s[:i], s[j:])
                break
    print(st)
    return answer

# 알파벳 소문자로 이루어진 문자.
# 문자열에서 같은 알파벳 2개 붙어 있는 짝찾기.
# 그둘을 제거하 앞뒤 문자열을 이어 붙힌다.
# 위 행위를 반복하는데 이행위가 가능하면 1을 불가하면 0을.


test12_dumy01 = "baabaa"
test12_dumy02 = "cdcd"

test12(test12_dumy01)
