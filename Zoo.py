class Zoo:
    def __init__(self) -> None:
        self.animals = []

    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()

    def get_all_info(self):
        for animal in self.animals:
            print(f"{animal.name}'s info:")
            animal.special_info()

    def add_animal(self, animal):
        if animal in self.animals:
            print('animal already in zoo...')
            return

        self.animals.append(animal)
        print(f'{animal.name} added to the zoo!')
