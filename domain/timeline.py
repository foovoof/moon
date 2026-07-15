"""
Timeline
========

Module: `domain/timeline.py`
Layer: `domain`

Part of the Moon Intelligence & Investigation Platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Timeline:
    """Domain model representing a timeline.

    This is a scaffold definition. Extend with the fields required
    by the `standards/data_dictionary/` specification for this entity.
    """

    id: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
