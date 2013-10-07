import os
import re
from flask import Flask, url_for, render_template, request
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')
import data


app = Flask(__name__, template_folder=tmpl_dir)
app.debug = True

appdata = data.load("data.json")

@app.route("/")
def main_page():
    """
    Returns main page of the website, address "/"
    """
    return render_template("main.html", data=appdata)
    
@app.route("/list")
def project_list():
    """
    Returns a list of projects on the website, address "/list"
    """
    project_count = data.get_project_count(appdata)
    return render_template("list.html", data=appdata, count=project_count)
    
@app.route("/techniques")
def project_tech():
    """
    Returns a list of techniques we have used on the website, address "/techniques".
    Each technique also lists projects where the technique was used.
    """
    techniques = data.get_technique_stats(appdata)
    return render_template("tech.html", techs=techniques)
    
@app.route("/project/<int:id>")
def project_single(id):
    """
    Returns a page with description for a single project, adress "/project/<project_id>".
    """
    single_project = data.get_project(appdata, id)
    return render_template("single.html", data=single_project)
    
@app.route("/search", methods=['POST'])
def search_results():
    """
    Sanitizes the search string, counts objects in search results and returns search results page. 
    """
    sanitized_search = re.sub('[^a-zA-Z0-9\n\.]', ' ', request.form['key'])
    search_function = data.search(appdata, search=sanitized_search)
    results_count = len(search_function)
    return render_template("search.html", data=search_function, count=results_count, term=sanitized_search)


@app.errorhandler(404)
def page_not_found(error):
    """
    Returns a user friendly message if the requested page was not found on the server.
    """
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
