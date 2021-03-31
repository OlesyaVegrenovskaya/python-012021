class Polozka:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}."


class Film(Polozka):
    def __init__(self, name, genre, length ):
        super().__init__(name, genre)
        self.length = length
    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}. Delká filmů je {self.length} minut."


class Serial(Polozka):
    def __init__(self, name, genre, number_of_episodes, episode_length):
        super().__init__(name, genre)
        self.number_of_episodes = number_of_episodes
        self.episode_length = episode_length
    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}. Série se skládá z {self.number_of_episodes} epizod. Delká epizodu trvá {self.episode_length} minut. "

VratneLahve = Film("Vratné lahve", "komedie", 99)
Chernobyl = Serial("Černobyl", "drama", 5, 50)

print(VratneLahve.get_info())
print(Chernobyl.get_info())
