import random

random.seed()

class Player:
    score = 0

    def __init__(self, name):
        self.name = name

    def startFight(self, otherPlayer, limit = 100):
        while self.score < limit and otherPlayer.score < limit:
            self.score += random.randint(0, 20)
            otherPlayer.startFight(self)


def main():
    Anna = Player("anna")
    Bev = Player("bev")
    Anna.startFight(Bev)
    print("Annas Score: ", Anna.score)
    print("Bevs Score: ", Bev.score)


if __name__ == "__main__":
    main()
