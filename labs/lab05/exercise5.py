Ely = input("Enter your score")
Daniel = input("Enter your score")
Hugo = input("Enter your score")

Scores = [int(Ely), int(Daniel), int(Hugo)]
average_score = sum(Scores) / len(Scores)
Total_Score = sum(Scores)
print("\n--- Class Scores Summary ---")
print(f"Ely's Score: {Ely} (Type: {type(Ely).__name__})")
print(f"Daniel's Score: {Daniel} (Type: {type(Daniel).__name__})")
print(f"Hugo's Score: {Hugo} (Type: {type(Hugo).__name__})")
print(f"Total Score: {Total_Score}")
print(f"Average Score: {average_score:.2f}")