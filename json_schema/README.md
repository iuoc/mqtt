
`iuoc_payload.schema` is the definition of the *IUOC* payload message.
These schema can be used for OCs payloads validation.

# Example / test

Two payload examples are provided:

* `iuoc_valid_payload.json.json`: it does follow the IUOC schema spec.
* `iuoc_not_valid_payload.json`: it does NOT follow the IUOC schema spec.

`check-jsonschema` can used to validate or do experiments with schema or payloads

* Installation: `pip install check-jsonschema`
* Usage:

```shell
	$ check-jsonschema  --schemafile iuoc_payload.schema iuoc_not_valid_payload.json
```
