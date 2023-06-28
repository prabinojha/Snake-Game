# ANNOTATE EVERYTHING AFTER COMPLETING CODE TO UNDERSTAND WHAT IT MEANS
# ASK GPT TO DO IT 

# TODO: Add a restart button on the game over screen to restart the game and show the score on this screen as well
    # Make sure an apple doesn't spawn on the snake's body

from tkinter import *
import random

# These are the game constants that won't be changed

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE =  50 # Size of things in the game such as the snake's body part and food
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)
            
class Food:
    
    # This is the constructor for the food class
    
    def __init__(self):
        
        # x position of the food is randomly generated between 0 and the width of the game
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        
        # y position of the food is randomly generated between 0 and the height of the game
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        
        self.coordinates = [x, y]
        
        # Creating the food on the canvas in a random position
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

def next_turn(snake, food):
    
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y-= SPACE_SIZE
    
    elif direction == "down":
        y+= SPACE_SIZE

    elif direction == "left":   
        x-= SPACE_SIZE

    elif direction == "right":
        x+= SPACE_SIZE
        
    snake.coordinates.insert(0, (x, y))
    
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOUR)  
    
    snake.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
            
            global score
            
            score+=1
            
            label.config(text=("Score:{}".format(score)))
            
            canvas.delete("food") 
            
            food = Food()
    
    else: 
        del snake.coordinates[-1]
        
        canvas.delete(snake.squares[-1])
        
        del snake.squares[-1]
        
    if check_collisions(snake):
        game_over() 
        
    else:
        window.after(SPEED, next_turn, snake, food)
        
def change_direction(new_direction):
    
    global direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
            
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
            
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
            
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    
    # Checking to see if the snake collides with the boundaries of the game
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    # Checking if the snake collides with itself
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text=("Score: {}".format(score)))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Centering the window on the screen when it appears upon starting

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Key bindings for the snake

window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))

# Setting the snake and class 

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()