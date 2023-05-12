import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_markdown_filter'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_material'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_material_extensions'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mkdocs_table_reader_plugin'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])

