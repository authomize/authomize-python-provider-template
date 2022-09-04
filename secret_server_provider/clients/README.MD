## Create OpenAPI client for Secret Server


* Download the OpenAPI swagger.json file - https://integrations.secretservercloud.com/RestApiDocs.ashx
* Save here an call it swagger.json
* Install OpenAPI Generator - https://openapi-generator.tech/docs/installation
* Run:
```
openapi-generator-cli generate -i swagger.json -g python -o secret_server_openapiclient -p packageVersion=3.0.0 -p infoEmail=info@authomize.com --skip-validate-spec --package-name secret_server_openapiclient --template-dir templates/python
```
* Reinstall dependency: pip uninstall secret-server-openapiclient; pip install -e .[secretserver]
