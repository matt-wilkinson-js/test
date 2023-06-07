import os
import yaml
import markdown
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
# set to current directory
path= '/Users/matt.wilkinson/Desktop/'
os.chdir(path)
# creates repo (will be removed for final script)
os.mkdir("test_repo")
# change directory path
path2= '/Users/matt.wilkinson/Desktop/test_repo'
os.chdir(path2)
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
with open('mktest.yml','w') as dump_file:
    yaml.dump(contents, dump_file)
# add mapping spec template
mdtest = markdown.markdown('''
# Add object name

** Last Edited: **

## Description

Add description of the object

## Jira Tickets
| Jira Ticket | Description | Function     |
|-------------|-------------|--------------|
|             |             | Architecture |
## Selection Criteria

Add selection criteria for the object

## Target to Source

{{ read_excel('add_name_here.xlsx', engine='openpyxl', sheet_name="Add_sheet_name_here") }}

## Mapping Steps

1. Add sequential steps here

## Diagram

```mermaid
flowchart LR
a-->b
```

## Tests & Checks

Add tests & checks here
[x]
[ ]
    ''')

with open('mdtest.md','w') as f:
    f.write(mdtest)
os.mkdir("docs")
os.mkdir(".github")
path3= '/Users/matt.wilkinson/Desktop/test_repo/docs'
os.chdir(path3)
index = markdown.markdown('about')
with open('index.md','w') as f:
    f.write(index)
os.makedirs("Staging")
os.makedirs("Raw Data Vault")
os.makedirs("Business Data Vault")
os.makedirs("Presentation Layer")