from what import What

SUCCESS = 0


def run_setup_command(command):
    return What('python setup.py', command)