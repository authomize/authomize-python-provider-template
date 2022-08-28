## Create OpenAPI client for Secret Server


* Download the OpenAPI swagger.json file - https://integrations.secretservercloud.com/RestApiDocs.ashx
* Save here an call it original_swagger.json
* Update the swagger file:
1. Copy original_swagger.json to updated_swagger.json
2. Open in VIM updated_swagger.json
3. Run: `%s/"type": "integer"/"type": ["integer", "null"]/g`
4. Run: `%s/"type": "string"/"type": ["string", ""]/g`
5. Save the file
* Install OpenAPI Generator - https://openapi-generator.tech/docs/installation
* Run:
```
openapi-generator-cli generate -i updated_swagger.json -g python -o secret_server_openapiclient -p packageVersion=3.0.0 -p infoEmail=info@authomize.com --skip-validate-spec --package-name secret_server_openapiclient
```
* Reinstall dependency: pip uninstall secret-server-openapiclient; pip install -e .[secretserver]
