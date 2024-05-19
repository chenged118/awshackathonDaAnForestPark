# Display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 60
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMAGE_PATH = 'graphics/0/bg.png'
GRID_IMAGE_PATH = 'graphics/0/gridline.png'
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/0/symbols'

# Text
TEXT_COLOR = 'White'
# You need to provide your own font in the below directory
# I downloaded Kidspace font from https://www.dafont.com/kidspace.font
UI_FONT = 'graphics/font/kidspace.ttf'
UI_FONT_SIZE = 40
WIN_FONT_SIZE = 110

# 5 Symbols for demo
# symbols = {
#     'diamond': f"{SYM_PATH}/0_diamond.png", 
#     'floppy': f"{SYM_PATH}/0_floppy.png",
#     'hourglass': f"{SYM_PATH}/0_hourglass.png",
#     'seven': f"{SYM_PATH}/0_seven.png",
#     'telephone': f"{SYM_PATH}/0_telephone.png"
# }

# 4 Symbols for more wins
symbols = {
    # 'diamond': f"{SYM_PATH}/0_diamond.png", 
    # 'floppy': f"{SYM_PATH}/0_floppy.png",
    # 'hourglass': f"{SYM_PATH}/0_hourglass.png",
    # 'hourglass2': f"{SYM_PATH}/0_hourglass.png",
    # 'telephone': f"{SYM_PATH}/0_telephone.png",
    'bonus': f"{SYM_PATH}/00.jpg",
    'wild': f"{SYM_PATH}/01.jpg",
    'gold': f"{SYM_PATH}/02.jpg",
    'green': f"{SYM_PATH}/03.jpg",
    'blue': f"{SYM_PATH}/04.jpg",
    # 'red': f"{SYM_PATH}/05.png",
    # 'purple': f"{SYM_PATH}/06.png",
    # 'a': f"{SYM_PATH}/07_A.png",
    # 'k': f"{SYM_PATH}/08_K.png",
    # 'q': f"{SYM_PATH}/09_Q.png",
    # 'j': f"{SYM_PATH}/10_J.png",
}