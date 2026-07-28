import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    answer = next(iter(answer))
    return answer