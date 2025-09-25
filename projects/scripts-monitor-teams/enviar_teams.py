import requests

from settings import TEAMS_WEBHOOK_URL

def enviar_alerta_teams(mensaje):
    if not TEAMS_WEBHOOK_URL:
        print("[WARN] La variable TEAMS_WEBHOOK_URL no esta definida. No se envio la alerta.")
        return

    payload = {"mensaje": mensaje}
    try:
        response = requests.post(TEAMS_WEBHOOK_URL, json=payload, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error al enviar alerta a Teams: {e}")
