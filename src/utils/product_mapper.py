"""
Manufacturing Analytics Platform

Product normalization utilities.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductInfo:
    """Normalized product information."""

    original: str
    normalized: str


class ProductMapper:
    """
    Maps manufacturing product names into
    standardized portfolio categories.
    """

    def normalize(self, product: str) -> str:
        """
        Normalize a product name.

        Placeholder implementation.
        """
        return product.strip().upper()

    def map(self, product: str) -> ProductInfo:
        """
        Create normalized product metadata.
        """
        return ProductInfo(
            original=product,
            normalized=self.normalize(product),
        )
