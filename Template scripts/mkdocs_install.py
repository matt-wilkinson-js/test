import sys
import subprocess
# install all python packages for mkdocs
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_markdown_filter'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_material'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_material_extensions'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_table_reader_plugin'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown'])
# import python packages
import os
import yaml
import markdown
# set to current directory
path= os.getcwd()
os.chdir(path)
# add in mkdocs yaml file
contents = {
    'site_name': 'dp-c3fn-packaging', 
    'site_url': 'https://mappingspecexample.com/', 
    'nav': [{'Home': [{'About': 'index.md'}]}, {'Staging': [{'test': 'Staging/test.md'}]}, {'Raw Data Vault': [{'Hubs': [{'Hub Test 1': 'Raw Data Vault/hub.md'}, {'Hub Test 2': 'Raw Data Vault/test.md'}]}, {'Satellites': [{'Sat Test 1': 'Raw Data Vault/test.md'}]}, {'Links': [{'Link Test 1': 'Raw Data Vault/test.md'}]}]}, {'Business Data Vault': [{'Item Specification Component BR': 'Business Data Vault/ITEM_SPECIFICATION_COMPONENT_BR.md'}]}, {'Presentation Layer': [{'Facts': [{'Agg Item Primary Plastics': 'Presentation Layer/AGG_ITEM_PRIMARY_PLASTICS.md'}, {'Fact Item Specification Component': 'Presentation Layer/FACT_ITEM_SPECIFICATION_COMPONENT.md'}]}, {'Dimensions': [{'Dim Test 1': 'Presentation Layer/test.md'}]}]}], 
    'theme': {'name': 'material', 'features': ['navigation.tabs', 'navigation.sections', 'toc.integrate', 'navigation.top', 'navigation.expand', 'navigation.path', 'search.suggest', 'search.highlight', 'content.tabs.link', 'content.code.annotation', 'content.code.copy', 'navigation.tracking'], 'language': 'en', 'palette': [{'scheme': 'default', 'toggle': {'icon': 'material/toggle-switch-off-outline', 'name': 'Switch to dark mode'}, 'primary': 'deep orange', 'accent': 'green'}, {'scheme': 'slate', 'toggle': {'icon': 'material/toggle-switch', 'name': 'Switch to light mode'}, 'primary': 'deep orange', 'accent': 'green'}], 'icon': {'repo': 'fontawesome/brands/github'}, 'font': {'text': 'Mary Ann'}}, 
    'markdown_extensions': [{'pymdownx.highlight': {'anchor_linenums': True}}, 'pymdownx.inlinehilite', 'pymdownx.snippets', 'admonition', {'pymdownx.arithmatex': {'generic': True}}, 'footnotes', 'pymdownx.details', {'pymdownx.superfences': {'custom_fences': [{'name': 'mermaid', 'class': 'mermaid'}]}}, 'pymdownx.mark', 'attr_list', {'pymdownx.emoji': None}, 'def_list', {'pymdownx.tasklist': {'custom_checkbox': True}}, 'tables'], 
    'repo_name': 'dp-c3fn-packaging', 'repo_url': 'https://github.com/sainsburys-tech/dp-c3fn-packaging/tree/PFBP-290', 
    'plugins': ['search', 'markdown-filter', 'table-reader']
    }
print(contents)
print(type(contents)) 
with open('mkdocs.yml','w') as dump_file:
    yaml.dump(contents, dump_file)

# create new directory folders  
if not os.path.exists(".github"): os.mkdir(".github")    
if not os.path.exists("docs"): os.mkdir("docs")
os.chdir('docs')
# Add index file and data vault folders
index = markdown.markdown('about')
with open('index.md','w') as f:
    f.write(index)
if not os.path.exists("Staging"):os.makedirs("Staging")
if not os.path.exists("Raw Data Vault"):os.makedirs("Raw Data Vault")
if not os.path.exists("Business Data Vault"):os.makedirs("Business Data Vault")
if not os.path.exists("Presentation Layer"):os.makedirs("Presentation Layer")
# Change path to github
path
os.chdir(path)
os.chdir('.github')
# Add github actions
github = {'name': 'ci', True: {'push': {'branches': ['master', 'main']}}, 'permissions': {'contents': 'write'}, 'jobs': {'deploy': {'runs-on': 'ubuntu-latest', 'steps': [{'uses': 'actions/checkout@v3'}, {'uses': 'actions/setup-python@v4', 'with': {'python-version': 3.8}}, {'uses': 'actions/cache@v2', 'with': {'key': '${{ github.ref }}', 'path': '.cache'}}, {'run': 'pip install mkdocs-material'}, {'run': 'pip install mkdocs-markdown-filter'}, {'run': 'pip install mkdocs-table_reader_plugin'}, {'run': 'pip install openpyxl'}, {'run': 'mkdocs gh-deploy --force'}]}}}
with open('mkdocsupdate.yml','w') as dump_file:
    yaml.dump(github, dump_file)