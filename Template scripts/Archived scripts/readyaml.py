import yaml
with open('/Users/matt.wilkinson/Documents/GitHub/test/.github/workflows/ci.yml','r') as read_file:
    contents = yaml.safe_load(read_file)
    print(contents)
    print(type(contents))