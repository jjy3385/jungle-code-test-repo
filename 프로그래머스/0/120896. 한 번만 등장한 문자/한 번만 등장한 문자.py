def solution(s):
    answer = ''
    count = {}
    temp_list = []
    for ch in s:
        count[ch] = count.get(ch,0) + 1
    for c in count:
        if count[c] == 1:
            temp_list.append(c)
    answer = ''.join(sorted(temp_list))
    return answer