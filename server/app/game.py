from collections import namedtuple

OpenGame = namedtuple('OpenGame', ['target_player_count', 'current_players'])
OpenGamePlayer = namedtuple('OpenGamePlayer', ['name', 'race'])

class GameManager:

    @staticmethod
    def get_open_games():
        result = []
        current_players = [OpenGamePlayer(name='Test1', race='Undead'), OpenGamePlayer(name='Test2', race='Dwarves')]
        result.append(OpenGame(target_player_count=1, current_players=current_players))
        return result