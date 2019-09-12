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
        html_start = """
        <!DOCTYPE html >
        <html lang = "en-US" >
        <head >
           <meta charset = 'utf-8' >
            <meta http-equiv = "X-UA-Compatible" content = "IE=edge" >
            <meta name = "viewport" content = "width=device-width,maximum-scale=2" >
            <link rel = "stylesheet" type = "text/css" media = "screen" href = "/hpeproliant.github.io/assets/css/style.css?v=a9c09387dd73c4b8dbf928d9a83a6b95132c0d1c" >
        <!-- Begin Jekyll SEO tag v2.5.0 -->
        <title > HPE Proliant CI LOGS < /title >
        <meta name = "generator" content = "Jekyll v3.8.5" / >
        <meta property = "og:title" content = "HPE Proliant CI LOGS" / >
        <meta property = "og:locale" content = "en_US" / >
        <link rel = "canonical" href = "https://hpproliant.github.io/hpeproliant.github.io/" / >
        <meta property = "og:url" content = "https://hpproliant.github.io/hpeproliant.github.io/" / >
        <meta property = "og:site_name" content = "HPE Proliant CI LOGS" / >
        <script type = "application/ld+json" >
        {"@type": "WebSite", "headline": "HPE Proliant CI LOGS", "url": "https://hpproliant.github.io/hpeproliant.github.io/", "name": "HPE Proliant CI LOGS", "@context": "http://schema.org"} < /script >
        <!-- End Jekyll SEO tag -->
        </head >
        <body >
         <!-- HEADER -->
            <div id = "header_wrap" class = "outer" >
               <header class = "inner" >
                  <a id = "forkme_banner" href = "https://github.com/hpproliant/hpeproliant.github.io" > View on GitHub < /a >
                  <h1 id = "project_title" > HPE Proliant CI LOGS < /h1 >
                  <h2 id = "project_tagline" > </h2 >
                </header >
            </div >
            <!-- MAIN CONTENT -->
            <div id = "main_content_wrap" class = "outer">
              <section id = "main_content" class = "inner">
                <style type = "text/css" media = "screen">
          .container {
              margin: 10px auto
              max-width: 600px
              text-align: center
          }
          h1 {
              margin: 30px 0
              font-size: 4em
              line-height: 1
            letter-spacing: -1px
          }
        </style >
        < div class = "container" > """

        html_end = """
        </div>
              </section>
            </div>
            <!-- FOOTER  -->
            <div id="footer_wrap" class="outer">
              <footer class="inner">
                <p class="copyright">HPE Proliant CI LOGS maintained by <a href="https://github.com/hpproliant">hpproliant</a></p>
                <p>Published with <a href="https://pages.github.com">GitHub Pages</a></p>
              </footer>
            </div>
          </body>
        </html>
"""
        html_page = html_start + table_start + "</table>\n" + html_end
        with open(os.path.join(path, (path.split('/')[-1] + '.html')), "w") as file:
            file.write(html_page)


create_html(os.getcwd())

