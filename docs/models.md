# Model Fields and Aliases

## Fields

### ONSUD

The [ONSUD model](https://github.com/DemocracyClub/uk-geo-utils/blob/17f7b175461057e6dfe0160acfc4ae7316157515/uk_geo_utils/models.py#L60-L88) provides a django model field for each field in the ONSUD.

See the ONSUD [release notes](https://www.arcgis.com/sharing/rest/content/items/64fbb8bb4ddc4acd8bce9489d87ec4fe/data) for the description of each field.

### ONSPD

The [ONSPD model](https://github.com/DemocracyClub/uk-geo-utils/blob/17f7b175461057e6dfe0160acfc4ae7316157515/uk_geo_utils/models.py#L99-L147) provides a django model field for each field in the ONSPD.

See the ONSPD [release notes](https://www.arcgis.com/sharing/rest/content/items/abff4f6fc0514c53bf02c9b9100d6523/data) for the description of each field.

### Aliases

Where comparable fields exist in the ONSUD and ONSPD with different names, there are some convenience aliases defined on the models. This allows us to reference comparable columns using a consistent name across models. The following field names may be used interchangably and called on either model:

| ONSPD    | ONSUD  |
| ---------|--------|
| oscty    | cty    |
| oslaua   | lad    |
| osward   | ward   |
| oshlthau | hlthau |
| ru11ind  | ruc11  |
