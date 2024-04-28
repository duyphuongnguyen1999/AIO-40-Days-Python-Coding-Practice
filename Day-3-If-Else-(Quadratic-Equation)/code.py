def quadratic_equation(a, b, c):
    if a == 0:
        assert b != -0, "b must not zero"
        x = -c / b
        print(f"{x = }")
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            print("The equation has no solution")
        elif delta == 0:
            x1 = -b / (2 * a)
            x2 = -b / (2 * a)
            print(f"{x1 = }\n{x2 = }")
        else:
            x1 = (-b - delta**0.5) / (2 * a)
            x2 = (-b + delta**0.5) / (2 * a)
            print(f"{x1 = }\n{x2 = }")


def main():
    quadratic_equation(a=2, b=6, c=4)
    quadratic_equation(a=1, b=2, c=1)
    quadratic_equation(a=4, b=6, c=3)


if __name__ == "__main__":
    main()
