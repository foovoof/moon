"""
Base Fetcher
============

Module: `collectors/transport/base_fetcher.py`
Layer: `collectors/transport`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseFetcher(ABC):
    """Abstract base class for base fetcher implementations."""

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the base fetcher behaviour."""
        raise NotImplementedError
