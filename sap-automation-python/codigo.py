import subprocess
import win32com.client
import time
import psutil

# Open SAP GUI
sap_executable_path = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

connection_name = "YOUR_CONNECTION_NAME"  # Change to your connection name
username = "YOUR_USERNAME"  # Change to your username
password = "YOUR_PASSWORD"  # Change to your password

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

# Check if saplogon.exe is running
if is_process_running("saplogon.exe"):
    # Kill task if running
    subprocess.run('TASKKILL /F /IM saplogon.exe /T')

subprocess.Popen([sap_executable_path])

# Wait process to open
while not is_process_running("saplogon.exe"):
    time.sleep(5) #Change if your system take longer to open SAP Logon window
    
try:
    #  Connect SAP GUI using win32com.client
    sap_gui_app = win32com.client.GetObject("SAPGUI")  
    application = sap_gui_app.GetScriptingEngine  
    
    if not application:
        print("Error connecting SAP GUI Scripting.")
    else:
        
        connection = application.OpenConnection(connection_name, True)  
        session = connection.Children(0)
    
        # Authenticate in SAP
        session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = username #
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = password  # 
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = len(password)  
        session.findById("wnd[0]").sendVKey(0)  
    
        # Maximizar la ventana de SAP
        session.findById("wnd[0]").maximize()
    
        #Here you can paste your SAP GUI Script to downoload the file you need- You can use SAP GUI Scripting tool for this and  check the format.
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nmb52" # Transaction name
        session.findById("wnd[0]").sendVKey(0) 
    

except Exception as e:
    print(f"An error occurred: {e}")
 


