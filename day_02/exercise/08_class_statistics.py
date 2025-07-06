student_scores = [98, 75, 100, 86, 100, 3]

lowest_score = min(student_scores)
print(lowest_score)
highest_score = max(student_scores)
print(highest_score)

average = sum(student_scores)/len(student_scores)
print(average)

print(sorted(student_scores, reverse=True))
