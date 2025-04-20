import os
import platform
import subprocess
import sys

def build_executable():
    # Get the current platform
    current_platform = platform.system().lower()
    
    # Define the PyInstaller command
    pyinstaller_cmd = [
        'pyinstaller',
        '--name=pmclient',
        '--onefile',
        '--clean',
        'main.py'
    ]
    
    # Add platform-specific options
    if current_platform == 'windows':
        pyinstaller_cmd.extend(['--icon=NONE'])  # Add icon if needed
    elif current_platform == 'darwin':  # macOS
        pyinstaller_cmd.extend(['--windowed'])  # For macOS app bundle
    elif current_platform == 'linux':
        pyinstaller_cmd.extend(['--strip'])  # Strip symbols for smaller size
    
    # Run PyInstaller
    try:
        subprocess.run(pyinstaller_cmd, check=True)
        print(f"Successfully built executable for {current_platform}")
        print(f"Executable location: dist/pmclient{'.exe' if current_platform == 'windows' else ''}")
    except subprocess.CalledProcessError as e:
        print(f"Error building executable: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build_executable() 