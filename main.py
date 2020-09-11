import turtle
import math


def drawBoard():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100-200*i)
        drawer.pendown()
        drawer.forward(600)
    drawer.right(90)
    for i in range(2):
        drawer.penup()
        drawer.goto(-100+200*i, 300)
        drawer.pendown()
        drawer.forward(600)
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j*200, 275 - i * 200)
            drawer.pendown()

            drawer.write(num, font=("Arial", 12))
            num += 1
    screen.update()


def drawX(x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)

    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    screen.update()


def checkDraw():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count += 1
    if count > 3:
        return True
    else:
        return False


def drawO(x, y):
    drawer.penup()
    drawer.goto(x, y+75)
    drawer.pendown()

    drawer.setheading(0)

    for i in range(180):
        drawer.forward((150*math.pi)/180)
        drawer.right(2)

    screen.update()


def checkWon(l):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == l:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == l:
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == l:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == l:
        return True
    return False


def addO():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 - 200*i)
                    return
                board[i][j] = " "
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if (checkWon("x")):
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 - 200*i)
                    return
                board[i][j] = " "
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200*i)
                return
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] == "o"
                drawO(-200 + 200 * j, 200 - 200*i)
                return


def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i+1))


def deactivate():
    for i in range(9):
        screen.onkey(None, str(i+1))


def addX(row, col):
    if (board[row][col] == " "):
        drawX(-200 + 200 * col, 200 - 200 * row)
        board[row][col] = "x"
        if checkWon("x"):
            announcer.goto(-97, 330)
            announcer.write("You Won!", font=("Arial", 36))
            screen.update()
            deactivate()
        else:
            addO()
            if checkWon("o"):
                announcer.goto(-97, 330)
                announcer.write("You Lost!", font=("Arial", 36))
                screen.update()
                deactivate()
            elif checkDraw():
                announcer.goto(-97, 330)
                announcer.write("It is a Tie", font=("Arial", 36))
                screen.update()
                deactivate()


def sq_1():
    addX(0, 0)


def sq_2():
    addX(0, 1)


def sq_3():
    addX(0, 2)


def sq_4():
    addX(1, 0)


def sq_5():
    addX(1, 1)


def sq_6():
    addX(1, 2)


def sq_7():
    addX(2, 0)


def sq_8():
    addX(2, 1)


def sq_9():
    addX(2, 2)


functions = [sq_1, sq_2, sq_3, sq_4, sq_5, sq_6, sq_7, sq_8, sq_9]
drawer = turtle.Turtle()
announcer = turtle.Turtle()
root = turtle.Screen()._root
root.iconbitmap("icon.ico")
announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

drawer.pensize(10)
drawer.ht()
screen = turtle.Screen()
screen.tracer(0)
screen.title("Tic Tac Toe")
drawBoard()

board = [[" " for i in range(3)] for j in range(3)]


activate(functions)
screen.listen()

turtle.done()
