"""
Analyzer Factory
================

Module: `analyzers/analyzer_factory.py`
Layer: `analyzers`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from typing import Any


class AnalyzerFactory:
    """Factory responsible for building analyzer instances."""

    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, key: str, implementation: type) -> None:
        """Register a new implementation under ``key``."""
        cls._registry[key] = implementation

    @classmethod
    def create(cls, key: str, *args: Any, **kwargs: Any) -> Any:
        """Instantiate the implementation registered under ``key``."""
        if key not in cls._registry:
            raise ValueError(f"Unknown analyzer type: {key}")
        return cls._registry[key](*args, **kwargs)

    @classmethod
    def available(cls) -> list[str]:
        """Return the list of registered implementation keys."""
        return sorted(cls._registry.keys())
