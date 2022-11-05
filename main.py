from Clownfish import Clownfish
from Goose import Goose
from Lion import Lion
from Owl import Owl
from Whale import Whale
from Zoo import Zoo

zoo = Zoo()

zoo.add_animal(Lion('Lion', 'Simba', '4'))
zoo.add_animal(Lion('Lion', 'Nala', '4'))
zoo.add_animal(Whale('Whale', 'Willy', '12'))
zoo.add_animal(Goose('Goose', 'Akka', '45'))
zoo.add_animal(Owl('Owl', 'Hedwig', '80'))
zoo.add_animal(Clownfish('Fish', 'Nemo', '95'))
zoo.add_animal(Clownfish('Fish', 'Marlin', '120'))


zoo.get_all_info()

for i in range(1, 8):
    print(f'\nday {i}: \n')
    zoo.feed_all_animals()
