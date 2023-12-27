import tkinter as tk
import random
import tkinter.messagebox as msgbox

root = tk.Tk()
root.title("贪食蛇游戏")
root.resizable(False, False)

# 设置画布大小
canvas = tk.Canvas(root, width=600, height=400, bg='black')
canvas.pack()

# 初始化蛇的位置
snake = [(300, 200), (290, 200), (280, 200)]
# 设置食物的初始位置
food = (300, 200)

score = 0
score_label = tk.Label(root, text="分数: 0", font=("Arial", 14))
score_label.pack()

# 绘制蛇和食物
def draw_snake():
    for segment in snake:
        canvas.create_rectangle(*segment, segment[0]+10, segment[1]+10, fill='green')

def place_food():
    global food
    food = (random.randint(0, 59)*10, random.randint(0, 39)*10)
    canvas.create_oval(*food, food[0]+10, food[1]+10, fill='red')

direction = 'Right'

def restart_game():
    global snake, direction
    # 重置蛇的位置和方向
    snake = [(300, 200), (290, 200), (280, 200)]
    direction = 'Right'
    score = 0
    score_label.config(text="分数: 0")
    place_food()
    game_loop()

def game_over():
    response = msgbox.askyesno("游戏结束", "再来一局？")
    if response:
        restart_game()
    else:
        root.destroy()

def change_direction(new_dir):
    global direction
    if new_dir == 'Left' and direction != 'Right':
        direction = 'Left'
    elif new_dir == 'Right' and direction != 'Left':
        direction = 'Right'
    elif new_dir == 'Up' and direction != 'Down':
        direction = 'Up'
    elif new_dir == 'Down' and direction != 'Up':
        direction = 'Down'

root.bind("<Left>", lambda event: change_direction('Left'))
root.bind("<Right>", lambda event: change_direction('Right'))
root.bind("<Up>", lambda event: change_direction('Up'))
root.bind("<Down>", lambda event: change_direction('Down'))

def game_loop():

    global score

    # 移动蛇
    x, y = snake[0]
    if direction == 'Left':
        x -= 10
    elif direction == 'Right':
        x += 10
    elif direction == 'Up':
        y -= 10
    elif direction == 'Down':
        y += 10
    new_head = (x, y)

    # 检查蛇是否碰到墙壁或自己
    if x < 0 or x >= 600 or y < 0 or y >= 400 or new_head in snake:
        game_over()
        return

    snake.insert(0, new_head)

    # 检查蛇是否吃到食物
    if new_head == food:
        score += 1
        score_label.config(text=f"分数: {score}")
        place_food()
    else:
        snake.pop()


    canvas.delete(tk.ALL)
    draw_snake()
    canvas.create_oval(*food, food[0]+10, food[1]+10, fill='red')

    root.after(100, game_loop)

place_food()
game_loop()

root.mainloop()
