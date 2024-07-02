import turtle
import pandas as pd


# Functions
def answer_check(answer, a_list, b_list):
    """
    Expects an answer parameter as a string to check it in the a_list (list). If true, it returns True, appends value
    to the b_list (list) and removes from the a_list (list) else, it returns False.

    :param answer: Expects it as string.
    :param a_list: Expects an iterable and mutable object such list.
    :param b_list: Expects an iterable and mutable object such list.
    :return: Returns boolean value.
    """
    for values in a_list:
        if answer == values:
            b_list.append(values)
            a_list.remove(answer)
            print("yes")
            return True
    print("no")
    return False


# Screen settings
screen = turtle.Screen()
screen.title("Türkiye Şehir Bulma Oyunu")
image = "türkiye_haritası_çizimi_4.gif"
screen.setup(1200, 600)
screen.addshape(image)
turtle.shape(image)

# Data related setup
data = pd.read_csv("turkey_cities.csv")
all_cities = data.city.to_list()
guessed_cities = []

# Default score variable
score = 0

# Main game loop
while len(guessed_cities) < 81:
    answer_state = screen.textinput(title="Şehirleri Bul!(Çıkmak için 'çıkış' yazınız)",
                                    prompt=f"""             Skor: {score}/81
    Bir şehir ismi giriniz:                                                     """)
    proper_answer = answer_state.title()
    print(proper_answer)

    # Conditions related to the main game logic
    if proper_answer == "Çıkış":
        missing_cities = [city for city in all_cities if city not in guessed_cities]
        new_data = pd.DataFrame(missing_cities)
        new_data.to_csv()
        print(missing_cities)
        # For loop to write missing answers
        for city in missing_cities:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("red")
            remaining_city = data[data.city == city]
            t.goto(int(remaining_city.iloc[0, 1]), int(remaining_city.iloc[0, 2]))
            t.write(remaining_city.city.item())
        # Last score after finishing the game
        t_score = turtle.Turtle()
        t_score.hideturtle()
        t_score.penup()
        t_score.goto(351, -208)
        t_score.write(f"Skor: {score}", font=("Arial", 24, "bold"))
        break

    # If condition to check the answer which is typed by the user
    if answer_check(proper_answer, all_cities, guessed_cities):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == proper_answer]
        print(city_data.iloc[0, 1])
        # t.goto(int(city_data.x), int(city_data.y)) ==> this method is soon to be obsolete for pandas
        t.goto(int(city_data.iloc[0, 1]), int(city_data.iloc[0, 2]))
        t.write(city_data.city.item())
        score += 1
        continue
    else:
        continue

screen.mainloop()
