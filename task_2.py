import turtle


def koch_curve(t, size, n):
    """Draw a Koch curve."""
    angels = [60, -120, 60, 0]
    # Basic case
    if n == 0:
        t.forward(size)
    else:
        for a in angels:
            koch_curve(t, size, n - 1)
            t.left(a)


def draw_snowflake(size, n, t):
    """Draw a snowflake"""
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    t.speed(0)
    for _ in range(3):
        koch_curve(t, size, n)
        t.right(120)


def main():
    screen = turtle.Screen()
    turtle.bgcolor("lightblue")
    screen.title("Koch Snowflake")

    t = turtle.Turtle()
    t.color("blue")
    try:
        level = int(screen.textinput("Recursion Level:", "Enter recursion level:"))
        side = 30
        draw_snowflake(side, level, t)
        screen.mainloop()
    except ValueError:
        print("Invalid input. Please provide integer value.")


main()
