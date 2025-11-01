import board
import displayio
import terminalio
import digitalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from fourwire import FourWire
import adafruit_ili9341

# Release any existing display
displayio.release_displays()

# ---------------- EyeSPI pin assignments (Fruit Jam bottom header) ----------------
spi = board.SPI()          # SCK=GPIO14, MOSI=GPIO15
tft_cs = board.A2          # GPIO28
tft_dc = board.A1          # GPIO27
tft_reset = board.A0       # GPIO26
tft_backlight = board.A3   # GPIO29

# ---------------- Display setup ----------------
display_bus = FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=48_000_000,  # 48 MHz stable for EyeSPI
)

display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=0  # change to 90/180/270 as needed
)

# ---------------- Backlight control ----------------
bl = digitalio.DigitalInOut(tft_backlight)
bl.direction = digitalio.Direction.OUTPUT
bl.value = True

# ---------------- DisplayIO scene ----------------
main_group = displayio.Group()
display.root_group = main_group

# background
bitmap = displayio.Bitmap(320, 240, 1)
palette = displayio.Palette(1)
palette[0] = 0x101010
bg = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group.append(bg)

# title text
title = label.Label(terminalio.FONT, text="Fruit Jam + ILI9341", color=0xFFFFFF, x=60, y=30)
main_group.append(title)

# some shapes to verify color + positioning
main_group.append(Rect(40, 60, 100, 60, fill=0xFF0000))   # red rectangle
main_group.append(Rect(160, 60, 100, 60, fill=0x00FF00))  # green rectangle
main_group.append(Circle(160, 160, 40, fill=0x0000FF))    # blue circle

# info label
footer = label.Label(terminalio.FONT, text="displayio demo", color=0xFFFF00, x=100, y=230)
main_group.append(footer)

while True:
    pass
