import markdown

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
