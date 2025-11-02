import time
import board
import displayio
import digitalio
import terminalio
from adafruit_display_text import label
from fourwire import FourWire          # <- use the separate module
import adafruit_ili9341

# 1) release any built-in display
if hasattr(board, "DISPLAY"):
    board.DISPLAY.auto_refresh = False
displayio.release_displays()

# 2) short power-up delay
time.sleep(0.5)

# 3) your pin remap
tft_backlight = board.D6   # backlight
tft_dc        = board.D7   # D/C
tft_reset     = board.D8   # RST
tft_cs        = board.D9   # CS

# 4) backlight on
bl = digitalio.DigitalInOut(tft_backlight)
bl.direction = digitalio.Direction.OUTPUT
bl.value = True

# 5) SPI bus
spi = board.SPI()  # hardware SPI from Fruit Jam

# 6) display bus — NOTE: FourWire from the fourwire module
display_bus = FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=24_000_000,
)

# 7) ILI9341 driver
display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=0,
)

# 8) simple screen to prove it works
main = displayio.Group()
display.root_group = main

text = label.Label(
    terminalio.FONT,
    text="D6 BL  D7 DC  D8 RST  D9 CS",
    color=0xFFFFFF,
    x=10,
    y=20,
)
main.append(text)

while True:
    pass
