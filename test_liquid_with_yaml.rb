require 'liquid'
require 'yaml'

# Load the gear.yml file
gear_data = YAML.load_file('_data/gear.yml')

# Sample Liquid template
template = Liquid::Template.parse("\n| Category | Item | Weight (oz) | Notes |\n|----------|------|-------------|-------|\n{% for tag in tags %}{% if tag.parent == null %}| **{{ tag.name }}** | | | |\n{% for subtag in tags %}{% if subtag.parent == tag.name %}| - {{ subtag.name }} | | | |\n{% for item in items %}{% if item.tags contains subtag.name %}| | {{ item.name }} | {{ item.weight_oz }} | {{ item.notes }} |\n{% endif %}{% endfor %}{% endif %}{% endfor %}{% endif %}{% endfor %}")

# Render the template with the data from gear.yml
output = template.render('tags' => gear_data['tags'], 'items' => gear_data['items'])

# Write the output to a temporary markdown file
File.open('temp_gear_list.md', 'w') do |file|
  file.write(output)
end 