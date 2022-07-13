# Import mysqlconnection config
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

class Recipe:
    # Use a alias for the database; call in classmethods as cls.db
    # For staticmethod need to call the database name not alias
    db = "recipes_belt_prep"

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # Needed to create this to capture the creator of the recipe
        self.creator = data['creator']

    # CRUD CREATE METHODS
    @classmethod
    def create_recipe(cls,data):
        """Create a recipe"""
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    # CRUD READ METHODS
    @classmethod
    def get_all_recipes(cls):
        """Get all the recipes in db"""
        query = "SELECT users.first_name AS creator, recipes.* FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for r in results:
            all_recipes.append(cls(r))
        return all_recipes

    @classmethod
    def get_one_recipe(cls,data):
        """Get one recipe to display"""
        query = "SELECT users.first_name AS creator, recipes.* FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        return cls(connectToMySQL(cls.db).query_db(query,data)[0])

    # CRUD UPDATE METHODS
    @classmethod
    def update_recipe(cls,data):
        """Update the recipe"""
        query = "UPDATE recipes SET (name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_30)s, date_made=%(date_made)s, recipe_id=%(recipe_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    # CRUD DELETE METHODS
    @classmethod
    def delete_recipe(cls,data):
        """Delete recipe"""
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    # FORM VALIDATION
    @staticmethod
    def validate_new_form(recipe):
        """Validate the new recipe create form"""
        is_valid = True # We set True until False
        if len(recipe['name']) < 2:
            flash("The name must be at least 2 characters.", "danger")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("The description can not be blank.", "danger")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("The description can not be blank.", "danger")
            is_valid = False
        if recipe['date_made'] == '':
            flash("Please enter a date.", "danger")
            is_valid = False
        return is_valid
               


