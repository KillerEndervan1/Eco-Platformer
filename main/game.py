import pygame as pg
import math,sys
import random as r
pg.init()
display = pg.display.set_mode((640,480))
class s():
    clock = pg.time.Clock()
    x,y =350,455
    p = pg.image.load('plr.png')
    p.convert()
    plr = p.get_rect()
class player():
    def left():
        s.x -=1
    def right():
        s.x +=1
class gmap():
    b = pg.image.load('B.png')
    b.convert()
    t = pg.image.load('trash.png')
    t.convert()
    c = pg.image.load('cloud.png')
    c.convert()
    g = pg.image.load('grass.png')
    g.convert()
    b = pg.transform.rotozoom(b,0,650)
    bg = b.get_rect()
    bg.center = 320,300
    g = pg.transform.rotozoom(g,0,1.9)
    ga = g.get_rect()
    ga.center = 30,450
    gb = g.get_rect()
    gb.center = 90,450
    gc = g.get_rect()
    gc.center = 150,450
    gd = g.get_rect()
    gd.center = 210,450
    ge = g.get_rect()
    ge.center = 270,450
    gf = g.get_rect()
    gf.center = 330,450
    g1 = g.get_rect()
    g1.center = 390,450
    g2 = g.get_rect()
    g2.center = 450,450
    g3 = g.get_rect()
    g3.center = 510,450
    g4 = g.get_rect()
    g4.center = 570,450
    g5 = g.get_rect()
    g5.center = 630,450
    c1 =c.get_rect()
    c2 =c.get_rect()
    trash = t.get_rect()
class game():
    x,y =r.randint(20,600),455
    gmap.trash.center = x,y
    pg.display.set_icon(s.p)
    pg.display.set_caption('ecoplatformer - наслаждайтесь сбором мусора')
    while True:
        s.clock.tick(60)
        gmap.c1.center = 400,10
        gmap.c2.center = 100,50
        s.plr.center = s.x,s.y
        display.blits(((gmap.b,gmap.bg,None),(gmap.g,gmap.ga,None),(gmap.g,gmap.gb,None),(gmap.g,gmap.gc,None),(gmap.g,gmap.gd,None),(gmap.g,gmap.ge,None),(gmap.g,gmap.gf,None),(gmap.g,gmap.g1,None),(gmap.g,gmap.g2,None),(gmap.g,gmap.g3,None),(gmap.g,gmap.g4,None),(gmap.g,gmap.g5,None),(gmap.t,gmap.trash,None),(gmap.c,gmap.c2,None),(gmap.c,gmap.c1)))
        display.blit(s.p,s.plr,None)
        if s.x == x and s.y == y:
            print('win!')
            s.x,s.y = 320,455
            x,y =r.randint(20,600),455
            gmap.trash.center = x,y
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    player.left()
                if event.key == pg.K_d:
                    player.right()
        pg.display.update()
        pg.display.flip()
