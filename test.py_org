import os


def create_html(path):
    if os.path.isdir(path):
        cmd_list = os.listdir(path)
        if len(cmd_list) == 0 or path.split('/')[-1] == '.git':
            return
        table_start = "<table>\n"
        for i in cmd_list:
            new_path = os.path.join(path, i)
            if os.path.isdir(new_path):
                table_start = table_start + \
                    "<tr><td><a href = 'https://hpproliant.github.io/hpeproliant.github.io/{}/{}.html'>{}</a></td></tr>\n".format(
                        new_path.split('/home/zuul/upload/hpproliant.github.io/')[-1], i, i)
                create_html(new_path)
            elif '.html' not in i:
                table_start = table_start + \
                    "<tr><td><a href = 'https://hpproliant.github.io/hpeproliant.github.io/{}'>{}</a></td></tr>\n".format(
                        new_path.split('/home/zuul/upload/hpproliant.github.io/')[-1], i)
        html_page = "<html>\n<body>\n" + table_start + "</table>\n" + "</body>\n</html>"
        with open(os.path.join(path, (path.split('/')[-1] + '.html')), "w") as file:
            file.write(html_page)


create_html(os.getcwd())

