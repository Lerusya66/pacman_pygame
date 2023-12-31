import pygame


class Walls():
    def createList(self):
        '''Создает список объектов пайгейма - стены'''
        walls = []
        # walls.append(pygame.Rect((x, y), (width, height)))
        walls.append(pygame.Rect((100, 48), (448, 8)))
        walls.append(pygame.Rect((100, 55), (7, 152)))
        walls.append(pygame.Rect((180, 200), (8, 64)))
        walls.append(pygame.Rect((268, 248), (8, 64)))
        walls.append(pygame.Rect((140, 88), (48, 32)))
        walls.append(pygame.Rect((220, 88), (64, 32)))
        walls.append(pygame.Rect((364, 88), (65, 32)))
        walls.append(pygame.Rect((460, 88), (49, 32)))
        walls.append(pygame.Rect((100, 200), (86, 8)))
        walls.append(pygame.Rect((140, 152), (48, 16)))
        walls.append(pygame.Rect((316, 55), (16, 65)))
        walls.append(pygame.Rect((540, 55), (8, 153)))
        walls.append(pygame.Rect((460, 200), (88, 8)))
        walls.append(pygame.Rect((460, 152), (49, 16)))
        walls.append(pygame.Rect((412, 152), (16, 112)))
        walls.append(pygame.Rect((364, 200), (50, 16)))
        walls.append(pygame.Rect((268, 152), (112, 16)))
        walls.append(pygame.Rect((316, 166), (16, 50)))
        walls.append(pygame.Rect((220, 152), (16, 112)))
        walls.append(pygame.Rect((235, 200), (49, 16)))
        walls.append(pygame.Rect((100, 256), (88, 8)))
        walls.append(pygame.Rect((460, 256), (89, 8)))
        walls.append(pygame.Rect((460, 296), (89, 8)))
        walls.append(pygame.Rect((460, 352), (88, 8)))
        walls.append(pygame.Rect((460, 296), (9, 64)))
        walls.append(pygame.Rect((412, 296), (17, 65)))
        walls.append(pygame.Rect((220, 296), (16, 64)))
        walls.append(pygame.Rect((460, 200), (8, 64)))
        walls.append(pygame.Rect((100, 296), (88, 8)))
        walls.append(pygame.Rect((179, 296), (9, 64)))
        walls.append(pygame.Rect((100, 352), (88, 8)))
        walls.append(pygame.Rect((100, 352), (8, 193)))
        walls.append(pygame.Rect((107, 440), (33, 16)))
        walls.append(pygame.Rect((100, 536), (448, 9)))
        walls.append(pygame.Rect((540, 352), (8, 193)))
        walls.append(pygame.Rect((508, 440), (34, 16)))
        walls.append(pygame.Rect((268, 248), (40, 8)))
        walls.append(pygame.Rect((340, 248), (41, 8)))
        walls.append(pygame.Rect((460, 200), (9, 64)))
        walls.append(pygame.Rect((139, 392), (49, 17)))
        walls.append(pygame.Rect((171, 406), (17, 51)))
        walls.append(pygame.Rect((220, 392), (64, 17)))
        walls.append(pygame.Rect((364, 392), (65, 17)))
        walls.append(pygame.Rect((460, 392), (49, 17)))
        walls.append(pygame.Rect((460, 406), (17, 51)))
        walls.append(pygame.Rect((412, 440), (17, 50)))
        walls.append(pygame.Rect((364, 488), (145, 17)))
        walls.append(pygame.Rect((267, 440), (114, 17)))
        walls.append(pygame.Rect((316, 358), (16, 51)))
        walls.append(pygame.Rect((220, 440), (16, 50)))
        walls.append(pygame.Rect((139, 488), (145, 17)))
        walls.append(pygame.Rect((372, 248), (9, 64)))
        walls.append(pygame.Rect((268, 304), (113, 7)))
        walls.append(pygame.Rect((268, 344), (112, 16)))
        walls.append(pygame.Rect((316, 455), (16, 50)))
        # Стена блокирует центр игрового поля, создает ловушку для антител
        walls.append(pygame.Rect((268, 248), (112, 64)))
        return walls
