# Installation

## Requirements

* Python 3
* Django >= 1.11
* PostgreSQL, PostGIS

## Installation

* `pip install uk-geo-utils`
* Add to `INSTALLED_APPS` in django settings:

```python
INSTALLED_APPS = [
    ...
    'uk_geo_utils',
]
```

* Apply migrations: `python manage.py migrate`
