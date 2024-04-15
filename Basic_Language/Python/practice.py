def solution(gems):
    possible_answers = []
    length = len(gems)

    buy_list = []
    buy_unique = set()

    left = 0
    right = 0
    buy_list.append(gems[0])
    buy_unique = set(buy_list)

    while right < length and left <= right:
        if len(buy_unique) < 4:
            right += 1

            if right < length:
                buy_list.append(gems[right])
                buy_unique = set(buy_list)

        elif len(buy_unique) > 4:
            buy_list.pop(0)
            buy_unique = set(buy_list)
            left -= 1

        else:
            possible_answers.append([left, right, right - left + 1])

            right += 1
            if right < length:
                buy_list.append(gems[right])

            buy_list.pop(0)
            left += 1

            buy_unique = set(buy_list)

    # 정답 후보에서 정답 가려내기
    min_length = possible_answers[0][2]
    min_length_idx = -1

    for idx, elem in enumerate(possible_answers):
        min_length = min(min_length, elem[2])
        min_length_idx = idx

    answer = [possible_answers[min_length_idx]
              [0], possible_answers[min_length_idx][1]]

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
