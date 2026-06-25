def solution(array):
    
    dict = {}
    for a in array:
        if a in dict:
            dict[a] += 1
        else:
            dict[a] = 1
    max_count = max(dict.values());
    
    temp = []
    for key,value in dict.items():
        if value == max_count:
            temp.append(key)
            
    if len(temp) > 1:
        return -1
    else:
        return temp[0]
