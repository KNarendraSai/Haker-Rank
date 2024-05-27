def is_vowel(char):
    return char.lower() in 'aeiou'
def calculate_scores(s):
    stuart_score = 0
    kevin_score = 0
    length = len(s)

    for i in range(length):
        if is_vowel(s[i]):
            kevin_score += length - i
        else:
            stuart_score += length - i

    return stuart_score, kevin_score
def minion_game(s):
    stuart_score, kevin_score = calculate_scores(s)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
