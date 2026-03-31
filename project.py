import random
# define quiz questions
questions = [{"question":"Which is the largest country in Africa?","choices":['A:' 'Kenya', 'B:' 'Nigeria', 'C:' 'Algeria', 'D:' 'Rwanda'], 'answer':'C' },{"question":"in which year did Kenya become a republic?", "choices":['A:' '1963', 'B:' '1964', 'C:' '1965', 'D:' '1962'], 'answer':'B'}, {"question":"the following are cabohydrates except?", "choices":['A:' 'Beans', 'B:' 'Yams', 'C:' 'Maize', 'D:' 'Potatoes'], 'answer':'A'}]

score = 0

for q in questions:
    print(q['question'])
    for choice in q["choices"]:
        print(choice)

    ans = input("Enteryour answer (A/B/C/D): ")

    correct_ans = q["answer"]
    if ans == correct_ans:
                print("correct!")
                score += 1
    else:
        print("wrong")

print("Your total score is", score)

            






