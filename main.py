from jinja2 import Template, Environment, FileSystemLoader
from data import content

# load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader('./templates'))

index_template = env.get_template('index.html')
output_from_parsed_template = index_template.render(materias=content)

# write the parsed template
with open("./index.html", "w") as chap_page:
  chap_page.write(output_from_parsed_template)
