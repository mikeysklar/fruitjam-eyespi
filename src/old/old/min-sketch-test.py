import time
import board
import displayio
import terminalio
import digitalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from fourwire import FourWire
import adafruit_ili9341

# --------------------------------------------------------------------
# 1. Release built-in display on Fruit Jam (prevents "A1 in use")
# --------------------------------------------------------------------
if hasattr(board, "DISPLAY"):
    board.DISPLAY.auto_refresh = False
displayio.release_displays()

# --------------------------------------------------------------------
# 2. Power-up delay (important for EyeSPI displays)
# --------------------------------------------------------------------
print("Waiting for display power-up...")
time.sleep(0.5)  # 500 ms is usually enough; increase to 1–2 s if still blank

# --------------------------------------------------------------------
# 3. EyeSPI pin assignments (confirmed from your schematic)
# --------------------------------------------------------------------
spi = board.SPI()          # SCK=GPIO14, MOSI=GPIO15
tft_cs = board.A2          # GPIO28
tft_dc = board.A1          # GPIO27
tft_reset = board.A0       # GPIO26
tft_backlight = board.A3   # GPIO29

# --------------------------------------------------------------------
# 4. Backlight control
# --------------------------------------------------------------------
bl = digitalio.DigitalInOut(tft_backlight)
bl.direction = digitalio.Direction.OUTPUT
bl.value = True

# --------------------------------------------------------------------
# 5. Initialize SPI display bus
# --------------------------------------------------------------------
display_bus = FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=24_000_000,  # lower to 24 MHz for reliable startup
)

# --------------------------------------------------------------------
# 6. Initialize ILI9341 driver
# --------------------------------------------------------------------
display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=0
)

print("Display initialized!")

# --------------------------------------------------------------------
# 7. Create simple graphics scene
# --------------------------------------------------------------------
main_group = displayio.Group()
display.root_group = main_group

# Background
bitmap = displayio.Bitmap(320, 240, 1)
palette = displayio.Palette(1)
palette[0] = 0x000020
bg = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group.append(bg)

# Labels & shapes
title = label.Label(terminalio.FONT, text="Fruit Jam EyeSPI OK!", color=0xFFFFFF, x=50, y=30)
main_group.append(title)
main_group.append(Rect(20, 60, 80, 60, fill=0xFF0000))
main_group.append(Rect(120, 60, 80, 60, fill=0x00FF00))
main_group.append(Circle(240, 150, 40, fill=0x0000FF))

footer = label.Label(terminalio.FONT, text="DisplayIO test", color=0xFFFF00, x=90, y=220)
main_group.append(footer)

while True:
    pass
