import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from datetime import datetime

# ── Theme ────────────────────────────────────────────────────────────────────
BG     = "#0f1117"
CARD   = "#1a1d27"
GREEN  = "#1fc98e"
GREENS = ["#1fc98e", "#17a877", "#0f8760", "#0a6649", "#064433", "#03291e"]
TEXT   = "#e8eaf0"
MUTED  = "#7b7f93"

plt.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor":   CARD,
    "axes.edgecolor":   "#2a2d3a",
    "axes.labelcolor":  TEXT,
    "xtick.color":      MUTED,
    "ytick.color":      MUTED,
    "text.color":       TEXT,
    "font.family":      "monospace",
    "grid.color":       "#2a2d3a",
    "grid.linestyle":   "--",
    "grid.alpha":       0.6,
})

PERIODS = ["hashrate", "h1", "h3",  "h6",  "h12", "h24"]
LABELS  = ["Now",      "1h", "3h",  "6h",  "12h", "24h"]
AVG_P   = ["h1", "h3", "h6", "h12", "h24"]
AVG_L   = ["1h", "3h", "6h", "12h", "24h"]


def _fmt(v: float) -> str:
    return f"{v:,.0f}"


def plot_current_hashrate_bar(ax, workers: list):
    """Horizontal bar — current hashrate per worker."""
    sorted_workers = sorted(workers, key=lambda w: float(w["hashrate"]), reverse=True)
    names     = [w["id"] for w in sorted_workers]
    curr_vals = [float(w["hashrate"]) for w in sorted_workers]
    y_pos     = np.arange(len(names))
    bars      = ax.barh(y_pos, curr_vals, color=GREEN,
                        zorder=3, linewidth=0, height=0.55)

    for bar, v in zip(bars, curr_vals):
        ax.text(v + max(curr_vals) * 0.015,
                bar.get_y() + bar.get_height() / 2,
                f"{_fmt(v)} H/s",
                va="center", fontsize=7, color=TEXT)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel("Hashrate (H/s)", fontsize=10)
    ax.set_title("Current hashrate per worker",
                 fontsize=11, color=TEXT, pad=8)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(curr_vals) * 1.2)


def plot_24h_avg_hashrate_bar(ax, workers: list):
    """Horizontal bar — 24h average hashrate per worker."""
    sorted_workers = sorted(workers, key=lambda w: float(w["h24"]), reverse=True)
    names  = [w["id"] for w in sorted_workers]
    vals   = [float(w["h24"]) for w in sorted_workers]
    y      = np.arange(len(names))
    height = 0.55

    bars = ax.barh(y, vals, height, color=GREEN, zorder=3, linewidth=0)

    for bar, v in zip(bars, vals):
        cy = bar.get_y() + bar.get_height() / 2
        # value label at the end of the bar
        ax.text(v + max(vals) * 0.012, cy,
                f"{_fmt(v)} H/s",
                ha="left", va="center", fontsize=7, color=TEXT)

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel("Hashrate (H/s)", fontsize=10)
    ax.set_title("24h Average hashrate per worker",
                 fontsize=11, color=TEXT, pad=8)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(vals) * 1.2)


def plot_week_avg_sharerate_bar(ax, workers: list):
    """Horizontal bar — 1 week average share rate per worker."""
    sorted_workers = sorted(workers, key=lambda w: float(w["w1"]), reverse=True)
    names  = [w["id"] for w in sorted_workers]
    vals   = [float(w["w1"]) for w in sorted_workers]
    y      = np.arange(len(names))
    height = 0.55

    bars = ax.barh(y, vals, height, color=GREEN, zorder=3, linewidth=0)

    for bar, v in zip(bars, vals):
        cy = bar.get_y() + bar.get_height() / 2
        # value label at the end of the bar
        ax.text(v + max(vals) * 0.012, cy,
                f"{int(v)}",
                ha="left", va="center", fontsize=7, color=TEXT)

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel("Share Rate per Hour", fontsize=10)
    ax.set_title("1 week Average share rate per worker",
                 fontsize=11, color=TEXT, pad=8)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(vals) * 1.2)


def plot_24h_avg_sharerate_bar(ax, workers: list):
    """Horizontal bar — 24h average share rate per worker."""
    sorted_workers = sorted(workers, key=lambda w: float(w["h24"]), reverse=True)
    names  = [w["id"] for w in sorted_workers]
    vals   = [float(w["h24"]) for w in sorted_workers]
    y      = np.arange(len(names))
    height = 0.55

    bars = ax.barh(y, vals, height, color=GREEN, zorder=3, linewidth=0)

    for bar, v in zip(bars, vals):
        cy = bar.get_y() + bar.get_height() / 2
        # value label at the end of the bar
        ax.text(v + max(vals) * 0.012, cy,
                f"{int(v)}",
                ha="left", va="center", fontsize=7, color=TEXT)

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_xlabel("Share Rate per Hour", fontsize=10)
    ax.set_title("24h Average share rate per worker",
                 fontsize=11, color=TEXT, pad=8)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(0, max(vals) * 1.2)


def plot_avg_line(ax, avg_hashrate: dict):
    """Line chart — account-level average hashrate over time."""
    vals = [float(avg_hashrate[p]) for p in AVG_P]

    ax.plot(AVG_L, vals, color=GREEN, linewidth=2.5,
            marker="o", markersize=7, zorder=3)
    ax.fill_between(AVG_L, vals, min(vals) * 0.97,
                    color=GREEN, alpha=0.12, zorder=2)

    for label, v in zip(AVG_L, vals):
        ax.text(label, v + max(vals) * 0.012,
                _fmt(v), ha="center", fontsize=8.5, color=MUTED)

    ax.set_ylabel("H/s", fontsize=10)
    ax.set_title("Account avg hashrate over time",
                 fontsize=11, color=TEXT, pad=8)
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_ylim(min(vals) * 0.97, max(vals) * 1.05)


def build_dashboard(data: dict, output_path: str = "nanopool_dashboard.png"):
    """Compose the full 3-panel dashboard and save to disk."""
    avg     = data["avgHashrate"]
    balance = float(data["balance"])
    hashrate = float(data["hashrate"])
    workers_shares = data["workersShares"]
    workers_hashrate = data.get("workers", [])

    fig = plt.figure(figsize=(16, 10), facecolor=BG)
    today = datetime.today().strftime("%d/%m/%Y")
    fig.suptitle(f"Nanopool XMR — Mining Dashboard — {today}",
                 fontsize=16, fontweight="bold", color=TEXT, y=0.97)

    summary = (
        f"Balance: {balance:.5f} XMR  │  "
        f"Current hashrate: {hashrate:,.0f} H/s  │  "
        f"Workers: {len(workers_hashrate)}"
    )
    fig.text(0.5, 0.93, summary, ha="center", fontsize=10, color=MUTED)

    gs = gridspec.GridSpec(2, 2, figure=fig,
                           hspace=0.42, wspace=0.32,
                           left=0.07, right=0.97,
                           top=0.89,  bottom=0.08)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    plot_current_hashrate_bar(ax1, workers_hashrate)
    plot_24h_avg_hashrate_bar(ax2, workers_hashrate)
    plot_week_avg_sharerate_bar(ax3, workers_shares)
    plot_24h_avg_sharerate_bar(ax4, workers_shares)
    #plot_avg_line(ax4, avg)

    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor=BG)
    print(f"Dashboard saved → {output_path}")
    plt.show()
