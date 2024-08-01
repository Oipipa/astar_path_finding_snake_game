from settings import * 

class Snake:
    def __init__(self):
        self.body = [(width // 2, height // 2)]
        self.direction = pygame.K_RIGHT
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            new_head = (head_x, head_y - cell_size)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + cell_size)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - cell_size, head_y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (head_x + cell_size, head_y)
        
        self.body.insert(0, new_head)

        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        self.growing = True

    def change_direction(self, direction):
        opposite_directions = {pygame.K_UP: pygame.K_DOWN, pygame.K_DOWN: pygame.K_UP, 
                               pygame.K_LEFT: pygame.K_RIGHT, pygame.K_RIGHT: pygame.K_LEFT}
        if direction != opposite_directions.get(self.direction):
            self.direction = direction

    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, green, (*segment, cell_size, cell_size))