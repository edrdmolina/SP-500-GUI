from UI import FileHandlerGUI

# Add path to Directories to these constant variables.
INITIAL_DIR = "/Users/edrdmolina/Desktop/InProcess"
TEMP_DIR = "/Users/edrdmolina/Desktop/Temp_dir"
TARGET_DIR = "/Users/edrdmolina/Desktop/Target_dir"

app = FileHandlerGUI(initial_dir=INITIAL_DIR, temp_dir=TEMP_DIR, target_dir=TARGET_DIR)
app.run()
