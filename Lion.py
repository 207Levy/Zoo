
from Mammal import Mammal


class Lion(Mammal):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name, special_info)

    def feed(self):
        print(f'You fed {self.name} with 6 kilos of meat.')
