# Importing flask
import flask

#  Creating the Blueprint that will represent the application
home_page_app = flask.Blueprint(
    # Setting the name for the application
    name = "home_app",
    # Setting the import name to the name of the current file
    import_name = "app",
    # Setting the template folder path
    template_folder = "home_page/templates",
    # Setting the static folder path
    static_folder = "static"
)