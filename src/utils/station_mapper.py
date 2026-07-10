"""
Manufacturing Analytics Platform

Station normalization utilities.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StationInfo:
    """Normalized station information."""

    original: str
    normalized: str


class StationMapper:
    """
    Standardizes manufacturing station names.
    """

    def normalize(self, station: str) -> str:
        """
        Normalize station name.
        """
        return station.strip().upper()

    def map(self, station: str) -> StationInfo:
        """
        Create normalized station metadata.
        """
        return StationInfo(
            original=station,
            normalized=self.normalize(station),
        )
