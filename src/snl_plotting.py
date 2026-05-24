"""Plotting helpers shared by the SNL notebooks."""

from __future__ import annotations

import numpy as np
from matplotlib.ticker import FormatStrFormatter


def finite_nonzero_values(data, eps: float = 1e-5):
    """Return finite nonzero values after removing tiny background values."""
    arr = np.asarray(data, dtype=float)
    return arr[np.isfinite(arr) & (np.abs(arr) > eps)]


def format_colorbar_decimal(display, digits: int = 5) -> None:
    """Format nilearn colorbars without scientific notation."""
    try:
        fmt = f"%.{digits}f"
        display._cbar.ax.yaxis.set_major_formatter(FormatStrFormatter(fmt))
        display._cbar.ax.xaxis.set_major_formatter(FormatStrFormatter(fmt))
        display._cbar.ax.yaxis.offsetText.set_visible(False)
        display._cbar.ax.xaxis.offsetText.set_visible(False)
        display._cbar.update_ticks()
    except Exception:
        pass
