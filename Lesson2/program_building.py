def scores_to_rating(score1,score2,score3,score4,score5):
    
    score1 = float(score1)
    score2 = float(score2)
    score3 = float(score3)
    score4 = float(score4)
    score5 = float(score5)

    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    avg_score = sum/3

    if avg_score < 1:
        rating = "Terrible"
    elif avg_score < 2:
        rating = "Bad"
    elif avg_score < 3:
        rating = "OK"
    elif avg_score < 4:
        rating = "Good"
    else:
        rating = "Excellent"

    return rating