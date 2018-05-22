# Installation

## Requirements

* Python 3
* Django >= 1.11
* PostgreSQL, PostGIS

## Installation

* `pip install git+git://github.com/DemocracyClub/uk-geo-utils.git`
* Add to `INSTALLED_APPS` in django settings:

```python
INSTALLED_APPS = [
    ...
    'uk_geo_utils',
]
```

* Apply migrations: `python manage.py migrate`
