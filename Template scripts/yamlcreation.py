import yaml

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
    
github = {'name': 'ci', True: {'push': {'branches': ['master', 'main']}}, 'permissions': {'contents': 'write'}, 'jobs': {'deploy': {'runs-on': 'ubuntu-latest', 'steps': [{'uses': 'actions/checkout@v3'}, {'uses': 'actions/setup-python@v4', 'with': {'python-version': 3.8}}, {'uses': 'actions/cache@v2', 'with': {'key': '${{ github.ref }}', 'path': '.cache'}}, {'run': 'pip install mkdocs-material'}, {'run': 'pip install mkdocs-markdown-filter'}, {'run': 'pip install mkdocs-table_reader_plugin'}, {'run': 'pip install openpyxl'}, {'run': 'mkdocs gh-deploy --force'}]}}}

with open('citest.yml','w') as dump_file:
    yaml.dump(github, dump_file)