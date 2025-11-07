import time
import board
import displayio
import digitalio
import terminalio
from adafruit_display_text import label
from fourwire import FourWire
import adafruit_ili9341

# --- release built-in display (Fruit Jam) ---
if hasattr(board, "DISPLAY"):
    board.DISPLAY.auto_refresh = False
displayio.release_displays()

time.sleep(0.5)

# --- your pins ---
tft_backlight = board.D6   # backlight
tft_dc        = board.D7   # D/C
tft_reset     = board.D8   # RST
tft_cs        = board.D9   # CS

# --- backlight on ---
bl = digitalio.DigitalInOut(tft_backlight)
bl.direction = digitalio.Direction.OUTPUT
bl.value = True

# --- SPI bus ---
spi = board.SPI()  # Fruit Jam HW SPI

# --- display bus @ 48 MHz (drop to 40_000_000 if flaky) ---
display_bus = FourWire(
    spi,
    command=tft_dc,
    chip_select=tft_cs,
    reset=tft_reset,
    baudrate=96_000_000,
)

# --- display ---
display = adafruit_ili9341.ILI9341(
    display_bus,
    width=320,
    height=240,
    rotation=0,
)

# --- root group ---
main = displayio.Group()
display.root_group = main

# full-screen bg we can recolor quickly
bg_bitmap = displayio.Bitmap(320, 240, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x000000
bg = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette)
main.append(bg)

# text on top so we know pins
text = label.Label(
    terminalio.FONT,
    text="RP2350 @ 48MHz SPI",
    color=0xFFFFFF,
    x=40,
    y=20,
)
main.append(text)

pins = label.Label(
    terminalio.FONT,
    text="D6 BL  D7 DC  D8 RST  D9 CS",
    color=0xFFFFFF,
    x=20,
    y=40,
)
main.append(pins)

# some colors to cycle through
colors = [
    0x000000,  # black
    0xFF0000,  # red
    0x00FF00,  # green
    0x0000FF,  # blue
    0xFFFF00,  # yellow
    0xFF00FF,  # magenta
    0x00FFFF,  # cyan
    0xFFFFFF,  # white
    0x202020,  # dim gray
]

i = 0
while True:
    bg_palette[0] = colors[i]
    i = (i + 1) % len(colors)
    time.sleep(0.5)
