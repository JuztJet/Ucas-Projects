import pygame


class home:
    def __init__(self, screen, w, h, Manager_class):

        self.screen = screen
        self.w = w
        self.h = h
        self.managerr = Manager_class()

        self.show_logo = True
        self.logo = pygame.image.load('Assets/spritesheet.png')
        self.play_button_image = pygame.image.load('Assets/play_button.png')
        self.skins_button_image = pygame.image.load('Assets/skins_button.png')
        self.settings_button_image = pygame.image.load('Assets/settings_button.png')
        self.frame_height = 800
        self.frame_image = [
            pygame.transform.smoothscale(pygame.image.load('Assets/frame_start.png').convert_alpha(),
                                         (15200, self.frame_height)),
            # pygame.transform.smoothscale(pygame.image.load('Assets/frame_end.png'), (w, h))
        ]

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.level_text_font = [
            pygame.font.Font(None, 27),
            pygame.font.Font(None, 27),
            pygame.font.Font(None, 27),
            pygame.font.Font(None, 27),
            pygame.font.Font(None, 27),
            
        ]
        self.level_frame_image = pygame.transform.smoothscale(pygame.image.load('Assets/level_frame.png').convert_alpha(), (2250, 150))
        self.level_test = pygame.image.load('Assets/level_test.png')
        self.level_frame_image_rect = [
            self.level_test.get_rect(topleft=(600, 200)),
            self.level_test.get_rect(topleft=(800, 200)),
            self.level_test.get_rect(topleft=(1000, 200)),
            self.level_test.get_rect(topleft=(1200, 200)),
            self.level_test.get_rect(topleft=(600, 400)),
        ]

        self.level_frame_image_row = [1,1,1,1,1]
        self.level_frame_image_x = [0,0,0,0,0]


        self.level_button = [
            pygame.Surface((150, 150)),
            pygame.Surface((150, 150)),
            pygame.Surface((150, 150)),
            pygame.Surface((150, 150)),
            pygame.Surface((150, 150)),
            
        ]
        self.level_text_type = [
            'Level 1',
            'Level 2',
            'Level 3',
            'Level 4',
            'Level 5',
            
        ]
        self.level_text = [
            self.level_text_font[0].render(self.level_text_type[0], True, '#74CAE2'),
            self.level_text_font[1].render(self.level_text_type[1], True, '#74CAE2'),
            self.level_text_font[2].render(self.level_text_type[2], True, '#74CAE2'),
            self.level_text_font[3].render(self.level_text_type[3], True, '#74CAE2'),
            self.level_text_font[4].render(self.level_text_type[4], True, '#74CAE2'),
            
        ]
        self.level_text_rect = [
            self.level_text[0].get_rect(center = (self.level_frame_image_rect[0].centerx, self.level_frame_image_rect[0].centery)),
            self.level_text[1].get_rect(center = (self.level_frame_image_rect[1].centerx, self.level_frame_image_rect[1].centery)),
            self.level_text[2].get_rect(center = (self.level_frame_image_rect[2].centerx, self.level_frame_image_rect[2].centery)),
            self.level_text[3].get_rect(center = (self.level_frame_image_rect[3].centerx, self.level_frame_image_rect[3].centery)),
            self.level_text[4].get_rect(center = (self.level_frame_image_rect[4].centerx, self.level_frame_image_rect[4].centery)),
            
        ]

        self.level_button[0].blit(self.level_frame_image, (0, 0), (0, 0, 470, 150))
        self.level_button[1].blit(self.level_frame_image, (0, 0), (0, 0, 470, 150))
        self.level_button[2].blit(self.level_frame_image, (0, 0), (0, 0, 470, 150))
        self.level_button[3].blit(self.level_frame_image, (0, 0), (0, 0, 470, 150))
        self.level_button[4].blit(self.level_frame_image, (0, 0), (0, 0, 470, 150))
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.transition_colour = '#7ED957'
        self.transition_width = 0
        self.transition = False
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.level_num, self.game, self.home_screen = 0, False, True
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.login_image =pygame.image.load('Assets/login.png')
        self.login_image_rect = pygame.Rect(((w/2)-250,h*0.52), (500,170))
        self.login_image_row = 1
        self.login_x=0
        self.login_button_clicked = False
        self.login_frame_y = h

        self.login_text_text = 'Enter username here'
        self.login_font = pygame.font.Font(None, 40)
        self.login_text = self.login_font.render(self.login_text_text, True, '#e0e0e0')
        self.login_text_rect = self.login_text.get_rect(bottomleft=(self.w/2-170, self.login_frame_y+120))
        self.login_clicked = False

        self.login_image_button = pygame.Surface((500, 170))  # New surface
        self.login_image_button.blit(self.login_image, (0, 0), (0, 0, 500, 170))
        self.login_text_clicked = False

        self.login_note_1_font = pygame.font.SysFont('Arial', 12)
        self.login_note_1_raw_text = "-Make a new account if you've never made one"
        self.login_note_1_text = self.login_note_1_font.render(self.login_note_1_raw_text, True, 'Black')
        self.login_note_1_text_rect = self.login_note_1_text.get_rect(topleft=(790, self.login_frame_y+120))

        self.login_note_2_font = pygame.font.SysFont('Arial', 12)
        self.login_note_2_font.bold = True
        self.login_note_2_raw_text = "This account already exists"
        self.login_note_2_text = self.login_note_2_font.render(self.login_note_2_raw_text, True, 'Red')
        self.login_note_2_text_rect = self.login_note_2_text.get_rect(topleft=(790, self.login_frame_y+120))

        self.login_button_font = pygame.font.SysFont('comicsansms', 58)
        self.login_button_text = self.login_button_font.render('Enter', True, 'White')
        self.login_button_rect = pygame.Rect((self.w/2-150, self.login_frame_y+150), (100, 30))
        self.login_button_clicked = False
        self.login_button_colour = 'dark gray'

        self.username_exists = False
        self.logged_in = False
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.col_frame = [1, 1]
        self.frame_image_x = [0, 0]
        self.clicked_level_frame_1 = [False, False, False]

        self.play_button_rect = pygame.Rect((0, h * 0.4), (328, 150))
        self.skins_button_rect = pygame.Rect((0, h * 0.55), (328, 150))

        self.settings_button_rect = pygame.Rect((0, h * 0.7), (328, 150))

        self.logo_rect = self.logo.get_rect(topleft=(w/2-250, -30))

        self.x, self.y = 0, 0
        self.row = 1
        self.col = 1
        self.col_play_button = [1, 1, 1]

        self.button_tick = [0, 0, 0]
        self.button_x = [0, 0, 0]

        self.play_button = pygame.Surface((470, 150))
        self.play_button.blit(self.play_button_image, (0, 0), (0, 0, 470, 150))

        self.skins_button = pygame.Surface((470, 150))  # New surface
        self.skins_button.blit(self.skins_button_image, (0, 0), (0, 0, 470, 150))

        self.settings_button = pygame.Surface((470, 150))  # New surface
        self.settings_button.blit(self.settings_button_image, (0, 0), (0, 0, 470, 150))
        self.mouse_clicked = False
        self.mouse_clicked_2 = False

    def generate_image(self, x, y, width, height, ):
        self.image = pygame.Surface((500, 500))
        self.image.blit(self.logo, (0, 0), (x, y, width, height))
    def login_image_animation(self, mouse_pos):
        if self.login_button_clicked:
            self.login_button_clicked_animation(mouse_pos)

        if self.login_image_rect.collidepoint(mouse_pos):
            if self.mouse_clicked:
                self.login_button_clicked = True
            if self.login_image_row!=9:
                self.login_image_row +=1
                self.login_x +=500


                self.login_image_button = pygame.Surface((500, 170))  # New surface
                self.login_image_button.blit(self.login_image, (0, 0), (self.login_x, 0, 500, 170))

        elif self.login_image_row!=1:
                self.login_image_row -=1
                self.login_x -=500
                self.login_image_button = pygame.Surface((500, 170))  # New surface
                self.login_image_button.blit(self.login_image, (0, 0), (self.login_x, 0, 500, 170))

    def login_button_clicked_animation(self, mouse_pos):

        if self.login_image_rect.y >420:

            self.login_image_rect.y-=30
            self.login_frame_y-=100
            self.login_text_rect.y = self.login_frame_y+120-28
            self.login_note_1_text_rect = self.login_note_1_text.get_rect(topleft=(self.login_text_rect.x-3, self.login_frame_y+120))
            self.login_note_2_text_rect = self.login_note_2_text.get_rect(topleft=(self.login_text_rect.x, self.login_frame_y+133))
            self.login_button_rect = pygame.Rect((self.w/2-100, self.login_frame_y+210), (200, 50))

            

        if self.login_text_rect.collidepoint(mouse_pos) and self.mouse_clicked and self.login_text_text == 'Enter username here':
            self.login_text_text = ''
            self.login_text = self.login_font.render(self.login_text_text, True, '#e0e0e0')
            self.login_text_clicked = True

        pygame.draw.rect(self.screen, 'White', ((self.w/2-210, self.login_frame_y), (420,350)),0,45)
        pygame.draw.rect(self.screen, 'Black', ((self.login_text_rect.x-2, self.login_text_rect.y-6), (330,35)),1,2)
        
        self.screen.blit(self.login_text, self.login_text_rect)
        self.screen.blit(self.login_note_1_text, self.login_note_1_text_rect)
        
        
        if len(self.login_text_text) >0 and self.login_text_clicked:
            self.login_button_enter_code(mouse_pos)
            if self.username_exists:
                    self.screen.blit(self.login_note_2_text, self.login_note_2_text_rect)
            pygame.draw.rect(self.screen, self.login_button_colour, self.login_button_rect, 0, 4)
            self.screen.blit(self.login_button_text, (self.login_button_rect.x + 47, self.login_button_rect.y+7))

    def login_button_enter_code(self, mouse_pos):
        if self.login_button_rect.collidepoint(mouse_pos):
            self.login_button_colour = 'light gray'
            if self.mouse_clicked:
                if not self.username_exists:
                    self.managerr.add_user(self.login_text_text)
                self.logged_in = True
        elif  self.login_button_colour == 'light gray':
            self.login_button_colour = 'dark gray'



    def add_text_to_username(self, raw_text):
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            self.login_text_text = self.login_text_text[:-1]
        elif len(self.login_text_text) < 12:
            if type(raw_text) == str:
                self.login_text_text += self.login_text_text.join(filter(None, [raw_text]))
        self.login_text = self.login_font.render(self.login_text_text, True, '#e0e0e0')
        if self.login_text_text != '':
            self.username_exists = self.managerr.check_username_existance(self.login_text_text)
            

    def create_list_logo(self):
        if self.row != 12:
            self.row += 1
            self.x += 500

            self.generate_image(self.x, self.y, 500, 500)
        elif self.col != 24 and self.row != 6:
            self.row = 1
            self.col += 1
            self.x = 0
            self.y += 500
            self.generate_image(self.x, self.y, 500, 500)
        else:
            self.row = 1
            self.col = 1
            self.x, self.y = 0, 0
            self.generate_image(self.x, self.y, 500, 500)
        # print("row =", self.row, "column =", self.col, "    x =", self.x, "y =", self.y)

    def create_button(self, mouse_pos, index_1, img, rect, button):



        if rect.collidepoint(mouse_pos):
            if self.col_play_button[index_1] != 12:  # Checking column num

                self.button_x[index_1] += 470
                self.col_play_button[index_1] += 1

                button = pygame.Surface((470, 150))  # New surface
                button.blit(img, (0, 0), (self.button_x[index_1], 0, 470, 150))

        elif self.col_play_button[index_1] != 1:

            self.button_x[index_1] -= 470
            self.col_play_button[index_1] -= 1

            button = pygame.Surface((470, 150))  # New surface
            button.blit(img, (0, 0), (self.button_x[index_1], 0, 470, 150))

        return button

    def level_frame(self, mouse_pos):
        if self.play_button_rect.collidepoint(mouse_pos):
            if self.mouse_clicked:
                self.show_logo = False
                if self.clicked_level_frame_1[0] == False:
                    self.clicked_level_frame_1[0] = True
                    self.col_frame[0] = 1
                    self.frame_image_x[0] = 0
                elif self.clicked_level_frame_1[0]:
                    self.clicked_level_frame_1[0] = False
        if self.clicked_level_frame_1[0]:

            if self.col_frame[0] != 15:  # Checking column num
                # print(4)
                self.frame_image_x[0] += 950
                self.col_frame[0] += 1

                self.frame_surface = pygame.Surface((950, self.frame_height))  # New surface
                self.frame_surface.blit(self.frame_image[0], (0, 0), (self.frame_image_x[0], 0, 950, self.frame_height))
                self.screen.blit(self.frame_surface, (500, 100))
            else:
                self.screen.blit(self.frame_surface, (500, 100))
                for counter in range(0, len(self.level_frame_image_rect)):
                    self.screen.blit(self.level_button[counter], self.level_frame_image_rect[counter])
                    self.screen.blit(self.level_text[counter], self.level_text_rect[counter])
        elif self.clicked_level_frame_1[0] == False:
            if self.col_frame[0] !=1:
                self.frame_image_x[0] -= 950
                self.col_frame[0] -= 1

                self.frame_surface = pygame.Surface((950, self.frame_height))  # New surface
                self.frame_surface.blit(self.frame_image[0], (0, 0), (self.frame_image_x[0], 0, 950, self.frame_height))
                self.screen.blit(self.frame_surface, (500, 100))
            

        for counter in range(0, len(self.level_frame_image_rect)):
            if self.level_frame_image_rect[counter].collidepoint(mouse_pos):
                if self.mouse_clicked and self.clicked_level_frame_1[0]:
                    self.screen.fill('White')
                    return True, counter+1
                if self.level_frame_image_row[counter] !=15:
                    self.level_frame_image_row[counter] +=1

                    self.level_button[counter] = pygame.Surface((150, 150))

                    self.level_button[counter].blit(self.level_frame_image, (0, 0), (self.level_frame_image_x[counter], 0, 150, 150))
                    self.level_frame_image_x[counter] +=150
                    self.level_text_font[counter].set_point_size(self.level_text_font[counter].get_point_size()+1)
                    self.level_text[counter] = self.level_text_font[counter].render(self.level_text_type[counter], True, 'Black')
                    self.level_text_rect[counter] = self.level_text[counter].get_rect(center = (self.level_frame_image_rect[counter].centerx, self.level_frame_image_rect[counter].centery))
            elif self.level_frame_image_row[counter] != 1:
                self.level_frame_image_row[counter] -= 1

                self.level_button[counter] = pygame.Surface((150, 150))

                self.level_button[counter].blit(self.level_frame_image, (0, 0), (self.level_frame_image_x[counter], 0, 150, 150))
                self.level_frame_image_x[counter] -= 150
                self.level_text_font[counter].set_point_size(self.level_text_font[counter].get_point_size() - 1)
                self.level_text[counter] = self.level_text_font[counter].render(self.level_text_type[counter], True,
                                                                                '#74CAE2')
                self.level_text_rect[counter] = self.level_text[counter].get_rect(
                    center=(self.level_frame_image_rect[counter].centerx, self.level_frame_image_rect[counter].centery))
        if self.transition:
            return True, self.level_num
        else:
            return False, 0


    def game_transition(self):
        if self.transition_width <= self.w:
            s = pygame.Surface((self.transition_width, self.h))  # the size of your rect
            self.transition_width += self.w * 0.02

            #s.set_alpha(230)  # alpha level
            #self.screen.fill('White')
            s.fill(('#74C850'))  # this fills the entire surface
            self.screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
            return False, True
        else:
            s = pygame.Surface((self.transition_width, self.h))  # the size of your rect
            s.fill(('#74C850'))  # this fills the entire surface
            self.screen.blit(s, (0, 0))  # (0,0) are the top-left coordinates
            pygame.mouse.set_visible(False)
            return True, False

    def mouse_click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.mouse_clicked_2 == False:
                self.mouse_clicked = True
                self.mouse_clicked_2 = True
            else:
                self.mouse_clicked = False
        else:
            self.mouse_clicked_2 = False
    def update(self, mouse_pos):
        if self.show_logo:
            self.create_list_logo()
            self.screen.blit(self.image, self.logo_rect)
        if not self.logged_in:
            self.login_image_animation(mouse_pos)
            self.screen.blit(self.login_image_button, self.login_image_rect)
            
        else:
            
            self.play_button = self.create_button(mouse_pos, 0, self.play_button_image, self.play_button_rect,
                                                self.play_button)
            self.skins_button = self.create_button(mouse_pos, 1, self.skins_button_image, self.skins_button_rect,
                                                self.skins_button)
            self.settings_button = self.create_button(mouse_pos, 2, self.settings_button_image, self.settings_button_rect,
                                                    self.settings_button)



            
            self.screen.blit(self.play_button, self.play_button_rect)
            self.screen.blit(self.skins_button, self.skins_button_rect)
            self.screen.blit(self.settings_button, self.settings_button_rect)
            
            # pygame.draw.rect(self.screen, "Black", self.level_frame_image_rect[0],3)
            # pygame.draw.rect(self.screen, "Blue", self.level_frame_image_rect[1],3)
            # pygame.draw.rect(self.screen, "Black", self.level_frame_image_rect[2],3)
            # pygame.draw.rect(self.screen, "Black", self.level_frame_image_rect[3],3)

        
        
        
        self.mouse_click()
        self.transition, self.level_num = self.level_frame(mouse_pos)

        if self.transition:
            self.game, self.home_screen = self.game_transition()


        return self.level_num, self.game, self.home_screen


