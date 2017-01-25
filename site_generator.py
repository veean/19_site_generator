import os
import json
import jinja2
import markdown


def get_config_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as config:
            return json.load(config)


def mutate_md_to_html(md_filepath):
    if os.path.exists(md_filepath):
        extentions = ['codehilite', 'fenced_code']
        with open(md_filepath, 'r', encoding='utf-8') as md:
            return markdown.markdown(md.read(), extentions=extentions)



if __name__ == '__main__':
    pass


