def main():
    import sys
    from tests.common import run_nose2

    behave = run_behave()
    sys.exit(behave)

if __name__ == '__main__':
    main()
