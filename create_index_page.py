import jinja2
import os
from convert import get_config, save_html_file


def form_article_path(markdown_path):
    path_to_save = os.path.dirname(markdown_path)
    extension = '.html'
    new_filename = os.path.splitext(os.path.basename(markdown_path))[0] + extension
    final_path = os.path.join(path_to_save, new_filename)
    return final_path


if __name__ == '__main__':
    config = get_config()
    with open('index_template.html', 'r') as template_file:
        template = template_file.read()

    html_jinja_template = jinja2.Template(template)
    html_jinja_template.globals['form_article_path'] = form_article_path
    result_html = html_jinja_template.render(text="Взлом с помощью </body>",
                                             topics=config['topics'],
                                             articles=config['articles'])
    save_html_file(result_html, './html/index.html')
