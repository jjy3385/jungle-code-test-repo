def solution(id_pw, db):
    dict_db = dict(db)
    if id_pw[0] not in dict_db.keys():
        return "fail"
    if id_pw[1] == dict_db[id_pw[0]]:
        return "login"
    else:
        return "wrong pw"