import pygame
import math





class Golf_Ball:
    def __init__(self, grav, x_pos, y_pos, colour, mass, dt, w, h, mouse_pos, screen, box_width, box_height, mouse_img_rect):
        self.mouse_img_rect = mouse_img_rect
        self.screen = screen
        self.resisting = False
        self.box_width= box_width
        self.box_height=box_height
        self.grav = grav  # -3.5
        self.dt = dt

        self.w = w
        self.h = h
        self.visible = True
        self.initial_vel = 0
        self.x_vel, self.y_vel = 0, 0
        self.resultant = 0
        self.mouse_pos = mouse_pos
        self.fired = True
        self.hit_time = 0
        self.held_down = False
        self.line = False
        self.boundary_pos = [(), (), ()]
        self.fired_resultant = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.colour = colour
        self.mass = mass
        self.angle = 0
        self.shoot = False
        self.resistance = 100
        self.velocity_constant = 0.15
        self.image = pygame.transform.smoothscale(pygame.image.load('Assets/golf.png').convert_alpha(), (40, 40))
        self.image_copy = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.spin_angel = 0
        self.x_inverse, self.y_inverse = False, False
        self.mask = pygame.mask.from_surface(self.image)
        self.previous_rect = self.rect.copy()

        print(2)

    def mouse_click_manager(self):
        if pygame.mouse.get_pressed()[0] == True and self.shoot == False:

            if self.rect.colliderect(self.mouse_img_rect):

                if self.line == False and self.held_down == False:
                    self.held_down = True
                    self.line = True
            if self.line and self.held_down == False and self.resultant <= 190:
                self.held_down = True
                self.line = False
                print("Hit")
                self.fired_resultant = self.resultant * self.velocity_constant
                self.initial_vel = int(round((((self.fired_resultant) / self.mass) * 1), 0))
                self.shoot = True
                self.x_inverse, self.y_inverse = False, False

        elif pygame.mouse.get_pressed()[0] == False:
            self.held_down = False

    def line_manager(self):
        if self.line:

            if abs(self.rect.centerx - self.mouse_pos[0]) != 0:
                self.angle = math.degrees(math.atan(abs(self.rect.centery - self.mouse_pos[1]) / abs(self.rect.centerx  - self.mouse_pos[0])))
                if self.mouse_pos[1] < self.rect.centery:
                    self.angle = self.angle * -1
                if self.mouse_pos[0] < self.rect.centerx:
                    self.angle = abs(self.angle - 90) + 90
            elif abs(self.rect.centerx  - self.mouse_pos[0]) == 0:
                if self.mouse_pos[1] > self.rect.centery:
                    self.angle = 90
                else:
                    self.angle = -90

            self.resultant = math.sqrt(abs(self.rect.centerx  - self.mouse_pos[0]) ** 2 + abs(self.rect.centery - self.mouse_pos[1]) ** 2)
            if self.resultant <= 190:
                self.boundary_pos[0] = self.mouse_pos

            if self.resultant > 190:
                pygame.draw.line(self.screen, "Red", (self.rect.centerx , self.rect.centery), self.boundary_pos[0], 3)
            elif self.resultant > 120:
                pygame.draw.line(self.screen, "Orange", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)
            elif self.resultant > 70:
                pygame.draw.line(self.screen, "Yellow", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)

            else:
                pygame.draw.line(self.screen, "Black", (self.rect.centerx , self.rect.centery), self.mouse_pos, 3)

    def shooting(self):
        self.previous_rect = self.rect.copy()
        self.x_vel = self.initial_vel * (math.cos(math.radians(self.angle)))
        self.y_vel = self.initial_vel * (math.sin(math.radians(self.angle)))
        if self.x_inverse:
            self.x_vel *= -1
        if self.y_inverse:
            self.y_vel *= -1
        self.rect.centerx -= self.x_vel * self.dt
        self.rect.centery -= self.y_vel * self.dt
        if not self.resisting:
            self.initial_vel -= self.resistance * self.dt
            if self.initial_vel <= 10:
                self.shoot = False


        # self.rect = pygame.Rect((self.x_pos - 10, self.y_pos - 10), (20, 20))

        #print( '- Xpos=', self.x_pos, '- Ypos=', self.y_pos, '-  Speed=', self.initial_vel, self.dt)
        # self.rect.move_ip(self.x_pos,self.y_pos)

    def bounce_detection(self):
        if self.rect.left <= self.box_width:#Left
            if self.rect.left < self.box_width:
                self.rect.left = self.box_width+1

            if self.x_inverse:
                self.x_inverse = False
            else:
                self.x_inverse = True

        if self.rect.right >= (self.box_width+self.w):#Right
            if self.rect.right > (self.box_width + self.w):
                self.rect.right = self.box_width+self.w-1
            if self.x_inverse:
                self.x_inverse = False
            else:
                self.x_inverse = True

        if self.rect.top <= self.box_height:#Top
            if self.rect.top < self.box_height:
                self.rect.top = self.box_height+1
            if self.y_inverse:
                self.y_inverse = False
            else:
                self.y_inverse = True

        if (self.rect.bottom) >= self.box_height+self.h:#Bottom
            if (self.rect.bottom) > self.box_height + self.h:
                self.rect.bottom = self.box_height+self.h-1
            if self.y_inverse:
                self.y_inverse = False
            else:
                self.y_inverse = True




    def update(self, mouse_pos, dt, mouse_img_rect):
        self.mouse_pos = mouse_pos
        self.dt = dt
        self.mouse_img_rect = mouse_img_rect

        if self.visible:
            if self.shoot:
                self.shooting()
                self.bounce_detection()
                self.spin_angel += self.initial_vel * 6 * self.dt
                self.image_copy = pygame.transform.rotate(self.image, self.spin_angel)

            else:
                self.mouse_click_manager()
                self.line_manager()

            self.resistance = 300
            self.screen.blit(self.image_copy, (self.rect.centerx - int(self.image_copy.get_width() / 2),
                                               self.rect.centery - int(self.image_copy.get_height() / 2)))
            pygame.draw.rect(self.screen, 'White', self.rect, 1)
            pygame.draw.line(self.screen, 'Blue', self.rect.center, self.previous_rect.center, 2  )
            #print(self.rect.center, self.previous_rect.center)

            #print(self.dt)