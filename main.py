import time
import random
import string
from matplotlib import pyplot as plt

def random_input(n):    # Random input
    rand_str = ""
    for i in range(n):  # n개의 문자 생성
        rand_str += str(random.choice(string.ascii_uppercase)) # 랜덤한 대문자 문자열 생성
    return rand_str

def MAX(num1, num2):    # 더 큰 값 반환
    if num1 > num2:
        return num1
    else:
        return num2

def LCS_LENGTH(X, Y, i, j):     # LCS의 길이를 구하는 함수
    if c[i][j] != -1:
        return c[i][j]
    else:
        if X[i-1] == Y[j-1]:
            c[i][j] = LCS_LENGTH(X, Y, i-1, j-1) + 1
        else:
            c[i][j] = MAX(LCS_LENGTH(X,Y,i,j-1), LCS_LENGTH(X,Y,i-1,j))

        return c[i][j]


n_array = [50,100,150,200,250,300,350,400,450,500]    # number of input
actual_running_time = [0 for num in range(len(n_array))]  # actual running time

for iter, n in enumerate(n_array):

        # random sequence 생성
        X = random_input(n)
        Y = random_input(n)

        # 0번째 row 또는 col에서는 배열 값이 0, 그 외에는 배열 값이 -1
        c = [[-1 for col in range(n+1)] for row in range(n+1)]
        for row in range(n+1):
            c[row][0] = 0
        for col in range(n+1):
            c[0][col] = 0


        start = time.time()

        LCS_LENGTH(X, Y, n, n)  # X와 Y 사이의 LCS의 길이를 구함

        end = time.time()-start # 실행 시간 측정


        print("Length of LCS : ", c[n][n])  # LCS의 길이 출력
        actual_running_time[iter] = end  # 한 n에서의 수행 시간의 평균을 저장


for iter, n in enumerate(n_array):  # average actual running time 출력
    print("n = ", n, ", actual running time : ", actual_running_time[iter])



# Plot

plt.plot(n_array, actual_running_time, marker='o', color='b')
plt.title('Actual Running time')
plt.xlabel('n')
plt.ylabel('running time')
plt.xticks([50,100,150,200,250,300,350,400,450,500]) # x축 단위 설정

plt.show()

