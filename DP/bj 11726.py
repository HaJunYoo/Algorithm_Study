'''
동적 계획법의 핵심은 memoization 리스트를 사용하는 것

- 빈 리스트를 만들기 (입력값에 따른)
- 초기값을 설정
- 점화식 기반으로 계산값 적용하기
- 특정 입력값에 따른 계산값을 리스트에서 추출하기

일반적인 동적 계획법 문제는

통상 코드 자체는 간결하므로,

**가장 적은 경우의 수부터 계산을 해본 후, 패턴을 찾아,**식(점화식)을 세우는 것이 핵심

n = 1 부터 차례대로 나열하면서 점화식 패턴을 찾아봅니다
'''



n = int(input())
dp = [0] * 1001 # memoization
dp[1] = 1
dp[2] = 2


for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index - 2] # 점화식 설립
print (dp[n] % 10007)