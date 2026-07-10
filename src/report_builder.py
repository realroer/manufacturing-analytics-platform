"""
Manufacturing Analytics Platform

Report generation utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class ReportSection:
    """
    Represents one section of an analytics report.
    """

    title: str
    content: Dict


class ReportBuilder:
    """
    Builds structured manufacturing reports
    from KPI calculation results.
    """

    def executive_summary(
        self,
        metrics: Dict,
    ) -> ReportSection:
        """
        Build executive KPI summary.
        """

        return ReportSection(
            title="Executive Summary",
            content=metrics,
        )

    def product_summary(
        self,
        metrics: Dict,
    ) -> ReportSection:
        """
        Build product-level report.
        """

        return ReportSection(
            title="Product Performance",
            content=metrics,
        )

    def station_summary(
        self,
        metrics: Dict,
    ) -> ReportSection:
        """
        Build station-level report.
        """

        return ReportSection(
            title="Station Performance",
            content=metrics,
        )

    def trend_summary(
        self,
        metrics: Dict,
    ) -> ReportSection:
        """
        Build trend analysis section.
        """

        return ReportSection(
            title="Trend Analysis",
            content=metrics,
        )

    def build(
        self,
        metrics: Dict,
    ) -> List[ReportSection]:
        """
        Build the complete manufacturing report.
        """

        return [
            self.executive_summary(metrics),
            self.product_summary(metrics),
            self.station_summary(metrics),
            self.trend_summary(metrics),
        ]
