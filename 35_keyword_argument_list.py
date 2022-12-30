# Belajar Keywords Argument List

# Keywords Argument List itu menggunakan '**'

def create_html(tag, text, **attribute):
    html = f"<{tag}"

    print(attribute)
    # Cara mengakses Keyword Argument List
    for key, value in attribute.items():
        html = html + f" {key}={value}"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("H1", "Ini Judul")
print(html)

html = create_html("div", "Ini Div", style="Ini Contoh")
print(html)

html = create_html("a", "Ini Link", href="www.google.com", style="Contoh Link")
print(html)