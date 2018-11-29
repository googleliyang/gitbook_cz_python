import pygame
import pygame.locals
import configparser
import random


cf = configparser.ConfigParser()
cf.read('./config.ini', encoding="utf-8")  # python3

# bg
bg = pygame.image.load(cf.get('airplane', 'bg_img'))

# move speed
bullet_step = cf.getint('bullet', 'step')
airplane_step = cf.getint('airplane', 'step')

# bullet
bullet_img = pygame.image.load(cf.get('bullet', 'bullet_img'))
enemy_bullet_img = pygame.image.load(cf.get('bullet', 'enemy_bullet_img'))

# hero & blowup
airplane_img = pygame.image.load(cf.get('airplane', 'hero_img'))
hero_blowup_n1 = pygame.image.load(cf.get('airplane', 'hero_blowup_n1'))
hero_blowup_n2 = pygame.image.load(cf.get('airplane', 'hero_blowup_n2'))
hero_blowup_n3 = pygame.image.load(cf.get('airplane', 'hero_blowup_n3'))
hero_blowup_n4 = pygame.image.load(cf.get('airplane', 'hero_blowup_n4'))

# enemy
enemy_plane_img = pygame.image.load(cf.get('enemy', 'enemy0_down0'))
enemy1_downn1 = pygame.image.load(cf.get('enemy', 'enemy0_down1'))
enemy1_downn2 = pygame.image.load(cf.get('enemy', 'enemy0_down2'))
enemy1_downn3 = pygame.image.load(cf.get('enemy', 'enemy0_down3'))
enemy1_downn4 = pygame.image.load(cf.get('enemy', 'enemy0_down4'))

enemy_list = []


class Plane():
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.step = airplane_step
        self.bullets = []

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def m_left(self):
        self.x -= self.step
        if self.x < 0:
            self.x = 0

    def m_right(self):
        self.x += self.step
        if self.x > 380:
            self.x = 380

    def m_up(self):
        self.y -= self.step
        if self.y < 0:
            self.y = 0

    def m_down(self):
        self.y += self.step
        if self.y > 580:
            self.y = 580

    def display_all_bullets(self):
        print(self.bullets)
        for bullet in self.bullets:
            if not bullet.aimed:
                bullet.display()
                bullet.move()

    def shoot(self):
        bullet = Bullet(self.x + 39, self.y - 39, self.screen)
        self.bullets.append(bullet)

    def destroy(self, num, img_str):
        print('done..')
        self.screen.blit(num == 5 and bg or eval(img_str+str(num)),
                         (self.x, self.y))
        pygame.display.update()


class HeroPlane(Plane):

    def __init__(self, x, y, img, screen):
        Plane.__init__(self, x, y, img, screen)

    def destroy(self, num, img_str):
        self.screen.blit(bg, (0, 0))
        super().destroy(num, img_str)


class EnemyPlane(Plane):
    def __init__(self, x, y, img, screen):
        Plane.__init__(self, x, y, img, screen)
        self.step = random.randint(1, 5)
        self.is_destroy = False
        self.des_num = 1
        self.arrow = 'l'

    def auto_shoot(self):
        if random.randint(1, 10) == 2:
            bullet = EnemyBullet(self.x + 20, self.y + 100, self.screen)
            self.bullets.append(bullet)

    def auto_move(self):
        y_ = random.randint(1, 5)
        x_ = random.randint(1, 5)
        if self.arrow == 'l':
            self.x -= x_
        else:
            self.x += x_
        if self.x >= 450:
            self.arrow = 'l'
        elif self.x <= 0:
            self.arrow = 'r'
        self.y += y_


class Bullet:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.img = bullet_img
        self.screen = screen
        self.aimed = False

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= bullet_step
        self.if_shoot_aim()

    def if_shoot_aim(self):
        for enemy in enemy_list:
            if enemy.is_destroy:
                continue
            print('enemy x is %s y is %s, self x is %s y is %s' %
                  (enemy.x, enemy.y, self.x, self.y))
            if abs(enemy.x - self.x) < 50 and abs(enemy.y - self.y) < 20:
                print('Destroy one')
                enemy.is_destroy = True
                self.aimed = True


class EnemyBullet(Bullet):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.img = enemy_bullet_img

    def move(self):
        self.y += bullet_step


class GameController:
    def __init__(self):
        pass

    @staticmethod
    def create_enemy(screen, num):
        for i in range(1, num):
            p_x = random.randint(0, 400)
            p_y = random.randint(0, 100)
            enemy_plane = EnemyPlane(p_x, p_y, enemy_plane_img, screen)
            enemy_plane.auto_shoot()
            enemy_list.append(enemy_plane)


def main():

    # 创建窗口
    screen = pygame.display.set_mode((480, 700), 0, 32)
    # 添加到主窗口上
    screen.blit(bg, (0, 0))

    # 加载飞机图片
    x, y = 200, 550
    hero_plane = HeroPlane(x, y, airplane_img, screen)
    GameController.create_enemy(screen, 8)
    end, num = False, 1
    while True:

        if not end:

            # 重新画一层盖住旧的背景层
            screen.blit(bg, (0, 0))

            hero_plane.display_all_bullets()

            hero_plane.draw()

            for enemy in enemy_list:
                enemy.auto_move()
                # check if destroy
                # if destroy : draw four img else
                if enemy.is_destroy:
                    if enemy.des_num <= 5:
                        enemy.destroy(enemy.des_num, 'enemy1_downn')
                        enemy.des_num += 1
                    else:
                        enemy_list.remove(enemy)
                        GameController.create_enemy(screen, 0)

                else:
                    if enemy.y >= 580:
                        print('explode')
                        end = True
                    else:
                        enemy.display_all_bullets()
                        enemy.auto_shoot()
                        enemy.draw()

            # 刷新页面
            pygame.display.update()

            for event in pygame.event.get():
                type_ = event.type
                if type_ == pygame.QUIT:
                    print('quit')
                    pygame.quit()
                    exit()
                elif type_ == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP:
                        print('up')
                        hero_plane.m_up()
                    elif key == pygame.K_DOWN:
                        hero_plane.m_down()
                    elif key == pygame.K_LEFT:
                        hero_plane.m_left()
                    elif key == pygame.K_RIGHT:
                        hero_plane.m_right()
                    elif key == pygame.K_SPACE:
                        print('shoot')
                        hero_plane.shoot()
                    elif key == pygame.K_ESCAPE:
                        print('explode')
                        end = True
                        pass
        else:
            if num <= 5:
                hero_plane.destroy(num, 'hero_blowup_n')
            num += 1
            for event in pygame.event.get():
                type_ = event.type
                if type_ == pygame.QUIT:
                    print('quit')
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main()
