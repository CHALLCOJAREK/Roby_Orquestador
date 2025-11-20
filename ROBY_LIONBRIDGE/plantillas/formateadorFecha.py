import json
import time
import re
from datetime import datetime

def quitar_zona_horaria(fecha):
    # Elimina cualquier zona como " -03", " +0200", " -05:00"
    return re.sub(r'\s[+-]\S*$', '', fecha).strip()

# Ruta al archivo JSON
ruta_json = 'C:/Proyectos/ROBY_LIONBRIDGE/plantillas/fechavencimientoLB.json'

print("📂 Abriendo archivo JSON...")
time.sleep(0.6)

with open(ruta_json, 'r', encoding='latin1') as f:
    data = json.load(f)

print("✅ Archivo cargado correctamente.")
time.sleep(0.6)

fecha_texto = data["Fecha Vencimiento"]
print(f"🗓️ Fecha encontrada en JSON: {fecha_texto}")
time.sleep(0.6)

# Limpiar la zona horaria si la tiene
fecha_texto_limpio = quitar_zona_horaria(fecha_texto)
print(f"🧹 Fecha limpia (sin zona): {fecha_texto_limpio}")
time.sleep(0.6)

try:
    print("🔎 Intentando parsear como formato en inglés...")
    fecha_obj = datetime.strptime(fecha_texto_limpio, "%B %d, %Y %I:%M %p")
    print("✅ Parseo exitoso en formato en inglés.")
except ValueError:
    try:
        print("⚠️ Formato en inglés no válido. Intentando formato ISO...")
        fecha_obj = datetime.strptime(fecha_texto_limpio, "%Y-%m-%d %H:%M")
        print("✅ Parseo exitoso en formato ISO.")
    except ValueError:
        print("❌ Error: Formato de fecha no reconocido.")
        raise ValueError(f"Formato de fecha no reconocido: {fecha_texto}")

time.sleep(0.6)

fecha_formateada = fecha_obj.strftime("%Y-%m-%d %H:%M")
print(f"🛠️ Fecha formateada: {fecha_formateada}")
time.sleep(0.6)

data["Fecha Vencimiento"] = fecha_formateada
print("✍️ Sobrescribiendo la fecha en el diccionario...")
time.sleep(0.8)

with open(ruta_json, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Archivo JSON actualizado exitosamente. 🚀")
time.sleep(0.10)