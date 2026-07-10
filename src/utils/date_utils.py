"""
Manufacturing Analytics Platform

Date helper utilities.
"""

from __future__ import annotations

from datetime import datetime


class DateUtils:
    """
    Common date utilities used throughout
    the analytics platform.
    """

    @staticmethod
    def month_key(dt: datetime) -> str:
        """Return YYYY-MM."""
        return dt.strftime("%Y-%m")

    @staticmethod
    def year_key(dt: datetime) -> str:
        """Return YYYY."""
        return dt.strftime("%Y")

    @staticmethod
    def day_key(dt: datetime) -> str:
        """Return YYYY-MM-DD."""
        return dt.strftime("%Y-%m-%d")

    @staticmethod
    def quarter_key(dt: datetime) -> str:
        """Return YYYY-Qn."""
        quarter = (dt.month - 1) // 3 + 1
        return f"{dt.year}-Q{quarter}"
