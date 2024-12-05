class DeterministicDie:

    def __init__(self) -> None:
        super().__init__()
        self.times_rolled = 0
        self.value = 1

    def roll(self):
        v = self.value
        self.value += 1
        if self.value > 100:
            self.value = 1
        self.times_rolled += 1
        return v

    def __repr__(self) -> str:
        return f"DeterministicDie(value={self.value}, times_rolled={self.times_rolled})"


class Player:

    def __init__(self, start_pos):
        super().__init__()
        self.pos = start_pos
        self.score = 0

    def take_turn(self, die):
        roll = die.roll() + die.roll() + die.roll()
        self.pos += roll
        while self.pos > 10:
            self.pos -= 10
        self.score += self.pos

    def __repr__(self) -> str:
        return f"Player(pos={self.pos}, score={self.score})"


def play_game(player1, player2, die):
    while True:
        player1.take_turn(die)
        if player1.score >= 1000:
            break
        player2.take_turn(die)
        if player2.score >= 1000:
            break
    losing_score = min(player1.score, player2.score)
    return die.times_rolled * losing_score
