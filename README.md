# HIGH SCHOOL OF SOMEWHERE CITY
This study project has implemented for practice and master django, django orm, raw sql.
The application helps keep records of high school staff and students.

This release have:
- Sqlite3 database with related tables and data containing information of students, classes, teachers, staff and parents.
  * All matches of names and addresses are random. Data was taken from MySQL open database named sakila.  
- Default django administration
- Default Django templates showing necessary at current information
- Bootstrap styles

Next releases will have:
- New tables
- Authentication and permissions. 
- API
- Django's templates will be changed to really front-end using vue.js or another js framework. 
- Test cases

## The project structure
source: source root directory
  - apps: contains apps
    - main: main app
  config: the project's configuration package
    - env.template contains project's credentials examples

## DB SCHEMA

![schema](stuff/school_main_schema_003.jpg)
## Initialization
```git clone <repository_url>```

```poetry install && poetry shell```

```make runserver```
