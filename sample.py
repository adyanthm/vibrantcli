from vibrant import fg, bg, style, init, reset

init(autoreset_enabled=True)

print("=== BASIC COLORS ===")
print(fg.red + "Red text")
print(fg.green + "Green text")
print(fg.blue + "Blue text")

print("\n=== BACKGROUND COLORS ===")
print(bg.red + "Red background")
print(bg.green + "Green background")
print(bg.blue + fg.white + "Blue bg + white text")

print("\n=== STYLES ===")
print(style.bold + "Bold text")
print(style.underline + "Underline text")
print(style.strikethrough + "Strikethrough text")
print(style.bold + style.underline + "Bold + Underline")

print("\n=== RGB ===")
print(fg.rgb(255, 100, 0) + "Orange (fg)")
print(bg.rgb(0, 100, 255) + "Blue-ish background")

print("\n=== HEX ===")
print(fg.hex("#ff6600") + "HEX orange")
print(fg.hex("ff6600") + "HEX without #")
print(bg.hex("#0066ff") + "HEX blue background")

print("\n=== COMBINATIONS ===")
print(bg.blue + fg.yellow + style.bold + "Styled combo")

print("\n=== RESET TEST (autoreset) ===")
print(fg.red + "This should be red", end="")
print(" ← this should NOT be red")

print("\n=== MANUAL RESET ===")
print(fg.green + "Green text" + reset)
print("Normal text again")
