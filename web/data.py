#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

"""
Module: data
Documentation: http://www.ida.liu.se/~TDP003/portfolio-api/

General requirements:

1. Data is saved as an UTF-8 encoded JSON file.
2. The portfolio should use the fields project_no, project_name, 
   start_date, end_date, course_id, course_name, techniques_used, 
   description, long_description, image, external_link.
3. The data module must only depend on the fields project_no, 
   project_name, and techniques_used existing.
4. Dates in the data should use the ISO 8601 format.
"""

def load(filename):
    """
    Loads JSON formatted project data from a file and returns a list.

    load reads objects from a UTF-8 encoded JSON file, and returns a list of projects.

    On errors, None is returned.

    Parameters:
        filename (string) - The filename containing project data.
    
    Returns: list 
        All the project data from the read file, or None.
    """
    try:
        with open(filename, encoding='utf8') as f:
            return json.load(f)
    except:
        return None

def get_project_count(db):
    """
    Retrieves the number of projects in a project list.

    Parameters:
        db (list) - A list as returned by load.
    Returns: number
        The number of projects in the list.
    """
    return len(db)

def get_project(db, id):
    """ 
    Fetches the project with the specified id from the specified list.

    If the specified project id does not exist, None is returned.

    Parameters:
        db (list) - A list as returned by load.
        id (number) - The ID number of the wanted project.
    Returns: dict
        All project data for the specified project, or None.
    """
    for project in db:
        if project["project_no"] == id:
            return project
    return None

def search(db, sort_by='start_date', sort_order='desc', 
        techniques=None, search=None, search_fields=None):
    """ 
    Fetches and sorts projects matching criteria from the specified list.

    Parameters:
        db (list) - A list as returned by load.
        sort_by (string) - The name of the field to sort by.
        sort_order (string) - The order to sort in. 'asc' for ascending, 'desc' for descending.
        techniques (list) - List of techniques that projects must have to be returned. An empty list means this field is ignored
        search (string) - Free text search string.
        search_fields (list) - The fields to search for search in. If search_fields is empty, no results are returned. If search_fields is None, all fields are searched.
    Returns: list
        A list containing dictionaries for all the projects conforming to the specified search criteria.
    """
    # Techniques: - Add those who have all techniques:
    if techniques is not None and techniques:
        new_db = []
        for project in db:
            add_tech = True
            for tech in techniques:
                if tech not in project["techniques_used"]:
                    add_tech = False
                    break
            if add_tech: new_db.append(project)
        db = new_db

    # Search fields:
    def local_find(search_string, string_to_search_in):
        if not type(string_to_search_in) is str:
            string_to_search_in = str(string_to_search_in)
        if search_string.lower() in string_to_search_in.lower():
            return True
        return False

    if search is not None:
        new_db = []
        if search_fields is not None and not search_fields:
            return []
        else:
            fields_to_search = search_fields if search_fields else db[0].keys()
            for field in fields_to_search:
                for project in db:
                    if local_find(search, project[field]):
                        if project not in new_db:
                            new_db.append(project)
        db = new_db

    # Sort by and sort order:
    if not db:
        return []
    elif sort_by not in db[0].keys():
        return None
    elif sort_order == "asc":
        db.sort(key=lambda x: x[sort_by])
    elif sort_order == "desc":
        db.sort(key=lambda x: x[sort_by], reverse=True)
    else:
        return None

    return db

def get_techniques(db):
    """ 
    Fetches a list of all the techniques from the specified project list.

    Parameters:
        db (list) - A list as returned by load.
    Returns: list
        A alphabetically sorted list containing the names of all techniques in db.
    """
    tech_list = []
    for project in db:
        for tech in project["techniques_used"]:
            tech_list.append(tech)
    return sorted(list(set(tech_list)))

# >>> sorted(list(set(itertools.chain(*[ project["techniques_used"] for project in db ]))))

def get_technique_stats(db):
    """
    Collects and returns statistics for all techniques in the specified project list.

    The key of each entry in the returned dictionary is the technique name, and the value is a list of dictionaries for each of the projects using the technique.

    Each of those dictionaries representing a project has the keys:

    id (int): Project number
    name (string): Name of the project

    Parameters:
    db (list) - A list as returned by load.
    Returns: dict
    """
    tech_list = get_techniques(db)
    tech_stats_dict = { tech:[] for tech in tech_list }
    for project in db:
        for tech in tech_list:
            if tech in project["techniques_used"]:
                tech_stats_dict[tech].append(
                        {"id": project["project_no"]
                        , "name": project["project_name"]
                        })
    for tech in tech_stats_dict:
        tech_stats_dict[tech].sort(key=lambda x: x["name"])
    return tech_stats_dict
