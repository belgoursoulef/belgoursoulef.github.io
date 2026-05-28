import re

def fix_html(content):
    # Match the end of ac-reflection, followed by ANY whitespace or </div> tags
    # up to the next structure block.
    pattern = re.compile(
        r'(                            </ul>\n                        </div>)(?:\s|</div>)*?(?=\n                <button class="accordion"|\n            </div>\n\n            <!-- AC|\n            </div>\n\n        </div>)',
        re.MULTILINE
    )
    
    fixed = pattern.sub(r'\1\n                    </div>\n                </div>', content)
    return fixed
    
def process(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c2 = fix_html(c)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(c2)

process('competences.html')
process('competences-fr.html')
print("Repaired DIVs correctly!")
