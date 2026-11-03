import math
def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h: return scores[nodeIndex]
    if isMax:
        return max(minimax(depth+1, nodeIndex*2, False, scores, h), minimax(depth+1, nodeIndex*2+1, False, scores, h))
    else:
        return min(minimax(depth+1, nodeIndex*2, True, scores, h), minimax(depth+1, nodeIndex*2+1, True, scores, h))
if __name__ == "__main__":
    scores = list(map(int, input("Enter leaf node scores separated by space: ").split()))
    h = math.log2(len(scores))
    print("Optimal value:", minimax(0, 0, True, scores, int(h)))