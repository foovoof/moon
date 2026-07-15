"""
Collector Factory
=================

Module: `collectors/collector_factory.py`
Layer: `collectors`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from typing import Any


class CollectorFactory:
    """Factory responsible for building collector instances."""

    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, key: str, implementation: type) -> None:
        """Register a new implementation under ``key``."""
        cls._registry[key] = implementation

    @classmethod
    def create(cls, key: str, *args: Any, **kwargs: Any) -> Any:
        """Instantiate the implementation registered under ``key``."""
        if key not in cls._registry:
            raise ValueError(f"Unknown collector type: {key}")
        return cls._registry[key](*args, **kwargs)

    @classmethod
    def available(cls) -> list[str]:
        """Return the list of registered implementation keys."""
        return sorted(cls._registry.keys())
