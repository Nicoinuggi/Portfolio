import csv
from datetime import datetime

from settings import LOG_FILE

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_ejecucion(script, status, detalle=""):
    ahora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if status == "INICIO":
        fila = {
            "script": script,
            "timestamp_inicio": ahora,
            "timestamp_fin": "",
            "status": "INICIO",
            "detalle": ""
        }
        existe = LOG_FILE.exists()
        with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fila.keys())
            if not existe:
                writer.writeheader()
            writer.writerow(fila)

    else:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

        for row in reversed(rows):
            if row["script"] == script and row["status"] == "INICIO":
                row["timestamp_fin"] = ahora
                row["status"] = status
                row["detalle"] = detalle
                break

        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["script", "timestamp_inicio", "timestamp_fin", "status", "detalle"])
            writer.writeheader()
            writer.writerows(rows)
