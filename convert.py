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


def convert_markdown_to_html(markdown_path, article_title, template):
    input_file = codecs.open('./articles/' + markdown_path,
                             mode="r",
                             encoding="utf-8")
    markdown_text = input_file.read()
    html = markdown.markdown(markdown_text)
    result_html = jinja2.Template(template).render(content=html,
                                                   title=article_title)
    return result_html


def form_path_to_save_html(markdown_path):
    path_to_save = os.path.join('./html', os.path.dirname(markdown_path))
    test_path_and_make_dir(path_to_save)
    extension = '.html'
    new_filename = os.path.splitext(os.path.basename(markdown_path))[0] + extension
    final_path = os.path.join(path_to_save, new_filename)
    return final_path


def save_html_file(html_text, path_to_save):
    with codecs.open(path_to_save, "w", encoding="utf-8",
                     errors="xmlcharrefreplace") as output_file:
        output_file.write(html_text)
    return True


if __name__ == '__main__':
    config = get_config()
    articles = config['articles']
    test_path_and_make_dir('./html')
    with open('template.html', 'r') as template_file:
        template = template_file.read()
    for article in articles:
        html_article = convert_markdown_to_html(article['source'],
                                                article['title'],
                                                template)
        path_to_save_html = form_path_to_save_html(article['source'])
        save_html_file(html_article, path_to_save_html)
