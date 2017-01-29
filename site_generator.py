from urllib.parse import quote
import markdown
import argparse
import jinja2
import json
import sys
import os


SITE_ROOT = 'site'
TEMPLATE_ROOT = 'templates'
TEMPLATE_INDEX = 'template_index.html'
TEMPLATE_BASIC = 'template_article.html'
SITE_ARTICLES = 'site/articles'
ARTICLES_DIR = 'articles/'
INDEX_PAGE_NAME = 'index.html'


def get_config_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as config:
            return json.load(config)


def prepare_site_structure():
    if not os.path.exists(SITE_ROOT):
        os.makedirs(SITE_ROOT)

    for article in os.scandir(ARTICLES_DIR):
        article_dir = os.path.join(SITE_ARTICLES, article.name)
        if not os.path.exists(article_dir):
            os.makedirs(article_dir)


def extract_md_to_html(md_filepath):
    if os.path.exists(md_filepath):
        with open(md_filepath, 'r', encoding='utf-8') as md:
            return markdown.markdown(md.read(), output_format='html5', extentions=['codehilite', 'fenced_code'])


def save_generated_html(data, output_filepath, new_borned_html):
    with open(output_filepath, 'w', encoding='utf-8') as html:
        html.write(new_borned_html.render(content=data))


def prepare_jinja_env(templates_destination):
    prepared_jinja = jinja2.Environment(autoescape=True)
    prepared_jinja.loader = jinja2.FileSystemLoader(templates_destination)
    return prepared_jinja


def create_articles_pages(config):
    jinja_with_settings = prepare_jinja_env(TEMPLATE_ROOT)
    template_article = jinja_with_settings.get_template(TEMPLATE_BASIC)
    for article in config['articles']:
        md_to_extract = os.path.join(ARTICLES_DIR, article['source'])
        without_extention, _ = os.path.splitext(article['source'])
        path_to_save_html = os.path.join(SITE_ARTICLES, '{}.html'.format(without_extention))
        article['text'] = extract_md_to_html(md_to_extract)
        save_generated_html(article, path_to_save_html, template_article)


def create_index_page(config):

    jinja_with_settings = prepare_jinja_env(TEMPLATE_ROOT)
    template_file = jinja_with_settings.get_template(TEMPLATE_INDEX)
    path_to_store_index = os.path.join(SITE_ROOT, INDEX_PAGE_NAME)
    for article in config['articles']:
        without_extention, _ = os.path.splitext(article['source'])
        article['source_for_index'] = quote(os.path.join(ARTICLES_DIR, '{}.html'.format(without_extention)))
    save_generated_html(config, path_to_store_index, template_file)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Generates static site from md files')
    argparser.add_argument('config', help='Specify path to config file')
    config_parameter = argparser.parse_args()

    prepare_site_structure()
    try:
        site_structure = get_config_file(config_parameter.config)
        create_index_page(site_structure)
        create_articles_pages(site_structure)
        print('Static site generating successfully completed!')
    except (FileNotFoundError, FileExistsError):
        sys.exit(1)
