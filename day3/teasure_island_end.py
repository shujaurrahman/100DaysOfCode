# final project for Day 3
print("Welcom to Treasure Island.")
print("Your mission is to find the treasure.")
case1=input("Where do you wanna go? left or right : ")
case1=case1.lower()
if case1=='left':
    print("Where do you wanna do? swim or wait: ")
    case2=input()
    case2=case2.lower()
    if case2=='wait':
        case3=input("Which door? red , blue or yellow: ")
        case3=case3.lower()
        if case3=='yellow':
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")