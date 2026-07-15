"""
Base Normalizer
===============

Module: `normalizers/base_normalizer.py`
Layer: `normalizers`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseNormalizer(ABC):
    """Abstract base class for base normalizer implementations."""

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the base normalizer behaviour."""
        raise NotImplementedError
