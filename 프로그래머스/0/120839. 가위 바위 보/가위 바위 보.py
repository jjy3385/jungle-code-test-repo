def solution(rsp):
    rsp_win = {'2':'0','0':'5','5':'2'}
    answer = "".join([rsp_win[x] for x in rsp])
    return answer