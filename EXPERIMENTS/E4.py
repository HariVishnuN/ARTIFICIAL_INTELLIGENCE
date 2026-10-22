import itertools
def solve_cryptarithmetic(word1, word2, result):
    letters = list(set(word1 + word2 + result))
    if len(letters) > 10: return None
    first_letters = {word1[0], word2[0], result[0]}
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[char] == 0 for char in first_letters): continue
        num1 = int("".join(str(mapping[char]) for char in word1))
        num2 = int("".join(str(mapping[char]) for char in word2))
        num_res = int("".join(str(mapping[char]) for char in result))
        if num1 + num2 == num_res: return mapping
    return None
if __name__ == "__main__":
    w1, w2, res = "SEND", "MORE", "MONEY"
    print(f"Solving: {w1} + {w2} = {res}\n")
    solution = solve_cryptarithmetic(w1, w2, res)
    if solution:
        print("Solution Mapping:", solution)
        val1 = "".join(str(solution[c]) for c in w1)
        val2 = "".join(str(solution[c]) for c in w2)
        val_res = "".join(str(solution[c]) for c in res)
        print(f"Result: {val1} + {val2} = {val_res}")
    else:
        print("No solution found.")