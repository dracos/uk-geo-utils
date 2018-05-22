# Importing Data

`django-uk-geo-utils` is most useful for users of AddressBase. Unfortunately AddressBase is proprietary data so it isn't accessible to everyone. If you have a licence for AddressBase or access via the [PSMA](https://www.ordnancesurvey.co.uk/business-and-government/public-sector/mapping-agreements/public-sector-mapping-agreement.html), import AddressBase Standard, ONSUD and ONSPD. If you don't have access to AddressBase, skip straight to ONSPD. You don't need ONSUD.

## AddressBase Standard

Ordnance Survey AddressBase contains UPRNs (Unique Property Reference Number), addresses, and grid references for UK properties. Order a copy of AddressBase Standard and download from the Ordnance Survey FTP. The import is done in 2 stages:

First we need to do some pre-processing on the data:

`python manage.py clean_addressbase /path/to/data`

Then the processed files can be imported:

`python manage.py import_cleaned_addresses /path/to/data`

## ONSUD

ONS UPRN Directory is the companion dataset to AddressBase and handles mapping UPRNs to a variety of administrative, electoral, and statistical geographies. Grab the latest release from the [Office for National Statistics](https://ons.maps.arcgis.com/home/search.html?t=content&q=tags%3AONS%20UPRN%20Directory&start=1&sortOrder=desc&sortField=modified), extract and import it:

`python manage.py import_onsud /path/to/data`

## ONSPD

ONS Postcode Directory maps postcodes to grid references and a variety of administrative, electoral, and statistical geographies. Grab the latest release from the [Office for National Statistics](https://ons.maps.arcgis.com/home/search.html?t=content&q=tags%3AONS%20Postcode%20Directory&start=1&sortOrder=desc&sortField=modified), extract and import it:

`python manage.py import_onspd /path/to/data`
