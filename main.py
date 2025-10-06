import json
import time
import requests
import schedule

# === Chargement de la configuration ===
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        TOKEN = config["telegram_token"]
        CHAT_ID = config["telegram_chat_id"]
        INTERVAL = config.get("update_interval_minutes", 10)
except Exception as e:
    print(f"❌ Erreur de chargement du fichier config.json : {e}")
    exit()

# === Fonction pour envoyer un message Telegram ===
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"⚠️ Erreur Telegram : {response.text}")
    except Exception as e:
        print(f"❌ Impossible d'envoyer le message Telegram : {e}")

# === Message de démarrage ===
print("🔍 Démarrage du bot A+...")
send_telegram_message("🤖 Bot A+ est bien en ligne et prêt à surveiller le marché !")

# === Exemple de fonction d’analyse fictive ===
def check_market_updates():
    print("📊 Analyse du marché en cours...")
    # Simule une mise à jour : ici, tu pourras plus tard ajouter les vraies analyses
    # (ex: récupération du prix via ccxt, détection de signaux, etc.)
    fake_signal = "Aucun signal fort détecté pour le moment."
    send_telegram_message(f"📈 Mise à jour automatique : {fake_signal}")

# === Planification de la tâche ===
schedule.every(INTERVAL).minutes.do(check_market_updates)
print(f"⏱️ Mises à jour prévues toutes les {INTERVAL} minutes.")

# === Boucle principale ===
while True:
    schedule.run_pending()
    time.sleep(5)
