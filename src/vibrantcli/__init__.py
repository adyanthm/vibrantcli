from .fg import fg
from .bg import bg
from .style import style
from .autoreset import autoreset
from .windows import enable_windows_ansi

reset = style.reset

def init(autoreset_enabled=False):
    enable_windows_ansi()
    if autoreset_enabled:
        autoreset()

__all__ = ["fg", "bg", "style", "autoreset", "reset", "init"]