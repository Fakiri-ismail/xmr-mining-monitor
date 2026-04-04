import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://xmr.nanopool.org/api/v1"
WALLET   = os.getenv("WALLET_ADDRESS")


def get_data(url: str) -> dict:
    """Generic GET request to Nanopool API."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    payload = response.json()
    if not payload.get("status"):
        raise ValueError(f"API returned error: {payload}")
    return payload["data"]


def get_user_data() -> dict:
    """Fetch full user data: balance, hashrate, workers."""
    url = f"{BASE_URL}/user/{WALLET}"
    return get_data(url)


def get_workers_shares(data: dict) -> list:
    """Extract workers shares."""
    workers_shares = []
    w_names  = [w["id"] for w in data.get("workers", [])]
    for w_name in w_names:
        url = f"{BASE_URL}/load_account/{WALLET}/{w_name}"
        share_rate = get_data(url).get("shareRateHistory", [])
        avg_share_rate = calculate_avg_share_rate(share_rate)
        workers_shares.append({
            "id": w_name,
            **avg_share_rate
        })
    return workers_shares



def calculate_avg_share_rate(share_rate: list) -> dict:
    """Calculate average share rate for different time windows."""
    if share_rate:
        return {
            "h1": int(share_rate[0]["sum"]),
            "h6": sum(int(s["sum"]) for s in share_rate[0:6]) / 6,
            "h12": sum(int(s["sum"]) for s in share_rate[0:12]) / 12,
            "h24": sum(int(s["sum"]) for s in share_rate[0:24]) / 24,
            "w1": sum(int(s["sum"]) for s in share_rate) / len(share_rate)
        }

    return {"h1": 0, "h6": 0, "h12": 0, "h24": 0, "w1": 0}

if __name__ == "__main__":
    data = get_user_data()
    print(get_workers_shares(data))