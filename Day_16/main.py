# from turtle import Screen, Turtle

# amar = Turtle()

# print(amar)
# amar.shape("turtle")
# amar.color("DarkSeaGreen4")
# amar.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electirc"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
  
# table.align = "l"
# table.align = "r"

print(table)
