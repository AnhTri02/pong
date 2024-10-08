import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tri pong")

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PINK = (254,127,156)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
  
  COLOR = WHITE
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height


  def draw(self,win):
    pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win, paddles):
    win.fill((PINK))
    
    for paddle in paddles:
        paddle.draw(win)
    
    
    
    pygame.display.update()


def main():
  run = True
  clock = pygame.time.Clock()
  
  
  left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
  right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH , HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT )
  
  while run:
      clock.tick(FPS)
      draw(WIN,[left_paddle, right_paddle] )
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
          break
        
  pygame.quit()


if __name__ == '__main__':
    main()
