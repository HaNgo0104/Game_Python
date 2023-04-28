import pygame
pygame.init()

WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
font = pygame.font.SysFont("calibri", 40, True, False)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
MOCCASIN = (255, 228, 181)

def draw_board(board):
    screen.fill(MOCCASIN)

    for i in range(10):
        lines = 1
        if i % 3 == 0:
            lines = 3
        pygame.draw.line(screen, BROWN, (50 + 50 * i, 50), (50 + 50 * i, 500), lines)
        pygame.draw.line(screen, BROWN, (50, 50 + 50 * i), (500, 50 + 50 * i), lines)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = font.render(str(board[i][j]), True, BLACK)
                x = j * 50 + 70
                y = i * 50 + 55
                screen.blit(num, (x, y))


def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False
    return True


def mouse_operation(board, press):
    mouse_pos = pygame.mouse.get_pos()

    if 50 <= mouse_pos[0] <= 500 and 50 <= mouse_pos[1] <= 500:
        row = (mouse_pos[1] - 50) // 50
        col = (mouse_pos[0] - 50) // 50
        press = (row, col)

    keys = pygame.key.get_pressed()
    for i in range(1, 10):
        if keys[pygame.K_KP1 + i - 1] or keys[pygame.K_1 + i - 1]:
            if press is not None:
                row, col = press
                if is_valid_move(board, row, col, i):
                    board[row][col] = i
    return press


def run():
    board = [
        [0, 0, 1, 9, 8, 4, 7, 6, 0],
        [6, 0, 0, 0, 5, 7, 0, 0, 0],
        [8, 0, 7, 0, 1, 0, 0, 0, 0],
        [9, 6, 0, 3, 0, 8, 1, 0, 5],
        [1, 8, 5, 0, 2, 0, 0, 7, 3],
        [3, 0, 0, 0, 0, 0, 2, 0, 8],
        [2, 1, 0, 0, 0, 0, 0, 3, 6],
        [0, 0, 0, 1, 0, 0, 0, 0, 4],
        [0, 9, 6, 0, 0, 2, 5, 1, 0],
    ]
    
    press = None
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        press = mouse_operation(board, press)
        draw_board(board)

        if press is not None:
            row, col = press
            pygame.draw.rect(screen, BROWN, (50 + col * 50, 50 + row * 50, 50, 50), 3)

        pygame.display.update()
        clock.tick(60)

run()
