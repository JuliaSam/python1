import random

minimum_number = 1
maximum_number = 90
card_line_length = 9
card_line_power = 5
card_lines_number = 3

class GameCardField:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def empty_field():
        return GameCardField("_")

    @staticmethod
    def crossed_out_field():
        return GameCardField("*")

    def is_empty(self):
        return self.value == GameCardField.empty_field().value

    def is_crossed_out(self):
        return self.value == GameCardField.crossed_out_field().value

    def is_number(self):
        return (not self.is_empty()) and (not self.is_crossed_out())


class GameCard:
    def __init__(self, lines):
        self.lines = lines

    def cross_out_number(self, number):
        for line in self.lines:
            for i in range(len(line)):
                if line[i].is_number() and line[i].value == number:
                    line[i] = GameCardField.crossed_out_field()
                    return True
        return False

    def has_uncrossed_out_numbers(self):
        for line in self.lines:
            for field in line:
                if field.is_number():
                    return True
        return False

    def __str__(self):
        stringify = ""
        for line in self.lines:
            for field in line:
                if field.is_number():
                    stringify += str(field.value) + '\t'
                else:
                    stringify += field.value + '\t'
            stringify += '\n'

        return stringify


class GameCardGenerator:
    @staticmethod
    def generate_random_card():
        card_power = card_line_power * card_lines_number
        try:
            numbers = random.sample(range(minimum_number, maximum_number + 1), card_power)
        except ValueError:
            return None

        lines_numbers = [numbers[i: (i + card_line_power)] for i in range(0, len(numbers), card_line_power)]
        for line_numbers in lines_numbers:
            line_numbers.sort(reverse = True)

        card_lines = []
        for line_index in range(card_lines_number):
            line = []
            try:
                line_numbers_positions = random.sample(range(card_line_length), card_line_power)
            except ValueError:
                return None

            for line_number_index in range(card_line_length):
                if line_number_index in line_numbers_positions:
                    number = lines_numbers[line_index].pop()
                    line.append(GameCardField(number))
                else:
                    line.append(GameCardField.empty_field())

            card_lines.append(line)

        return GameCard(card_lines)


class Game:
    def __init__(self):
        self.human_card = GameCardGenerator.generate_random_card()
        self.computer_card = GameCardGenerator.generate_random_card()

    def play(self):
        print("Let's begin the game!")
        bag = [i for i in range(minimum_number, maximum_number + 1)]
        random.shuffle(bag)

        while len(bag) > 0:
            barrel = bag.pop()
            print("\nNew barrel: " + str(barrel) + " (" + str(len(bag)) + " left)")
            print("----------- YOUR CARD ------------")
            print(self.human_card)
            print("----------------------------------")
            print("-----------  II CARD  ------------")
            print(self.computer_card)
            print("----------------------------------")

            user_answer = input("Do you want to cross out the number? (y / otherwise)")
            if user_answer == 'y' and not self.human_card.cross_out_number(barrel):
                print("You tried to cross out the number that doesn't exist on your card.")
                print("The game is over! You lose!")
                return
            elif self.human_card.cross_out_number(barrel):
                print("You missed the number on your card.")
                print("The game is over! You lose!")
                return

            self.computer_card.cross_out_number(barrel)

            human_not_filled = self.human_card.has_uncrossed_out_numbers()
            computer_not_filled = self.computer_card.has_uncrossed_out_numbers()

            if not human_not_filled and not computer_not_filled:
                print("The game is over! It's a draw.")
                return
            elif not human_not_filled:
                print("The game is over! You win!")
                return
            elif not computer_not_filled:
                print("The game is over! You lose!")
                return


game = Game()
game.play()
