from Mammal import Mammal


class Whale(Mammal):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name, special_info)

    def feed(self):
        print(f'You fed {self.name} with 2000 kg of plankton.')
