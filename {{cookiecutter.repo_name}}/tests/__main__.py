from tests.common import run_nose2, run_behave, run_pyflakes


def main():
    import sys

    nose2 = run_nose2()
    behave = run_behave()
    pyflakes = run_pyflakes()
    sys.exit(nose2 + behave + pyflakes)


if __name__ == '__main__':
    main()
