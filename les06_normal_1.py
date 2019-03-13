# normal 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП

# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = str(name)
        self.health = int(health)
        self.damage = int(damage)
        self.armor = float(armor)
        print(name + ' родился с ' + str(health) + ' жизни, ' + str(damage) + ' урона, ' + str(armor) + ' защиты')


class Player(Person):
    def __init__(self, name):
        super().__init__(name, random.randrange(80, 120), random.randrange(15, 25), 1.2)
        self.level = 1

    def level_up(self):
        self.armor += 0.05
        self.level += 1


class Enemy(Person):
    def __init__(self, name):
        super().__init__(name, random.randrange(25, 35), random.randrange(13, 20), 1)


class Game:
    def __init__(self):
        self.player = Player(input("Введите имя игрока: "))
        self.enemies = self._generate_enemy(4)

    def _generate_enemy(self, number):
        return [Enemy("Enemy #" + str(i)) for i in range(0, number)]

    def _calc_damage(self, atacker, defender):
        return atacker.damage // defender.armor

    def _is_game_finished(self):
        return self.player.health <= 0 or len(self.enemies) == 0

    def simulate(self):
        player_turn = random.randrange(0, 1) == 0
        print("Первым ходит " + ("Игрок" if player_turn else "Враг"))

        while not self._is_game_finished():
            anEnemy = self.enemies[random.randrange(0, len(self.enemies))]
            if player_turn:
                damage_value = self._calc_damage(self.player, anEnemy)
                print(self.player.name + " нанёс " + str(damage_value) + " урона врагу " + anEnemy.name)
                if anEnemy.health <= damage_value:
                    self.enemies.remove(anEnemy)
                    print("Враг " + anEnemy.name + " убит")
                    self.player.level_up()
                else:
                    anEnemy.health -= damage_value
                    print("У врага " + anEnemy.name + " осталось " + str(anEnemy.health) + " здоровья")
            else:
                damage_value = self._calc_damage(anEnemy, self.player)
                print("Враг " + anEnemy.name + " нанёс " + str(damage_value) + " урона игроку " + self.player.name)
                self.player.health -= damage_value
                if self.player.health <= 0:
                    print("Игрок " + self.player.name + " не оправдал наших ожиданий. Это наши проблемы.")
                else:
                    print("У игрока " + self.player.name + " осталось " + str(self.player.health) + " здоровья")
            print("---------------------")
            player_turn = not player_turn

        print("\nКонец игры.")


game = Game()
game.simulate()