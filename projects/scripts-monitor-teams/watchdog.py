import csv
from datetime import datetime, timedelta

import pandas as pd

from enviar_teams import enviar_alerta_teams
from enviar_teams_watchdog import enviar_watchdog
from settings import CONFIG_FILE, LOG_FILE

SHEET_NAME = "scripts"

def leer_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            print(f"[INFO] Log leido correctamente desde {LOG_FILE}")
            return list(csv.DictReader(f))
    except Exception as e:
        print(f"[ERROR] Falla al leer el log: {e}")
        enviar_alerta_teams(f"No se pudo leer el log `{LOG_FILE}`: {e}")
        return []

def leer_config_desde_excel(path=CONFIG_FILE):
    try:
        df = pd.read_excel(path, sheet_name=SHEET_NAME)
        df = df[df["activo"] == 1]
        print(f"[INFO] Configuracion leida. Scripts activos: {len(df)}")
        return df
    except Exception as e:
        print(f"[ERROR] Falla al leer la configuracion: {e}")
        enviar_alerta_teams(f"Error al leer el archivo de configuracion: {e}")
        return pd.DataFrame()

def verificar():
    logs = leer_logs()
    ahora = datetime.now()
    df_config = leer_config_desde_excel()
    mensajes_watchdog = []

    for _, cfg in df_config.iterrows():
        script = cfg["script"]
        msg = f"\n=> Verificando script: **{script}**"
        print(msg)
        mensajes_watchdog.append(msg)

        if pd.notna(cfg.get("dias_mes")):
            dias_validos = [int(d.strip()) for d in str(cfg["dias_mes"]).split(",")]
            if ahora.day not in dias_validos:
                msg = f"[SKIP] Dia del mes {ahora.day} no esta en {dias_validos}"
                print(msg)
                mensajes_watchdog.append(msg)
                continue

        if pd.notna(cfg.get("dias_semana")):
            dias_semana_validos = [int(d.strip()) for d in str(cfg["dias_semana"]).split(",")]
            if ahora.weekday() not in dias_semana_validos:
                msg = f"[SKIP] Dia de la semana {ahora.weekday()} no esta en {dias_semana_validos}"
                print(msg)
                mensajes_watchdog.append(msg)
                continue

        t_ini, t_fin = None, None
        if pd.notna(cfg.get("hora_fija")):
            try:
                partes = str(cfg["hora_fija"]).split(":")
                if len(partes) < 2:
                    raise ValueError(f"Formato invalido en hora_fija: {cfg['hora_fija']}")
                h, m = int(partes[0]), int(partes[1])
                t_ini = ahora.replace(hour=h, minute=m, second=0, microsecond=0)
                t_fin = t_ini + timedelta(minutes=int(cfg["tolerancia_min"]))
                msg = f"[INFO] Ventana fija: {t_ini.time()} - {t_fin.time()}"
                print(msg)
                mensajes_watchdog.append(msg)
            except Exception as e:
                print(f"[ERROR] Problema en hora_fija para `{script}`: {e}")
                continue
        elif pd.notna(cfg.get("frecuencia_min")):
            try:
                frecuencia = int(cfg["frecuencia_min"])
                tolerancia = int(cfg["tolerancia_min"])
                minutos_totales = ahora.hour * 60 + ahora.minute
                ciclos = minutos_totales // frecuencia
                base_minuto = ciclos * frecuencia
                t_ini = ahora.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(minutes=base_minuto)
                t_fin = t_ini + timedelta(minutes=tolerancia)
                msg = f"[INFO] Ventana frecuencia: {t_ini.time()} - {t_fin.time()}"
                print(msg)
                mensajes_watchdog.append(msg)
            except Exception as e:
                print(f"[ERROR] Problema en frecuencia/tolerancia para `{script}`: {e}")
                continue
        else:
            msg = "[SKIP] No hay hora_fija ni frecuencia definida."
            print(msg)
            mensajes_watchdog.append(msg)
            continue

        if ahora < t_ini:
            msg = f"[INFO] Todavia no llego el horario pactado de hoy para {script}."
            print(msg)
            mensajes_watchdog.append(msg)
            continue

        ejecuciones_script = [
            l for l in logs
            if l["script"] == script and l["status"] in ("OK", "ERROR") and l["timestamp_fin"]
        ]
        if not ejecuciones_script:
            print(f"[ALERTA] No hay ejecuciones registradas para `{script}`.")
            enviar_alerta_teams(f"El script `{script}` nunca se ejecuto segun el log.")
            continue

        ult_error = next(
            (l for l in reversed(ejecuciones_script) if l["status"] == "ERROR"),
            None
        )

        fue_recuperado = False
        if ult_error:
            timestamp_error = datetime.strptime(ult_error["timestamp_fin"], "%d-%m-%Y %H:%M:%S")
            for l in ejecuciones_script:
                if l["status"] == "OK":
                    timestamp_ok = datetime.strptime(l["timestamp_fin"], "%d-%m-%Y %H:%M:%S")
                    if timestamp_ok > timestamp_error:
                        fue_recuperado = True
                        break

        if ult_error and not fue_recuperado:
            print(f"[ALERTA] Error no corregido desde {ult_error['timestamp_fin']}")
            enviar_alerta_teams(
                f"El script `{script}` tuvo un error el {ult_error['timestamp_fin']} y no fue corregido aun."
            )
            continue

        ejec_en_ventana = [
            l for l in ejecuciones_script
            if t_ini <= datetime.strptime(l["timestamp_fin"], "%d-%m-%Y %H:%M:%S") <= t_fin
        ]

        if not ejec_en_ventana:
            ejecuciones_hoy = [
                l for l in ejecuciones_script
                if datetime.strptime(l["timestamp_fin"], "%d-%m-%Y %H:%M:%S").date() == ahora.date()
            ]
            if ejecuciones_hoy:
                msg = "[INFO] Ejecutado correctamente, aunque fuera de la ventana."
                print(msg)
                mensajes_watchdog.append(msg)
            else:
                print("[ALERTA] No se ejecuto dentro de la ventana ni en el dia.")
                enviar_alerta_teams(
                    f"El script `{script}` no se ejecuto entre {t_ini.strftime('%H:%M')} y {t_fin.strftime('%H:%M')} ni en el resto del dia."
                )
        else:
            msg = "[OK] Ejecutado correctamente dentro de la ventana."
            print(msg)
            mensajes_watchdog.append(msg)

    if mensajes_watchdog:
        texto = "\n".join(mensajes_watchdog)
        enviar_watchdog(f"\n{texto}\n```")

if __name__ == "__main__":
    verificar()
