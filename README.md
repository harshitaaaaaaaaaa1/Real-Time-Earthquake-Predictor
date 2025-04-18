INSTALLATIONS
1. Install Python 3.11.0
  1.Go to the official Python website:
  https://www.python.org/downloads/
  2.Click on Download Python 3.11.0 .
  3.Run the installer:
  ✅ Check the box: Add Python to PATH.
    Click Install Now.
  4.After installation, verify by opening Command Prompt and typing:
    python –version

2. Install Visual Studio Code (VS Code)
  1.Visit: https://code.visualstudio.com/
  2.Click Download for your operating system (Windows/macOS/Linux).
  3.Run the installer:
    •Accept terms.
    •Check Add to PATH and Register Code as an editor (optional).
    •Finish the installation.
3. Install Python Extension for VS Code
  1.Open VS Code.
  2.Go to the Extensions view (left sidebar or Ctrl+Shift+X).
  3.Search for Python and install the extension by Microsoft.
  4.Restart VS Code.

EXECUTION STEPS
1.Open VS Code
2.Click on Terminal and select new terminal
3. To create Virtual environment eneter ‘-m venv <<any environment name>>’ (If error occurs, download virtual environment for python)
4. <<any environment name>>/bin/activate
5. pip install --upgrade pip 
6.To install the packages ‘pip install -r requirements.txt’. Requeriments.txt file contains all the packages necessary for execution. 
7.Run application with ‘python main.py’ i.e in root directory of project repo.
8. Go to local host when application starts and use slider to choose dates for prediction in app.
