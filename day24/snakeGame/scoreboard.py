from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        try:
            with open("day24/snakeGame/data.txt") as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day24/snakeGame/data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.updateScoreboard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", align="center", font=("Arial", 24, "normal"))

    def tail_msg(self):
        self.goto(30, 30)
        self.write(f"Head collided with body! BOOM.", align="center", font=("Arial", 24, "normal"))
