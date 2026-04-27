class fg:
  black   = "\033[30m"
  red     = "\033[31m"
  green   = "\033[32m"
  yellow  = "\033[33m"
  blue    = "\033[34m"
  magenta = "\033[35m"
  cyan    = "\033[36m"
  white   = "\033[37m"
  reset   = "\033[39m"
  
  @staticmethod
  def rgb(r,g,b):
    return f"\033[38;2;{r};{g};{b}m"

  @staticmethod
  def hex(code):
    code = code.lstrip('#')    
    if len(code) !=6:
      raise ValueError("HEX value must be 6 characters (RRGGBB)")

    try:
      r = int(code[0:2], 16)
      g = int(code[2:4], 16)
      b = int(code[4:6], 16)
      return fg.rgb(r, g, b)
      
    except ValueError:
      raise ValueError("Invalid HEX Color")