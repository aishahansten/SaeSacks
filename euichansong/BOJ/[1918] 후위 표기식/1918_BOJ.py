# in coming priority
icp= {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
# in stack priority
isp= {
    '(': 0,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
sentence = input()
stack = []
for i in sentence:
    # 닫는 괄호일때
    if i == ')':
        # 스택에서 여는 괄호 나올때 까지
        while stack[-1] != '(':
            # 스택에서 팝하고 연산자 프린트
            print(stack.pop(), end = '')
        # 여는 괄호 버림
        stack.pop()
    # 연산자라면
    elif i in '+-*/(':
        # 스택이 비어있지 않으면
        if not stack:
            # 연산자 스택에 추가
            stack.append(i)
        # 스택이 비어있으면
        else:
            # 우선순위가 들어올 연산자가 스택의 탑에 있는 연산자보다 크다면
            if icp[i] > isp[stack[-1]] :
                # 스택에 넣음
                stack.append(i)
            # 그렇지 않다면
            else:
                # 스택이 비어있고 스택의 탑에 있는 연산자의 우선순위가 들어올 연산자보다 높을때 까지
                while stack and isp[stack[-1]] >= icp[i] :
                    # 스택에서 팝하고 출력
                    print(stack.pop(), end = '')
                # 스택에 연산자 push
                stack.append(i)
    # 연산자나 괄호가 아니라면
    else:
        # 출력
        print(i, end = '')
# 스택이 빌때까지
while stack:
    # 스택에 남은 연산자 팝 하고 출력
    print(stack.pop(), end = '')






