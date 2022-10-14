import pygame
pygame.init()
display = pygame.display.set_mode((250,250))
display.fill((0,100,0))
SCALE = 5
max_so_far = 0
max_val = 0
n = 2
UPPER_LIMIT = 20
iters = {}
start_cord = (0,0)
BLACK = (0,0,0)
font = pygame.font.Font(None,50)
for i in range(2,UPPER_LIMIT + 1):
  n = i
  count = 0
  start_number = i
  while True:
    if n == 1:
      iters[start_number * SCALE] = count * SCALE
      if count > max_so_far:
        max_so_far = count
        max_val = start_number
      break
    elif n % 2 == 0:
      n = n/2
      count += 1
    else:
      n = (n * 3) + 1
      count += 1

coords = list(iters.items())
pygame.draw.lines(display,BLACK, False,coords)
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display , (0, 0))
msg = font.render(str(max_so_far), True, BLACK)
display.blit(msg, (10,10))
pygame.display.update()