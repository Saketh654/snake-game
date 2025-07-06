import pygame, sys, random, socket, time

pygame.init()
WIDTH, HEIGHT = (840,640)
CELL_SIZE = 20
WHITE, GREEN, RED = (255,255,255), (0,255,0), (255,0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (CELL_SIZE, 0)
food=[200,200]
speed = 5

def send_metric(metric_name,value):
    try:
        timestamp = int(time.time())
        message = f"{metric_name} {value} {timestamp}\n"
        sock = socket.socket()
        sock.connect(('localhost',2003))
        sock.sendall(message.encode())
        sock.close()
    except:
        pass

def move(snake, direction):
    head_x, head_y = snake[0]
    dx, dy = direction
    head = (head_x + dx,  head_y + dy)
    snake.insert(0, head)
    snake.pop()
    return snake

def check_collision(snake):
    return snake[0] in snake[1:] or not (0 <= snake[0][0] < WIDTH and 0 <= snake[0][1] <HEIGHT)
    
def food_detection(food,speed):
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        pos1=random.randint(0,600)
        pos2=random.randint(0,600)
        pos1=pos1-(pos1%20)
        pos2=pos2-(pos2%20)
        food = [pos1,pos2]
        snake.append((900,900))
        speed+=1
        send_metric("snakegame.speed", speed)
        send_metric("snakegame.score", len(snake))
    return food,speed


def draw():
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0,20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0,-20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20,0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20,0):
                direction = (20, 0)
            

    snake = move(snake, direction)
    food,speed= food_detection(food,speed)    
    if check_collision(snake):
        print("Game Over")
        break
    
    draw()
    clock.tick(speed)