# Simple implementation of GalaxyInvanders game
# Rohan Roy (India) - 3 Nov 2013

VER = "1.1.244"

# "add various aliens"

import simplegui, math, random, time

#Global const
FIELD_WIDTH = 850
FIELD_HEIGHT = 500
TOP_MARGIN = 75
LEFT_MARGIN = 25
ALIEN_WIDTH = 48
ALIEN_HEIGHT = 55

PLAYER_SPEED = 10
BULLET_SPEED = 10
BULLET_POWER = 1
BONUS_SPEED = 10
ALIEN_SPEED = [3, 5]

# Images:
pImage = simplegui.load_image('https://dl.dropbox.com/s/zhnjucatewcmfs4/player.png')

aImages = []
for i in range(7):
    aImages.append([])
aImages[0].append(simplegui.load_image('https://dl.dropbox.com/s/0cck7w6r0mt8pzz/alien_1_1.png'))
aImages[0].append(simplegui.load_image('https://dl.dropbox.com/s/j0kubnhzajbdngu/alien_1_2.png'))
aImages[0].append(simplegui.load_image('https://dl.dropbox.com/s/zkeu6hqh9bakj25/alien_1_3.png'))

aImages[1].append(simplegui.load_image('https://dl.dropbox.com/s/e75mkcylat70lnd/alien_2_1.png'))
aImages[1].append(simplegui.load_image('https://dl.dropbox.com/s/pgjvaxg0z6rhco9/alien_2_2.png'))
aImages[1].append(simplegui.load_image('https://dl.dropbox.com/s/en0hycfsi3cuzuo/alien_2_3.png'))

aImages[2].append(simplegui.load_image('https://dl.dropbox.com/s/fu9weoll70acs8f/alien_3_1.png'))
aImages[2].append(simplegui.load_image('https://dl.dropbox.com/s/b2rxru2nt5q2r1u/alien_3_2.png'))
aImages[2].append(simplegui.load_image('https://dl.dropbox.com/s/x66vgj9fc2jlg53/alien_3_3.png'))

aImages[3].append(simplegui.load_image('https://dl.dropbox.com/s/7o04ljg52kniyac/alien_4_1.png'))
aImages[3].append(simplegui.load_image('https://dl.dropbox.com/s/b3v6tvami0rvl6r/alien_4_2.png'))
aImages[3].append(simplegui.load_image('https://dl.dropbox.com/s/j451arcevsag36h/alien_4_3.png'))

aImages[4].append(simplegui.load_image('https://dl.dropbox.com/s/jlhdigkm79nncnm/alien_5_1.png'))
aImages[4].append(simplegui.load_image('https://dl.dropbox.com/s/wvlvjsa8yl6gka3/alien_5_2.png'))
aImages[4].append(simplegui.load_image('https://dl.dropbox.com/s/rrg4y1tnsbrh04r/alien_5_3.png'))

aImages[5].append(simplegui.load_image('https://dl.dropbox.com/s/oufyfy590tzf7cx/alien_6_1.png'))
aImages[5].append(simplegui.load_image('https://dl.dropbox.com/s/p4ehd9f6mo2xfzc/alien_6_2.png'))
aImages[5].append(simplegui.load_image('https://dl.dropbox.com/s/815gq3xyh6wmc0t/alien_6_3.png'))

aImages[6].append(simplegui.load_image('https://dl.dropbox.com/s/bv4ycocuomsvj50/alien_7_1.png'))
aImages[6].append(simplegui.load_image('https://dl.dropbox.com/s/krs2gtvdxxve79z/alien_7_2.png'))
aImages[6].append(simplegui.load_image('https://dl.dropbox.com/s/v2wczi8lxwczq87/alien_7_3.png'))

#backgrounds
bckg = []
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/ibfu2t9vrh4bhxd/back01.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/pcl8vzby25ovis8/back02.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/g8nwo1t9s4i9usg/back03.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/ee8oilluf7pe98h/back04.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/7jfgjoxinzwwlx4/back05.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/wh01g2q3607snvz/back06.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/b72ltp2xii9utnr/back07.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/av73jek8egezs1w/back08.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/ik54ttfklv3x3ai/back09.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/e9e6kpyg3yuoenc/back10.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/zrabwnnvlwvn7it/back11.jpg"))
bckg.append(simplegui.load_image("https://dl.dropbox.com/s/a2infkx0rmn8b8m/back12.jpg"))

# sounds
sndPlayer = simplegui.load_sound('https://dl.dropbox.com/s/vl3as0o2m2wvlwu/player_shoot.wav')
sndAlien = simplegui.load_sound('https://dl.dropbox.com/s/m4x0tldpze29hcr/alien_shoot.wav')
sndPlayerExplosion = simplegui.load_sound('https://dl.dropbox.com/s/10fn2wh7kk7uoxh/explosion%2001.wav')
sndAlienHit = simplegui.load_sound('https://dl.dropbox.com/s/80qdvup27n8j6r1/alien_hit.wav')
sndAlienExplosion = simplegui.load_sound('https://dl.dropbox.com/s/qxm3je9vdlb469g/explosion_02.wav')
sndBonus = simplegui.load_sound('https://dl.dropbox.com/s/tzp7e20e5v19l01/bonus.wav')
sndPause = simplegui.load_sound('https://dl.dropbox.com/s/uzs9nixpd22asno/pause.wav')
sndTheme = simplegui.load_sound('https://dl.dropbox.com/s/52zo892uemfkuzm/theme_01.mp3')

sounds = [sndPlayer, sndAlien, sndPlayerExplosion, sndAlienExplosion, \
          sndBonus, sndPause, sndTheme, sndAlienHit]

#Global variables
GameRunning = False
GameEnded = False
player_speed = 0
mes = ""
timer_counter = 0
lives = 0
level = 1
scores = 0
killed = 0
current_back = 0
paused = False
shoot_count = 0
level_time = []
ready, go = False, False
#player = [FIELD_WIDTH //2, FIELD_HEIGHT - 30 + TOP_MARGIN]

#game objects
user_bullet = []
weapon_level = 1
weapon_speed = BULLET_SPEED
alien_bullets = []
alien_fleet = None
player = None
frame = None
aTimer = None
dTimer = None
bonuses = []
dCounter = 0
back = False
bonus_count = [0, 0, 0, 0]
player_killed = False
player_killed_at = 0

level_map = []
for i in range(7):
    level_map.append([])
level_map[0] = [  0,   0,   0,   0]
level_map[1] = [129,   0,   0,   0]
level_map[2] = [195, 129,   0,   0]
level_map[3] = [255, 195,  60,   0]
level_map[4] = [255, 231, 195, 195]
level_map[5] = [255, 255, 231, 195]
level_map[6] = [255, 255, 255, 231]

def draw_text(canvas, text, point, size, delta, color):
    canvas.draw_text(text, point, size, color[0])
    canvas.draw_text(text, [point[0]-delta[0], \
                            point[1]-delta[1]], size, color[1])

class Bonus:
    def __init__ (self, kind, point):
        self.kind = kind
        self.x = point[0]
        self.y = point[1]
        self.v = BONUS_SPEED #velocity
        self.width = 36
        self.height = 36
        return self
    
    def move(self):
        self.y += self.v
        return self
    
    def draw(self, canvas):
        if self.kind == 0: #speed of bullet
            canvas.draw_circle([self.x, self.y], 15, 3, "LightBlue")
            canvas.draw_text("WS", [self.x-12, self.y+5], self.width //2, "LightBlue")
        elif self.kind == 1: #weapon level
            canvas.draw_circle([self.x, self.y], 15, 3, "Red")
            canvas.draw_text("WL", [self.x-12, self.y+5], self.width //2, "Red")
        elif self.kind == 2: #life
            canvas.draw_circle([self.x, self.y], 15, 3, "LightGreen")
            canvas.draw_text("LF", [self.x-12, self.y+5], self.width //2, "LightGreen")
        elif self.kind == 3: #weapon power
            canvas.draw_circle([self.x, self.y], 15, 3, "8010df")
            canvas.draw_text("WP", [self.x-12, self.y+5], self.width //2, "8010df")
        return self
    
    def execute(self):
        global weapon_speed, weapon_level, player, scores, bonus_count
        bonus_count[self.kind] += 1
        if self.kind == 0: #speed of bullet
            weapon_speed += 1
            delta = round(math.pow(20, (1 + (1.0*level-1)/32))*5)
            scores = scores + delta
        elif self.kind == 1: #weapon level
            weapon_level += 1
            delta = round(math.pow(30, (1 + (1.0*level-1)/32))*5)
            scores = scores + delta
        elif self.kind == 2: #life
            player.lives += 1
            delta = round(math.pow(100, (1 + (1.0*level-1)/32))*5)
            scores = scores + delta
        elif self.kind == 3: #weapon power
            player.power += 0.1
            delta = round(math.pow(100, (1 + (1.0*level-1)/32))*5)
            scores = scores + delta
        sndBonus.play()        
        return self

def dHandler():
    global dCounter, back, player_killed
    dCounter += 1
    if dCounter % 10 == 0:
        if back:
            frame.set_canvas_background("Red")
        else:
            frame.set_canvas_background("black")
        back = not back;       
            
    if dCounter > 50:
        dCounter = 0
        player_killed = False
        dTimer.stop()
        frame.set_canvas_background("black")

class Bullet:
    def __init__ (self, point, color, velocity):
        self.x = point[0]
        self.y = point[1]
        self.color = color
        self.v = velocity
        self.width = 1
        self.height = 1
        
    def draw(self, canvas):
        canvas.draw_line([self.x, self.y-5], [self.x, self.y+5], 3, self.color)
        
    def move(self):
        self.y += self.v

class Alien:
    def __init__(self, point, kind):
        self.x = point[0]
        self.y = point[1]
        self.kind = kind
        self.flying = False
        self.vy = 0
        self.vx = 0
        self.health = self.get_max_health()
        self.width = 20
        self.height = 20
    
    def get_max_health(self):
        return 1+0.6 * self.kind[1]
        
    def shoot(self):
        if len(alien_bullets)<level*2:
            bullet = Bullet([self.x, self.y], "LightRed", BULLET_SPEED)
            alien_bullets.append(bullet)
            sndAlien.play()
    
    def move(self, point):
        if self.flying:
            koef = 1.5
            self.y += (self.vy / koef)
            if self.x>player.x:
                self.x -= (self.vx / koef)
            else:
                self.x += (self.vx / koef)
            if self.vx<ALIEN_SPEED[0]:
                self.vx += 1
            if self.vy<ALIEN_SPEED[1]:
                self.vy += 1
        else:
            self.x = point[0]
            self.y = point[1]
        
    def draw(self, canvas):
        if aImages[self.kind[1]][self.kind[0]].get_width()==0:
            w = 15
            h = 15
            canvas.draw_circle([self.x, self.y], 15, 5, "Red")
        else:
            # img = aImages[self.kind[1]][self.kind[0]]
            img = aImages[self.kind[1]][self.kind[0]]
            self.width = w = img.get_width()
            self.height = h = img.get_height()
            canvas.draw_image(img, (w//2, h//2), (w, h), (self.x, self.y), (w, h))
        if self.health<>self.get_max_health():
            ratio = w * (self.health*1.0) / self.get_max_health()
            canvas.draw_line([self.x-w//2, self.y-h//2-3], [self.x+w//2, self.y-h//2-3], 4, "red")
            canvas.draw_line([self.x-w//2, self.y-h//2-3], [self.x-w//2+ratio, self.y-h//2-3], 4, "green")
        return canvas
        
class AliensFleet:
    def __init__ (self, point):
        def is_high_level(place):
            map_ = (level-1)%7
            row = level_map[map_][place[1]] #255 - 0
            return (row & (1 << place[0]))<>0			
        self.x = point[0]
        self.y = point[1]
        self.aliens = []
        self.pattern = [255, 255, 255, 255]
        self.y_velocity = ALIEN_HEIGHT//3 + 1
        self.x_velocity = - ALIEN_WIDTH//3 + 1
        for i in range(self.get_aliens_count()):
            point = self.get_alien_position(i)
            place = self.get_alien_place(i)
            alien_level = (level-1)//7 + is_high_level(place)
            alien = Alien(point, [random.randrange(3), alien_level])
            self.aliens.append(alien)
        
    def get_aliens_count(self):
        c = 0
        for i in range(4):
            for j in range(8):
                if (self.pattern[i] & (1 << j))<>0:
                    c+=1
        return c
        
    def get_alien_position(self, n):
        #returns a screen x, y of alien with number n
        point = self.get_alien_place(n)
        x = point[0]*(ALIEN_WIDTH + 3) + self.x
        y = point[1]*(ALIEN_HEIGHT + 3) +self.y
        point = [x, y]
        return point
    
    def get_alien_place(self, n):
        #returns a fleet x, y of alien with number n
        x, y, c = 0, 0, 0
        for i in range(4):
            for j in range(8):
                if (self.pattern[i] & (1 << j))<>0:
                    if c==n:
                        x, y = j, i
                    c+=1
        point = [x, y]
        return point    
    
    def move_aliens(self):
        i = 0
        for alien in self.aliens:
            point = self.get_alien_position(i)
            alien.move(point)
            i += 1
        return self
    
    def move_down(self):
        self.y += self.y_velocity
        if self.y>400:
            player.explode()
            self.y = 100
        self.move_aliens()
    
    def move_side(self):
        self.x -= self.x_velocity
        # check borders of fleet:
        left = 8
        right = -1
        for i in range(len(self.aliens)):
            point = self.get_alien_place(i)
            if point[0]<left:
                left = point[0]
            if point[0]>right:
                right = point[0]
        if (self.x+(left+1)*60 < LEFT_MARGIN + 10) or (self.x + (right+1)*45>FIELD_WIDTH-LEFT_MARGIN-60):
            self.x_velocity = -self.x_velocity
        self.move_aliens()
        
    def draw(self, canvas):
        for alien in self.aliens:
            alien.draw(canvas)
    
    def make_shoot(self):        
        for alien in self.aliens:
            if len(alien_bullets) < level * 3 + 1:
                if random.randrange(101)<2: # 
                    alien.shoot()
        return self
    
    def alien_fly(self):
        i = 0
        for alien in self.aliens:
            if alien.flying:
                i += 1
            if (i<1+level) and (random.randrange(1000)<3) and (time.time()-level_time[len(level_time)-1]>60):
                alien.flying=True
    
    def check_death(self):
        global scores, killed, player
        i = 0
        for bullet in user_bullet:
            for i in range(len(self.aliens)): 
                alien = self.aliens[i]
                if isBulletHit(bullet, alien):
                    if alien.health-player.power<=0:
                        point = self.get_alien_place(i)
                        sndAlienExplosion.play()
                        self.aliens.remove(alien)
                        x = ~int((1 << point[0]))
                        self.pattern[point[1]] = self.pattern[point[1]] & x
                        user_bullet.remove(bullet)
                        delta = round(math.pow(5, (1 + (1.0*level-1)/32))*5)
                        scores = scores + delta
                        killed += 1
                        x = random.randrange(1000)
                        if x<5:
                            bonus = Bonus(3, [alien.x, alien.y])
                            bonuses.append(bonus)
                        elif x<50:
                            bonus = Bonus(2, [alien.x, alien.y])
                            bonuses.append(bonus)
                        elif x<120:
                            bonus = Bonus(1, [alien.x, alien.y])
                            bonuses.append(bonus)
                        elif x<200:
                            bonus = Bonus(0, [alien.x, alien.y])
                            bonuses.append(bonus)
                        if killed % 500 == 0:
                            player.lives += 1
                            sndBonus.play()
                        break
                    else:
                        user_bullet.remove(bullet)
                        alien.health -= player.power
                        sndAlienHit.play()
            i += 1
    
class Player:
    def __init__(self, point, lives):
        self.x = point[0]
        self.y = point[1]
        self.lives = 3
        self.speed = player_speed
        self.power = BULLET_POWER
        self.width = 20
        self.height = 20
        
    def draw(self, canvas):
        draw_user_image(canvas, [self.x, self.y])
        
    def move(self):
        self.x += player_speed
        if self.x<LEFT_MARGIN*2:
            self.x = LEFT_MARGIN*2
        if self.x>FIELD_WIDTH:
            self.x=FIELD_WIDTH
                
    def draw_lives_counter(self, canvas):
        if self.lives < 5:
            for i in range(self.lives):                
                draw_user_image(canvas, [150+i*35, 15])
        else:
            draw_user_image(canvas, [150, 15])
            canvas.draw_text(" x "+str(int(self.lives)), [170, 25], 25, "Yellow")
    
    def explode(self):
        global dTimer, alien_bullets, user_bullet, weapon_level, weapon_speed
        global alien_fleet, player_killed_at, player_killed, player_speed
        player_speed = 0
        player_killed_at = time.time()
        sndPlayerExplosion.play()
        for alien in alien_fleet.aliens:
            alien.flying = False
        player_killed = True
        alien_bullets = []
        user_bullet = []
        bonuses = []
        weapon_level = level // 10 + 1
        weapon_speed = BULLET_SPEED
        self.lives -= 1
        if self.lives<0:
            stop_game()
        dTimer = simplegui.create_timer(25, dHandler)
        dTimer.start()
        
#helper functions
def dummy(key):
    return key

def pause():
    global paused
    paused = not paused
    sndPause.play()
    
def draw_user_image(canvas, point):
    # draw a image of user ship
    # 
    global player
    if pImage.get_width()==0:
        canvas.draw_circle(point, 12, 5, "Yellow")
    else:
        canvas.draw_image(pImage, (25, 36), (49, 72), point, (34, 50))
        player.width = pImage.get_width()
        player.height = pImage.get_height()
    return canvas
    
def draw_lives(canvas):
    # draw lives counter
    canvas.draw_text("Lives : ", [30, 25], 25, "Red")
    if player<>None:
       player.draw_lives_counter(canvas)
    return canvas

def draw_weapons(canvas):
    canvas.draw_text("Weapon : ", [30, 60], 25, "Red")
    canvas.draw_text("Rocket lvl: "+str(int(weapon_level)), [135, 60], 25, "Yellow")
    
    canvas.draw_text("WS:"+str(weapon_speed/10.0), [280, 48], 10, "00c5fe")
    canvas.draw_text("WP:"+str(player.power), [280, 61], 10, "00c5fe")
    return canvas

def draw_level(canvas):
    canvas.draw_text("Level : ", [FIELD_WIDTH-200, 50], 50, "Red")
    canvas.draw_text(str(level), [FIELD_WIDTH-50, 50], 50, "Yellow")
    return canvas

def draw_scores(canvas):
    canvas.draw_text(str(int(scores)), [400, 50], 50, "LightBlue")
    return canvas

def draw_screen(canvas):
    # border of board
    canvas.draw_image(bckg[current_back], (425, 250), (850, 500), \
                      (LEFT_MARGIN+FIELD_WIDTH//2, TOP_MARGIN+FIELD_HEIGHT//2),\
                      (FIELD_WIDTH, FIELD_HEIGHT))
    canvas.draw_polygon([[LEFT_MARGIN, TOP_MARGIN], 
                         [LEFT_MARGIN, FIELD_HEIGHT+TOP_MARGIN], 
                         [FIELD_WIDTH+LEFT_MARGIN, FIELD_HEIGHT+TOP_MARGIN], 
                         [FIELD_WIDTH+LEFT_MARGIN, TOP_MARGIN]], 2, 'Orange')
    
    return canvas

def draw_start_screen(canvas):
    img_count = 1 + len(aImages)*(len(aImages[0])) + len(bckg)
    loaded_img_count = 0
    
    if pImage.get_width()<>0:
        loaded_img_count += 1
    for bImage in bckg:
        if bImage.get_width()<>0:
            loaded_img_count += 1
    for aImg in aImages:
        for img in aImg:
            if img.get_width()<>0:
                loaded_img_count += 1
    loaded_sounds = 0
    for snd in sounds:
        if snd <> None:
            loaded_sounds += 1
    
    draw_text(canvas, "SPACE INVANDERS", [220, 150], 50, [3, 3], ["blue", "yellow"])
    canvas.draw_text("ver. - "+VER, [600, 170], 20, "yellow")
    canvas.draw_text("03 nov. 2013", [600, 190], 20, "yellow")
 
    draw_text(canvas, "CONTROLS:", [110, 210], 24, [2, 2], ["green", "yellow"])
    
    draw_text(canvas, "Arrows - to left and right, space - to fire, P to pause game", [110, 240], 24, [2, 2], ["green", "yellow"])
    
    draw_text(canvas, "Bonuses: ", [110, 280], 24, [2, 2], ["green", "yellow"])
    
    b = Bonus(0, [125, 310])
    b.draw(canvas)
    draw_text(canvas, " - increase user's bullet speed", [150, 320], 24, [2, 2], ["green", "yellow"])
    
    b = Bonus(1, [125, 350])
    b.draw(canvas)
    draw_text(canvas, " - increase user's bullet number", [150, 360], 24, [2, 2], ["green", "yellow"])
    
    b = Bonus(2, [125, 390])
    b.draw(canvas)
    draw_text(canvas, " - add life", [150, 400], 24, [2, 2], ["green", "yellow"])
    
    b = Bonus(3, [125, 430])
    b.draw(canvas)
    draw_text(canvas, " - increase weapon power", [150, 440], 24, [2, 2], ["green", "yellow"])
    
    if loaded_img_count<img_count:
        draw_text(canvas, "Please, wait for loading...", [280, 500], 40, [3, 3], ["Blue", "Yellow"])
        
        s = "Loaded "+str(loaded_img_count)+" images of "+str(img_count)
        draw_text(canvas, s, [110, 550], 20, [2, 2], ["Blue", "yellow"])
        
        s = "Loaded "+str(loaded_sounds)+" sounds of "+str(len(sounds))
        draw_text(canvas, s, [510, 550], 20, [2, 2], ["Blue", "yellow"])
    else:
        draw_text(canvas, "Click to start game", [300, 500], 40, [3, 3], ["Blue", "yellow"])
        frame.set_mouseclick_handler(click_handler)        
    return canvas

def draw_end_screen(canvas):
    draw_text(canvas, "Game over!", [350, 180], 50, [2, 2], ["Blue", "Yellow"])
    
    draw_text(canvas, "Your score is "+str(int(scores)), [330, 240], 35, [2, 2], ["blue", "Yellow"])
    
    draw_text(canvas, "You shoot "+str(int(shoot_count))+" times", [150, 320], 24, [2, 2], ["blue", "Yellow"])
    draw_text(canvas, "You kill a "+str(killed)+" aliens", [150, 360], 24, [2, 2], ["blue", "Yellow"])
    if shoot_count == 0:
        s = "0"
    else:
        s = str(int(10000*float(killed)/shoot_count)/100.0)
    draw_text(canvas, "Your accuracy is "+s+"%", [150, 400], 24, [2, 2], ["blue", "Yellow"])
    
    i = 0
    for bc in bonus_count:
        b = Bonus(i, [505, 310 + 40*i])
        b.draw(canvas)
        draw_text(canvas, " - used "+str(bonus_count[i])+" times", [530, 320+40*i], 24, [2, 2], ["blue", "yellow"])
        i += 1
    
    draw_text(canvas, "Click to start new game", [300, 500], 40, [2, 2], ["blue", "Yellow"])
    canvas.draw_text("ver. - "+VER, [600, 540], 15, "yellow");
    return canvas

def draw_game_objects(canvas):
    player.draw(canvas)
    #draw_user_image(canvas, Player)
    for bullet in alien_bullets:
        bullet.draw(canvas)
    for bullet in user_bullet:
        bullet.draw(canvas)
    for bonus in bonuses:
        bonus.draw(canvas)
    alien_fleet.draw(canvas)
    readyGo()
    if paused:        
        draw_text(canvas, "P A U S E", [380, 350], 50, [2, 2], ["Green", "Yellow"])
    if ready:
        draw_text(canvas, "R E A D Y", [380, 350], 50, [2, 2], ["Green", "Yellow"])
    if go:
        draw_text(canvas, "G O ! ! !", [380, 350], 50, [2, 2], ["Green", "Yellow"])
    sndTheme.play()
    return canvas

def moving_objects():
    global timer_counter
    if not GameRunning:
        return None
        
    if paused or ready or go or player_killed:
        return None
        
    timer_counter += 1
    player.move()
    
    for alien in alien_fleet.aliens:
        if alien.flying:
            alien.move([0,0])
            if isBulletHit(alien, player):
                player.explode()
                
            if alien.y>FIELD_HEIGHT + TOP_MARGIN+20:
                alien.y = TOP_MARGIN
    for bonus in bonuses:
        bonus.move();
        if bonus.y > FIELD_HEIGHT + TOP_MARGIN+20:
            bonuses.remove(bonus)
        if isBulletHit(bonus, player):
            bonus.execute()
            bonuses.remove(bonus)
            
    for bullet in user_bullet:
        bullet.move()
        alien_fleet.check_death()
        
    for bullet in user_bullet:
        if bullet.y<TOP_MARGIN+25:
           user_bullet.remove(bullet)
            
    # for bullet in alien_bullets:
    bullets_to_delete = []
    for bullet in list(alien_bullets):
        bullet.move()
        if bullet.y > FIELD_HEIGHT + TOP_MARGIN -10:
            bullets_to_delete.append(bullet)
        if isBulletHit(bullet, player):
            player.explode()
            
    for bullet in bullets_to_delete:
        if bullet in alien_bullets:
            alien_bullets.remove(bullet)
        
    alien_fleet.make_shoot()
    alien_fleet.alien_fly()
    
    if level<30:
        x = 60 - level
    else:
        x = 1
    if timer_counter % x == 0:
        alien_fleet.move_side()
    if timer_counter % (100 + x) == 0:
        alien_fleet.move_down()
    if alien_fleet.get_aliens_count() == 0:
        new_level()
                
# Handler to draw on canvas
def draw(canvas):
    draw_screen(canvas)
    canvas.draw_text(mes, [250, 250], 40, "Yellow")
    
    ######################
    #check a begin of game
    #
    if GameEnded:
        draw_end_screen(canvas)
    elif not GameRunning:
        draw_start_screen(canvas)
    else:
        ##################
        # game info
        draw_lives(canvas)
        draw_weapons(canvas)
        draw_level(canvas)
        draw_scores(canvas)
        draw_game_objects(canvas)
    return canvas

def readyGo():
    global ready, go
    ready = time.time()-level_time[len(level_time)-1]<0.7
    go = (not ready) and time.time()-level_time[len(level_time)-1]<1.5
    player_killed = time.time() - player_killed_at < 1.2
    
#Initialization and start of game
def start_game():
    global GameRunning, alien_fleet, player, GameEnded
    global scores, killed, level, level_time, bonus_count
    scores = 0
    bonus_count = [0, 0, 0, 0]
    killed = 0
    level = 0
    GameEnded = False
    GameRunning = True
    new_level()
    player = Player([FIELD_WIDTH //2, FIELD_HEIGHT + TOP_MARGIN-20], 3)
    return None

def stop_game():
    global GameRunning, GameEnded
    # aTimer.stop()
    GameEnded = True
    GameRunning = False
    level_time.append(time.time())
    frame.set_keydown_handler(dummy)
    frame.set_keyup_handler(dummy)    
    return None
    
# Handler for mouse click
def click_handler(position):
    if not GameRunning:
        start_game()
    #else:
    #    stop_game()
    return position

#### keydown_handler
def keydown(key):
    global keypressed, mes, shoot_count, player_speed
    keypressed = key
    if (key == simplegui.KEY_MAP['p']) or \
       (key == simplegui.KEY_MAP['P']):
        pause()
    else:
        if (key == simplegui.KEY_MAP['right']):
            #player.move('right')
            player_speed = PLAYER_SPEED
        elif (key == simplegui.KEY_MAP['left']):
            # player.move('left')
            player_speed = -PLAYER_SPEED
                
        if (key == simplegui.KEY_MAP['space'])and(GameRunning):
            if len(user_bullet) < weapon_level:
                b = Bullet([player.x, player.y], "LightBlue", -weapon_speed)
                user_bullet.append(b)  
                sndPlayer.play()
                shoot_count += 1
    return
#### keyup_handler to stop keydown
def keyup(key):
    global player_speed
    #if keytimer.is_running():
    #    keytimer.stop()
    if (key == simplegui.KEY_MAP['right'])or(key == simplegui.KEY_MAP['left']):
        player_speed = 0
    return

def isBulletHit(bullet, obj):
    if (bullet.y+bullet.height//2+2 > obj.y-obj.height // 2) and (bullet.y-bullet.height//2-2<obj.y+obj.height//2):
        if (bullet.x+bullet.width//2 +2> obj.x - obj.width//2) and (bullet.x-bullet.width//2 -2< obj.x + obj.width//2):
            return True
        else:
            return False
    else:
        return False        

def new_level():
    global level, alien_fleet, user_bullet, alien_bullets, current_back, player
    global level_time, player_speed
    level_time.append(time.time())
    current_back = random.randrange(12)
    level += 1
    player_speed = 0
    user_bullet = []
    alien_bullets = []
    alien_fleet = AliensFleet([250, 100])
    if level % 10 == 0:
        player.lives += 1
        sndBonus.play()
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Galaxian", 900, 600, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)    
    
aTimer = simplegui.create_timer(60, moving_objects)
aTimer.start()

# Start the frame animation
frame.start()
