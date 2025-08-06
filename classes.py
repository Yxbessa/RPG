class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.Xp = 0

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")
