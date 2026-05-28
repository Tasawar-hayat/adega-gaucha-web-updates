import re

files = [
    'index.html',
    'adega_hero_v4_updated.html',
    'adega_original_hero_with_new_header.html'
]

old_logo = 'https://adegagaucha.com/wp-content/uploads/2023/11/logo.png'
new_logo = 'https://adegagaucha.com/wp-content/uploads/2026/02/Adega-Logo-White-4-1.png'

for file_name in files:
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_logo, new_logo)
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_name}")
    except Exception as e:
        print(f"Error updating {file_name}: {e}")
