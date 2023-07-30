# Recipe App

Recipe app is an api to create, add, edit or delete recipes.

## build and run project

Docker is required to run a project.

```bash
make build
```
run a project.
```bash
make run
```

## Usage
populate database with fixture data

```python
make populate_database
```
create a super user
```python
make createsuperuser
```
after running a project you should be able to perform CRUD operations on the following endpoint:

**localhost:8000/api/recipe**
