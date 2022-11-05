from Animal import Animal


class Bird(Animal):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name)
        self.wings_span = special_info

    def special_info(self):
        print(f'''
This is an animal of type {self.animal_type}. 
the wing-span is {self.wings_span} cm.''')
