try:
    from .main import run
except ImportError:
    from main import run

run()
