"""
Base Collector
==============

Module: `collectors/base_collector.py`
Layer: `collectors`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseCollector(ABC):
    """Abstract base class for base collector implementations."""

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the base collector behaviour."""
        raise NotImplementedError
