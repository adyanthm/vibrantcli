import builtins

# Why _ before variable names?? devs ignore it + import * does not include vars starting with _

_enabled = False

# we dont want to lose this...
_og_print = builtins.print

def autoreset(enable=True):
  global _enabled

  if enable and not _enabled:
    # simulate print below !
    def new_print(*args, **kwargs):
      from .style import style
      new_args=[str(arg) + style.reset for arg in args]
      _og_print(*new_args, **kwargs)

    builtins.print=new_print
    _enabled=True

  elif not enable and _enabled:
    builtins.print=_og_print
    _enabled=False