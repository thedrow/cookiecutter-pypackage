def main():
    import sys
    from tests.common import run_behave

    behave = run_behave()
    sys.exit(behave)

if __name__ == '__main__':
    main()
