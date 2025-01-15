import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    requirements = ["requests", "pytube"]
    for package in requirements:
        try:
            install(package)
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")

if __name__ == "__main__":
    main()
