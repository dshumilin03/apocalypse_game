# <editor-fold desc="Imports">
import pygame
import random
import sys
from os import path
import time

# </editor-fold>

# <editor-fold desc="vars">
won = False
about = False
paused = False
dead = False
intro = True
gear = False
target = False
skin1 = False
skin2 = False
skin3 = False
choiced_player_image = 0
authorization_procedure = True
sy = 1
sx = 3
pts = 0
volume = 0
need = 100
shootlimit = 9
meteors = 8
# </editor-fold>

# <editor-fold desc="Fonts">
pygame.font.init()
smalltext = pygame.font.SysFont("comicsansms", 25)
mediumtext = pygame.font.SysFont("comicsansms", 50)
smallmediumtext = pygame.font.SysFont("comicsansms", 35)
largetext = pygame.font.SysFont("comicsansms", 75)
# </editor-fold>

# <editor-fold desc="Screen">
img_dir = path.join(path.dirname(__file__), 'img')
WIDTH = 480
HEIGHT = 600
FPS = 60
# </editor-fold>

# <editor-fold desc="colors">
GRAY = (75, 75, 75)
GRAY2 = (65, 65, 65)
GRAY_SELECTION = (40, 40, 50)
GRAY_SELECTION2 = (50, 50, 60)
GRAY_SELECTION3 = (40, 40, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
D_RED = (200, 0, 0)
GREEN = (0, 255, 0)
D_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 160, 255)
# </editor-fold>

# <editor-fold desc="initialize pygame and create game window">
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apocalypse")
clock = pygame.time.Clock()
# </editor-fold>

# <editor-fold desc="Sounds">
crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.set_volume(0.08 * (0.01 * volume))
pygame.mixer.music.load("purpleheart.mp3")
pygame.mixer.music.set_volume(0.2 * (0.01 * volume))
laser_sound = pygame.mixer.Sound("laser2.wav")
laser_sound.set_volume(0.1 * (0.01 * volume))
pygame.mixer.music.play(-1)
player_crashed = pygame.mixer.Sound("player_crash.wav")
player_crashed.set_volume(0.3 * (0.01 * volume))

# </editor-fold>

# <editor-fold desc="Load all game graphics">
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
menu_background = pygame.image.load(path.join(img_dir, "71.jpg")).convert()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_blue.png")).convert()
player_img2 = pygame.image.load(path.join(img_dir, "playerShip2_blue.png")).convert()
player_img3 = pygame.image.load(path.join(img_dir, "playerShip3_blue.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
game_over_img = pygame.image.load(path.join(img_dir, "68.jpg")).convert()
about_img = pygame.image.load(path.join(img_dir, "about.png")).convert()
lock_img = pygame.image.load(path.join(img_dir, "lock.png")).convert()
pygame.transform.scale(lock_img, (50, 35))
about_img_rect = about_img.get_rect()
game_over_img_rect = game_over_img.get_rect()
menu_background_rect = menu_background.get_rect()
background_rect = background.get_rect()
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []


# </editor-fold>


def menu():
    global gear
    global about
    global dead
    global intro
    global pts
    global running
    global paused
    global authorization_procedure
    select_1 = False
    select_2 = False
    select_3 = False
    select_4 = False
    authorization_procedure = False
    intro = True
    first_select = False
    while intro:

        screen.blit(menu_background, menu_background_rect)
        menu_text = mediumtext.render("Apocalypse", True, LIGHT_BLUE)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 302 >= mouse[0] >= 180 and 200 >= mouse[1] >= 155:
            first_select = False
            select_1 = True
            select_2 = False
            select_3 = False
            select_4 = False
        elif first_select is False:
            select_1 = False

        if 380 >= mouse[0] >= 115 and 285 >= mouse[1] >= 245:
            first_select = False
            select_1 = False
            select_2 = True
            select_3 = False
            select_4 = False
        elif first_select is False:
            select_2 = False

        if 315 >= mouse[0] >= 170 and 377 >= mouse[1] >= 340:
            first_select = False
            select_1 = False
            select_2 = False
            select_3 = True
            select_4 = False
        elif first_select is False:
            select_3 = False

        if 358 >= mouse[0] >= 128 and 547 >= mouse[1] >= 510:
            first_select = False
            select_1 = False
            select_2 = False
            select_4 = True
            select_3 = False
        elif first_select is False:
            select_4 = False

        if select_1 is False:
            Play = mediumtext.render("PLAY", True, LIGHT_BLUE)
            screen.blit(Play, [180, 140])
        else:
            Play = mediumtext.render("PLAY", True, BLUE)
            screen.blit(Play, [180, 140])

        if select_2 is False:
            gears = mediumtext.render("SETTINGS", True, LIGHT_BLUE)
            screen.blit(gears, [110, 230])
        else:
            gears = mediumtext.render("SETTINGS", True, BLUE)
            screen.blit(gears, [110, 230])

        if select_3 is False:
            quit = mediumtext.render("QUIT", True, LIGHT_BLUE)
            screen.blit(quit, [170, 320])
        else:
            quit = mediumtext.render("QUIT", True, BLUE)
            screen.blit(quit, [170, 320])

        if select_4 is False:
            stats_text = mediumtext.render("Statistics", True, LIGHT_BLUE)
            screen.blit(stats_text, [125, 490])
        else:
            stats_text = mediumtext.render("Statistics", True, BLUE)
            screen.blit(stats_text, [125, 490])

        screen.blit(menu_text, [110, 0])

        pygame.draw.rect(screen, WHITE, ((395, 150), (75, 50)))
        if 470 >= mouse[0] >= 395 and 200 >= mouse[1] >= 150 and click[0] == 1:
            ladders()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if select_1:
                    intro = False
                    inventory()

                elif select_3:
                    quit()
                    pygame.quit()
                else:
                    intro = True
                    running = False

                if select_4:
                    player_statistics()

                if select_2:
                    gear = True
                    settings()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    if first_select:
                        if select_1:
                            select_1, select_2 = select_2, select_1
                        elif select_2:
                            select_2, select_3 = select_3, select_2
                        elif select_3:
                            select_3, select_4 = select_4, select_3
                        elif select_4:
                            select_4, select_1 = select_1, select_4

                    if not first_select:
                        select_1 = True
                        first_select = True
                if event.key == pygame.K_RETURN:
                    if select_1:
                        intro = False
                        inventory()

                    elif select_2:
                        gear = True
                        settings()
                    elif select_3:
                        quit()
                        pygame.quit()
                    elif select_4:
                        player_statistics()

        pygame.display.update()
        clock.tick(60)


def auth(name, password_field):
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    query = "SELECT login, user_password, nickname FROM players where login = ('{}') and" \
            " user_password = ('{}')".format(name, password_field)
    cursor.execute(query)
    row = cursor.fetchone()
    if row is not None:

        player.nickname = row[2]
        cnx.close()
        return True
    else:
        cnx.close()
        return False


def sign(nickname, name, password_field):
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    query = "INSERT INTO players(nickname, login, user_password) VALUES('{}', '{}', '{}')".format(
        nickname, name, password_field)

    try:
        cursor.execute(query)
    except mysql.connector.errors.IntegrityError:
        return False
    queries = ["INSERT INTO daily_current_ladder(user_nickname, user_max_daily_points) VALUES('{}', 0)",
               "INSERT INTO weekly_current_ladder(user_nickname, user_max_weekly_points) VALUES('{}', 0)",
               "INSERT INTO monthly_current_ladder(user_nickname, user_max_monthly_points) VALUES('{}', 0)",
               "INSERT INTO daily_past_ladder(user_nickname, user_past_daily_points) VALUES('{}', 0)",
               "INSERT INTO weekly_past_ladder(user_nickname, user_past_weekly_points) VALUES('{}', 0)",
               "INSERT INTO monthly_past_ladder(user_nickname, user_past_monthly_points) VALUES('{}', 0)",
               "INSERT INTO inventory(user_nickname, space_ship2, space_ship3) VALUES('{}', false, false)",
               "INSERT INTO statistics(user_nickname, max_points, total_points, games_played, max_daily_points, "
               "max_weekly_points, max_monthly_points) VALUES('{}', 0, 0, 0, 0, 0, 0)"]
    for elem in queries:
        cursor.execute(elem.format(nickname))

    cnx.commit()
    cnx.close()
    return True


def update_stats(points):
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    query = "UPDATE statistics SET total_points = total_points + %s WHERE user_nickname = %s"
    query2 = "UPDATE statistics SET games_played = games_played + 1 WHERE user_nickname = %(nick)s"
    query3 = "SELECT max_points, max_daily_points, max_weekly_points, max_monthly_points FROM statistics WHERE " \
             "user_nickname = %(nick)s"
    params = {'nick': player.nickname}
    data2 = (points, player.nickname)
    cursor.execute(query, data2)
    cursor.execute(query2, params)
    cursor.execute(query3, params)
    row = cursor.fetchone()

    if row[0] < points:
        cursor.execute("UPDATE statistics SET max_points = %s WHERE user_nickname = %s", data2)
        if points >= 1000:
            cursor.execute("UPDATE inventory SET space_ship3 = %s WHERE user_nickname = %s", (1, player.nickname))
        elif points >= 350:
            cursor.execute("UPDATE inventory SET space_ship2 = %s WHERE user_nickname = %s", (1, player.nickname))

    if row[1] < points:
        cursor.execute("UPDATE statistics SET max_daily_points = %s WHERE user_nickname = %s", data2)
    if row[2] < points:
        cursor.execute("UPDATE statistics SET max_weekly_points = %s WHERE user_nickname = %s", data2)
    if row[3] < points:
        cursor.execute("UPDATE statistics SET max_monthly_points = %s WHERE user_nickname = %s", data2)

    cnx.commit()
    cnx.close()


def show_stats():
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    query = "SELECT max_points, total_points, games_played,  max_daily_points, max_weekly_points, max_monthly_points" \
            " FROM statistics WHERE user_nickname = %(nick)s"
    params = {'nick': player.nickname}
    cursor.execute(query, params)
    row = cursor.fetchone()
    cnx.close()
    return row


def authorization_window():
    latency = 0
    name = ""
    password_field = ""
    selection_1 = False
    selection_2 = False
    need_to_start = False
    need_to_quit = False
    start_latency = False
    wrong_data = False
    need_to_reg = False
    while authorization_procedure is True:
        screen.fill(GRAY)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        authorization_text = mediumtext.render("Authorization", True, WHITE)
        login_text = smalltext.render("Username", True, WHITE)
        password_text = smalltext.render("Password", True, WHITE)
        text_log_in = smalltext.render("Log in", True, WHITE)
        text_cancel = smalltext.render("Cancel", True, WHITE)
        text_sign_in = smalltext.render("Sign in", True, WHITE)
        invalid_data = smalltext.render("Wrong password or login", True, RED)
        screen.blit(authorization_text, (75, 0))
        screen.blit(login_text, (25, 143))
        screen.blit(password_text, (25, 215))

        username_text = smalltext.render(name, True, WHITE)
        password_field_text = smalltext.render(password_field, True, WHITE)
        hidden_password_text = smalltext.render("*" * len(password_field), True, WHITE)

        screen.blit(username_text, (155, 143))
        screen.blit(hidden_password_text, (155, 212))

        pygame.draw.rect(screen, WHITE, (150, 143, 315, 38), 3)
        pygame.draw.rect(screen, WHITE, (150, 215, 315, 38), 3)

        pygame.draw.rect(screen, WHITE, (50, 315, 100, 45), 3)
        # pygame.draw.rect(screen, BLACK, (53, 318, 94, 39), 3)

        pygame.draw.rect(screen, WHITE, (225, 315, 100, 45), 3)
        # pygame.draw.rect(screen, BLACK, (228, 318, 94, 39), 3)

        pygame.draw.rect(screen, WHITE, (355, 315, 100, 45), 3)

        if 465 > mouse[0] > 150 and 181 > mouse[1] > 143 and click[0] == 1:
            selection_1 = True
            selection_2 = False
        elif 465 > mouse[0] > 150 and 181 + 73 > mouse[1] > 143 + 73 and click[0] == 1:
            selection_2 = True
            selection_1 = False
        elif click[0] == 1:
            selection_1 = False
            selection_2 = False

        if 150 > mouse[0] > 50 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION, (52, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if auth(name, password_field) is True:
                        need_to_start = True
                        start_latency = True
                    else:
                        wrong_data = True
        elif 325 > mouse[0] > 225 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION, (227, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    start_latency = True
                    need_to_quit = True
        elif 450 > mouse[0] > 360 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION, (357, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    start_latency = True
                    need_to_reg = True
        screen.blit(text_log_in, (65, 315))
        screen.blit(text_cancel, (236, 316))
        screen.blit(text_sign_in, (365, 315))

        if wrong_data is True:
            screen.blit(invalid_data, (25, 260))

        if start_latency is True:
            latency += 1

        if latency == 7:
            latency = 0
            if need_to_start:
                menu()
            elif need_to_quit:
                pygame.quit()
                quit()
            elif need_to_reg:
                registration_window()

        if selection_1 is True:
            pygame.draw.rect(screen, GRAY_SELECTION, (147, 140, 321, 44), 3)
        if selection_2 is True:
            pygame.draw.rect(screen, GRAY_SELECTION, (147, 212, 321, 44), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    selection_2, selection_1 = selection_1, selection_2

                if (event.unicode.isalpha() or event.unicode.isdigit() or event.unicode == '_') and len(
                        name) < 15 and selection_1 is True:
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE and selection_1 is True:
                    name = name[:-1]

                if (event.unicode.isalpha() or event.unicode.isdigit() or event.unicode == '_') and len(
                        password_field) < 15 and selection_2 is True:
                    password_field += event.unicode
                elif event.key == pygame.K_BACKSPACE and selection_2 is True:
                    password_field = password_field[:-1]

        pygame.display.update()
        clock.tick(60)


def registration_window():
    latency = 0
    name = ""
    password_field = ""
    nickname = ""
    selection_3 = False
    selection_1 = False
    selection_2 = False
    need_to_quit = False
    start_latency = False
    need_to_reg = False
    wrong_data = False
    need_to_back = False
    while authorization_procedure is True:
        screen.fill(GRAY2)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        registration_text = mediumtext.render("Registration", True, WHITE)
        nickname_text = smalltext.render("Nickname", True, WHITE)
        login_text = smalltext.render("Username", True, WHITE)
        password_text = smalltext.render("Password", True, WHITE)
        text_sign_in = smalltext.render("Sign in", True, WHITE)
        text_cancel = smalltext.render("Cancel", True, WHITE)
        text_back = smalltext.render("Back", True, WHITE)
        invalid_data = smalltext.render("This login has already been taken", True, RED)
        screen.blit(registration_text, (102, -10))
        screen.blit(login_text, (25, 143))
        screen.blit(password_text, (25, 215))
        screen.blit(nickname_text, (25, 71))
        nickname_text_writeble = smalltext.render(nickname, True, WHITE)
        username_text = smalltext.render(name, True, WHITE)
        password_field_text = smalltext.render(password_field, True, WHITE)
        hidden_password_text = smalltext.render("*" * len(password_field), True, WHITE)

        screen.blit(nickname_text_writeble, (155, 143 - (212 - 140)))
        screen.blit(username_text, (155, 143))
        screen.blit(hidden_password_text, (155, 212))

        pygame.draw.rect(screen, WHITE, (150, 143, 315, 38), 3)
        pygame.draw.rect(screen, WHITE, (150, 215, 315, 38), 3)
        pygame.draw.rect(screen, WHITE, (150, 71, 315, 38), 3)

        pygame.draw.rect(screen, WHITE, (50, 315, 100, 45), 3)
        # pygame.draw.rect(screen, BLACK, (53, 318, 94, 39), 3)

        pygame.draw.rect(screen, WHITE, (225, 315, 100, 45), 3)
        # pygame.draw.rect(screen, BLACK, (228, 318, 94, 39), 3)

        pygame.draw.rect(screen, WHITE, (355, 315, 100, 45), 3)

        if 465 > mouse[0] > 150 and 181 > mouse[1] > 143 and click[0] == 1:
            selection_1 = False
            selection_2 = True
            selection_3 = False
        elif 465 > mouse[0] > 150 and 181 + 73 > mouse[1] > 143 + 73 and click[0] == 1:
            selection_2 = False
            selection_1 = False
            selection_3 = True
        elif 465 > mouse[0] > 150 and 181 + 73 > mouse[1] > 143 - 73 and click[0] == 1:
            selection_2 = False
            selection_1 = True
            selection_3 = False
        elif click[0] == 1:
            selection_3 = False
            selection_1 = False
            selection_2 = False

        if 150 > mouse[0] > 50 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION2, (52, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if sign(nickname, name, password_field) is True:
                        need_to_reg = True
                        start_latency = True
                    else:
                        wrong_data = True
        elif 325 > mouse[0] > 225 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION2, (227, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    start_latency = True
                    need_to_quit = True
        elif 450 > mouse[0] > 360 and 315 < mouse[1] < 360 and click[0] == 1:
            pygame.draw.rect(screen, GRAY_SELECTION2, (357, 317, 96, 41))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    start_latency = True
                    need_to_back = True
        screen.blit(text_sign_in, (60, 315))
        screen.blit(text_cancel, (236, 316))
        screen.blit(text_back, (375, 315))

        if wrong_data is True:
            screen.blit(invalid_data, (25, 260))

        if start_latency is True:
            latency += 1

        if latency == 7:
            latency = 0
            if need_to_reg:
                authorization_window()
            elif need_to_quit:
                pygame.quit()
                quit()
            elif need_to_back:
                authorization_window()

        if selection_1 is True:
            pygame.draw.rect(screen, GRAY_SELECTION3, (147, 68, 321, 44), 3)
        if selection_2 is True:
            pygame.draw.rect(screen, GRAY_SELECTION3, (147, 140, 321, 44), 3)
        if selection_3 is True:
            pygame.draw.rect(screen, GRAY_SELECTION3, (147, 212, 321, 44), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    if selection_1:
                        selection_2, selection_1 = selection_1, selection_2
                    elif selection_2:
                        selection_3, selection_2 = selection_2, selection_3
                    elif selection_3:
                        selection_3, selection_1 = selection_1, selection_3

                if (event.unicode.isalpha() or event.unicode.isdigit() or event.unicode == '_') and len(
                        nickname) < 15 and selection_1 is True:
                    nickname += event.unicode
                elif event.key == pygame.K_BACKSPACE and selection_1 is True:
                    nickname = nickname[:-1]

                if (event.unicode.isalpha() or event.unicode.isdigit() or event.unicode == '_') and len(
                        name) < 15 and selection_2 is True:
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE and selection_2 is True:
                    name = name[:-1]

                if (event.unicode.isalpha() or event.unicode.isdigit() or event.unicode == '_') and len(
                        password_field) < 15 and selection_3 is True:
                    password_field += event.unicode
                elif event.key == pygame.K_BACKSPACE and selection_3 is True:
                    password_field = password_field[:-1]

        pygame.display.update()
        clock.tick(60)


def died():
    global sx
    global sy
    global dead
    dead = True
    sy = 1
    sx = 3
    timer = 0
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(game_over_img, game_over_img_rect)
        killed = largetext.render("YOU DIED", True, RED)
        screen.blit(killed, [55, 100])
        pygame.display.update()
        clock.tick(15)
        timer += 1
        if timer == 45:
            menu()


def pause():
    global paused
    global running
    global gear
    running = False
    paused = True
    while paused:
        screen.fill(GRAY)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 344 >= mouse[0] >= 139 and 200 >= mouse[1] >= 155:
            play = mediumtext.render("RESUME", True, BLUE)
            screen.blit(play, [136, 140])
        else:
            play = mediumtext.render("RESUME", True, LIGHT_BLUE)
            screen.blit(play, [136, 140])

        if 380 >= mouse[0] >= 120 and 285 >= mouse[1] >= 245:
            gears = mediumtext.render("SETTINGS", True, BLUE)
            screen.blit(gears, [110, 230])
        else:
            gears = mediumtext.render("SETTINGS", True, LIGHT_BLUE)
            screen.blit(gears, [110, 230])
        if 315 >= mouse[0] >= 170 and 377 >= mouse[1] >= 340:
            About = mediumtext.render("MENU", True, BLUE)
            screen.blit(About, [170, 320])
        else:
            About = mediumtext.render("MENU", True, LIGHT_BLUE)
            screen.blit(About, [170, 320])

        pause_text = mediumtext.render("Game is Paused", True, YELLOW)
        screen.blit(pause_text, [65, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running = True

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 344 >= mouse[0] >= 139 and 200 >= mouse[1] >= 155:
                    paused = False
                    running = True

                if 380 >= mouse[0] >= 120 and 285 >= mouse[1] >= 245:
                    settings()

                if 315 >= mouse[0] >= 170 and 377 >= mouse[1] >= 340:
                    paused = False
                    menu()

        pygame.display.update()
        clock.tick(60)


def skin_check():
    global skin1
    global skin2
    global skin3
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    query = "SELECT space_ship2, space_ship3 FROM inventory WHERE " \
            "user_nickname = %(nick)s"
    cursor.execute(query, {'nick': player.nickname})
    row = cursor.fetchone()
    if row[0] == 1:
        skin2 = True
    if row[1] == 1:
        skin3 = True
    skin1 = True


def ladders_check():
    import mysql.connector
    cnx = mysql.connector.connect(user='regular_player', password='', host='127.0.0.1', database='apocalypse')
    cursor = cnx.cursor()
    self_daily = "SELECT max_daily_points FROM statistics WHERE user_nickname = %(nick)s"
    self_weekly = "SELECT max_weekly_points FROM statistics WHERE user_nickname = %(nick)s"
    self_monthly = "SELECT max_monthly_points FROM statistics WHERE user_nickname = %(nick)s"
    self_data = {'nick': player.nickname}
    max_daily = "SELECT user_nickname, max_daily_points FROM statistics ORDER BY max_daily_points DESC LIMIT 5"
    max_weekly = "SELECT user_nickname, max_weekly_points FROM statistics ORDER BY max_weekly_points DESC LIMIT 5"
    max_monthly = "SELECT user_nickname, max_monthly_points FROM statistics ORDER BY max_monthly_points DESC LIMIT 5"
    cursor.execute(self_daily, self_data)
    self_d = cursor.fetchone()
    cursor.execute(self_weekly, self_data)
    self_w = cursor.fetchone()
    cursor.execute(self_monthly, self_data)
    self_m = cursor.fetchone()

    cursor.execute(max_daily)
    top5_d = cursor.fetchall()

    cursor.execute(max_weekly)
    top5_w = cursor.fetchall()

    cursor.execute(max_monthly)
    top5_m = cursor.fetchall()
    cnx.close()
    return self_d, self_m, self_w, top5_d, top5_w, top5_m


def inventory():
    global running
    global intro
    skin_choice = True
    skin_check()
    select1 = False
    select2 = False
    select3 = False
    select4 = False
    select5 = False
    global dead
    global pts
    global choiced_player_image
    while skin_choice:
        screen.fill(GRAY)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        choose_text = mediumtext.render("Select the ship", True, WHITE)
        start_text = mediumtext.render("Start", True, WHITE)
        back_text = mediumtext.render("Back", True, WHITE)

        player_img.set_colorkey(BLACK)
        screen.blit(player_img, (30, 50))

        if skin2:
            player_img2.set_colorkey(BLACK)
            screen.blit(player_img2, (190, 50))
        else:
            pygame.draw.rect(screen, BLACK, ((182, 40), (126, 100)))
            screen.blit(lock_img, (212, 55))
        if skin3:
            player_img3.set_colorkey(BLACK)
            screen.blit(player_img3, (350, 50))
        else:
            pygame.draw.rect(screen, BLACK, ((340, 40), (120, 100)))
            screen.blit(lock_img, (367, 55))

        pygame.draw.rect(screen, WHITE, ((20, 40), (120, 100)), 3)
        pygame.draw.rect(screen, WHITE, ((182, 40), (126, 100)), 3)
        pygame.draw.rect(screen, WHITE, ((340, 40), (120, 100)), 3)

        pygame.draw.rect(screen, WHITE, ((150, 250), (150, 70)), 3)
        pygame.draw.rect(screen, WHITE, ((150, 350), (150, 70)), 3)

        if 140 >= mouse[0] >= 20 and 140 >= mouse[1] >= 40 and click[0] == 1 and skin1:
            select1 = True
            select2 = False
            select3 = False
            player.image = skin1
        elif 308 >= mouse[0] >= 182 and 140 >= mouse[1] >= 40 and click[0] == 1 and skin2:
            select1 = False
            select2 = True
            select3 = False
            player.image = skin2
        elif 460 >= mouse[0] >= 340 and 140 >= mouse[1] >= 40 and click[0] == 1 and skin3:
            select1 = False
            select2 = False
            select3 = True
            player.image = skin3
        elif click[0] == 1 and not select4:
            select1 = select2 = select3 = False

        if 297 >= mouse[0] >= 152 and 317 >= mouse[1] >= 252:
            select4 = True
        else:
            select4 = False

        if 297 >= mouse[0] >= 152 and 417 >= mouse[1] >= 353:
            select5 = True
        else:
            select5 = False

        if select1:
            pygame.draw.rect(screen, BLACK, ((17, 36), (126, 108)), 3)
            player.image = pygame.transform.scale(player_img, (50, 35))
        if select2:
            pygame.draw.rect(screen, BLACK, ((179, 36), (132, 108)), 3)
            player.image = pygame.transform.scale(player_img2, (50, 35))
        if select3:
            pygame.draw.rect(screen, BLACK, ((337, 36), (126, 108)), 3)
            player.image = pygame.transform.scale(player_img3, (50, 35))
        if select4:
            pygame.draw.rect(screen, GRAY_SELECTION, ((152, 252), (146, 66)))
        if select5:
            pygame.draw.rect(screen, GRAY_SELECTION, ((152, 352), (146, 66)))

        screen.blit(choose_text, [65, 150])
        screen.blit(start_text, [158, 245])
        screen.blit(back_text, [167, 345])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and select4 and (select1 or select2 or select3):
                for s in mobs.sprites():
                    s.kill()
                for s in bullets.sprites():
                    s.kill()
                for s in explosions.sprites():
                    s.kill()
                player.rect.centerx = WIDTH // 2
                player.rect.bottom = HEIGHT - 10
                spawn()
                skin_choice = False
                dead = False
                pts = 0
                running = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and select5:
                skin_choice = False
                menu()

        pygame.display.update()
        clock.tick(60)


def ladders():
    looking_stats = True
    select1 = True
    select2 = False
    stats = ladders_check()
    self_md = stats[0]
    self_mw = stats[1]
    self_mm = stats[2]
    top5_d = stats[3]
    top5_w = stats[4]
    top5_m = stats[5]
    select3 = True
    select4 = False
    select5 = False
    while looking_stats:
        ladders_text = mediumtext.render("Ladders", True, WHITE)
        screen.fill(GRAY)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cl_text = smalltext.render("Current ladder", True, WHITE)
        pl_text = smalltext.render("Past ladder", True, WHITE)
        daily_text = smallmediumtext.render("Daily", True, WHITE)
        weekly_text = smallmediumtext.render("Weekly", True, WHITE)
        monthly_text = smallmediumtext.render("Monthly", True, WHITE)
        self_nick_text = smalltext.render(str(player.nickname), True, WHITE)

        print(mouse)

        pygame.draw.rect(screen, WHITE, (10, 73, 225, 35), 2)  # boxes of ladder_names
        pygame.draw.rect(screen, WHITE, (245, 73, 225, 35), 2)

        pygame.draw.rect(screen, WHITE, (10, 120, 146, 50), 2)
        pygame.draw.rect(screen, WHITE, (166, 120, 146, 50), 2)
        pygame.draw.rect(screen, WHITE, (322, 120, 146, 50), 2)

        pygame.draw.rect(screen, WHITE, (10, 185, 460, 40), 2)  # top players of ladder
        pygame.draw.rect(screen, WHITE, (10, 255, 460, 40), 2)
        pygame.draw.rect(screen, WHITE, (10, 310, 460, 40), 2)
        pygame.draw.rect(screen, WHITE, (10, 365, 460, 40), 2)
        pygame.draw.rect(screen, WHITE, (10, 420, 460, 40), 2)
        pygame.draw.rect(screen, WHITE, (10, 475, 460, 40), 2)

        if 316 >= mouse[0] >= 167 and 572 >= mouse[1] >= 534:
            menu_text = mediumtext.render("MENU", True, BLUE)
            screen.blit(menu_text, [167, 515])
        else:
            menu_text = mediumtext.render("MENU", True, LIGHT_BLUE)
            screen.blit(menu_text, [167, 515])

        screen.blit(ladders_text, (145, 0))

        screen.blit(cl_text, (36, 73))
        screen.blit(pl_text, (288, 73))
        screen.blit(daily_text, (42, 115))
        screen.blit(weekly_text, (177, 115))
        screen.blit(monthly_text, (330, 115))

        if 235 >= mouse[0] >= 10 and 108 >= mouse[1] >= 73 and click[0] == 1:
            select1 = True
            select2 = False
        elif 470 >= mouse[0] >= 245 and 108 >= mouse[1] >= 73 and click[0] == 1:
            select2 = True
            select1 = False

        if 156 >= mouse[0] >= 10 and 170 >= mouse[1] >= 120 and click[0] == 1:
            select3 = True
            select4 = False
            select5 = False
        elif 312 >= mouse[0] >= 166 and 170 >= mouse[1] >= 120 and click[0] == 1:
            select3 = False
            select4 = True
            select5 = False
        elif 468 >= mouse[0] >= 322 and 170 >= mouse[1] >= 120 and click[0] == 1:
            select3 = False
            select4 = False
            select5 = True
        elif click[0] == 1:
            select3 = False
            select4 = False
            select5 = False

        if select1:
            pygame.draw.rect(screen, GRAY_SELECTION, (8, 71, 230, 40), 3)
        elif select2:
            pygame.draw.rect(screen, GRAY_SELECTION, (243, 71, 230, 40), 3)
        if select3 and select1:
            pygame.draw.rect(screen, GRAY_SELECTION, (8, 118, 151, 55), 3)
            self_d_text = smalltext.render(str(self_md[0]), True, WHITE)
            top1_d_text = smalltext.render(str(top5_d[0][0]), True, WHITE)
            pts1_text = smalltext.render(str(top5_d[0][1]), True, WHITE)

            top2_d_text = smalltext.render(str(top5_d[1][0]), True, WHITE)
            pts2_text = smalltext.render(str(top5_d[1][1]), True, WHITE)

            top3_d_text = smalltext.render(str(top5_d[2][0]), True, WHITE)
            pts3_text = smalltext.render(str(top5_d[2][1]), True, WHITE)

            top4_d_text = smalltext.render(str(top5_d[3][0]), True, WHITE)
            pts4_text = smalltext.render(str(top5_d[3][1]), True, WHITE)

            top5_d_text = smalltext.render(str(top5_d[4][0]), True, WHITE)
            pts5_text = smalltext.render(str(top5_d[4][1]), True, WHITE)

            screen.blit(self_nick_text, [18, 188]) #nicks
            screen.blit(top1_d_text, [18, 256])
            screen.blit(top2_d_text, [18, 311])
            screen.blit(top3_d_text, [18, 363])
            screen.blit(top4_d_text, [18, 419])
            screen.blit(top5_d_text, [18, 474])

            screen.blit(self_d_text, [390, 187]) #pts
            screen.blit(pts1_text, [390, 258])
            screen.blit(pts2_text, [390, 312])
            screen.blit(pts3_text, [390, 366])
            screen.blit(pts4_text, [390, 421])
            screen.blit(pts5_text, [390, 475])

        elif select4 and select1:
            pygame.draw.rect(screen, GRAY_SELECTION, (164, 118, 151, 55), 3)
            self_w_text = smalltext.render(str(self_mw[0]), True, WHITE)
            top1_w_text = smalltext.render(str(top5_w[0][0]), True, WHITE)
            pts1_text = smalltext.render(str(top5_w[0][1]), True, WHITE)

            top2_w_text = smalltext.render(str(top5_w[1][0]), True, WHITE)
            pts2_text = smalltext.render(str(top5_w[1][1]), True, WHITE)

            top3_w_text = smalltext.render(str(top5_w[2][0]), True, WHITE)
            pts3_text = smalltext.render(str(top5_w[2][1]), True, WHITE)

            top4_w_text = smalltext.render(str(top5_w[3][0]), True, WHITE)
            pts4_text = smalltext.render(str(top5_w[3][1]), True, WHITE)

            top5_w_text = smalltext.render(str(top5_w[4][0]), True, WHITE)
            pts5_text = smalltext.render(str(top5_w[4][1]), True, WHITE)

        elif select5 and select1:
            pygame.draw.rect(screen, GRAY_SELECTION, (320, 118, 151, 55), 3)
            self_m_text = smalltext.render(str(self_mm[0]), True, WHITE)
            top1_m_text = smalltext.render(str(top5_m[0][0]), True, WHITE)
            pts1_text = smalltext.render(str(top5_m[0][1]), True, WHITE)

            top2_m_text = smalltext.render(str(top5_m[1][0]), True, WHITE)
            pts2_text = smalltext.render(str(top5_m[1][1]), True, WHITE)

            top3_m_text = smalltext.render(str(top5_m[2][0]), True, WHITE)
            pts3_text = smalltext.render(str(top5_m[2][1]), True, WHITE)

            top4_m_text = smalltext.render(str(top5_m[3][0]), True, WHITE)
            pts4_text = smalltext.render(str(top5_m[3][1]), True, WHITE)

            top5_m_text = smalltext.render(str(top5_m[4][0]), True, WHITE)
            pts5_text = smalltext.render(str(top5_m[4][1]), True, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 316 >= mouse[0] >= 167 and 572 >= mouse[1] >= 534:
                    looking_stats = False
                    menu()

        clock.tick(60)
        pygame.display.update()


def score(pts):
    pts_text = smalltext.render("Score: " + str(pts), True, YELLOW)
    screen.blit(pts_text, [0, 0])


def settings():
    global gear
    global volume
    global target
    global paused
    gear = True
    while gear:
        screen.fill(GRAY)
        volume0_pos = 140
        volume100_pos = 340
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if paused is True and 285 >= mouse[0] >= 157 and 357 >= mouse[1] >= 317:
            back_text = mediumtext.render("BACK", True, BLUE)
            screen.blit(back_text, [155, 300])
        elif paused is True:
            back_text = mediumtext.render("BACK", True, LIGHT_BLUE)
            screen.blit(back_text, [155, 300])
        if 307 >= mouse[0] >= 157 and 457 >= mouse[1] >= 417 and not paused:
            About = mediumtext.render("MENU", True, BLUE)
            screen.blit(About, [155, 400])
        elif not paused:
            About = mediumtext.render("MENU", True, LIGHT_BLUE)
            screen.blit(About, [155, 400])

        sound_text = mediumtext.render("VOLUME", True, LIGHT_BLUE)

        screen.blit(sound_text, [130, 25])

        pygame.draw.rect(screen, WHITE, ((140, 180), (200, 3)))

        if volume100_pos >= mouse[0] >= volume0_pos and 170 <= mouse[1] <= 190 and click[0] == 1:
            target = True
        elif click[0] == 0:
            target = False

        if target and volume100_pos >= mouse[0] >= volume0_pos:
            pygame.draw.circle(screen, WHITE, (mouse[0], 180), 10)
            volume = (mouse[0] - volume0_pos) // 2

        elif target and mouse[0] < volume0_pos:
            pygame.draw.circle(screen, WHITE, (volume0_pos, 180), 10)
            volume = 0
        elif target and mouse[0] > volume100_pos:
            pygame.draw.circle(screen, WHITE, (volume100_pos, 180), 10)
            volume = 100
        else:
            pygame.draw.circle(screen, WHITE, (volume * 2 + volume0_pos, 180), 10)

        if 100 > volume >= 10:
            volume_percentage = mediumtext.render(" " + str(volume) + "%", True, LIGHT_BLUE)

        elif volume < 10:
            volume_percentage = mediumtext.render("  " + str(volume) + "%", True, LIGHT_BLUE)

        elif volume == 100:
            volume_percentage = mediumtext.render(str(volume) + "%", True, LIGHT_BLUE)

        screen.blit(volume_percentage, [180, 85])

        crash_sound.set_volume(0.08 * (0.01 * volume))
        player_crashed.set_volume(0.3 * (0.01 * volume))
        laser_sound.set_volume(0.2 * (0.01 * volume))
        pygame.mixer.music.set_volume(0.2 * (0.01 * volume))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 335 >= mouse[0] >= 155 and 457 >= mouse[1] >= 417 and not paused:
                    gear = False
                    paused = False
                    menu()
                if 285 >= mouse[0] >= 157 and 357 >= mouse[1] >= 317 and paused is True:
                    gear = False
                    pause()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def player_statistics():
    stats = True
    stats_tuple = show_stats()
    max_points_text = smalltext.render('Maximum points:' + ' ' + str(stats_tuple[0]), True, WHITE)
    total_points_text = smalltext.render('Total points:' + ' ' + str(stats_tuple[1]), True, WHITE)
    games_played_text = smalltext.render('Games played:' + ' ' + str(stats_tuple[2]), True, WHITE)
    max_daily_points_text = smalltext.render('Maximum daily points:' + ' ' + str(stats_tuple[3]), True, WHITE)
    max_weekly_points_text = smalltext.render('Maximum weekly points:' + ' ' + str(stats_tuple[4]), True, WHITE)
    max_monthly_points_text = smalltext.render('Maximum monthly points:' + ' ' + str(stats_tuple[5]), True, WHITE)
    while stats:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)
        screen.fill(GRAY)

        if 316 >= mouse[0] >= 167 and 457 >= mouse[1] >= 417:
            menu_text = mediumtext.render("MENU", True, BLUE)
            screen.blit(menu_text, [167, 400])
        else:
            menu_text = mediumtext.render("MENU", True, LIGHT_BLUE)
            screen.blit(menu_text, [167, 400])

        pygame.draw.rect(screen, WHITE, (63, 20, 360, 320), 3)

        screen.blit(max_points_text, [73, 25])
        screen.blit(total_points_text, [73, 75])
        screen.blit(games_played_text, [73, 125])
        screen.blit(max_daily_points_text, [73, 175])
        screen.blit(max_weekly_points_text, [73, 225])
        screen.blit(max_monthly_points_text, [73, 275])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 316 >= mouse[0] >= 167 and 457 >= mouse[1] >= 417:
                    stats = False
                    menu()

        pygame.display.update()
        clock.tick(60)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        click = pygame.mouse.get_pressed()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 35))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 21
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # hitboxes CBEPXY
        self.rect.centerx = WIDTH // 2
        self.nickname = ''
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = meteor_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(sx, sy + 7)
        self.speedx = random.randrange(sx - 6, sy + 2)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(sx, sy + 7)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 40

    def update(self):
        explosions.add(self)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves out from screen
        if self.rect.bottom < 0:
            self.kill()


for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)

# <editor-fold desc="Working with sprites">
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()


# </editor-fold>


def spawn():
    for i in range(meteors):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


spawn()
authorization_window()
# menu()

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        click = pygame.mouse.get_pressed()
        # check for game over
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click[0] == 1:
                player.shoot()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullets) < shootlimit:  # shooting here
                player.shoot()
                pygame.mixer.Sound.play(laser_sound)

            if event.key == pygame.K_ESCAPE:
                pause()

    if 100 > pts >= 50:
        shootlimit = 8
        if sy + sx == 2:
            sy += 2
    if 150 > pts >= 100:
        shootlimit = 7
        if sy + sx == 4:
            sy += 2
    if 200 > pts >= 150:
        shootlimit = 6
        if sy + sx == 6:
            sy += 1
    if 250 > pts >= 200:
        shootlimit = 5
        if sy + sx == 7:
            sy += 1
    if 300 > pts >= 250:
        shootlimit = 4
        if sy + sx == 9:
            sy += 1
    if pts >= 300:
        shootlimit = 3
        if sy + sx == 11:
            sy += 2
    # Update
    pygame.display.update()
    all_sprites.update()
    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        pygame.mixer.Sound.play(crash_sound)
        pts += 1
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        update_stats(pts)
        pygame.mixer.Sound.play(player_crashed)
        running = False
        time.sleep(1)
        died()

    # Draw and render
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    score(pts)
    # helpful thing
    pygame.display.flip()

# 14) Ладдеры
# 15) Внедрение базы данных в игру (work in progress)
