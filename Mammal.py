from Animal import Animal


class Mammal(Animal):
    def __init__(self, animal_type, name, special_info) -> None:
        super().__init__(animal_type, name)
        self.pregnancy_time = special_info

    def special_info(self):
        print(f'''
This is an animal of type {self.animal_type}. 
the duration of the pregnancy is {self.pregnancy_time} months.''')
