def solution(id_list, report, k):
    blacklist = {}
    for i in id_list:
        blacklist[i] = {"cnt": 0, "reported": [], "reports": []}

    for r in report:
        me, you = r.split(" ")
        if me not in blacklist[you]["reported"]:
            blacklist[you]["reported"].append(me)
            blacklist[you]["cnt"] += 1
            blacklist[me]["reports"].append(you)

    answer = []
    for v in blacklist.values():
        cnt = 0
        for i in v["reports"]:
            if blacklist[i]["cnt"] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
