import turtle
import pandas

FONT = ('Comic Sans MS', 7, 'bold')
LOSE = ('Comic Sans MS', 15, 'bold')
WON = ('Comic Sans MS', 20, 'bold')

screen = turtle.Screen()
screen.title("Sri Lanka District Naming")
image = "sri_lanka_map.gif"
screen.addshape(image)
turtle.shape(image)


# Help to print coodinate where mouse clicked
def get_coordinates_on_map(x, y):
    print(x, y)


turtle.onscreenclick(get_coordinates_on_map)

# Load csv file
district_data = pandas.read_csv("sri_lanka_district.csv")

# Loop controllers
is_complete = False
count = 0
all_ready_on_map = []
error_mess = []


# Error message
def error_message():
    error_message = turtle.Turtle()
    error_message.penup()
    error_message.hideturtle()
    error_message.color("red")
    error_message.goto(x=-180, y=-180)
    error_message.write("District not found", move=False, align='right', font=LOSE)
    error_mess.append(error_message)


def clear_error_message():
    for t in error_mess:
        t.clear()
        t.hideturtle()
    error_mess.clear()


# Winner print message
def winner():
    winner = turtle.Turtle()
    winner.penup()
    winner.hideturtle()
    winner.color("plum")
    winner.goto(x=0, y=220)
    winner.write("Congratulation you know all the districts in Sri Lanka", move=False, align='center', font=WON)


def correct_position_mover(correct_position_data):
    # Convert the row to a list
    correct_position_data = matching_row.values.tolist()
    district = turtle.Turtle()
    district.penup()
    district.hideturtle()
    district.goto(x=correct_position_data[0][1], y=correct_position_data[0][2])
    district.write(f"{correct_position_data[0][0]}", move=False, align='left', font=FONT)
    all_ready_on_map.append(correct_position_data[0][0])


while not is_complete:

    answer_district = screen.textinput(title=f"Guess the district {count}/25", prompt="Answer here: ").title()
    print(answer_district)
    matching_row = district_data[district_data["district"] == answer_district]
    print(matching_row)

    if not matching_row.empty:
        if answer_district in all_ready_on_map:
            print("all ready on the map")
            continue
        correct_position_mover(correct_position_data=matching_row)
        count += 1

        clear_error_message()

        if count == 25:
            winner()
            is_complete = True
    else:
        print("District not found")
        error_message()

screen.mainloop()
screen.exitonclick()
