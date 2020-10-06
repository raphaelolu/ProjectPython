from urllib.request import urlopen

import random

import json


class Person:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    Score = 0


class Game:
    players = []

    def __init__(self, players):
        self.players = players
        score = 0
        totalScore = 0
        players = ()
        winner = ""
        intTheLead = ""


        #
        # counter = 0
        # totalScore = 0
        # getName = input("Hello please type your name to begin \n")
        # player1 = Person(getName)
        # while counter != 10:
        #     counter += 1
        #     if counter == 1:
        #         print("Hello " + player1.name() + " Welcome to the python bowling game")
        #         bowl = input("Please roll the ball by pressing and any key on the keypad\n")
        #         firstThrow = random.randint(1, 10)
        #         totalScore += firstThrow
        #         if firstThrow > 5:
        #             print(f"well done you scored a {firstThrow}")
        #         else:
        #             print(f"Unlucky scored a {firstThrow}")
        #         bowl2 = input("Please roll second ball by any key on the keypad\n")
        #         secondThrow = random.randint(1, 10)
        #         totalScore += secondThrow
        #         print(f"well done {player1.name()} you scored a {secondThrow} ")
        #         print(f"your total score is  {totalScore}")
        #         # TemporaryDictionary = [(f"round {counter}", totalScore)]
        #         # player1.Rounds.update(TemporaryDictionary)
        #         roundValue = {'firstThrow': firstThrow, 'secondThrow': secondThrow, 'TotalScore': totalScore}
        #         player1.Rounds[f'round {counter}'] = roundValue
        #     elif counter > 1:
        #         print(f" Welcome to round {counter}")
        #         bowl = input("Please roll ball by typing 1 on your keypad\n")
        #         firstThrow = random.randint(1, 10)
        #         totalScore += firstThrow
        #         if firstThrow > 5:
        #             print(f"well done you scored a {firstThrow}")
        #         else:
        #             print(f"Unlucky scored a {firstThrow}")
        #         bowl2 = input("Please roll second ball by pressing any key on the  keypad\n")
        #         secondThrow = random.randint(1, 10)
        #         print(f"well done  you  scored a {secondThrow}")
        #         totalScore += secondThrow
        #         print(f"your total score so far is {totalScore}")
        #         # TemporaryDictionary = [(f"round {counter}", totalScore)]
        #         # player1.Rounds.update(TemporaryDictionary)
        #         roundValue = {'firstThrow': firstThrow, 'secondThrow': secondThrow, 'TotalScore': totalScore}
        #         player1.Rounds[f'round {counter}'] = roundValue
        # print(f" Congrats {player1.name()} The game is now over, the results from the games were ...")
        # for key, value in player1.Rounds.items():
        #     print(f'{key} => {value}')
        # print(f" The total score for the game is {totalScore}")
        # player1.Score = totalScore
        # jsonObject = json.dumps(player1.Rounds)
        # print(jsonObject)
        # return jsonObject


def playGame():
    print("Hello welcome to the  boring python game ")
    getPlayerOne = input("Player one please type in your name")
    playerOne = Person(getPlayerOne)
    print(f"Hello {playerOne.name()}")
    getPlayerTwoName = input("Player two please type in your name")
    playerTwo = Person(getPlayerTwoName)
    print(f"Hello {playerTwo.name()}")
    players = []
    players.append(playerOne)
    players.append(playerTwo)
    game = Game(players)
    counter = 0
    totalScore = 0
    getName = input("Hello please type your name to begin \n")
    player1 = Person(getName)
    while counter != 10:
        counter += 1
        if counter == 1:
            print("Hello " + player1.name() + " Welcome to the python bowling game")
            bowl = input("Please roll the ball by pressing and any key on the keypad\n")
            firstThrow = random.randint(1, 10)
            totalScore += firstThrow
            if firstThrow > 5:
                print(f"well done you scored a {firstThrow}")
            else:
                print(f"Unlucky scored a {firstThrow}")
            bowl2 = input("Please roll second ball by any key on the keypad\n")
            secondThrow = random.randint(1, 10)
            totalScore += secondThrow
            print(f"well done {player1.name()} you scored a {secondThrow} ")
            print(f"your total score is  {totalScore}")
            # TemporaryDictionary = [(f"round {counter}", totalScore)]
            # player1.Rounds.update(TemporaryDictionary)
            roundValue = {'firstThrow': firstThrow, 'secondThrow': secondThrow, 'TotalScore': totalScore}
            player1.Rounds[f'round {counter}'] = roundValue
        elif counter > 1:
            print(f" Welcome to round {counter}")
            bowl = input("Please roll ball by typing 1 on your keypad\n")
            firstThrow = random.randint(1, 10)
            totalScore += firstThrow
            if firstThrow > 5:
                print(f"well done you scored a {firstThrow}")
            else:
                print(f"Unlucky scored a {firstThrow}")
            bowl2 = input("Please roll second ball by pressing any key on the  keypad\n")
            secondThrow = random.randint(1, 10)
            print(f"well done  you  scored a {secondThrow}")
            totalScore += secondThrow
            print(f"your total score so far is {totalScore}")
            # TemporaryDictionary = [(f"round {counter}", totalScore)]
            # player1.Rounds.update(TemporaryDictionary)
            roundValue = {'firstThrow': firstThrow, 'secondThrow': secondThrow, 'TotalScore': totalScore}
            player1.Rounds[f'round {counter}'] = roundValue
    print(f" Congrats {player1.name()} The game is now over, the results from the games were ...")
    for key, value in player1.Rounds.items():
        print(f'{key} => {value}')
    print(f" The total score for the game is {totalScore}")
    player1.Score = totalScore
    jsonObject = json.dumps(player1.Rounds)
    print(jsonObject)
    return jsonObject


playGame()
