# Questões 03 e 04: Precisa separar o client do server para testar localmente, ou pode avaliar apenas com o código.

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

student_data = {
    'name': [],
    'grade': []
}
database_df = pd.DataFrame(student_data)
database_df = database_df.set_index('name')

@app.post("/alunos")
def adicionar_aluno(nome: str, nota: float):
    global database_df
    if nome in database_df.index:
        database_df.loc[nome, 'grade'] = nota
        return {"message": "Nota atualizada."}
    else:
        new_student_data = pd.DataFrame({'grade': [nota]}, index=[nome])
        database_df = pd.concat([database_df, new_student_data])
        return {"message": "Aluno adicionado."}

@app.get("/alunos/{nome}")
def obter_nota(nome: str):
    if nome in database_df.index:
        grade = database_df.loc[nome, 'grade'].item()
        return {"nome": nome, "nota": grade}
    else:
        raise HTTPException(status_code=404, detail="Aluno não foi registrado.")

@app.get("/alunos")
def listar_alunos():
    global database_df
    df_reset = database_df.reset_index()
    df_reset.rename(columns={'index': 'name'}, inplace=True)
    result_list = df_reset.to_dict(orient="records")
    return result_list

client = TestClient(app)

def test_api():
    print(client.post("/alunos", params={"nome": "João", "nota": 8.5}).json())
    print(client.post("/alunos", params={"nome": "Maria", "nota": 9.0}).json())
    print(client.get("/alunos/João").json())
    print(client.get("/alunos").json())

if __name__ == "__main__":
    test_api()
