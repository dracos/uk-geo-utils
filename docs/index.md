# Django UK Geo Utils

A django app for geocoding with postcodes or UPRNs

`django-uk-geo-utils` provides a set models, management commands and helpers for working with

* [OS AddressBase](https://www.ordnancesurvey.co.uk/business-and-government/products/addressbase.html) and [ONS UPRN Directory](https://ons.maps.arcgis.com/home/search.html?t=content&q=tags%3AONS%20UPRN%20Directory&start=1&sortOrder=desc&sortField=modified)
* [ONS Postcode Directory](https://ons.maps.arcgis.com/home/search.html?t=content&q=tags%3AONS%20Postcode%20Directory&start=1&sortOrder=desc&sortField=modified)

to simplify the proces of mapping postcodes or UPRNs to grid references and a range of administrative, electoral, and statistical geographies in your django/PostGIS project.
