#game window
# loop
from turtle import Screen
from snake import Snake
import time
win=Screen()
win.setup(width=800,height=800)
win.bgcolor("black")
win.title("Snake Game")
win.tracer(0)
sam=Snake()# الاوبجيكت اتوماتيك بقا عنده ليستة اسمها تيرتلز
#my_snake.create_snake() هنا انا بدل مانعملها في الكلاس حطيتها في الكونستركتور... فا نادينا على الميثود جوا الكلاس 

game_on=True
while game_on:
    sam.move()
    win.update()
    time.sleep(0.1)
    win.listen()#بتخلي البرنامج يستمع لاي حاجة بتحصل في الشاشة زي الكيبورد والماوس
    win.onkey(sam.up, "w")# Up لاحظ اول حرف من الكلمة اللي عايزينها في الكيبورد لازم يكون كبير
    win.onkey(sam.down, "s")# Down لاحظ اننا لم نضع اقواس الميثود لو جوا اريجيومنت   
    win.onkey(sam.left, "a")# Left
    win.onkey(sam.right, "d")# Right
win.exitonclick()