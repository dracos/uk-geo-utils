# Changelog

## :package: [0.7.0](https://pypi.org/project/uk-geo-utils/0.7.0/) - 2019-11-15

* Tested on python 3.7
* Update for Jan 2019 ONSUD format change (ctry_flag column is removed)
* Fix `ResourceWarning`s

## :package: [0.6.0](https://pypi.org/project/uk-geo-utils/0.6.0/) - 2018-09-14

Add optional `--transaction` flag to `import_` commands

## :package: [0.5.0](https://pypi.org/project/uk-geo-utils/0.5.0/) - 2018-06-16

Add support for Django 2.0

## :package: [0.4.0](https://pypi.org/project/uk-geo-utils/0.4.0/) - 2018-06-12

Update for May 2018 ONSPD format changes

## :package: [0.3.0](https://pypi.org/project/uk-geo-utils/0.3.0/) - 2018-05-22

* Ensure we always throw error if no CSV files found to import
* Check for files before clearing old data in import scripts
* Throw `OnsudNotImportedException` and `OnspdNotImportedException`
* Expose `uprns` and `addresses` as properties in `AddressBaseGeocoder`
* Add field aliases to ONSUD model
* Add Documentation
* Distribute via PyPI

## :package: 0.2.0 - 2018-03-05

Update for Feb 2018 ONSUD format changes

## :package: 0.1.0 - 2018-03-05

First Release
