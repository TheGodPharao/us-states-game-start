import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# how to get coordinates of mouse click on a gif
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
# in this example, we don't need this code as the coordinates are already in the csv file

# TODO: make sure the title is Dynamic counting correct states entries in the form of 0/50
answer_state = screen.textinput(title="Guess The State", prompt="Type the correct State's name and "
                                                                "it'll appear on the screen")

data = pandas.read_csv("50_states.csv")
print(data)