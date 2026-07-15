"""
Base Analyzer
=============

Module: `analyzers/base_analyzer.py`
Layer: `analyzers`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseAnalyzer(ABC):
    """Abstract base class for base analyzer implementations."""

    @abstractmethod
    def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the base analyzer behaviour."""
        raise NotImplementedError
