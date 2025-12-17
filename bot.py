import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# TOKEN DEL BOT
TOKEN = os.environ[TELEGRAM_BOT_TOKEN]

# URL DE LA API A CONSUMIR
URL = "https://dolarapi.com/v1/dolares"

# TIMEZONE ARGENTINA BUENOS AIRES
AR_TZ = ZoneInfo("America/Argentina/Buenos_Aires")


def format_fecha_ar(iso_utc: str) -> str:
    # Ej: "2025-12-17T15:02:00.000Z"
    dt = datetime.fromisoformat(iso_utc.replace("Z", "+00:00"))
    dt_ar = dt.astimezone(AR_TZ)
    return dt_ar.strftime("%Y-%m-%d %H:%M:%S")

# FUNCIONES PARA OBTENER LA INFORMACION DEL DOLAR DE LA API


def get_dolar():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


def find_by_casa(data, casa_buscada: str):
    for item in data:
        if item.get("casa") == casa_buscada:
            return item
    return None

# FUNCIONES CONTROLADORAS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("✅ Listo. Usá /mep o /cripto")


async def mep(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_dolar()
    item = find_by_casa(data, "bolsa")
    if not item:
        await update.message.reply_text("No encontré la cotización MEP (bolsa).")
        return

    msg = (
        f"💱 {item['nombre']}\n"
        f"Compra: {item['compra']}\n"
        f"Venta: {item['venta']}\n"
        f"Actualizado (AR): {format_fecha_ar(item['fechaActualizacion'])}\n"
        f"Fuente: dolarapi.com"
    )
    await update.message.reply_text(msg)


async def cripto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_dolar()
    item = find_by_casa(data, "cripto")
    if not item:
        await update.message.reply_text("No encontré la cotización cripto.")
        return

    msg = (
        f"💱 {item['nombre']}\n"
        f"Compra: {item['compra']}\n"
        f"Venta: {item['venta']}\n"
        f"Actualizado (AR): {format_fecha_ar(item['fechaActualizacion'])}\n"
        f"Fuente: dolarapi.com"
    )
    await update.message.reply_text(msg)


# Funcion main
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("mep", mep))
    app.add_handler(CommandHandler("cripto", cripto))

    app.run_polling()


if __name__ == "__main__":
    main()
