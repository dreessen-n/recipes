# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt

# Import models class
from flask_app.models import user, recipe

# Create the routes

# CRUD CREATE ROUTES
@app.route('/recipes/create', methods=['POST'])
def create_new_recipe():
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/recipes')


# TODO CRUD READ ROUTES

# TODO CRUD UPDATE ROUTES

# TODO CRUD DELETE ROUTES
