import subprocess
import os

if __name__ == '__main__':
    for i in range(10):
        os.system("python anonymizer.py s r 10 | grep NCP")
