from pygame import K_i, K_UP, K_RIGHT, K_DOWN, K_LEFT

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 16
FPS = 45

#DIRS
LEVELS_DIR = 'levels/'
ASSETS_DIR = 'assets/'

#DIRECTIONS
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#EVENTS
CAN_GO_EVENT = 1
GO_INTO_EVENT = 2
GO_OUT_EVENT = 3
TAKE_ITEM_EVENT = 4
THROW_ITEM_EVENT = 5

#PLAYER
MAX_ITEMS = 24
MAX_HEALTH = 100
UNHUNGRY_STEPS = 10  # TODO change


#KEYS
INVENTORY_KEY = K_i
UP_KEY = K_UP
RIGHT_KEY = K_RIGHT
DOWN_KEY = K_DOWN
LEFT_KEY = K_LEFT

#INVENTORY
INVENTORY_BORDER_COLOR = (67, 67, 67)
INVENTORY_LOW_SPACE = 10
INVENTORY_MAX_SPACE = 50
INVENTORY_X = 20
INVENTORY_Y = 50
INVENTORY_COLOR = (94, 94, 94)
INVENTORY_CHOOSE_COLOR = (255, 165, 0)
INVENTORY_CELL = 32
INVENTORY_COLS = 4
INVENTORY_ROWS = 6
INVENTORY_SPACES = 5
INVENTORY_FONT_COLOR = (230, 230, 0)
INVENTORY_TITLE = 'Инвентарь'

INVENTORY_WIDTH = INVENTORY_COLS * INVENTORY_CELL + 2 * INVENTORY_LOW_SPACE + INVENTORY_SPACES * (INVENTORY_COLS - 1)
INVENTORY_HEIGHT = INVENTORY_MAX_SPACE + \
                   INVENTORY_ROWS * INVENTORY_CELL + \
                   INVENTORY_LOW_SPACE + INVENTORY_SPACES * (INVENTORY_ROWS - 1)

#GUI
GUI_X = INVENTORY_X
GUI_Y = INVENTORY_Y + INVENTORY_HEIGHT + 75
GUI_BORDER = 20  # отступ - рамка
GUI_BUTTON_COLOR = (255, 0, 0)
GUI_COLOR = INVENTORY_COLOR  # цвет заднего плана
GUI_BUTTON_BORDER_WIDTH = 10  # отступ-ширина ОТ ТЕКСТА на кнопке
GUI_BUTTON_BORDER_HEIGHT = 5
GUI_WIDTH = INVENTORY_WIDTH + 100
GUI_BUTTON_SPACE = 20  # расстояние между кнопками и текстом-описанием
GUI_BUTTON_INDENT = 20
