import math
def alpha_beta(depth, nodeIndex, isMax, scores, alpha, beta, h):
    if depth == h: return scores[nodeIndex]
    if isMax:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, False, scores, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, True, scores, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break
        return best
if __name__ == "__main__":
    scores = list(map(int, input("Enter leaf node scores separated by space: ").split()))
    h = math.log2(len(scores))
    print("Optimal value:", alpha_beta(0, 0, True, scores, -math.inf, math.inf, int(h)))