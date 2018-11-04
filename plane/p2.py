import pygame, copy, random, math
from Vec2d import Vec2d
from pygame.locals import *
from sys import exit
from threading import *
from time import sleep
background = './bg.jpg'
my_plan_picture = './plane01.png'
enemy_picture = './enemy.png'
my_bullet_picture = './bullet.png'
enemy_bullet_picture = './enemybullet.png'
boom_picture = './boom.png'
boss_picture = './boss.png'
fire_picture = './fire.png'
plan_not_defeat = './plane8888.png'
box = './box.png'
missile = './daodan.png'
lock = './lock.png'
music = './bgm.mp3'
pygame.init()


class Plan(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN, 32)
        # 游戏组件
        self.background = pygame.image.load(background).convert()
        self.my_plan_picture = pygame.image.load(my_plan_picture).convert_alpha()
        self.enemy_picture = pygame.image.load(enemy_picture).convert_alpha()
        self.my_bullet_picture = pygame.image.load(my_bullet_picture).convert_alpha()
        self.enemy_bullet_picture = pygame.image.load(enemy_bullet_picture).convert_alpha()
        self.small_plan = pygame.transform.scale(self.my_plan_picture, (50, 35))
        self.boom_picture = pygame.image.load(boom_picture).convert_alpha()
        self.boss_picture = pygame.image.load(boss_picture).convert_alpha()
        self.fire_picture = pygame.image.load(fire_picture).convert_alpha()
        self.not_defeat_picture = pygame.image.load(plan_not_defeat).convert_alpha()
        self.box_picture = pygame.image.load(box).convert_alpha()
        self.missile_picture = pygame.image.load(missile).convert_alpha()
        self.lock_picture = pygame.image.load(lock).convert_alpha()
        pygame.mixer_music.load(music)
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(50)
        # 时间标志
        # self.clock = pygame.time.Clock()
        self.time_record = 0
        # 存在的各种子弹数组
        self.my_bullets = []
        self.enemy_bullets = []
        self.missile_list = [[], []]
        # 本机子弹速度和数量
        self.my_bullet_speed = 20
        self.my_bullet_number = 1
        # 能量
        self.my_power = 1000
        self.sub_my_power = 0
        # 存在的敌机
        self.live_enemy = []
        # 正在爆炸的坐标
        self.booming_pos = []
        # 剩余生命
        self.my_life = 3
        # 初始化本机且不无敌
        self.my_plan_pos = [900, 500]
        self.now_plan_picture = self.my_plan_picture
        self.is_not_defeat = 0
        # 初始化导弹数为0
        self.missile_number = 0
        # 初始化字体
        self.my_font = pygame.font.SysFont('kaiti', 22, True, True)
        # 初始化得分
        self.my_count = 0
        # 道具
        self.box_list = []
        self.have_box = 0
        self.fire_time = 0
        # 初始化boss坐标，并且无boss
        self.have_boss = 0
        self.boss_pos = [800, -250]
        self.boss_do_shut = 0
        self.boss_life = 350
        # boss左右移动方向
        self.boss_toward = -1
        # 难度值
        self.hard = 0

    # 移动本机
    def move_my_plan(self):
        my_plan_move = pygame.mouse.get_rel()
        # 超出边界则不移动
        if 0 < self.my_plan_pos[0]+self.my_plan_picture.get_width()/2+my_plan_move[0] < 1920:
            self.my_plan_pos[0] += my_plan_move[0]
        if 0 < self.my_plan_pos[1]+self.my_plan_picture.get_height()/2+my_plan_move[1] < 1080:
            self.my_plan_pos[1] += my_plan_move[1]
        self.screen.blit(self.now_plan_picture, self.my_plan_pos)

    # 创造本机子弹
    def create_my_bullet(self):
        # 间隔某段时间就添加子弹
        if self.time_record % self.my_bullet_speed == 0:
            if self.my_bullet_number == 1:
                self.my_bullets.append([self.my_plan_pos[0]+68, self.my_plan_pos[1]-13])
            elif self.my_bullet_number == 2:
                self.my_bullets.append([self.my_plan_pos[0]+53, self.my_plan_pos[1]-13])
                self.my_bullets.append([self.my_plan_pos[0]+83, self.my_plan_pos[1]-13])
        # 子弹轨迹
        for bullet in self.my_bullets:
            if bullet[1] <= 0:
                # 销毁超出范围的子弹
                self.my_bullets.remove(bullet)
            else:
                # 没超出范围则向上移动4像素
                bullet[1] -= 4
                self.screen.blit(self.my_bullet_picture, bullet)
        # 创造僚机子弹
        if self.fire_time > 0:
            self.screen.blit(self.fire_picture, [self.my_plan_pos[0] - 15, self.my_plan_pos[1] + 30])
            self.screen.blit(self.fire_picture, [self.my_plan_pos[0] + 130, self.my_plan_pos[1] + 30])
            if self.time_record % 20 == 0:
                self.my_bullets.append([self.my_plan_pos[0] - 8, self.my_plan_pos[1] + 30])
                self.my_bullets.append([self.my_plan_pos[0] + 140, self.my_plan_pos[1] + 30])
            self.fire_time -= 1
        # 如果场上没有导弹就创造一个导弹
        if self.missile_number > 0 and len(self.missile_list[0]) == 0:
            # 导弹起始点为当前本机坐标
            missile_pos = copy.deepcopy([self.my_plan_pos[0]+50, self.my_plan_pos[1]-50])
            self.missile_list[0] = missile_pos
            self.missile_number -= 1
        # 发射导弹
        if len(self.missile_list[0]) > 0:
            # 导弹打向敌机
            if len(self.live_enemy) > 0:
                enemy_pos = [self.live_enemy[0][0]-10, self.live_enemy[0][1]-20]
                vec = (Vec2d(enemy_pos) - Vec2d(self.missile_list[0])).normalized()
                self.missile_list[1] = vec
                # 改变导弹朝向
                angle = 270-vec.get_angle()
                toward = pygame.transform.rotate(self.missile_picture, angle)
                # 画出标记
                self.screen.blit(self.lock_picture, [enemy_pos[0]-10, enemy_pos[1]])
                self.screen.blit(toward, (self.missile_list[0]))
                self.missile_list[0][0] += self.missile_list[1][0] * 6
                self.missile_list[0][1] += self.missile_list[1][1] * 6

    # 创造多种道具效果
    def show_box(self):
        # 第一种，创造两个发射普通子弹的僚机
        if self.have_box == 1:
            self.fire_time = 1500
            self.have_box = 0
        # 第二种，清屏
        elif self.have_box == 2:
            self.enemy_bullets = []
            self.have_box = 0
        # 第三种，发射跟踪导弹
        elif self.have_box == 3:
            self.missile_number = 30
            self.have_box = 0
        # 第四种，无敌
        elif self.have_box == 4:
            self.is_not_defeat = 1600
            self.have_box = 0

    # 创造敌机
    def create_enemy(self):
        # 间隔某段时间就创建新的敌机
        if self.time_record % (250-self.hard*40) == 0:
            x = random.randint(0, 1920)
            vec_x = random.randint(-1920, 1920)
            vec_y = random.randint(200, 500)
            vec_normal = Vec2d(vec_x, vec_y).normalized()
            self.live_enemy.append([x, 0, vec_normal, [vec_x, vec_y]])
        # 移动敌机
        for enemy_pos in self.live_enemy:
            # 销毁超出范围的敌机并扣一分
            if enemy_pos[1] >= 1080:
                self.live_enemy.remove(enemy_pos)
                if self.my_count > 0:
                    self.my_count -= 1
            # 改变碰壁敌机的移动方向
            elif enemy_pos[0] < 10 or enemy_pos[0] > 1910:
                new_vec_x = 1000-enemy_pos[0]
                new_vec_y = random.randint(enemy_pos[3][1] + 200, enemy_pos[3][1] + 500)
                new_vec_normal = Vec2d(new_vec_x, new_vec_y).normalized()
                self.live_enemy[self.live_enemy.index(enemy_pos)][2] = new_vec_normal
                self.live_enemy[self.live_enemy.index(enemy_pos)][3] = [new_vec_x, new_vec_y]
        for enemy_pos in self.live_enemy:
            # 到达随机方向向量的y坐标附近就随机一个新的方向
            if enemy_pos[3][1]-30 < enemy_pos[1] < enemy_pos[3][1]+30:
                new_vec_x = random.randint(-1920, 1920)
                new_vec_y = random.randint(enemy_pos[3][1]+400, enemy_pos[3][1]+500)
                new_vec_normal = Vec2d(new_vec_x, new_vec_y).normalized()
                self.live_enemy[self.live_enemy.index(enemy_pos)][2] = new_vec_normal
                self.live_enemy[self.live_enemy.index(enemy_pos)][3] = [new_vec_x, new_vec_y]
            # 否则按单位向量移动敌机
            else:
                self.live_enemy[self.live_enemy.index(enemy_pos)][0] += self.live_enemy[self.live_enemy.index(enemy_pos)][2][0]
                self.live_enemy[self.live_enemy.index(enemy_pos)][1] += self.live_enemy[self.live_enemy.index(enemy_pos)][2][1]
        # 画出敌机
        for enemy_pos in self.live_enemy:
            # 按照飞机中心为标准
            self.screen.blit(self.enemy_picture, [enemy_pos[0]-self.enemy_picture.get_width()/2, enemy_pos[1]-self.enemy_picture.get_height()/2])

    # 创造敌机子弹
    def create_enemy_bullet(self):
        # 敌机随机概率发射朝向本机的子弹
        for enemy in self.live_enemy:
            if random.randint(0, 1600-300*self.hard) == 0:
                enemy_pos = [enemy[0]-20, enemy[1]+15]
                normal_vec = (Vec2d(self.my_plan_pos[0]+self.my_plan_picture.get_width()/4+20, self.my_plan_pos[1]+self.my_plan_picture.get_height()/4) - Vec2d(enemy_pos)).normalized()
                self.enemy_bullets.append([enemy_pos, normal_vec])
        # 画出子弹轨迹
        for bullet in self.enemy_bullets:
            if 0 < bullet[0][0] < 1920 and bullet[0][1] < 1080:
                bullet[0][0] += bullet[1][0]*2
                bullet[0][1] += bullet[1][1]*2
                self.screen.blit(self.enemy_bullet_picture, bullet[0])
            # 销毁超出范围的子弹
            else:
                self.enemy_bullets.remove(bullet)

    # boss发射子弹
    def boss_shut(self):
        do_shut = random.randint(1, 3)
        # 第一种方法,圆形
        if do_shut == 1:
            for x in range(21):
                angle = math.pi / 10
                copy_pos = copy.deepcopy([self.boss_pos[0] + 140, self.boss_pos[1] + 100])
                normal_vec = Vec2d(math.cos(x*angle), math.sin(x*angle)).normalized()
                self.enemy_bullets.append([copy_pos, normal_vec])
        # 第二种方法，螺旋
        elif do_shut == 2:
            for x in range(-10, 11):
                angle = math.pi / 10
                copy_pos = copy.deepcopy([self.boss_pos[0] + 140, self.boss_pos[1] + 100])
                normal_vec = Vec2d(math.cos(x * angle), math.sin(x * angle)).normalized()
                self.enemy_bullets.append([copy_pos, normal_vec])
                sleep(0.05)
        # 第三种方法，来回
        elif do_shut == 3:
            for x in range(-10, 11):
                angle = math.pi / 10
                copy_pos = copy.deepcopy([self.boss_pos[0] + 140, self.boss_pos[1] + 100])
                normal_vec = Vec2d(math.cos(x * angle), abs(math.sin(x * angle))).normalized()
                self.enemy_bullets.append([copy_pos, normal_vec])
                sleep(0.1)

    # 创造boss
    def create_boss(self):
        if self.my_count == 100 and self.have_boss == 0:
            self.have_boss = 1
        if self.have_boss == 1:
            # 登场
            if self.boss_pos[1] < 60:
                it_font = pygame.font.SysFont('heiti', 60, True)
                text = it_font.render('Boss Coming!', True, (random.randint(100, 205), self.time_record % 255, random.randint(100, 200)))
                self.screen.blit(text, (800, 500))
                self.boss_pos[1] += 0.3
                self.screen.blit(self.boss_picture, self.boss_pos)
            else:
                if self.time_record % (800-self.hard*100) == 0:
                    Thread(target=self.boss_shut).start()
                # 左右移动
                if self.boss_pos[0] < 0 or self.boss_pos[0] > 1600:
                    self.boss_toward = self.boss_toward - 2 * self.boss_toward
                self.boss_pos[0] += self.boss_toward / 2
                self.screen.blit(self.boss_picture, self.boss_pos)

    # 判断是否击中敌机
    def judge_damage_enemy(self):
        width = self.enemy_picture.get_width()
        height = self.enemy_picture.get_height()
        for enemy in self.live_enemy:
            for bullet_pos in self.my_bullets:
                # 敌机坐标
                enemy_pos = copy.deepcopy([enemy[0], enemy[1]])
                # 判断敌机是否在子弹周围
                if enemy_pos[0]-width/2 <= bullet_pos[0] <= enemy_pos[0]+width/2 and enemy_pos[1] <= bullet_pos[1] <= enemy_pos[1]+height:
                    # 删除击中敌机的子弹
                    self.my_bullets.remove(bullet_pos)
                    # 在没有道具的情况下有概率爆出道具
                    if random.randint(1, 15) == 5 and self.have_box == 0 and len(self.box_list) == 0:
                        self.box_list.append([enemy_pos[0]-30, enemy_pos[1]-70])
                    # 向爆炸列表中添加坐标并初始化爆炸时间为0
                    try:
                        self.live_enemy.remove(enemy)
                    except ValueError:
                        pass
                    self.booming_pos.append([[enemy_pos[0]-width/2, enemy_pos[1]-height/2], 0])
                    # 得分+1
                    self.my_count += 1
                # 判断导弹是否击中敌机
                if len(self.missile_list[0]) > 0:
                    if enemy_pos[0]-width/2 <= self.missile_list[0][0] <= enemy_pos[0]+width/2 and enemy_pos[1]-20 <= self.missile_list[0][1] <= enemy_pos[1]+20:
                        # 删除该导弹
                        self.missile_list = [[], []]
                        # 在没有道具的情况下有概率爆出道具
                        if random.randint(1, 15) == 5 and self.have_box == 0 and len(self.box_list) == 0:
                            self.box_list.append([enemy_pos[0]-30, enemy_pos[1]-70])
                        # 向爆炸列表中添加坐标并初始化爆炸时间为0
                        try:
                            self.live_enemy.remove(enemy)
                        except ValueError:
                            pass
                        self.booming_pos.append([[enemy_pos[0]-width/2, enemy_pos[1]-height/2], 0])
                        # 得分+1
                        self.my_count += 1
        # 判断是否击中boss
        if self.have_boss == 1:
            for bullet in self.my_bullets:
                if self.boss_pos[0] < bullet[0] < self.boss_pos[0]+280 and self.boss_pos[1] < bullet[1] < self.boss_pos[1]+100:
                    self.booming_pos.append([bullet, 0])
                    self.my_bullets.remove(bullet)
                    # boss血量-1
                    self.boss_life -= 1
                    self.my_count += 1

    # 判断是否击中本机
    def judge_damage_me(self):
        width = self.enemy_picture.get_width()
        height = self.enemy_picture.get_height()
        for bullet in self.enemy_bullets:
            if self.my_plan_pos[0]+20 < bullet[0][0] < self.my_plan_pos[0]+80 and self.my_plan_pos[1] < bullet[0][1] < self.my_plan_pos[1]+80:
                # 删除该子弹并添加爆炸
                self.enemy_bullets.remove(bullet)
                self.booming_pos.append([self.my_plan_pos, 0])
                # 生命-1
                self.my_life -= 1
                # 设置无敌时间并重置坐标
                self.is_not_defeat = 400
                self.my_plan_pos = [900, 800]
        # 判断撞击
        for enemy in self.live_enemy:
            enemy_pos = copy.deepcopy([enemy[0] - width / 2, enemy[1] - height / 2])
            if enemy_pos[0]-10 < self.my_plan_pos[0]+self.my_plan_picture.get_width()/2 < enemy_pos[0]+60 and enemy_pos[1]-10 < self.my_plan_pos[1]+self.my_plan_picture.get_height()/2 < enemy_pos[1]+60:
                # 向爆炸列表中添加坐标并初始化爆炸时间为0
                try:
                    self.live_enemy.remove(enemy)
                except ValueError:
                    pass
                self.booming_pos.append([[enemy_pos[0], enemy_pos[1]], 0])
                self.booming_pos.append([self.my_plan_pos, 0])
                # 生命-1
                self.my_life -= 1
                # 设置无敌时间并重置坐标
                self.is_not_defeat = 400
                self.my_plan_pos = [900, 800]

    # 移动道具盒子
    def move_box(self):
        for box_pos in self.box_list:
            box_pos[1] += 1
            self.screen.blit(self.box_picture, box_pos)
            # 判断是否捡到
            if self.my_plan_pos[0]-50 < box_pos[0] < self.my_plan_pos[0]+70 and self.my_plan_pos[1]-60 < box_pos[1] < self.my_plan_pos[1]+20:
                self.box_list.remove(box_pos)
                # 随机一个道具效果
                self.have_box = random.randint(1, 4)

    # 使本机无敌
    def remove_not_defeat(self):
        if self.is_not_defeat > 0:
            self.now_plan_picture = self.not_defeat_picture
            self.is_not_defeat -= 1
        else:
            # 恢复普通状态
            self.now_plan_picture = self.my_plan_picture

    # 显示数据
    def draw_life_count(self):
        # 显示剩余生命
        for number in range(self.my_life):
            self.screen.blit(self.small_plan, [number*50, 10])
        # 显示得分
        string = '得分 %d' % self.my_count
        submit = self.my_font.render(string, True, (150, 200, 0))
        self.screen.blit(submit, (1800, 20))
        # 显示难度系数
        how_hard = self.my_font.render('难度 %d' % self.hard, True, (0, 50, 230))
        pygame.draw.line(self.screen, (255, 100, 0), (1850, 150), (1850, 150-self.hard*10), 10)
        pygame.draw.lines(self.screen, (0, 150, 150), True, [(1844, 100), (1856, 100), (1856, 110), (1844, 110), (1844, 120), (1856, 120), (1856, 130), (1844, 130), (1844, 140), (1856, 140), (1856, 150), (1844, 150)], 2)
        pygame.draw.line(self.screen, (0, 150, 150), (1856, 100), (1856, 150), 2)
        # 显示剩余能量
        self.screen.blit(how_hard, (1800, 50))
        how_hard = self.my_font.render('能量', True, (0, 230, 50))
        self.screen.blit(how_hard, (28, 215))
        pygame.draw.line(self.screen, (0, 50, 255), (50, 200), (50, 200-self.my_power/10), 14)
        pygame.draw.lines(self.screen, (255, 50, 0), True, [(43, 100), (58, 100), (58, 200), (43, 200)], 2)
        # 显示boss血条
        if self.boss_life > 0:
            pygame.draw.line(self.screen, (5, 250, 100), self.boss_pos, (self.boss_pos[0] + self.boss_life*1.1, self.boss_pos[1]), 13)

    # 爆炸特效
    def boom(self):
        # 依次爆炸
        for pos in self.booming_pos:
            if pos[1] <= 80:
                self.screen.blit(self.boom_picture, pos[0])
                # 爆炸延迟
                pos[1] += 1

    # 开始主循环
    def began(self):
        over = 0
        while 1:
            # 隐藏鼠标
            pygame.mouse.set_visible(False)
            # 时间标志
            self.time_record += 1
            # time_pass = self.clock.tick()
            # pass_second = self.time_pass/1000.0
            # 判断退出
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    exit()
                elif event.type == KEYDOWN:
                    keys_press = pygame.key.get_pressed()
                    # alt+f4退出
                    if keys_press[K_LALT] and keys_press[K_F4]:
                        pygame.display.quit()
                        exit()
                    # 调节难度
                    elif keys_press[K_LCTRL]:
                        if self.hard != 5:
                            self.hard += 1
                        else:
                            self.hard = 0
                # 使用能量
                elif event.type == MOUSEBUTTONDOWN and self.my_power > 0:
                        self.sub_my_power = 1
                elif event.type == MOUSEBUTTONUP:
                    self.my_bullet_speed = 20
                    self.my_bullet_number = 1
                    self.sub_my_power = 0
            # 消耗能量
            if self.sub_my_power == 1 and self.my_power > 0:
                self.my_bullet_speed = 10
                self.my_bullet_number = 2
                self.my_power -= 1.9
            else:
                self.my_bullet_speed = 20
                self.my_bullet_number = 1
            # 恢复能量
            if self.my_power < 1000:
                self.my_power += 0.4
            self.screen.blit(self.background, (0, 0))
            self.remove_not_defeat()
            if self.boss_life > 0:
                self.create_boss()
            else:
                self.have_boss = 0
            self.move_my_plan()
            self.create_enemy()
            self.create_my_bullet()
            self.create_enemy_bullet()
            self.judge_damage_enemy()
            # 无敌状态
            if self.is_not_defeat == 0:
                self.judge_damage_me()
            self.move_box()
            self.show_box()
            self.boom()
            self.draw_life_count()
            # 结束游戏
            if self.my_life < 0:
                over += 1
            if over == 1:
                font = pygame.font.SysFont('kaiti', 50, True)
                text = font.render('Game Over!', True, (255, 20, 50))
                self.screen.blit(text, (800, 400))
                text = font.render('最终得分 %d' % self.my_count, True, (255, 20, 50))
                self.screen.blit(text, (780, 500))
                pygame.display.update()
            if self.my_life >= 0:
                pygame.display.update()


plane = Plan()
plane.began()
