class Gun:

    def __init__(self, name, demage, bullet):
        self.name = name
        self.demage = demage
        self.bullet = bullet

    # __str__ 是在打印实例的时候执行的
    def __str__(self):
        return '{0} demage {1} bullet {2}'.format(self.name, self.demage, self.bullet)

    def add_bullet(self, bullet_num):
        self.bullet += bullet_num

    def shoot(self, enemy, demage):
        if self.bullet <= 0:
            print('The gun have no bullet, auto add')
            self.add_bullet()
        self.bullet -= 1
        enemy.hp -= demage
        if enemy.hp <= 0:
            print('enemy %s is died' % enemy.name)
            return
        print('{0} demage is {1}, {2} left blood is {3}'.format(
            self.name, demage, enemy.name, enemy.hp))


class Player:

    def __init__(self, name, hp, demage):
        self.name = name
        self.hp = hp
        self.demage = demage
        self.gun = None

    def fire(self, aim):
        if self.gun is None:
            print('You dont have gun, Please get gun first')
            return
        else:
            self.gun.shoot(aim, self.demage)

    def __str__(self):
        return 'Name：%s remain hp %s demage %s gun %s' % (self.name, self.hp, self.demage, self.gun)


def test_():
    gun = Gun('ak47', 100, 100)
    print(gun)
    gun.add_bullet(100)
    print(gun)


#  not have gun
def test2():
    gun = Gun('ak47', 100, 100)
    p1 = Player('lizi', 100, 20)
    p2 = Player('beau', 100, 20)
    p1.fire(p2)
    p1.fire(p2)


#  have gun
def test2():
    gun = Gun('ak47', 100, 100)
    p1 = Player('lizi', 100, 80)
    p1.gun = Gun('Ak47', 100, 20)
    p2 = Player('beau', 100, 80)
    p1.fire(p2)
    p1.fire(p2)
    print(p1)
    print(p2)



if __name__ == '__main__':
    test2()
