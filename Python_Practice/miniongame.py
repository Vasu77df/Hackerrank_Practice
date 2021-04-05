def minion_game(string):
    vowel = ['A', 'E', 'I, O', 'U']
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string) - i
        else:
            S+=len(string) - i
    if S>K:
        print(f"Stuart {S}")
    elif K>S:
        print(f"Kevin {K}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)