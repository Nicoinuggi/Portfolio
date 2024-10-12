import subprocess
import win32com.client
import time
import os
from datetime import timedelta
from datetime import datetime
import calendar
import psutil

# 1. Abrir SAP GUI usando subprocess (reemplaza el script en .bat)
sap_executable_path = r'C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe'

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == process_name.lower():
            return True
    return False

# Verificar si el proceso saplogon.exe está corriendo
if is_process_running("saplogon.exe"):
    # Si el proceso está corriendo, lo cerramos de forma silenciosa
    subprocess.run('taskkill /IM saplogon.exe /F >nul 2>&1')
else:
    subprocess.Popen([sap_executable_path])
# Cerrar cualquier instancia previa de SAP GUI (similar a taskkill en PowerShell)
# subprocess.run('taskkill /IM saplogon.exe /F', shell=True)

# Abrir SAP GUI

# Esperar unos segundos para que SAP GUI se inicie (ajusta según sea necesario)
time.sleep(5)

# 2. Conectar a SAP GUI usando win32com.client
sap_gui_app = win32com.client.GetObject("SAPGUI")  # Conectar a SAP GUI
application = sap_gui_app.GetScriptingEngine  # Obtener el motor de scripting

if not application:
    print("Error connecting SAP GUI Scripting.")
else:
    # Abrir una conexión en SAP GUI (equivalente a tu VBA)
    connection = application.OpenConnection("CONNECTION NAME", True)  # Cambia al nombre de tu conexión
    session = connection.Children(0)

    # 3. Autenticarse en SAP
    session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = "USER"  # Cambia al nombre de usuario
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = "PASSWORD"  # Cambia a tu contraseña
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus()
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = len("PASSWORD")  # Ajustar la posición del cursor
    session.findById("wnd[0]").sendVKey(0)  # Simular la tecla "Enter"

    # Maximizar la ventana de SAP
    session.findById("wnd[0]").maximize()

    # 4. Ejecutar el script de SAP
    # Aquí es donde puedes pegar tu lógica de SAP recordar poner () luego de Cada SETFOCUS, press, select y ver sendVkey (0)  y caret
 


