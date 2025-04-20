# Performance Monitor Client

A command-line client for connecting to the Performance Monitor server.

## Building Executables

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Instructions

#### For Linux Users:
```bash
# Install Python and pip if not already installed
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Clone the repository
git clone <repository-url>
cd client

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the executable
python build.py

# Make the executable file executable
chmod +x dist/pmclient

# Test the executable
./dist/pmclient connect --auth-key YOUR_AUTH_KEY --host-url http://example.com
```

#### For macOS Users:
```bash
# Install Python and pip if not already installed
# (If you don't have Homebrew, install it first: https://brew.sh/)
brew install python

# Clone the repository
git clone <repository-url>
cd client

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the executable
python build.py

# Make the executable file executable
chmod +x dist/pmclient

# Test the executable
./dist/pmclient connect --auth-key YOUR_AUTH_KEY --host-url http://example.com
```

#### For Windows Users:
```bash
# Clone the repository
git clone <repository-url>
cd client

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Build the executable
python build.py

# Test the executable
.\dist\pmclient.exe connect --auth-key YOUR_AUTH_KEY --host-url http://example.com
```

## Usage

### Connecting to Server
```bash
# Linux/macOS
./dist/pmclient connect --auth-key YOUR_AUTH_KEY --host-url http://example.com

# Windows
.\dist\pmclient.exe connect --auth-key YOUR_AUTH_KEY --host-url http://example.com
```

### Disconnecting from Server
```bash
# Linux/macOS
./dist/pmclient disconnect

# Windows
.\dist\pmclient.exe disconnect
```

## Making the Command Available System-Wide

### Linux/macOS:
```bash
# Create a symbolic link (requires sudo on Linux)
sudo ln -s "$(pwd)/dist/pmclient" /usr/local/bin/pmclient

# Now you can use the command from anywhere
pmclient connect --auth-key YOUR_AUTH_KEY --host-url http://example.com
```

### Windows:
1. Add the `dist` directory to your system's PATH
2. Open System Properties > Advanced > Environment Variables
3. Under System Variables, find and select "Path"
4. Click "Edit" and add the full path to your `dist` directory
5. Click "OK" to save

## Troubleshooting

### Common Issues:

#### Linux/macOS:
- If you get "Permission denied" error:
  ```bash
  chmod +x dist/pmclient
  ```
- If you get "command not found" after adding to PATH:
  ```bash
  source ~/.bashrc  # or source ~/.zshrc for zsh users
  ```

#### Windows:
- If the executable doesn't run, make sure you're running Command Prompt or PowerShell as Administrator
- If you get a security warning, you may need to unblock the file in Properties

## Platform-Specific Notes

### Windows
- The executable is named `pmclient.exe`
- You can add the `dist` directory to your PATH for global access

### macOS
- The executable is named `pmclient`
- You may need to make it executable: `chmod +x pmclient`
- If you get security warnings, you may need to allow the app in System Preferences > Security & Privacy

### Linux
- The executable is named `pmclient`
- You may need to make it executable: `chmod +x pmclient`
- Some distributions might require additional dependencies for PyInstaller 