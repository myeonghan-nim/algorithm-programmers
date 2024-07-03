def solution(friends, gifts):
    num_friends = len(friends)

    give_and_take = [[0] * num_friends for _ in range(num_friends)]
    for gift in gifts:
        give, take = gift.split(" ")
        give_and_take[friends.index(give)][friends.index(take)] += 1

    gift_indexes = [0] * num_friends
    for i in range(num_friends):
        gift_indexes[i] = sum(give_and_take[i]) - sum([row[i] for row in give_and_take])

    answers = [0] * num_friends
    for i in range(num_friends):
        for j in range(num_friends):
            if i != j:
                gave, took = give_and_take[i][j], give_and_take[j][i]
                give_idx, take_idx = gift_indexes[i], gift_indexes[j]
                if gave > took:
                    answers[i] += 1
                elif gave == took and give_idx > take_idx:
                    answers[i] += 1

    max_answers = max(answers)
    if all([answer == max_answers for answer in answers]):
        return 0
    else:
        return max_answers
