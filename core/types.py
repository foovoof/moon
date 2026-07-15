"""
Types
=====

Module: `core/types.py`
Layer: `core`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

class Types:
    """Placeholder implementation for types.

    TODO: implement according to the relevant spec under
    `standards/`, `contracts/` and `governance/policies/`.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._args = args
        self._kwargs = kwargs

    def run(self, *args, **kwargs):
        """TODO: implement types."""
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented yet.")
