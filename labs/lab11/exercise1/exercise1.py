num_rounds = int(input())

final_score = 0
rounds_processed = 0


for i in range(num_rounds):
    score = int(input())
    
    if score > 100:
        score = score * 1.2   # add 20% bonus
    
    final_score += score
    rounds_processed += 1

print(f"final_score: {final_score:.1f}")
print(rounds_processed)
