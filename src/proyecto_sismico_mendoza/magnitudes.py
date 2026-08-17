"""Reglas iniciales de homogeneización de magnitudes sísmicas."""

from dataclasses import dataclass
from math import isfinite


DIRECT_TYPES = frozenset({"mw", "mww", "mwb", "mwr"})
LOCAL_TYPES = frozenset({"ml", "md", "m"})


@dataclass(frozen=True)
class MagnitudeResult:
    original_value: float
    original_type: str
    mw: float | None
    method: str


def to_mw(value: float, magnitude_type: str | None) -> MagnitudeResult:
    """Convierte una magnitud admitida a Mw sin perder el dato original."""
    numeric_value = float(value)
    if not isfinite(numeric_value):
        raise ValueError("La magnitud debe ser un número finito")

    original_type = "" if magnitude_type is None else str(magnitude_type).strip()
    normalized_type = original_type.casefold()

    if normalized_type in DIRECT_TYPES:
        return MagnitudeResult(numeric_value, original_type, numeric_value, "directa")
    if normalized_type in LOCAL_TYPES:
        mw = 0.97 * numeric_value + 0.1025
        return MagnitudeResult(numeric_value, original_type, mw, "conversion_local_regional")
    if normalized_type == "mb":
        mw = 0.554 * numeric_value + 1.765
        return MagnitudeResult(numeric_value, original_type, mw, "conversion_mb")

    return MagnitudeResult(numeric_value, original_type, None, "sin_conversion")

