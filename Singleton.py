class GameSettings:
    _instance = None

    def __init__(self):
        if GameSettings._instance is not None:
            raise RuntimeError("Класс GameSettings является одиночкой! Используйте метод get_instance().")
        self.volume = 0
        self.difficulty = ""

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

settings1 = GameSettings.get_instance()
settings2 = GameSettings.get_instance()

print(settings1 is settings2)

settings1.volume = 70
settings1.difficulty = "Hard"

print(settings2.volume)
print(settings2.difficulty)