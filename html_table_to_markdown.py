from bs4 import BeautifulSoup

def convert_html_to_markdown(html):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    
    # Find all the tables in the HTML
    tables = soup.find_all('table')
    
    markdown_output = ""
    
    for table in tables:
        # Extract all rows of the table
        rows = table.find_all('tr')
        
        # Add the header separator after the first row (this will create the alignment)
        first_row = True
        
        # Iterate through each row
        for row in rows:
            cols = row.find_all('td')
            markdown_row = "| "
            
            for col in cols:
                # Find the img tag inside the td and extract the src attribute
                img_tag = col.find('img')
                if img_tag:
                    img_src = img_tag.get('src')
                    # Create the markdown image syntax
                    markdown_row += f"![image]({img_src}) | "
            
            # Remove the trailing pipe and add a newline after each row
            markdown_output += markdown_row.rstrip('| ') + '\n'
            
            # Add the header separator after the first row
            if first_row:
                markdown_output += "|:---:|:---:|:---:|\n"
                first_row = False
        
        # Add a newline between tables
        markdown_output += '\n'
    
    return markdown_output.strip()

# Sample HTML content
html_content = """
<table>
  <tr>
    <td><img src='IMG_6654.JPG'/></td>
    <td><img src='IMG_6655.JPG'/></td>
    <td><img src='IMG_6656.JPG'/></td>
  </tr>
  <tr>
    <td><img src='IMG_6657.JPG'/></td>
    <td><img src='IMG_6660.JPG'/></td>
    <td><img src='IMG_6661.JPG'/></td>
  </tr>
  <tr>
    <td><img src='IMG_6662.JPG'/></td>
	<td><img src='IMG_6663.JPG'/></td>
  </tr>
</table>
"""

# Convert the HTML content to Markdown
markdown_result = convert_html_to_markdown(html_content)

# Output the result
print(markdown_result)
