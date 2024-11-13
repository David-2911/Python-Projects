from random import shuffle

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
bet_amount = list(range(1, 101))


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.balance = balance
        self.hand = []

    def hit(self, new_card):
        self.hand.append(new_card)

    def total_value(self):
        total = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == "Ace")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def place_bet(self):
        while True:
            try:
                self.amt = int(input(f"{self.name}, place a bet (1 - 100): $"))
                if self.amt in bet_amount:
                    if self.amt <= self.balance:
                        self.balance -= self.amt
                        print(
                            f"{self.name} placed a ${self.amt} bet! Current balance: ${self.balance}"
                        )
                        break
                    else:
                        print("Insufficient balance.")
                else:
                    print("Invalid bet amount. Please bet within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def credit(self):
        self.balance += self.amt * 2
        print(f"Amount Won: ${self.amt * 2}. Current balance: ${self.balance}")

    def debit(self):
        print(f"Amount Lost: ${self.amt}. Current balance: ${self.balance}")

    def reset_hand(self):
        self.hand = []


def game_on():
    answer = input("Do you want to play again? (Y/N): ").strip().upper()
    while answer not in ["Y", "N"]:
        answer = input("Invalid input. Please enter Y or N: ").strip().upper()
    return answer == "Y"


def main():
    player = Player("Player", 100)
    dealer = Player("Dealer", 0)
    new_deck = Deck()
    new_deck.shuffle()

    while True:
        player.reset_hand()
        dealer.reset_hand()
        new_deck.shuffle()

        for _ in range(2):
            player.hit(new_deck.deal_one())
            dealer.hit(new_deck.deal_one())

        print("\n----------")
        print("Your Cards:")
        for card in player.hand:
            print(card)
        print("----------\n")

        player.place_bet()

        while True:
            action = input("Do you wish to 'Hit' or 'Stand'? ").strip().capitalize()
            if action == "Hit":
                player.hit(new_deck.deal_one())
                print("\n----------")
                print("Your Cards:")
                for card in player.hand:
                    print(card)
                print("----------\n")
                if player.total_value() > 21:
                    print(f"{player.name} has bust! Game Over")
                    player.debit()
                    break
            elif action == "Stand":
                print(f"{player.name} stands.")
                break
            else:
                print("Invalid input. Please enter 'Hit' or 'Stand'.")

        while dealer.total_value() < 17:
            dealer.hit(new_deck.deal_one())

        print("\n----------")
        print("Dealer's Cards:")
        for card in dealer.hand:
            print(card)
        print("----------\n")

        if dealer.total_value() > 21:
            print(f"{dealer.name} has bust! {player.name} wins!")
            player.credit()
        elif player.total_value() > dealer.total_value():
            print(f"{player.name} wins!")
            player.credit()
        elif player.total_value() < dealer.total_value():
            print(f"{dealer.name} wins!")
            player.debit()
        else:
            print("It's a draw!")

        if not game_on():
            break


if __name__ == "__main__":
    main()
