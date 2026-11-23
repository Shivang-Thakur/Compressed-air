"""Shared config for the Compressor Leakage project.

HiveMQ credentials are NEVER hard-coded here.
Put them in a `.env` file in the project root (see `.env.example`)
or as environment variables. That way the code can go on GitHub
safely and the password never leaks.

.env format:
    HIVEMQ_HOST=xxxx.s1.eu.hivemq.cloud
    HIVEMQ_PORT=8883
    HIVEMQ_USERNAME=your-mqtt-username
    HIVEMQ_PASSWORD=your-mqtt-password
    MQTT_TOPIC=compressor/sensor

Streamlit Cloud par: .env file repo me mat daalo. Wahan app ki
Settings -> Secrets me wahi values paste karo (format ke liye
.streamlit/secrets.toml.example dekho). Ye file Streamlit ke
secrets ko bhi padh leti hai, taaki Cloud wala dashboard_live.py
bina code badle HiveMQ se jud sake. Streamlit install na ho ya
secrets na hon, to ye hissa chupchap skip ho jaata hai - koi crash nahi.
"""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_FILE = DATA_DIR / "compressor_data.csv"


def _load_dotenv():
    env_file = PROJECT_ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _load_streamlit_secrets():
    """Streamlit Cloud secrets (agar Streamlit runtime me chal raha ho)."""
    try:
        import streamlit as st

        secrets = dict(st.secrets)
    except Exception:
        return
    for key in ("HIVEMQ_HOST", "HIVEMQ_PORT", "HIVEMQ_USERNAME", "HIVEMQ_PASSWORD", "MQTT_TOPIC"):
        if key in secrets and secrets[key]:
            os.environ.setdefault(key, str(secrets[key]))


_load_dotenv()
_load_streamlit_secrets()

HIVEMQ_HOST = os.getenv("HIVEMQ_HOST", "YOUR_CLUSTER.s1.eu.hivemq.cloud")
HIVEMQ_PORT = int(os.getenv("HIVEMQ_PORT", "8883"))
HIVEMQ_USERNAME = os.getenv("HIVEMQ_USERNAME", "")
HIVEMQ_PASSWORD = os.getenv("HIVEMQ_PASSWORD", "")
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "compressor/sensor")


def check_credentials():
    """Return (ok, message). rc=5 fix starts here: no username = no login."""
    if not HIVEMQ_USERNAME or not HIVEMQ_PASSWORD:
        return False, (
            "HiveMQ username/password set nahi hai. "
            ".env file banao (.env.example dekho) ya environment variables set karo."
        )
    if "YOUR_CLUSTER" in HIVEMQ_HOST:
        return False, (
            "HIVEMQ_HOST abhi placeholder hai. HiveMQ Cloud console se apne "
            "cluster 'keenbee' ka asli host copy karke .env me daalo."
        )
    return True, "Credentials mil gaye."
