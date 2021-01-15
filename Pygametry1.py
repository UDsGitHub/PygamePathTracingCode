import pygame, sys
from pygame.locals import*
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption('My Pygame Window')

scrn_size = (500, 500)
screen = pygame.display.set_mode(scrn_size, 0, 32)

entity_size = (40, 60)
entity_location = [-25, 100]
entity_y_speed = 0
entity = pygame.Rect(entity_location, entity_size)
entity_org_pos = (entity.x, entity.y)

# test_rect = pygame.Rect(100, 100, 100, 50)

# movement stuff
moving_right = False
moving_left = False
moving = False

# proxy surface for line drawing
line_surf = pygame.Surface(scrn_size)
line_surf.fill((78, 50, 150))

rect_list = []
temp_rect = None


def motioning():
    global moving
    entity.y += entity_y_speed
    moving = True


counter = 0
pos_count = 1
entity_positions = [entity.center]
last_pos = entity_positions[0]
next_pos = entity_positions[0]
while True:
    screen.blit(line_surf, (0, 0))
    # pygame.draw.rect(screen, (0, 255, 255), entity)
    temp_rect = pygame.draw.rect(screen, (0, 255, 255), entity)
    rect_list.append(temp_rect)
    # pygame.draw.line(screen, (0, 0, 0), (100, 300), (400, 490))
    # entity_pos = (entity.x, entity.y)
    # pos1 = rect_list[0].topleft
    # entity_positions = [pos1]
    entity_positions.append(rect_list[counter].center)
    counter += 1
    # print(entity_positions)

    moving_right = True

    # screen bottom boundary collision
    if entity.y > scrn_size[1]-entity.height:
        entity_y_speed = -entity_y_speed
    else:
        entity_y_speed += 0.2
    motioning()

    if moving_right:
        entity.x += 3
    if moving_left:
        entity.x -= 3


    if moving:
        pygame.draw.line(line_surf, (0, 0, 0), last_pos, next_pos, 1)
        last_pos = entity_positions[pos_count-1]
        next_pos = entity_positions[pos_count]
    pos_count += 1

# collision stuff
#     if entity.colliderect(test_rect):
#         pygame.draw.rect(screen, (255, 0, 0), test_rect)
#     else:
#         pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_RIGHT:
        #         moving_right = True
        #         moving = True
        #     if event.key == K_LEFT:
        #         moving_left = True
        # if event.type == KEYUP:
        #     if event.key == K_RIGHT:
        #         moving_right = False
        #     if event.key == K_LEFT:
        #         moving_left = False

    pygame.display.update()
    clock.tick(60)
