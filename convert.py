import codecs
import markdown
import jinja2
import json
import os


def test_path_and_make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_config():
    with open("config.json", "r") as json_data_file:
        config = json.load(json_data_file)
    return config


def convert_markdown_to_htnl(markdown_path, article_title, template):
    input_file = codecs.open('./articles/' + markdown_path,
                             mode="r",
                             encoding="utf-8")
    markdown_text = input_file.read()
    html = markdown.markdown(markdown_text)
    result_html = jinja2.Template(template).render(content=html,
                                                   title=article_title)
    path_to_save = './html/' + os.path.dirname(markdown_path) + '/'
    test_path_and_make_dir(path_to_save)
    new_filename = os.path.basename(markdown_path).split('.')[0] + '.html'
    with codecs.open(path_to_save + new_filename,
                     "w", encoding="utf-8",
                     errors="xmlcharrefreplace") as output_file:
        output_file.write(result_html)


if __name__ == '__main__':
    config = get_config()
    articles = config['articles']
    test_path_and_make_dir('./html')
    with open('template.html', 'r') as template_file:
        template = template_file.read()
    for article in articles:
        convert_markdown_to_htnl(article['source'], article['title'], template)
