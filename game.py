import json

class Game:

    # O time a, sempre é o mandante do jogo
    # Time b sempre é o visitante
    # Se o valor de result for 0, então houve empate
    # Se o valor de result for 1, então o time da casa ganhou
    # Se o valor de result for -1, então o time visitante ganhou
    def __init__(self, team_a, team_b, result, competition):
        self.team_a = team_a
        self.team_b = team_b
        self.result = result
        self.competition = competition

        # Salva o resultado da partida
        json_game = {"team_a": team_a, "team_b": team_b, "result": result, "competition": competition};
        file_name = 'game-' + competition + '.json'
        with open(file_name, 'w') as f:
            json.dump(json_game, f)
