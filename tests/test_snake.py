import pytest
from game.snake import move, food_detection, check_collision

def test_move_right():
    snake = [(100,100)]
    direction = (20,0)
    result = move(snake.copy(),direction)
    assert result[0] == (120,100)
    assert len(result) == 1

def test_move_up():
    snake = [(100,100)]
    direction = (0,-20)
    result = move(snake.copy(),direction)
    assert result[0] == (100,80)

def test_food_detection_hit():
    snake = [(200, 200)]
    food = [200, 200]
    speed = 5
    new_food, new_speed = food_detection(food.copy(), speed)
    assert new_speed == speed + 1
    assert new_food != food
    assert len(snake) == 2

def test_food_detection_miss():
    snake = [(200, 200)]
    food = [220, 200]
    speed = 5
    new_food, new_speed = food_detection(food.copy(), speed)
    assert new_speed == speed
    assert new_food == food
    assert len(snake) == 1

def test_collision_wall():
    snake = [(860, 100)]
    assert check_collision(snake) is True

def test_collision_self():
    snake = [(100,100),(120,100), (100,100)]
    assert check_collision(snake) is True

def test_no_collision():
    snake = [(100,100),(80,100),(60,100)]
    assert check_collision(snake) is False

