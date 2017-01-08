import jinja2
from convert import form_path_to_save_html, get_config, save_html_file


if __name__ == '__main__':
    config = get_config()
    with open('index_template.html', 'r') as template_file:
        template = template_file.read()

    html_jinja_template = jinja2.Template(template)
    html_jinja_template.globals['form_path_to_save_html'] = form_path_to_save_html
    result_html = html_jinja_template.render(topics=config['topics'],
                                             articles=config['articles'])
    save_html_file(result_html, 'index.html')
