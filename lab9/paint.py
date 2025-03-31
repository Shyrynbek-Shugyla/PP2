import pygame

WIDTH, HEIGHT = 1200, 800  # Определяет ширину и высоту игрового окна.
FPS = 90  # Частота обновления экрана
draw = False  # Указывает, рисовать ли на экране
radius = 2  # Радиус кисти
color = 'blue'  # Цвет кисти
mode = 'pen'  # Режим рисования

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создание окна заданных размеров
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Для управления временем
screen.fill(pygame.Color('white'))  # Заполнение экрана белым цветом
font = pygame.font.SysFont('None', 60)  # Создание шрифта для отображения текста

def drawLine(screen, start, end, width, color):
    # Извлекаем x и y координаты начальной и конечной точек
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Вычисляем абсолютные различия в координатах x и y
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    # Коэффициенты для уравнения прямой Ax + By + C = 0
    A = y2 - y1  # Вертикально
    B = x1 - x2  # Горизонтально
    C = x2 * y1 - x1 * y2
    
    # Если линия более горизонтальная, чем вертикальная
    if dx > dy:
        # Убедитесь, что x1 слева от x2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам x
        for x in range(x1, x2):
            # Вычисляем координату y, используя уравнение прямой
            y = (-C - A * x) / B
            # Рисуем круг (пиксель) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    # Если линия более вертикальная, чем горизонтальная
    else:
        # Убедитесь, что y1 ниже y2
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        # Итерация по координатам y
        for y in range(y1, y2):
            # Вычисляем координату x, используя уравнение прямой
            x = (-C - B * y) / A
            # Рисуем круг (пиксель) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

def drawCircle(screen, start, end, width, color):
    # Извлекаем x и y координаты начальной и конечной точек
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Вычисляем центр круга
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    
    # Вычисляем радиус круга
    radius = abs(x1 - x2) / 2
    
    # Рисуем круг на экране
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)

def drawRectangle(screen, start, end, width, color):
    # Извлекаем x и y координаты начальной и конечной точек
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    # Вычисляем ширину и высоту прямоугольника
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    
    # Рисуем прямоугольник на экране в зависимости от положения начальной и конечной точки
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

def drawSquare(screen, start, end, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))

def drawRightTriangle(screen, start, end, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))

def drawEquilateralTriangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))

def drawRhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Закрытие программы, если окно закрыто
        
        # Обработка событий с клавиатуры
        if event.type == pygame.KEYDOWN:
            # Изменение режима в зависимости от нажатой клавиши
            if event.key == pygame.K_r:
                mode = 'rectangle'  # Устанавливаем режим для рисования прямоугольников
            if event.key == pygame.K_c:
                mode = 'circle'  # Устанавливаем режим для рисования кругов
            if event.key == pygame.K_p:
                mode = 'pen'  # Устанавливаем режим для использования пера
            if event.key == pygame.K_e:
                mode = 'erase'  # Устанавливаем режим для стирания
            if event.key == pygame.K_s:
                mode = 'square'  # Устанавливаем режим для рисования квадратов
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))  # Очищаем экран, заполняя его белым цветом

            # Изменение цвета в зависимости от нажатой клавиши
            if event.key == pygame.K_1:
                color = 'black'  # Устанавливаем цвет черный
            if event.key == pygame.K_2:
                color = 'green'  # Устанавливаем цвет зеленый
            if event.key == pygame.K_3:
                color = 'red'  # Устанавливаем цвет красный
            if event.key == pygame.K_4:
                color = 'blue'  # Устанавливаем цвет синий
            if event.key == pygame.K_5:
                color = 'yellow'  # Устанавливаем цвет желтый
            if event.key == pygame.K_t:
                mode = 'right_tri'  # Устанавливаем режим для рисования прямоугольных треугольников
            if event.key == pygame.K_u:
                mode = 'eq_tri'  # Устанавливаем режим для рисования равносторонних треугольников
            if event.key == pygame.K_h:
                mode = 'rhombus'  # Устанавливаем режим для рисования ромбов

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True  # Включаем рисование
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Рисуем круг (пиксель), если активен режим пера
            prevPos = event.pos  # Сохраняем текущую позицию как предыдущую

        
        if event.type == pygame.MOUSEBUTTONUP:
            # Когда кнопка мыши отпущена
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)  # Рисуем прямоугольник, если активен режим рисования прямоугольников
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)  # Рисуем круг, если активен режим рисования кругов
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, color)  # Рисуем квадрат, если активен режим рисования квадратов
            elif mode == 'right_tri':
                drawRightTriangle(screen, prevPos, event.pos, color)  # Рисуем прямоугольный треугольник, если активен режим рисования прямоугольных треугольников
            elif mode == 'eq_tri':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)  # Рисуем равносторонний треугольник, если активен режим рисования равносторонних треугольников
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)  # Рисуем ромб, если активен режим рисования ромбов
            draw = False  # Отключаем рисование


        
        if event.type == pygame.MOUSEMOTION:
            # Когда мышь двигается
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)  # Если рисование включено и активен режим пера, рисуем линию между последней и текущей позицией
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Если рисование включено и активен режим стирания, рисуем белую линию (стирать) между последней и текущей позицией
            lastPos = event.pos  # Обновляем последнюю позицию на текущую

    # Рисуем прямоугольник для отображения информации о радиусе
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))  # Рисуем белый прямоугольник для отображения информации о радиусе
    renderRadius = font.render(str(radius), True, pygame.Color(color))  # Рендерим текст, отображающий текущий радиус
    screen.blit(renderRadius, (5, 5))  # Отображаем текст на экране в указанной позиции

    pygame.display.flip()  # Обновляем экран
    clock.tick(FPS)  # Контролируем частоту кадров
