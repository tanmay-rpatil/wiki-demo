# Wiki - A Simple Markdown Compatible Wiki
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/> <img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/> <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>

- Done as part of CS50's Web Development with Python and JS
- Provides ability to read, edit, update articles in Markdown format
- Provides full access to all functionality via a REST API developed using django-rest-framework

## API overview

``` json
	'Api overview':'/api/'
	'List':'/api/entry-list/',
	'Detail View':'/api/entry-detail/<int:pk>/',
	'Create':'/api/entry-create/',
	'Update':'/api/entry-update/<int:pk>/',
	'Delete':'/api/entry-delete/<int:pk>/',
```

1. API overview:  ``` /api/ ``` : Returns the above the list of API formats
2. List: ``` /api/entry-list/ ``` : List all entry key:title pair
3. Detail View: ``` /api/entry-detail/<int:pk>/ ``` : Get all the data of one entry, by primary key
4. Create: ``` /api/entry-create/ ``` : Send POST request with the fields ```title``` and ```body``` to create an article
5. Update: ``` /api/entry-update/<int:pk>/ ``` : Send PUT request with the fields ```title``` and ```body``` to update an article
6. Delete: ``` /api/entry-delete/<int:pk>/ ``` : Send DELETE request here to delete an article

## Development

1. Get python version from runtime.txt
2. Install requirements from requirements.txt ( preferably setup a [virtual environment!](https://docs.python.org/3/library/venv.html))
3. Set environment variables ``` SECRET_KEY ``` and ``` DEBUG ``` to get your website up and running on a 'nix OS ( [guidefor other OS](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) )

    ``` bash 
    $ export SECRET_KEY=yourKeyHere
    $ export DEBUG=True #for development, for production set False
    
    ```
	Note - alternatively, add it to your shell's config files such as ``` ~/.bashrc ``` or ``` ~/.zshrc ```

### Development - Directory Organisation

1. wiki-demo/api djngo app for implementing the REST API
2. wiki-demo/encyclopedia django for Articles
3. Procfile for Heroku configurations
