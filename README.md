# vibrant

A simple, lightweight, and modern Python library for adding color and style to your terminal output.

---

## Installation

```bash
pip install vibrant
```

## Quick Start

```python
from vibrant import fg, bg, style, init

# You can initialize with autoreset so you don't have to manually reset colors after every color change!
init(autoreset_enabled=True)

print(fg.red + "red color")
print(bg.blue + fg.white + "white text on blue background")
print(fg.hex("#ff6600") + style.bold + "bold orange text using HEX")
```

---

## Features

### Colors (Standard & True Color)
Vibrant supports standard ANSI colors, as well as **RGB** and **HEX** for 24-bit True Color support.

```python
from vibrant import fg, bg

# Standard colors
print(fg.green + "success!")
print(fg.red + "error!")

# RGB Support
print(fg.rgb(255, 100, 0) + "RGB orange")
print(bg.rgb(0, 100, 255) + "RGB blue background")

# HEX Support (with or without #)
print(fg.hex("#ff6600") + "HEX orange")
print(bg.hex("0066ff") + "HEX blue background")
```

### Text Styles
Apply common text decorations with ease.

```python
from vibrant import style

print(style.bold + "Bold Text")
print(style.underline + "Underlined Text")
print(style.strikethrough + "Strikethrough")
print(style.bold + style.italic + "Bold and Italic")
```

### Automatic Reset
Are you tired of manually adding `reset` every time? Use `init()` or `autoreset()` to handle it globally.

> [!NOTE]
> When `autoreset` is enabled, use string concatenation (`+`) instead of commas (`,`) in `print()` to ensure colors apply correctly to the entire output.

```python
from vibrant import init, fg, autoreset
autoreset()
print(fg.red + "Everything is reset after each print call automatically")

# or 
init(autoreset_enabled=True)
print(fg.red + "Everything is reset after each print call automatically")
```

---

## Comparison

| Feature | `vibrant` | `colorama` | `termcolor` |
| :--- | :---: | :---: | :---: |
| **RGB Support** | ✅ | ❌ | ❌ |
| **HEX Support** | ✅ | ❌ | ❌ |
| **Simple API** | ✅ | ✅ | ✅ |
| **Auto-reset** | ✅ | ✅ | ❌ |

---

## License
MIT © [Adyanth M](https://github.com/adyanth)