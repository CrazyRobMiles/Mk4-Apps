""" Flashes random colours on your screen
""  By Pez (@Pezmc)
"""
___title___        = "Screen Party"
___license___      = "MIT"
___dependencies___ = ["ugfx_helper", "sleep"]
___categories___   = ["Homescreens"]
___bootstrapped___ = False

import random, ugfx, buttons, math, time
from app import App, restart_to_default
from homescreen import clean_up
from tilda import LED, Buttons

# Welcome
ugfx.init()
ugfx.clear(ugfx.BLACK)
ugfx.text(5, 5, "Press A to Start and B to stop", ugfx.WHITE)
ugfx.text(5, ugfx.height() - 20, "By Pez (@Pezmc)", ugfx.WHITE)

# Draw colours
grid_size = 20  
grid_width = math.ceil(ugfx.width() / grid_size)
grid_height = math.ceil(ugfx.height() / grid_size)
colour_list = [0xB0171F,0xDC143C,0xFFB6C1,0xFFAEB9,0xEEA2AD,0xCD8C95,0x8B5F65,0xFFC0CB,0xFFB5C5,0xEEA9B8,0xCD919E,0x8B636C,0xDB7093,0xFF82AB,0xEE799F,0xCD6889,0x8B475D,0xFFF0F5,0xEEE0E5,0xCDC1C5,0x8B8386,0xFF3E96,0xEE3A8C,0xCD3278,0x8B2252,0xFF69B4,0xFF6EB4,0xEE6AA7,0xCD6090,0x8B3A62,0x872657,0xFF1493,0xEE1289,0xCD1076,0x8B0A50,0xFF34B3,0xEE30A7,0xCD2990,0x8B1C62,0xC71585,0xD02090,0xDA70D6,0xFF83FA,0xEE7AE9,0xCD69C9,0x8B4789,0xD8BFD8,0xFFE1FF,0xEED2EE,0xCDB5CD,0x8B7B8B,0xFFBBFF,0xEEAEEE,0xCD96CD,0x8B668B,0xDDA0DD,0xEE82EE,0xFF00FF,0xEE00EE,0xCD00CD,0x8B008B,0x800080,0xBA55D3,0xE066FF,0xD15FEE,0xB452CD,0x7A378B,0x9400D3,0x9932CC,0xBF3EFF,0xB23AEE,0x9A32CD,0x68228B,0x4B0082,0x8A2BE2,0x9B30FF,0x912CEE,0x7D26CD,0x551A8B,0x9370DB,0xAB82FF,0x9F79EE,0x8968CD,0x5D478B,0x483D8B,0x8470FF,0x7B68EE,0x6A5ACD,0x836FFF,0x7A67EE,0x6959CD,0x473C8B,0xF8F8FF,0xE6E6FA,0x0000FF,0x0000EE,0x0000CD,0x00008B,0x000080,0x191970,0x3D59AB,0x4169E1,0x4876FF,0x436EEE,0x3A5FCD,0x27408B,0x6495ED,0xB0C4DE,0xCAE1FF,0xBCD2EE,0xA2B5CD,0x6E7B8B,0x778899,0x708090,0xC6E2FF,0xB9D3EE,0x9FB6CD,0x6C7B8B,0x1E90FF,0x1C86EE,0x1874CD,0x104E8B,0xF0F8FF,0x4682B4,0x63B8FF,0x5CACEE,0x4F94CD,0x36648B,0x87CEFA,0xB0E2FF,0xA4D3EE,0x8DB6CD,0x607B8B,0x87CEFF,0x7EC0EE,0x6CA6CD,0x4A708B,0x87CEEB,0x00BFFF,0x00B2EE,0x009ACD,0x00688B,0x33A1C9,0xADD8E6,0xBFEFFF,0xB2DFEE,0x9AC0CD,0x68838B,0xB0E0E6,0x98F5FF,0x8EE5EE,0x7AC5CD,0x53868B,0x00F5FF,0x00E5EE,0x00C5CD,0x00868B,0x5F9EA0,0x00CED1,0xF0FFFF,0xE0EEEE,0xC1CDCD,0x838B8B,0xE0FFFF,0xD1EEEE,0xB4CDCD,0x7A8B8B,0xBBFFFF,0xAEEEEE,0x96CDCD,0x668B8B,0x2F4F4F,0x97FFFF,0x8DEEEE,0x79CDCD,0x528B8B,0x00FFFF,0x00EEEE,0x00CDCD,0x008B8B,0x008080,0x48D1CC,0x20B2AA,0x03A89E,0x40E0D0,0x808A87,0x00C78C,0x7FFFD4,0x76EEC6,0x66CDAA,0x458B74,0x00FA9A,0xF5FFFA,0x00FF7F,0x00EE76,0x00CD66,0x008B45,0x3CB371,0x54FF9F,0x4EEE94,0x43CD80,0x2E8B57,0x00C957,0xBDFCC9,0x3D9140,0xF0FFF0,0xE0EEE0,0xC1CDC1,0x838B83,0x8FBC8F,0xC1FFC1,0xB4EEB4,0x9BCD9B,0x698B69,0x98FB98,0x9AFF9A,0x90EE90,0x7CCD7C,0x548B54,0x32CD32,0x228B22,0x00FF00,0x00EE00,0x00CD00,0x008B00,0x008000,0x006400,0x308014,0x7CFC00,0x7FFF00,0x76EE00,0x66CD00,0x458B00,0xADFF2F,0xCAFF70,0xBCEE68,0xA2CD5A,0x6E8B3D,0x556B2F,0x6B8E23,0xC0FF3E,0xB3EE3A,0x9ACD32,0x698B22,0xFFFFF0,0xEEEEE0,0xCDCDC1,0x8B8B83,0xF5F5DC,0xFFFFE0,0xEEEED1,0xCDCDB4,0x8B8B7A,0xFAFAD2,0xFFFF00,0xEEEE00,0xCDCD00,0x8B8B00,0x808069,0x808000,0xBDB76B,0xFFF68F,0xEEE685,0xCDC673,0x8B864E,0xF0E68C,0xEEE8AA,0xFFFACD,0xEEE9BF,0xCDC9A5,0x8B8970,0xFFEC8B,0xEEDC82,0xCDBE70,0x8B814C,0xE3CF57,0xFFD700,0xEEC900,0xCDAD00,0x8B7500,0xFFF8DC,0xEEE8CD,0xCDC8B1,0x8B8878,0xDAA520,0xFFC125,0xEEB422,0xCD9B1D,0x8B6914,0xB8860B,0xFFB90F,0xEEAD0E,0xCD950C,0x8B6508,0xFFA500,0xEE9A00,0xCD8500,0x8B5A00,0xFFFAF0,0xFDF5E6,0xF5DEB3,0xFFE7BA,0xEED8AE,0xCDBA96,0x8B7E66,0xFFE4B5,0xFFEFD5,0xFFEBCD,0xFFDEAD,0xEECFA1,0xCDB38B,0x8B795E,0xFCE6C9,0xD2B48C,0x9C661F,0xFF9912,0xFAEBD7,0xFFEFDB,0xEEDFCC,0xCDC0B0,0x8B8378,0xDEB887,0xFFD39B,0xEEC591,0xCDAA7D,0x8B7355,0xFFE4C4,0xEED5B7,0xCDB79E,0x8B7D6B,0xE3A869,0xED9121,0xFF8C00,0xFF7F00,0xEE7600,0xCD6600,0x8B4500,0xFF8000,0xFFA54F,0xEE9A49,0xCD853F,0x8B5A2B,0xFAF0E6,0xFFDAB9,0xEECBAD,0xCDAF95,0x8B7765,0xFFF5EE,0xEEE5DE,0xCDC5BF,0x8B8682,0xF4A460,0xC76114,0xD2691E,0xFF7F24,0xEE7621,0xCD661D,0x8B4513,0x292421,0xFF7D40,0xFF6103,0x8A360F,0xA0522D,0xFF8247,0xEE7942,0xCD6839,0x8B4726,0xFFA07A,0xEE9572,0xCD8162,0x8B5742,0xFF7F50,0xFF4500,0xEE4000,0xCD3700,0x8B2500,0x5E2612,0xE9967A,0xFF8C69,0xEE8262,0xCD7054,0x8B4C39,0xFF7256,0xEE6A50,0xCD5B45,0x8B3E2F,0x8A3324,0xFF6347,0xEE5C42,0xCD4F39,0x8B3626,0xFA8072,0xFFE4E1,0xEED5D2,0xCDB7B5,0x8B7D7B,0xFFFAFA,0xEEE9E9,0xCDC9C9,0x8B8989,0xBC8F8F,0xFFC1C1,0xEEB4B4,0xCD9B9B,0x8B6969,0xF08080,0xCD5C5C,0xFF6A6A,0xEE6363,0x8B3A3A,0xCD5555,0xA52A2A,0xFF4040,0xEE3B3B,0xCD3333,0x8B2323,0xB22222,0xFF3030,0xEE2C2C,0xCD2626,0x8B1A1A,0xFF0000,0xEE0000,0xCD0000,0x8B0000,0x800000,0x8E388E,0x7171C6,0x7D9EC0,0x388E8E,0x71C671,0x8E8E38,0xC5C1AA,0xC67171,0x555555,0x1E1E1E,0x282828,0x515151,0x5B5B5B,0x848484,0x8E8E8E,0xAAAAAA,0xB7B7B7,0xC1C1C1,0xEAEAEA,0xF4F4F4,0xFFFFFF,0xF5F5F5,0xDCDCDC,0xD3D3D3,0xC0C0C0,0xA9A9A9,0x808080,0x696969,0x000000,0xFCFCFC,0xFAFAFA,0xF7F7F7,0xF5F5F5,0xF2F2F2,0xF0F0F0,0xEDEDED,0xEBEBEB,0xE8E8E8,0xE5E5E5,0xE3E3E3,0xE0E0E0,0xDEDEDE,0xDBDBDB,0xD9D9D9,0xD6D6D6,0xD4D4D4,0xD1D1D1,0xCFCFCF,0xCCCCCC,0xC9C9C9,0xC7C7C7,0xC4C4C4,0xC2C2C2,0xBFBFBF,0xBDBDBD,0xBABABA,0xB8B8B8,0xB5B5B5,0xB3B3B3,0xB0B0B0,0xADADAD,0xABABAB,0xA8A8A8,0xA6A6A6,0xA3A3A3,0xA1A1A1,0x9E9E9E,0x9C9C9C,0x999999,0x969696,0x949494,0x919191,0x8F8F8F,0x8C8C8C,0x8A8A8A,0x878787,0x858585,0x828282,0x7F7F7F,0x7D7D7D,0x7A7A7A,0x787878,0x757575,0x737373,0x707070,0x6E6E6E,0x6B6B6B,0x696969,0x666666,0x636363,0x616161,0x5E5E5E,0x5C5C5C,0x595959,0x575757,0x545454,0x525252,0x4F4F4F,0x4D4D4D,0x4A4A4A,0x474747,0x454545,0x424242,0x404040,0x3D3D3D,0x3B3B3B,0x383838,0x363636,0x333333,0x303030,0x2E2E2E,0x2B2B2B,0x292929,0x262626,0x242424,0x212121,0x1F1F1F,0x1C1C1C,0x1A1A1A,0x171717,0x141414,0x121212,0x0F0F0F,0x0D0D0D,0x0A0A0A,0x080808,0x050505,0x030303]
colour_count = len(colour_list)
colour_index = 0
random.shuffle(colour_list)
def drawDiscoFrame():
    global grid_size, grid_width, grid_height, colour_list, colour_count, colour_index

    for x in range(0, grid_width):
        for y in range(0, grid_height):
            # randint isn't very random
            drawSquare(x, y, colour_list[random.randint(0, colour_count - 1)])

shiftX = 0
shiftY = 0
color_index = 0
def drawRandomSquare():
    global shiftX, shiftY, color_index

    # Random just draws diagonal lines, try to make it look more random
    x = (random.randint(0, grid_width) + shiftX) % grid_width
    y = (random.randint(0, grid_height) + shiftY) % grid_height

    # Just using random doesn't work...
    color_index = (color_index + random.randint(1, 5)) % colour_count
    drawSquare(x, y, colour_list[color_index])

    shiftX += 1
    shiftY += 1

def drawSquare(x, y, colour):
    ugfx.area(x*grid_size, y*grid_size, grid_size, grid_size, colour)

def badgeQuit():
    restart_to_default()

# Main Loop
startDisco = False
while True:
    if buttons.is_triggered(buttons.Buttons.BTN_A):
        startDisco = True
        drawDiscoFrame()
    elif buttons.is_triggered(buttons.Buttons.BTN_B):
        startDisco = False
        break
    elif buttons.is_triggered(tilda.Buttons.BTN_Menu):
        clean_up()
        App("launcher").boot()        

    if startDisco:
        drawRandomSquare()
        drawRandomSquare()
        drawRandomSquare()
        drawRandomSquare()
        drawRandomSquare()

    time.sleep_ms(1)

badgeQuit()
