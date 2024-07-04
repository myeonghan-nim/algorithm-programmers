def solution(bandage, health, attacks):
    hp = [health] * (attacks[-1][0] + 1)

    bonus_cnt, attck_idx = 0, 0
    for i in range(1, len(hp)):
        hp[i] = hp[i - 1]
        if i == attacks[attck_idx][0]:
            hp[i] -= attacks[attck_idx][1]
            attck_idx += 1
            bonus_cnt = 0
            continue

        bonus_cnt += 1
        if bonus_cnt == bandage[0]:
            hp[i] += bandage[1] + bandage[2]
            bonus_cnt = 0
        else:
            hp[i] += bandage[1]

        hp[i] = min(hp[i], health)
        if hp[i] <= 0:
            return -1

    if hp[-1] > 0:
        return hp[-1]
    else:
        return -1
