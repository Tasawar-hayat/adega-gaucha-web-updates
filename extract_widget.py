import re

file_path = r'c:\Users\DIGITAL META\Downloads\reviews-FINAL.html'
output_path = r'c:\Users\DIGITAL META\Downloads\elementor-reviews-widget.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract styles
style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
styles = style_match.group(0) if style_match else ''

# Extract body content (everything between <body> and </body>, then remove script inside it if needed, but wait, the script is inside body)
body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

# Clean up
widget_html = f"{styles}\n\n{body_content}"
widget_html = widget_html.strip()

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(widget_html)

print("Widget HTML created successfully at:", output_path)
