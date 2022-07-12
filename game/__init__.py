try:
    from .main import run
except ImportError:
    from main import run

if __name__ == "__main__":
    run()
