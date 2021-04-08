class Polozka:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}."


class Film(Polozka):
    def __init__(self, name, genre, length):
        super().__init__(name, genre)
        self.length = length

    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}. Delká filmů je {self.length} minut."

    def get_celkova_delka(self):
        return self.length


class Serial(Polozka):
    def __init__(self, name, genre, number_of_episodes, episode_length):
        super().__init__(name, genre)
        self.number_of_episodes = number_of_episodes
        self.episode_length = episode_length

    def get_info(self):
        return f"Žanr filmů {self.name} je {self.genre}. Série se skládá z {self.number_of_episodes} epizod. Delká epizodu trvá {self.episode_length} minut. "

    def get_celkova_delka(self):
        self.all_length = self.episode_length * self.number_of_episodes
        return self.all_length

class Uzivatel:
     def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0

     def pripocti_zhlednuti(self, delka):
        self.delka_sledovani += delka

VratneLahve = Film("Vratné lahve", "komedie", 99)
Chernobyl = Serial("Černobyl", "drama", 5, 50)
Marek = Uzivatel("Marek")
print(VratneLahve.get_info())
print(Chernobyl.get_info())
Marek.pripocti_zhlednuti(Chernobyl.get_celkova_delka())
Marek.pripocti_zhlednuti(VratneLahve.get_celkova_delka())
print(f"{Marek.uzivatelske_jmeno}  viděl {Marek.delka_sledovani} minut záznamu.")
