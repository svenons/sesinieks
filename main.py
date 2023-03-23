import turtle
import random
total_width = 3 * 100 + 2 * 20
total_height = 2 * 100 + 20

class Six():
    def __init__(self):
        # noteikumi
        NUM_SQUARES = 6
        NUM_FIGURES_EACH = 4

        # Turtle settings
        turtle.setup(800, 600)
        turtle.bgcolor("white")
        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0)

        def draw_square(x, y, size, color):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(size)
                turtle.left(90)
            turtle.end_fill()

        def draw_number(x, y, number):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color("black")
            turtle.write(number, align="center", font=("Arial", 24, "normal"))

        def draw_colored_squares():
            colors = ["blue", "green", "orange", "yellow", "red", "purple"]
            square_size = 100
            margin = 20
            num_squares_per_row = 3

            for i, color in enumerate(colors):
                row = i // num_squares_per_row
                col = i % num_squares_per_row
                x = col * (square_size + margin) - total_width // 2
                y = -row * (square_size + margin) + total_height // 2

                draw_square(x, y, square_size, color)
                draw_number(x + square_size // 2, y + square_size // 2 - 20, i + 1)

        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0)

        draw_colored_squares()

        num_players = int(turtle.numinput("Six", "Number of players (2-6):", default=2, minval=2, maxval=6))
        player_names = []
        for i in range(1, num_players+1):
            player_names.append(turtle.textinput("Six", f"Player {i} name:"))

        def draw_player_names(player_names, player_figures):
            num_players = len(player_names)
            font_size = 20
            padding = 50
            figure_radius = 10
            figure_spacing = 5
            figures_per_row = 2

            for i, name in enumerate(player_names):
                turtle.penup()

                if num_players == 2:
                    turtle.goto((-1)**i * (total_width // 2 + padding), 0)
                elif num_players == 3:
                    turtle.goto((-1)**i * (total_width // 2 + padding), (-1)**(i // 2) * (total_height // 2))
                elif num_players == 4:
                    turtle.goto((-1)**(i // 2) * (total_width // 2 + padding), (-1)**i * (total_height // 2))
                elif num_players == 5:
                    if i < 4:
                        turtle.goto((-1)**(i // 2) * (total_width // 2 + padding), (-1)**i * (total_height // 2))
                    else:
                        turtle.goto(-total_width // 2 - padding, 0)
                elif num_players == 6:
                    turtle.goto((-1)**(i // 3) * (total_width // 2 + padding), (-1)**i * (total_height // 2))

                turtle.pendown()
                turtle.color(player_figures[f'{name}color'])
                turtle.write(name[:10], align="center", font=("Arial", font_size, "normal"))

                num_squares = player_figures[name]
                for j in range(0, num_squares):
                    turtle.penup()
                    x_offset = ((j % figures_per_row) - 0.5 * (figures_per_row - 1)) * (figure_radius * 2 + figure_spacing)
                    y_offset = -font_size - figure_radius - (j // figures_per_row) * (figure_radius * 2 + figure_spacing)
                    turtle.goto(turtle.xcor() + x_offset, turtle.ycor() + y_offset)
                    turtle.pendown()
                    turtle.color(player_figures[f'{name}color'])
                    turtle.begin_fill()
                    turtle.circle(figure_radius)
                    turtle.end_fill()


        player_figures = {}
        color_list = ["black", "gray", "brown", "cyan", "darkblue", "darkgreen"]
        for name in player_names:
            player_figures[name] = 4
            color = random.choice(color_list)
            player_figures[f'{name}color'] = color
            color_list.remove(color)
        draw_player_names(player_names, player_figures)

        input()

        '''
        Vēlāk spēles gaitā vajazdētu šādi:

        player_figures[player_names[SP. SKAITLIS]] = 2
        draw_player_names(player_names, player_figures)
        '''

if __name__ == "__main__":
    game = Six()

