score1 = 85
score2 = 92.5
score3 = 78

average_score = (score1 + score2 + score3) / 3
print(f"Average score: {average_score} (type: {type(average_score)})")

average_score_int = int(average_score)
print(f"Average score (int): {average_score_int} (type: {type(average_score_int)})")

result = score1 ** 2 / score2 + score3 % 7
print(f"Result of expression: {result} (type: {type(result)})")

# compare int(score2) vs float(score1)
print(f"int(score2): {int(score2)} (type: {type(int(score2))})")
print(f"float(score1): {float(score1)} (type: {type(float(score1))})")  