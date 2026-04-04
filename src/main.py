from src.fetcher import get_user_data, get_workers_shares
from src.visualizer import build_dashboard
from datetime import datetime


def main():
    print("Fetching data from Nanopool...")
    data    = get_user_data()
    workers_shares = get_workers_shares(data)
    data["workersShares"] = workers_shares

    print("\nBuilding dashboard...")
    today = datetime.today().strftime("%d-%m-%Y")
    build_dashboard(data, output_path=f"nanopool_dashboard_{today}.png")


if __name__ == "__main__":
    main()
