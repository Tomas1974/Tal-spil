import random



score_tabel = {
"Plads": [1, 2, 3, 4],
"Navn": ["Tomas", "Sussi", "Signe", "Simon"],
"Score": [3, 2, 1, 1]}




def tjeck_score(ny_score):
    score = score_tabel["Score"]
    navn = score_tabel["Navn"]
            

    for index, scor in enumerate(score):
        if ny_score > scor:
            
            navn = navn[:index] + ["Mikkel"] + navn[index:-1]
            score = score[:index] + [ny_score] + score[index:-1]
            
            score_tabel["Navn"] = navn
            score_tabel["Score"] = score

            return score_tabel


                        




