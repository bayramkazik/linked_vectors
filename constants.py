# Colors

BACKGROUND_COLOR = 35, 39, 46
GRID_LINE_COLOR = 96, 96, 96, 32
GRID_POINT_COLOR = 128, 128, 128
ROOT_POINT_COLOR = 255, 0, 0
CHILD_POINT_COLOR = 255, 0, 0


# Sizes

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT

AREA_WIDTH, AREA_HEIGHT = 20, 20
AREA_SIZE = AREA_WIDTH, AREA_HEIGHT

GAP_WIDTH, GAP_HEIGHT = WINDOW_WIDTH / AREA_WIDTH, WINDOW_HEIGHT / AREA_HEIGHT
GAP_MIN, GAP_MAX = min(GAP_WIDTH, GAP_HEIGHT), max(GAP_WIDTH, GAP_HEIGHT)
GAP_SIZE = GAP_WIDTH, GAP_HEIGHT

POINT_RADIUS = max(1, GAP_MIN / 16)


# Window

WINDOW_ICON_RELATIVE_PATH = "assets/icon.png"
WINDOW_TITLE = "Linked Vectors"
