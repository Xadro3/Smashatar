import pygame
from pynput import keyboard

def loadImage(filename, colorkey=None):
    image = pygame.image.load(filename)

    if image.get_alpha() == None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image

class Sprite():
    def __init__(self,xPos,yPos, screen,key):
        self.xPos = xPos
        self.yPos = yPos
        self.screen = screen
        self.armL = loadImage("./Patrick Arm L.png")
        self.armR = loadImage("./Patrick Ashbringer arm.png")
        self.mainC = loadImage("Patrick_Armless2.png")
        self.table = loadImage("table.png")
        self.ability_1 = loadImage("BoJ.png")
        self.ability_2 = loadImage("DS.png")
        self.ability_3 = loadImage("HoW.png")
        self.ability_4 = loadImage("Judgement.png")
        self.ability_5 = loadImage("TV.png")
        self.pivot = [300,460]
        self.angle_1 = 180
        self.angle_2 = 205
        self.angle_3 = 100
        self.angle_4 = 215
        self.angle_5 = 125
        self.offset_1 = pygame.math.Vector2(0,0)
        self.offset_2 = pygame.math.Vector2(50,35)
        self.offset_3 = pygame.math.Vector2(-55,-170)
        self.offset_4 = pygame.math.Vector2(100,50)
        self.offset_5 = pygame.math.Vector2(-50,-105)
        self.lastKey = key
        self.hasKey = False;

    def draw(self,screen,image,position):
        screen.blit( image,position)


    def idle(self):


        self.draw(self.screen, self.armL, (190, 210))
        self.draw(self.screen, self.mainC, (180, 90))
        self.draw(self.screen, self.table, (0, 300))
        self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15) , (500, 485))
        self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
        self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
        self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
        self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
        self.draw(self.screen, self.armR, (355, 55))

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


        if hasattr(self.lastKey,'char'):
            if self.hasKey:
                if self.lastKey.char == '5':
                    self.screen.fill((0, 255, 0, 0))
                    self.draw(self.screen, self.armL, (190, 210))
                    self.draw(self.screen, self.mainC, (180, 90))
                    self.draw(self.screen, self.table, (0, 300))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15), (500, 485))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
                    rotated_arm = pygame.transform.rotozoom(self.armR, -self.angle_1, 1)
                    rotated_offset = self.offset_1.rotate(self.angle_1)
                    rect = rotated_arm.get_rect(center=self.pivot + rotated_offset)
                    self.screen.blit(rotated_arm, rect)
                if self.lastKey.char == '1':
                    self.screen.fill((0, 255, 0, 0))
                    self.draw(self.screen, self.armL, (190, 210))
                    self.draw(self.screen, self.mainC, (180, 90))
                    self.draw(self.screen, self.table, (0, 300))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15), (500, 485))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
                    rotated_arm = pygame.transform.rotozoom(self.armR, -self.angle_2, 1)
                    rotated_offset = self.offset_2.rotate(self.angle_2)
                    rect = rotated_arm.get_rect(center=self.pivot + rotated_offset)
                    self.screen.blit(rotated_arm, rect)
                if self.lastKey.char == '2':
                    self.screen.fill((0, 255, 0, 0))
                    self.draw(self.screen, self.armL, (190, 210))
                    self.draw(self.screen, self.mainC, (180, 90))
                    self.draw(self.screen, self.table, (0, 300))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15), (500, 485))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
                    rotated_arm = pygame.transform.rotozoom(self.armR, -self.angle_3, 1)
                    rotated_offset = self.offset_3.rotate(self.angle_3)
                    rect = rotated_arm.get_rect(center=self.pivot + rotated_offset)
                    self.screen.blit(rotated_arm, rect)
                if self.lastKey.char == 'q':
                    self.screen.fill((0, 255, 0, 0))
                    self.draw(self.screen, self.armL, (190, 210))
                    self.draw(self.screen, self.mainC, (180, 90))
                    self.draw(self.screen, self.table, (0, 300))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15), (500, 485))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
                    rotated_arm = pygame.transform.rotozoom(self.armR, -self.angle_4, 1)
                    rotated_offset = self.offset_4.rotate(self.angle_4)
                    rect = rotated_arm.get_rect(center=self.pivot + rotated_offset)
                    self.screen.blit(rotated_arm, rect)
                if self.lastKey.char == 'e':
                    self.screen.fill((0, 255, 0, 0))
                    self.draw(self.screen, self.armL, (190, 210))
                    self.draw(self.screen, self.mainC, (180, 90))
                    self.draw(self.screen, self.table, (0, 300))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_1, -15), (500, 485))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_2, -15), (380, 452))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_3, -15), (260, 419))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_4, -15), (140, 386))
                    self.draw(self.screen, pygame.transform.rotate(self.ability_5, -15), (20, 353))
                    rotated_arm = pygame.transform.rotozoom(self.armR, -self.angle_5, 1)
                    rotated_offset = self.offset_5.rotate(self.angle_5)
                    rect = rotated_arm.get_rect(center=self.pivot + rotated_offset)
                    self.screen.blit(rotated_arm, rect)




def keyPress(key,gamestate):
    gamestate.player.lastKey = key
    gamestate.player.hasKey = True
def keyRelease(key, gamestate):

    gamestate.player.hasKey = False



class GameState():
    running = True
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("smashatar")
    player = Sprite(1,448,screen,'h')

def game():
    gameState = GameState
    screen = gameState.screen
    pygame.key.set_repeat(1,0)
    listener = keyboard.Listener(lambda event: keyPress(event, gameState), lambda event: keyRelease(event,gameState))
    listener.start()


    while gameState.running:
        gameState.clock.tick(45)
        screen.fill((0, 255, 0, 0))
        gameState.player.idle();


        pygame.display.flip()
game()





