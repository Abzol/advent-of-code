import sys

matching_brace= {')':'(', ']':'[', '}':'{', '>':'<'}
score_value = {')':3, ']':57, '}':1197, '>':25137}
score_auto ={'(':1, '[':2, '{':3, '<':4}

def ver_one(input):
    lines = input.readlines()
    score = 0
    for line in lines:
        stack = []
        for c in line.rstrip():
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                if stack[-1] == matching_brace[c]:
                    stack.pop()
                else:
                    score += score_value[c]
                    break
    return score

def ver_two(input):
    lines = input.readlines()
    scores = []
    for line in lines:
        score = 0
        stack = []
        for c in line.rstrip():
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                if stack[-1] == matching_brace[c]:
                    stack.pop()
                else:
                    stack = []
                    break
        while (len(stack) > 0):
            score = score * 5
            score += score_auto[stack.pop()]
        if score > 0:
            scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]