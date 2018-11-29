import random
import pygame


class Movable:
    def __init__(self, screen, src):
        self.screen = screen
        self.img = Movable.load_src(src)
        self.width, self.height = Movable.get_width_height(self.img)
        self.x = 0
        self.y = 0

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self, x=0, y=0):
        pass

    @staticmethod
    def load_src(path):
        return pygame.image.load(path)

    @staticmethod
    def get_width_height(img):
        rect = img.get_rect()
        return rect.width, rect.height

    @staticmethod
    def run_in_test(m_thing, things):
        for t in things:
            if m_thing.x + m_thing.width > t.x and t.x + t.width > m_thing.x and m_thing.y + m_thing.height > t.y and t.y + t.height > m_thing.y:
                return t
        return None

    @staticmethod
    def run_in_test_list(m_things, things):
        for i, m in enumerate(m_things):
            return i, Movable.run_in_test(m, things)
        return -1, -1


class Plane(Movable):
    def __init__(self, screen):
        Movable.__init__(self, screen, 'feiji/hero1.png')
        screen_width = screen.get_rect().width
        screen_height = screen.get_rect().height
        self.x = (screen_width - self.width) / 2
        self.y = (screen_height - self.height)
        self.boundary_x = screen_width - self.width
        self.boundary_y = screen_height - self.height
        self.bullets = []
        self.booming = 0

    def display_bullets(self):
        for bullet in self.bullets:
            if bullet.move():
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def move(self, x=0, y=0):
        if self.booming:
            print('--------------', self.booming // 3)
            if self.booming // 3 == 0:
                self.img = pygame.image.load('feiji/hero_blowup_n1.png')
            elif self.booming // 3 == 1:
                self.img = pygame.image.load('feiji/hero_blowup_n2.png')
            elif self.booming // 3 == 2:
                self.img = pygame.image.load('feiji/hero_blowup_n3.png')
            elif self.booming // 3 == 3:
                self.img = pygame.image.load('feiji/hero_blowup_n4.png')
            else:
                self.x = -300
                self.y = -300
                return True
            self.booming += 1
        else:
            self.x += x
            self.y += y
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0
            if self.x > self.boundary_x:
                self.x = self.boundary_x
            if self.y > self.boundary_y:
                self.y = self.boundary_y
        self.display()
        self.display_bullets()

    def shoot(self):
        bullet = Bullet(self.x + self.width / 2, self.y, self.screen)
        bullet.move()
        self.bullets.append(bullet)

    def is_destroy(self, enemy):
        en = Movable.run_in_test(self, enemy)
        if not self.booming:
            self.booming = en is not None
        return en


class Enemy(Movable):
    def __init__(self, screen):
        Movable.__init__(self, screen, 'feiji/enemy0.png')
        self.x = random.random() * screen.get_rect().width * 0.8
        self.y = 0
        self.speed = random.randint(2, 8)
        self.booming = 0
        self.direction = 1

    def move(self, x=0, y=0):
        if self.booming:
            if self.booming // 3 == 0:
                self.img = pygame.image.load('feiji/enemy0_down1.png')
            elif self.booming // 3 == 1:
                self.img = pygame.image.load('feiji/enemy0_down2.png')
            elif self.booming // 3 == 2:
                self.img = pygame.image.load('feiji/enemy0_down3.png')
            elif self.booming // 3 == 3:
                self.img = pygame.image.load('feiji/enemy0_down4.png')
            else:
                return True
            self.booming += 1
        else:
            if self.x < 0 or self.x + self.width > self.screen.get_rect().width:
                self.direction = -self.direction
            self.x += self.speed * self.direction
            self.y += 10-self.speed
            if self.y > self.screen.get_rect().height:
                return True
        self.display()

    def is_shot(self, things):
        shot_bullet = Movable.run_in_test(self, things)
        if not self.booming:
            self.booming = shot_bullet is not None
        return shot_bullet


class Bullet(Movable):
    def __init__(self, x, y, screen):
        Movable.__init__(self, screen, 'feiji/bullet.png')
        self.x = x - self.width / 2
        self.y = y

    def move(self, x=0, y=0):
        self.y -= 5
        if self.y < 0:
            return True
        else:
            self.display()


def main():
    """
        游戏主程序
    """
    screen_width = 480
    screen_height = 700

    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    bg = pygame.image.load('feiji/background.png')
    option = set()
    hero = Plane(screen)
    enemy_list = list()
    # is_shooting = 0
    while True:
        # 绘制背景图片
        screen.blit(bg, (0, 0))
        # 绘制敌机
        if len(enemy_list) < 5:
            enemy_list.append(Enemy(screen))
        des_en = hero.is_destroy(enemy_list)
        if des_en and not des_en.booming:
            print('-' * 20, des_en in enemy_list)
            des_en.booming = True
            hero.move(-480)
        for enemy in enemy_list:
            blt = enemy.is_shot(hero.bullets)
            if blt:
                hero.bullets.remove(blt)
            if enemy.move():
                enemy_list.remove(enemy)
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == pygame.QUIT:
                print("exit")
                exit()
            # 响应用户是输入的上下左右
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if event.type == pygame.KEYDOWN:
                        option.add('left')
                    elif event.type == pygame.KEYUP:
                        option.discard('left')
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if event.type == pygame.KEYDOWN:
                        option.add('right')
                    elif event.type == pygame.KEYUP:
                        option.discard('right')
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if event.type == pygame.KEYDOWN:
                        option.add('up')
                    elif event.type == pygame.KEYUP:
                        option.discard('up')
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if event.type == pygame.KEYDOWN:
                        option.add('down')
                    elif event.type == pygame.KEYUP:
                        option.discard('down')

                # 检测按键是否是空格键
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # if event.type == pygame.KEYDOWN:
                    #     is_shooting = 1
                    # elif event.type == pygame.KEYUP:
                    #     is_shooting = 0
                    hero.shoot()
                    print('space')

        x = ('left' in option) * -10 + ('right' in option) * 10
        y = ('up' in option) * -10 + ('down' in option) * 10
        hero.move(x, y)
        # 刷新界面
        pygame.display.update()


if __name__ == '__main__':
    main()
