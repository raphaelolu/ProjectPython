from urllib.request import urlopen

import random

import json


class Person:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    totalScore = 0

    SpareValue = 0

    WasASpare = 0

    rounds = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    WasAStrike = 0

    StrikeScore = 0

    noSecondThrowBecauseStrike = 0

    gameStats =   {1: [1, 2,   "x",4],
                   2: [{0: 0}, "X",4],
                   3: [{0: 0}, "X",4],
                   4: [{0: 0}, "X",4],
                   5: [{0: 0}, "X",4],
                   6: [{0: 0}, "X",4],
                   7: [{0: 0}, "X",4],
                   8: [{0: 0}, "X",4],
                   9: [{0: 0}, "X",4],
                   10:[{0: 0}, "X",4]
                   }


raph = Person("raph")
print(f" {raph.gameStats[1][0].values()} and {raph.gameStats[1][1]}")


class Game:
    players = []

    def __init__(self, players):
        self.players = players
        score = 0
        totalScore = 0
        players = ()
        winner = ""
        intTheLead = ""


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
    temporaryValueHolder = 0
    counter = 0
    totalScore = 0

    while counter != 10:
        counter += 1
        bowl = input(f" {playerOne.name()} Please roll the ball by pressing any key on the keypad\n")
        firstThrow = random.randint(1, 10)
        if firstThrow == 10:
            print("that is a strike")
            playerOne.gameStats[counter][0][1] = 1
        # if playerOne.wasASpare == 1:
        if  counter != 1 and playerOne.gameStats[counter -1][2] == 1:
        # which would mean theres a spare
            playerOne.gameStats[counter -1][0]
            for key, value in playerOne.rounds.items():
                if key == counter - 1
                    value += firstThrow
                    playerOne.wasASpare = 0
        if firstThrow > 5:
            print(f"well done you scored a {firstThrow}")
        else:
            print(f"Unlucky scored a {firstThrow}")
        for key, value in playerOne.rounds.items():
            if key == counter:
                value += firstThrow
        playerOne.totalScore += firstThrow
        if playerOne.noSecondThrowBecauseStrike != 1:
            if player on is has not got a x
            bowl2 = input(f" {playerOne.name()} Please roll second ball by any key on the keypad\n")
            secondThrow = random.randint(1, 10)
            if secondThrow + firstThrow == 10:
                print(f" well done {playerOne.name()} you have a spare ")
                playerOne.wasASpare = 1
                playerOne.totalScore += secondThrow
            else:
                for key, value in playerOne.rounds.items():
                    if key == counter:
                        value += secondThrow
                        playerOne.totalScore += secondThrow
            if playerOne
            bowl3 = input(f" {playerTwo.name()} Please roll the ball by pressing  any key on the keypad\n")
            firstThrow = random.randint(1, 10)
            totalScore += firstThrow
            if firstThrow > 5:
                print(f"well done {playerTwo.name()} you scored a {firstThrow}")
            else:
                print(f"Unlucky  {playerTwo.name()} you scored a {firstThrow}")
            bowl4 = input(f"Please {playerTwo.name()} roll second ball by pressing any key on the keypad\n")
            secondThrow = random.randint(1, 10)
            if player one that round - 1 has x then add both rounds to round -1
            totalScore += secondThrow
            if secondThrow > 5:
                print(f"well done {playerTwo.name()} you  scored a {secondThrow}")
            else:
                print(f"unlucky {playerTwo.name()} you scored a {secondThrow}")
                print(f"your total score is {totalScore}")
                # TemporaryDictionary = [(f"round {counter}", totalScore)]
                # player1.Rounds.update(TemporaryDictionary)
                # roundValue = {'firstThrow': firstThrow, 'secondThrow': secondThrow, 'TotalScore': totalScore}
                # player1.Rounds[f'round {counter}'] = roundValue
        print(f"Good game {playerOne} and {playerTwo} the game is now over")
        if playerOne.totalScore > playerTwo.totalScore:
            print(f" Congrats {playerOne.name()} The game is now over, you are the winner")
        elif playerTwo.totalScore > playerOne.totalScore:
            print(f"well done {playerTwo} you have won the game")

        for key, value in playerOne.Rounds.items():
            print(f'{key} => {value}')
        print(f" The total score for the game is {totalScore}")
        player1.Score = totalScore
        jsonObject = json.dumps(player1.Rounds)
        print(jsonObject)
        return jsonObject


playGame()
