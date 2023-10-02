import turtle as t

def square():
    t.penup()

    for i in range(4):
        t.pendown()
        t.forward(90)
        t.left(90)
        t.penup()

def main():
    square()        

main()