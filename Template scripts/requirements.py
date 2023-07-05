import os
import subprocess
import sys

def install_requirements():
    # Specify the full path of the requirements file
    requirements_file = './Template Scripts/requirements.txt'

    # Run pip install command
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])

if __name__ == '__main__':
    install_requirements()