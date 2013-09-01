from .common import run_nose2, run_behave


def main():
    import sys

    nose2 = run_nose2()
    behave = run_behave()
    sys.exit(nose2 + behave)


if __name__ == '__main__':
    main()
