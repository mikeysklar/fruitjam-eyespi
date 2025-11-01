import board
import busio
import displayio
import terminalio
import digitalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle

# Import correct FourWire bus class
from fourwire import FourWire

import adafruit_ili9341
import adafruit_focaltouch

# Release any previous displays
displayio.release_displays()

# EyeSPI pin assignments (Fruit Jam bottom header)
spi = board.SPI()
tft_cs = board.A2
tft_dc = board.A1
tft_reset = board.A0
tft_backlight = board.A3

# Setup display bus
display_bus = FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=48_000_000,
)

# Setup display driver
display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=0
)

# Backlight on
bl = digitalio.DigitalInOut(tft_backlight)
bl.direction = digitalio.Direction.OUTPUT
bl.value = True

# Setup I2C touch
i2c = board.I2C()
touch = adafruit_focaltouch.Adafruit_FocalTouch(i2c, debug=False)

# Build DisplayIO scene
main_group = displayio.Group()
display.root_group = main_group

bitmap = displayio.Bitmap(320, 240, 1)
palette = displayio.Palette(1)
palette[0] = 0x202020
bg = displayio.TileGrid(bitmap, pixel_shader=palette)
main_group.append(bg)

title = label.Label(terminalio.FONT, text="Fruit Jam + ILI9341 + FocalTouch", color=0xFFFFFF, x=10, y=20)
main_group.append(title)

hint = label.Label(terminalio.FONT, text="Touch screen to move circle", color=0xFFFF00, x=10, y=40)
main_group.append(hint)

cursor = Circle(50, 50, 10, outline=0x00FF00)
main_group.append(cursor)

touch_label = label.Label(terminalio.FONT, text="x: --  y: --", color=0xFFFFFF, x=10, y=220)
main_group.append(touch_label)

while True:
    if touch.touched:
        pts = touch.touches
        if pts:
            p = pts[0]
            tx, ty = p["x"], p["y"]
            # Optional axis correction:
            # tx, ty = ty, tx
            # tx = 320 - tx
            # ty = 240 - ty
            cursor.x, cursor.y = tx, ty
            touch_label.text = f"x:{tx:3d} y:{ty:3d}"
    else:
        touch_label.text = "x: --  y: --"
