import os
from bs4 import BeautifulSoup
import re

# The convert_html_to_markdown function (as provided by you)
def convert_html_to_markdown(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table')
    
    markdown_output = ""
    
    for table in tables:
        rows = table.find_all('tr')
        
        first_row = True
        
        for row in rows:
            cols = row.find_all('td')
            markdown_row = "| "
            
            for col in cols:
                img_tag = col.find('img')
                if img_tag:
                    img_src = img_tag.get('src')
                    markdown_row += f"![]({img_src}) | "
            
            markdown_output += markdown_row.rstrip('| ') + '\n'
            
            if first_row:
                markdown_output += "|:---:|:---:|:---:|\n"
                first_row = False
        
        markdown_output += '\n'
    
    return markdown_output.strip()

# Function to process all `index.md` files in a directory and its subdirectories
def process_directory(directory):
    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(directory):
        # Check if the current directory contains an index.md file
        if 'index.md' in files:
            file_path = os.path.join(root, 'index.md')
            
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find all HTML tables in the content
            tables = re.findall(r'(<table.*?</table>)', content, re.DOTALL)
            
            # Replace HTML tables with Markdown tables
            for table_html in tables:
                markdown_table = convert_html_to_markdown(table_html)
                content = content.replace(table_html, markdown_table)

            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Processed {file_path}")

# Run the function on the desired directory
process_directory('Computers/Lenovo')
