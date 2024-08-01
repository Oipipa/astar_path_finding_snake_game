from node import Node
import heapq
from settings import *

def heuristic(node_position, goal_position):
    return abs(node_position[0] - goal_position[0]) + abs(node_position[1] - goal_position[1])

def a_star(snake, target_position):
    open_list = []
    closed_list = set()
    start_node = Node(snake.body[0])
    goal_node = Node(target_position)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        children = []
        for new_position in [(0, -cell_size), (0, cell_size), (-cell_size, 0), (cell_size, 0)]:
            node_position = (current_node.position[0] + new_position[0], 
                             current_node.position[1] + new_position[1])
            
            if node_position[0] < 0 or node_position[0] >= width or node_position[1] < 0 or node_position[1] >= height:
                continue

            if node_position in closed_list or node_position in [segment for segment in snake.body]:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        for child in children:
            if child.position in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = heuristic(child.position, goal_node.position)
            child.f = child.g + child.h

            if child.position not in [node.position for node in open_list]:
                heapq.heappush(open_list, child)

    return None

def is_path_safe(snake, path):
    snake_body_set = set(snake.body[:-1])
    for step in path[1:]:
        if step in snake_body_set:
            return False
    return True

def find_safe_path(snake, food, tail):
    path_to_food = a_star(snake, food.position)
    if path_to_food and is_path_safe(snake, path_to_food):
        return path_to_food
    
    path_to_tail = a_star(snake, tail)
    if path_to_tail and is_path_safe(snake, path_to_tail):
        return path_to_tail

    return path_to_tail