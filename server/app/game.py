import model

class GameManager:

    @staticmethod
    def get_open_games():
        repo = model.Repository.get_instance()
        result = repo.OpenGame.m.find().all()
        return result