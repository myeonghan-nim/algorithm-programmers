def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food_times_with_index = [(food, i + 1) for i, food in enumerate(food_times)]
    food_times_with_index.sort()

    previous_food_time, length = 0, len(food_times)
    for i, (food_time, _) in enumerate(food_times_with_index):
        time_to_finish = (food_time - previous_food_time) * length

        if k >= time_to_finish:
            k -= time_to_finish
            previous_food_time = food_time
            length -= 1
        else:
            k %= length
            remaining_foods = sorted(food_times_with_index[i:], key=lambda x: x[1])
            return remaining_foods[k][1]

    return -1
