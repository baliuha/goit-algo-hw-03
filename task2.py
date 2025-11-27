from turtle import Turtle, Screen


def koch_side(t: Turtle, depth: int) -> None:
    if depth == 0:
        t.forward(25)
    else:
        for angle in [60, -120, 60, 0]:
            koch_side(t, depth - 1)
            t.left(angle)


def koch_snowflake(depth: int) -> None:
    screen = Screen()
    t = Turtle()
    t.color("magenta")
    t.speed(0)
    t.penup()
    t.goto(-350, 100)
    t.pendown()

    for _ in range(3):
        koch_side(t, depth)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


def main():
    try:
        depth = int(input("Enter recursion level (0 - 6): "))
        if not (0 <= depth <= 6):
            raise ValueError("Depth must be in a range of 0 - 6")
    except ValueError as e:
        print("Invalid input:", e)
        exit(1)
    koch_snowflake(depth)


if __name__ == "__main__":
    main()
