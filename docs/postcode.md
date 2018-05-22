# Postcode

An abstraction over a UK postcode.

## Formatting

```python
>>> from uk_geo_utils.helpers import Postcode
>>> p = Postcode('sw1a1aa')
>>> p.with_space
'SW1A 1AA'
>>> p.without_space
'SW1A1AA'
```

## Comparison

```python
>>> from uk_geo_utils.helpers import Postcode
>>> Postcode('SW1A 1AA') == Postcode('sw 1a1  Aa')
True
```

## Validation

```python
>>> from uk_geo_utils.helpers import Postcode
>>> p = Postcode('foo')
>>> p = Postcode('foo', validate=True)
ValueError: Postcode must have at least 5 characters
```
