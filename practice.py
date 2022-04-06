def check(skill, skill_tree):
    pos = -1
    for skill_tree_elem in skill_tree:
        for i, skill_elem in enumerate(skill):
            if skill_tree_elem == skill_elem:
                if pos < i:
                    pos = i
                    break
                else:
                    return 0
    return 1

                    
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += check(skill, skill_tree)

    return answer

skill = input()
skill_trees = list(input().split())

print(solution(skill, skill_trees))