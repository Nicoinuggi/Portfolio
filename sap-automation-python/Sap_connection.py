import psutil
import subprocess
import win32com.client
import time

# Define SAP Logon path
sap_executable_path = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

# Define SAP connection parameters
connection_name = "YOUR_CONNECTION_NAME" 
username = "YOUR_USERNAME"  
password = "YOUR_PASSWORD"  

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

def kill_sap_process():
    subprocess.run('TASKKILL /F /IM saplogon.exe /T')

def start_sap_gui():
    subprocess.Popen([sap_executable_path])

def connect_to_existing_session():
    try:
        sap_gui_app = win32com.client.GetObject("SAPGUI")
        application = sap_gui_app.GetScriptingEngine
        connection = application.Children(0)  
        session = connection.Children(0)  
        return session
    except:
        return None

def open_new_sap_session():
    sap_gui_app = win32com.client.GetObject("SAPGUI")
    application = sap_gui_app.GetScriptingEngine
    connection = application.OpenConnection(sap_connection_name, True)
    session = connection.Children(0)
    return session

# Step 1: Check if saplogon.exe is running
if is_process_running("saplogon.exe"):
    print("SAP is running. Checking for existing session...")

    # Step 2: Try to connect to an existing session
    session = connect_to_existing_session()

    if session:
        print("Connected to existing SAP session.")
    else:
        print("No active session or session not responding. Restarting SAP...")

        # Step 3: Kill SAP process if session is unresponsive
        kill_sap_process()
        start_sap_gui()

        # Step 4: Wait until SAP GUI opens and connect to a new session
        while not is_process_running("saplogon.exe"):
            time.sleep(5)  # Adjust if needed
        session = open_new_sap_session()

        # Step 5: Authenticate only if a new session is started
        print("Authenticating in SAP...")
        session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = sap_username
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = sap_password
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = len(sap_password)
        session.findById("wnd[0]").sendVKey(0)  
        session.findById("wnd[0]").maximize()
else:
    print("SAP is not running. Starting SAP GUI...")

    # Start SAP and wait for it to open
    start_sap_gui()
    while not is_process_running("saplogon.exe"):
        time.sleep(5)  # Adjust if needed
    session = open_new_sap_session()

    # Authenticate since it's a new session
    print("Authenticating in SAP...")
    session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = sap_username
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = sap_password
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = len(sap_password)
    session.findById("wnd[0]").sendVKey(0) 
    session.findById("wnd[0]").maximize()

# Step 6: Run SAP transaction code (skip authentication if session was already active)
print("Running transaction...")
session.findById("wnd[0]/tbar[0]/okcd").text = "/nmb52"  # Replace with the desired transaction script
session.findById("wnd[0]").sendVKey(0)
