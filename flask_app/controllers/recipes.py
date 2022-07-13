# Import app
from flask_app import app
# Import modules from flask
from flask_app import Flask, render_template, request, redirect, session, url_for, flash, bcrypt

# Import models class
from flask_app.models import user, recipe
# CRUD CREATE ROUTES
@app.route('/recipe/create', methods=['POST'])
def create_new_recipe():
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Call staticmethod to validate form
    if not recipe.Recipe.validate_form(request.form):
        # Redirect back to new recipe page
        return redirect('/recipe/new')
    # Create data dict based on request form
    # the keys must match exactly to the var in the query set
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': int(request.form['under_30']),
        'date_made': request.form['date_made'],
        'user_id': session['id']
    }
    recipe.Recipe.create_recipe(data)
    return redirect('/dashboard')

# CRUD READ ROUTES
@app.route('/recipe/new')
def recipe_new():
    """Display the form to create a new recipe"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on user in session
    # the keys must match exactly to the var in the query set
    data = { 'id': session['id'] }
    # Call classmethod in models
    return render_template('recipe_new.html', user=user.User.get_user_by_id(data))

@app.route('/recipe/show/<int:recipe_id>')
def recipe_show_one(recipe_id):
    """Show the recipe on a page"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on recipe_id
    # The keys must match exactly to the var in the query set
    data = { 'id': recipe_id }
    # Create additonal data dict for user
    data_user = { 'id': session['id'] }
    # Call classmethods and render_template edit template with data filled in
    return render_template('recipe_show.html', one_recipe=recipe.Recipe.get_one_recipe(data), user=user.User.get_user_by_id(data_user)) 


# CRUD UPDATE ROUTES
@app.route('/recipe/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    """Edit the recipe"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on recipe_id
    # The keys must match exactly to the var in the query set
    data = { 'id': recipe_id }
    # Create additonal data dict for user
    data_user = { 'id': session['id'] }
    # Call classmethods and render_template edit template with data filled in
    return render_template('recipe_edit.html', one_recipe=recipe.Recipe.get_one_recipe(data), user=user.User.get_user_by_id(data_user)) 

@app.route('/recipe/update', methods=['POST'])
def update_recipe():
    """Update recipe after editing"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Call staticmethod to validate form
    if not recipe.Recipe.validate_form(request.form):
        # Redirect back to new recipe page
        id = int(request.form['id'])
        return redirect(f'/recipe/edit/{id}')
    # Create data dict based on recipe_id
    # The keys must match exactly to the var in the query set
    data = {
        'id': int(request.form['id']),
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30': int(request.form['under_30']),
        'date_made': request.form['date_made']
    }
    # Call classmethod in models
    recipe.Recipe.update_recipe(data)
    # Redirect to dashboard after update
    return redirect('/dashboard')

# CRUD DELETE ROUTES
@app.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    """Delete recipe if session user created"""
    # Check that user is logged in
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    # Create data dict based on recipe_id
    # The keys must match exactly to the var in the query set
    data = { 'id': recipe_id }
    # Call classmethod in models
    recipe.Recipe.delete_recipe(data)
    # Redirect back to dashboard after deletion
    return redirect('/dashboard')

