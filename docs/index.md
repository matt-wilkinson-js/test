# Home

## About
Data architecture mapping specifications for data product dp-c3fn-packaging

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Installation Instructions

Installation Steps for Setting Up MKDocs within your product repo.

* Clone your Github product repository:
    * Download Github Desktop
    * Click file and clone repository
    * Paste in the repository URL
    * Click clone
* Create a branch
    * Click current branch
    * New branch
    * Name the branch (Jira ticket no.)
    * Create branch
* Create a venv
* Activate venv
* Run python script (this will install):
    * All necessary python packages including MKDocs
    * MKDocs Yaml file with all needed extensions
    * Markdown template
    * Folder structure for MKDocs
    * Github actions for automating your deployment
* Add new md files to relevant folder sections
* Run mkdocs serve in your terminal to view site progress. Everytime you save a file in the repo it will rerun and show any changes to the site live before you deploy.
```
(.venv) matt.wilkinson@HOLBMAC2792 test % mkdocs serve  
INFO     -  Building documentation...  
INFO     -  Cleaning site directory  
INFO     -  Documentation built in 1.27 seconds  
INFO     -  [13:47:41] Watching paths for changes: 'docs', 'mkdocs.yml'  
INFO     -  [13:47:41] Serving on http://127.0.0.1:8000/
```
* When finished run mkdocs build
    * This creates all the requirements for the site to build
* Commit changes to Github
* Create a pull request
* Push to main will trigger Github action
* Site will be created/refreshed

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
