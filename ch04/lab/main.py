import random
import math
import pygame

pygame.init
#Part A
SCREEN_SIZE = [250, 250]
global WINDOW
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (0, 250, 250)
BLUE = (0, 0, 255)
RED_RECT = (0, 0, 125, 250)
BLUE_RECT = (125, 0, 250, 250)
MIDDLE = 125
team_chosen = True
PLAYERS = 2
WINDOW = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
win_prediction = "placeholder"
win_prediction = win_prediction.lower()


def dartboard():
    WINDOW.fill(WHITE)
    pygame.draw.circle(WINDOW, GREEN, (125, 125), 125, 0)

    pygame.draw.line(WINDOW, BLACK, (0, 125), (250, 125), 1)
    pygame.draw.line(WINDOW, BLACK, (125, 0), (125, 250), 1)


# Part B
#PART B
def dart_game_PartB(turns):
    for i in range(turns + 1):
        if i > 0:
            dartboard()
            pygame.draw.circle(WINDOW, color1, dart1, 5, 0)
            pygame.display.flip()
            pygame.time.wait(500)
            pygame.draw.circle(WINDOW, color2, dart2, 5, 0)
            pygame.display.flip()
            pygame.time.wait(500)
        dart1 = []
        dart2 = []
        color1 = RED
        color2 = BLUE
        for i in range(PLAYERS):
            x = random.randrange(0, 251)
            y = random.randrange(0, 251)
            distance_from_center = (math.hypot(abs(x - MIDDLE),
                                               abs(y - MIDDLE)))
            is_in_circle = (distance_from_center <= MIDDLE)
            if i == 0:
                if is_in_circle == False:
                    color1 = DARK_RED
                dart1.append(x)
                dart1.append(y)
            else:
                if is_in_circle == False:
                    color2 = PURPLE
                dart2.append(x)
                dart2.append(y)


dart_game_PartB(10)
print("who do you think will win: Red or Blue?")
# part C
while team_chosen == True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    BLUE_BUTTON = pygame.draw.rect(WINDOW, BLUE, BLUE_RECT)
    RED_BUTTON = pygame.draw.rect(WINDOW, RED, RED_RECT)
    pygame.display.flip()
    pygame.time.wait(500)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BLUE_BUTTON.collidepoint(mouse_x, mouse_y):
                win_prediction = "blue"
                print("you chose", win_prediction)
                team_chosen = False
            else:
                win_prediction = "red"
                print("you chose", win_prediction)
                team_chosen = False


def dart_game(turns, time):
    player1_score = 0
    player2_score = 0
    dartboard()
    for i in range(turns):
        # print("round", i + 1)
        dart1 = []
        dart2 = []
        color1 = RED
        color2 = BLUE
        redhit = False
        bluehit = False
        for i in range(PLAYERS):
            x = random.randrange(0, 251)
            y = random.randrange(0, 251)
            distance_from_center = (math.hypot(abs(x - MIDDLE),
                                               abs(y - MIDDLE)))
            is_in_circle = (distance_from_center <= MIDDLE)
            if i == 0:
                if is_in_circle == False:
                    color1 = DARK_RED
                else:
                    player1_score += 1
                    # redhit = True
                dart1.append(x)
                dart1.append(y)
            else:
                if is_in_circle == False:
                    color2 = PURPLE
                else:
                    player2_score += 1
                    # bluehit = True
                dart2.append(x)
                dart2.append(y)
                if i > 0:
                    # print("red", "shoots")
                    pygame.draw.circle(WINDOW, color1, dart1, 5, 0)
                    pygame.display.flip()
                    pygame.time.wait(time)
                    # if redhit == True:
                    #   # print("Hit!")
                    #   print("red has", player1_score, "points")
                    # else:
                    #   # print("Miss")
                    #   print("red has", player1_score, "points")

                    # print("blue", "shoots")
                    pygame.draw.circle(WINDOW, color2, dart2, 5, 0)
                    pygame.display.flip()
                    pygame.time.wait(time)
                    # if bluehit == True:
                    #   # print("Hit!")
                    #   # print("blue has", player2_score, "points")
                    # else:
                    #   # print("Miss")
                    #   # print("blue has", player2_score, "points")
    print("Final Score:")
    print("red had", player1_score, "points")
    print("blue had", player2_score, "points")
    if player1_score > player2_score:
        print("RED WINS!")
        return ("red")
    elif player1_score == player2_score:
        print("What a game,but its a tie")
        return ("tie")
    else:
        print("BLUE WINS")
        return ("blue")


dartboard()
winner = dart_game(10, 500)
if (win_prediction == "red") or (win_prediction == "blue"):
    if winner == win_prediction:
        print("wow how did you know", winner, "would win?")
    elif winner == "tie":
        print("who would have guessed tie anyway")
    else:
        print("it was a good guess but you are wrong")
else:
    print("your prediction could not be understood. sorry")
