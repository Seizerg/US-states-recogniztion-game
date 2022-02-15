import pandas
import turtle

screen = turtle.Screen()
screen.tracer(0)
screen.title("The US States")
pic = "blank_states_img.gif"
screen.addshape(pic)
turtle.shape(pic)
num = 0
present_states = []
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
gameIsOn = True
while gameIsOn:
    screen.update()
    input = screen.textinput(title=f"Your Guessed {num}/50 US States",
                             prompt="Enter a US state write on the map").title()
    if input == "Exit":
        missing_states=[]
        for state in state_list:
            if state not in present_states:
                missing_states.append(state)
        new_data= pandas.DataFrame(missing_states)
        new_data.to_csv("missing-states.csv")
        gameIsOn = False
    if input in state_list:
        if input not in present_states:
            present_states.append(input)
            x_cor = int(data[data["state"] == input].x)
            y_cor = int(data[data["state"] == input].y)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(x_cor, y_cor)
            state.write(arg=input, align="center", font=("Courier", 10, "normal"))
            num += 1
    if num > 51:
        gameIsOn = False


