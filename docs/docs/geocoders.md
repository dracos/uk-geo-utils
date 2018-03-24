# Geocoders

`uk_geo_utils.geocoders.AddressBaseGeocoder` and `uk_geo_utils.geocoders.OnspdGeocoder` provide abstractions for obtaining a grid reference or ONS code based on a postcode or UPRN.

## Points

`AddressBaseGeocoder` and `OnspdGeocoder` support a (postcode) `centroid` property. Additionally `AddressBaseGeocoder` supports an additional `get_point(self, uprn)` method.

Examples:

```python
>>> from uk_geo_utils.geocoders import AddressBaseGeocoder
>>> g = AddressBaseGeocoder('SA8 4DA')
>>> g.centroid
<Point object at 0x000000000000>
>>> g.get_point("10010020128")
<Point object at 0x000000000000>
```

```python
>>> from uk_geo_utils.geocoders import OnspdGeocoder
>>> g = OnspdGeocoder('SA8 4DA')
>>> g.centroid
<Point object at 0x000000000000>
```

Geocoder objects may be constructed with a string or a [Postcode object](postcode.md). In either case, whitespace and formatting is ignored:

```python
>>> from uk_geo_utils.geocoders import OnspdGeocoder
>>> from uk_geo_utils.helpers import Postcode
>>> g1 = OnspdGeocoder(Postcode('SA8 4DA'))
>>> g2 = OnspdGeocoder('sa 8 4  DA')
>>> g1.centroid == g2.centroid
True
```

## UPRNs

`AddressBaseGeocoder` supports a `get_uprns()` method.

Example:

```python
>>> from uk_geo_utils.geocoders import AddressBaseGeocoder
>>> g = AddressBaseGeocoder('SA8 4DA')
>>> g.get_uprns()
['10010020128', '10010020129', '100100624432', '100100624433', '100100624434', '100100624435', '100100624436', '100100624437', '100100624438', '100100624439']
```

## ONS Codes

`AddressBaseGeocoder` and `OnspdGeocoder` support a `get_code()` method which can be used to access [fields or aliases](models.md) on the ONSPD and ONSUD models based on a postcode or UPRN query.

* `AddressBaseGeocoder.get_code(self, code_type, uprn=None, strict=False)`
* `OnspdGeocoder.get_code(self, code_type)`

Examples:

```python
>>> from uk_geo_utils.geocoders import AddressBaseGeocoder
>>> g = AddressBaseGeocoder('SA8 4DA')
>>> g.get_code('ctry')
'W92000004'
>>> g.get_code('ctry', "10010020128")
'W92000004'
>>> g.get_code('ctry', "100100624439")
'W92000004'
```

```python
>>> from uk_geo_utils.geocoders import AddressBaseGeocoder
>>> g = AddressBaseGeocoder('SA8 4DA')
>>> g.get_code('lad')
uk_geo_utils.geocoders.MultipleCodesException: Postcode SA84DA covers UPRNs in more than one 'lad' area
>>> g.get_code('lad', "10010020128")
'W06000011'
>>> g.get_code('lad', "100100624439")
'W06000012'
>>> g.get_code('lad', "spoons")
addressbase.models.DoesNotExist
```

```python
>>> from uk_geo_utils.geocoders import OnspdGeocoder
>>> g = OnspdGeocoder('SA8 4DA')
>>> g.get_code('ctry')
'W92000004'
>>> g.get_code('lad')
'W06000012'
```
