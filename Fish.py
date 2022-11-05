from Animal import Animal


class Fish(Animal):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name)
        self.reachable_depth = special_info

    def special_info(self):
        print(f'''
This is an animal of type {self.animal_type}. 
the lowest depth they can reach is {self.reachable_depth} meters.''')
