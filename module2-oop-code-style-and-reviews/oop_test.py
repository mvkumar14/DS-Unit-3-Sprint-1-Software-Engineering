from oop_example import Game,Tic

game1 = Game()
print(game1.player1)
print(game1.rounds)

game1.add_round()
for _ in range(3):
    print(game1.winner())
