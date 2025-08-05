class Character:
    def __init__(self, name, character_class, level=1):
        self.name = name
        self.character_class = character_class
        self.level = level

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")
