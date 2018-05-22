# Extending the models

The `uk_geo_utils.models.Address`, `uk_geo_utils.models.Onsud` and `uk_geo_utils.models.Onspd` models each inherit from an abstract base class (`uk_geo_utils.models.AbstractAddress`, `uk_geo_utils.models.AbstractOnsud` and `uk_geo_utils.models.AbstractOnspd`, respectively)

This allows you to use model inheritance to extend these models in your project (for example, if you need to add additional fields). This offers better performance then using one-to-one relationships on large tables like this that contain millions of rows.

If you extend the base tables, declare keys to your project settings file with your extended model names:

```python
ADDRESS_MODEL = 'myapp.MyModel'
ONSUD_MODEL = 'myapp.MyModel'
ONSPD_MODEL = 'myapp.MyModel'
```

This will allow the `uk_geo_utils` management commands, helpers, etc to operate on your extended tables.
