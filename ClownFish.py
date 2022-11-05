
from Fish import Fish


class Clownfish(Fish):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name, special_info)

    def feed(self):
        print(f'You fed {self.name} 3 grams of algae.')
