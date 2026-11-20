"""Validador estricto de un subconjunto de JSON Schema (el que usan las herramientas de Ucoach)."""

from __future__ import annotations

TYPES = {"string": str, "integer": int, "number": (int, float), "boolean": bool, "object": dict, "array": list}


class ValidationError(ValueError):
    pass


def validate(value, schema: dict, path: str = "") -> None:
    t = schema.get("type")
    if t:
        allowed = t if isinstance(t, list) else [t]
        ok = False
        for name in allowed:
            if name == "null" and value is None:
                ok = True
            elif name in TYPES and isinstance(value, TYPES[name]) and not (
                    name in ("integer", "number") and isinstance(value, bool)):
                ok = True
        if not ok:
            raise ValidationError(f"{path or 'argumentos'}: se esperaba {t}")
    if value is None:
        return
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path}: valor no permitido; usa uno de {schema['enum']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            raise ValidationError(f"{path}: mínimo {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            raise ValidationError(f"{path}: máximo {schema['maximum']}")
    if isinstance(value, str):
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            raise ValidationError(f"{path}: máximo {schema['maxLength']} caracteres")
        if "pattern" in schema:
            import re
            if not re.fullmatch(schema["pattern"], value):
                raise ValidationError(f"{path}: formato no válido")
    if isinstance(value, list):
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ValidationError(f"{path}: máximo {schema['maxItems']} elementos")
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise ValidationError(f"{path}: mínimo {schema['minItems']} elementos")
        for i, item in enumerate(value):
            validate(item, schema.get("items", {}), f"{path}[{i}]")
    if isinstance(value, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in value:
                raise ValidationError(f"{path or 'argumentos'}: falta {req!r}")
        if schema.get("additionalProperties") is False:
            extra = set(value) - set(props)
            if extra:
                raise ValidationError(f"{path or 'argumentos'}: campos no admitidos {sorted(extra)}")
        for k, v in value.items():
            if k in props:
                validate(v, props[k], f"{path}.{k}" if path else k)
