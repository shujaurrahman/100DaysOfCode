class Animal:
    def __init__(self) -> None:
        self.num_eyes=2
    
    def breathe(self):
        print("Inhale,Exale.")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in the water")

tim=Fish()
tim.swim()
tim.breathe()
print(tim.num_eyes) 
