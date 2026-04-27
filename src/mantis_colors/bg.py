class bg:
  black   = "\033[40m"
  red     = "\033[41m"
  green   = "\033[42m"
  yellow  = "\033[43m"
  blue    = "\033[44m"
  magenta = "\033[45m"
  cyan    = "\033[46m"
  white   = "\033[47m"
  reset   = "\033[49m"
  
  @staticmethod
  def rgb(r,g,b):
    return f"\033[48;2;{r};{g};{b}m"
    
  @staticmethod
  def hex(code):
    code = code.lstrip('#')    
    if len(code) !=6:
      raise ValueError("HEX value must be 6 characters (RRGGBB)")

    try:
      r = int(code[0:2], 16)
      g = int(code[2:4], 16)
      b = int(code[4:6], 16)
      return bg.rgb(r, g, b)
      
    except ValueError:
      raise ValueError("Invalid HEX Color")