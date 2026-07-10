"""
Manufacturing Analytics Platform

Yield KPI calculations.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class YieldMetrics:
    """
    Represents manufacturing yield indicators.
    """

    first_pass_yield: float
    second_test_yield: float
    failure_rate: float


class YieldCalculator:
    """
    Manufacturing yield calculations.

    Public repository implementation.
    """

    def calculate_fpy(
        self,
        passed_first_run: int,
        total_first_run: int,
    ) -> float:
        """
        Calculate First Pass Yield.
        """

        if total_first_run == 0:
            return 0.0

        return passed_first_run / total_first_run * 100

    def calculate_sty(
        self,
        recovered_units: int,
        failed_first_run: int,
    ) -> float:
        """
        Calculate Second Test Yield.
        """

        if failed_first_run == 0:
            return 0.0

        return recovered_units / failed_first_run * 100

    def calculate_failure_rate(
        self,
        failed_units: int,
        total_units: int,
    ) -> float:
        """
        Calculate Failure Rate.
        """

        if total_units == 0:
            return 0.0

        return failed_units / total_units * 100

    def build_metrics(
        self,
        passed_first_run: int,
        total_first_run: int,
        recovered_units: int,
        failed_first_run: int,
    ) -> YieldMetrics:
        """
        Build complete yield metrics.
        """

        fpy = self.calculate_fpy(
            passed_first_run,
            total_first_run,
        )

        sty = self.calculate_sty(
            recovered_units,
            failed_first_run,
        )

        fr = self.calculate_failure_rate(
            failed_first_run,
            total_first_run,
        )

        return YieldMetrics(
            first_pass_yield=fpy,
            second_test_yield=sty,
            failure_rate=fr,
        )
