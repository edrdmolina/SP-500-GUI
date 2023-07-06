from UI import FileHandlerGUI

# Add path to Directories to these constant variables.
INITIAL_DIR = "/run/user/1000/gvfs/afp-volume:host=GuruBibliotheca.local,user=GuruBibliotheca,volume=Vault/Coastal Film Lab/SP-500V2ExportDir"
TEMP_DIR = "/home/sp500-ii/Pictures/SP-500-Temp-Dir"
TARGET_DIR = "/run/user/1000/gvfs/afp-volume:host=GuruBibliotheca.local,user=GuruBibliotheca,volume=Vault/Coastal Film Lab/scannedimages"

app = FileHandlerGUI(initial_dir=INITIAL_DIR, temp_dir=TEMP_DIR, target_dir=TARGET_DIR)
app.run()
