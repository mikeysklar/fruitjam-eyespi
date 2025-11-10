# 🧠 Fruit Jam → EyeSPI Display Adapter

![Fruit Jam to EyeSPI Adapter](images/fj-demo.jpeg)
*Single-sided breakout board CNC-milled, fiber-laser etched, and resin-coated.*

---

![Fruit Jam to EyeSPI Adapter](images/fj-scope-asm.jpeg)

## 🧩 Overview

This project is a **compact breakout PCB** that connects the **16-pin Adafruit Fruit Jam header** to an **18-pin EyeSPI FFC** connector for driving TFT displays 

It allows the **Fruit Jam** to output to Adafruit EyeSPI displays, enabling small embedded builds like:

- 🎧 **MP3 or media players**
- 🕹️ **Mini gaming consoles**
- 💻 **Pocket computers**
- 🔧 **Control panels and dashboards**
- 📟 **Status monitors**
- 🧩 **Rapid prototyping setups**

---


## 🧰 Features

- Converts **Fruit Jam 16-pin display header → 18-pin EyeSPI FFC**
- Plug-and-play with **Adafruit EyeSPI TFT displays**
- Fully compatible with **CircuitPython `displayio`**
- Fabricated as a **single-sided PCB** using **CNC + fiber laser**
- Protected with a **UV resin coat** for strength and finish
- Small footprint and easy hand-solder assembly

---

## 📁 Repository Structure

| Folder | Description |
|:-------|:-------------|
| `/hardware/` | KiCad schematic and PCB layout files |
| `/bom/` | Bill of Materials (BOM) in `.csv` and `.pdf` formats |
| `/3d/` | 3D STEP and render files for case design or visualization |
| `/images/` | Build photos, renders, and setup examples |
| `/docs/` | Notes, pinout diagrams, and fabrication details |

---

## 🧩 Hardware Design

- **Input:** 16-pin Fruit Jam display header  
- **Output:** 18-pin EyeSPI FFC (0.5 mm pitch)  
- **Board Type:** Single-sided PCB  
- **Fabrication:** CNC milled + laser etched traces + resin coat  
- **Connector Orientation:** FFC faces upward (standard EyeSPI alignment)

**Example Configuration:**

| Signal | From Fruit Jam | To EyeSPI |
|:-------|:----------------|:----------|
| 3V3 | Pin 1 | Pin 1 |
| GND | Pin 2 | Pin 2 |
| SCK | Pin 3 | Pin 3 |
| MOSI | Pin 4 | Pin 4 |
| DC | Pin 5 | Pin 5 |
| RST | Pin 6 | Pin 6 |
| CS | Pin 7 | Pin 7 |
| BL | Pin 8 | Pin 8 |
| ... | ... | ... |

*(Add your final verified pin mapping table and reference diagram here.)*

---

## 🧪 Testing & Compatibility

The adapter has been validated with the following setup:

- **CircuitPython 10.x**  
- **Adafruit Fruit Jam** (RP2350-based)  
- **Displays:**  
  - TL034WVS05-B1477A 480×480 TFT  
  - 1.9" 240×320 TFT (EyeSPI)  
- **Libraries:** `displayio`, `adafruit_st7789`, `adafruit_rgb_display`  

**Example Test Code:**

```python
import board, displayio
from adafruit_st7789 import ST7789

spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(display_bus, width=240, height=320, rotation=180)

