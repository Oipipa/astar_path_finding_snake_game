from settings import * 
import random 

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                random.randint(0, (height - cell_size) // cell_size) * cell_size)

    def draw(self):
        pygame.draw.rect(screen, red, (*self.position, cell_size, cell_size))