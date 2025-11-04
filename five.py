from bs4 import BeautifulSoup
import uvicorn

# Questão 05: Análise de HTML com BeautifulSoup, o computador não tinha os módulos instalados e o on-line não funciona.
def setup_question_05():
    html_content = """
<html>
<body>
  <table>
    <tr>
      <th>Jogador 1</th> 
      <th>Jogador 2</th> 
    </tr>
    <tr>
      <td>pedra</td> 
      <td>tesoura</td>
    </tr>
    <tr>
      <td>papel</td>
      <td>pedra</td>
    </tr>
    <tr>
      <td>tesoura</td>
      <td>pedra</td>
    </tr>
    <tr>
      <td>pedra</td>
      <td>pedra</td>
    </tr>
    <tr>
      <td>tesoura</td>
      <td>papel</td>
    </tr>
  </table>
</body>
</html>
"""
    with open("jogadas.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def run_question_05():
    print("--- Questão 05 ---")
    file_name = "jogadas.html"
    
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser") 

        win_conditions = {
            "pedra": "tesoura",
            "tesoura": "papel",
            "papel": "pedra"
        } 
        
        player_1_wins = 0
        
        table_rows = soup.find_all("tr")
        
        for row in table_rows[1:]: 
            columns = row.find_all("td")
            if len(columns) == 2:
                player_1_move = columns[0].text.strip()
                player_2_move = columns[1].text.strip()
                
                if win_conditions.get(player_1_move) == player_2_move: 
                    player_1_wins += 1
                    
        print(f"Vitórias do Jogador 1: {player_1_wins}") 

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("--------------------")

def cleanup_files():
    if os.path.exists("jogadas.html"):
        os.remove("jogadas.html")

if __name__ == "__main__":
    
    setup_question_05()
    run_question_05()
    
    cleanup_files()
