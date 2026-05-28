import re
from data import data

def generate_ul(ac_data, is_fr):
    keys_fr = [
        ("Ce que j'ai fait :", "Ce que j’ai fait :"),
        ("Pourquoi je l'ai fait :", "Pourquoi je l’ai fait :"),
        ("Comment je l'ai fait (méthode, outils, ressources) :", "Comment je l’ai fait (méthode, outils, ressources) :"),
        ("Mes difficultés :", "Mes difficultés :"),
        ("Ce que j'en ai appris :", "Ce que j’en ai appris :"),
        ("Ce que je ferais autrement :", "Ce que je ferais autrement :")
    ]
    keys_en = [
        ("What I did:", "What I did:"),
        ("Why I did it:", "Why I did it:"),
        ("How I did it (method, tools, resources):", "How I did it (method, tools, resources):"),
        ("My difficulties:", "My difficulties:"),
        ("What I learned from it:", "What I learned from it:"),
        ("What I would do differently:", "What I would do differently:")
    ]
    
    if is_fr:
        content_dict = ac_data['fr']
        keys = keys_fr
    else:
        content_dict = ac_data['en']
        keys = keys_en
        
    ul_html = '                            <ul style="list-style: none; padding-left: 0; margin-bottom: 0;">\n'
    for i, (display_key, data_key) in enumerate(keys):
        li_style = ' style="margin-bottom: 0.8rem;"' if i < 5 else ''
        text = content_dict.get(data_key, "")
        ul_html += f'                                <li{li_style}><strong>{display_key}</strong> <br><span\n                                        style="color: var(--gray-700);">{text}</span></li>\n'
    ul_html += '                            </ul>'
    return ul_html


def process_file(filename, is_fr):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    for ac_id, ac_data in data.items():
        # Find the button for this AC
        # <button class="accordion">AC11.03
        pattern = r'(<button class="accordion">\s*' + re.escape(ac_id) + r'.*?</button>\s*<div class="panel">.*?<div class="ac-reflection"[^>]*>.*?<h4[^>]*>.*?</h4>\s*)<ul.*?>.*?</ul>'
        
        # We need to escape backslashes in replacement string
        ul_replacement = generate_ul(ac_data, is_fr).replace('\\', '\\\\')
        
        content = re.sub(pattern, r'\g<1>' + ul_replacement, content, flags=re.DOTALL)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('competences-fr.html', True)
process_file('competences.html', False)
print("Update complete")
