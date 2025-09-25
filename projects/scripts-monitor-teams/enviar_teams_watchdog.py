import requests

from settings import TEAMS_WATCHDOG_WEBHOOK_URL

def enviar_watchdog(mensaje):
    if not TEAMS_WATCHDOG_WEBHOOK_URL:
        print("[WARN] La variable TEAMS_WATCHDOG_WEBHOOK_URL no esta definida. No se envio el resumen.")
        return

    payload = {"mensaje": mensaje}
    try:
        response = requests.post(TEAMS_WATCHDOG_WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error al enviar alerta a Teams: {e}")
