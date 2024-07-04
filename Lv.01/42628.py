from collections import deque


def solution(operations):
    answer = deque()
    for operation in operations:
        if operation == "D 1":
            if answer:
                answer.pop()
        elif operation == "D -1":
            if answer:
                answer.popleft()
        else:
            answer.append(int(operation.split()[1]))
        answer = deque(sorted(answer))
    return [answer[-1], answer[0]] if answer else [0, 0]
