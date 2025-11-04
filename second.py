# Questão 02: Trabalhando com Pandas, verificar se Pandas está importado no ambiente virtual.

import pandas as pd

def run_question_02():
    print("---- Questão 02 ----")
    associates_data = {
        "Luca Brasi": 12000,
        "Peter Clemenza": 17500,
        "Sal Tessio": 14300,
        "Tom Hagen": 16000,
        "Michael Corleone": 19500
    } 
    
    names = list(associates_data.keys())
    revenues = list(associates_data.values())

    weekly_revenues = pd.Series(revenues, index=names)

    total_revenue = weekly_revenues.sum() 
    average_revenue = weekly_revenues.mean() 
    top_associate = weekly_revenues.idxmax() 

    print(f"Total arrecadado na semana: {total_revenue}") 
    print(f"Média das receitas: {average_revenue}") 
    print(f"Associado que mais arrecadou: {top_associate}") 

    print("\nAssociados acima da média:")
    above_average = weekly_revenues[weekly_revenues > average_revenue] 
    print(above_average)
    print("--------------------")

run_question_02()
