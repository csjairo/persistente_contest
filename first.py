# Quest�o 01: Processamento de Arquivo de Texto
def setup_question_01():
    file_content = """Ana Silva#Engenharia#8.5
Carlos Souza#Direito#7.2
Fernanda Lima#Computação#9.3
João Pereira#Administração#6.8
Marina Rocha#Arquitetura#8.0
"""
    with open("dados_alunos.txt", "w", encoding="utf-8") as f:
        f.write(file_content)

def run_question_01():
    print("--- Questão 01 ---")
    file_name = "dados_alunos.txt"
    students_data = []
    grades_list = []
    total_grade = 0.0

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines() 

        if not lines:
            print("File is empty.")
            return

        for line in lines:
            parts = line.strip().split('#') 
            if len(parts) == 3:
                student_name = parts[0]
                grade = float(parts[2]) 
                
                students_data.append((student_name, grade))
                grades_list.append(grade)
                total_grade += grade

        average_grade = total_grade / len(grades_list)
        
        max_grade = -float('inf')
        max_grade_student = ""
        min_grade = float('inf')
        min_grade_student = ""

        for name, grade in students_data:
            if grade > max_grade:
                max_grade = grade
                max_grade_student = name
            if grade < min_grade:
                min_grade = grade
                min_grade_student = name

        print(f"Média da turma: {average_grade:.2f}") 
        print(f"Maior nota: {max_grade} ({max_grade_student})") 
        print(f"Menor nota: {min_grade} ({min_grade_student})") 

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("--------------------")

setup_question_01()
run_question_01()
