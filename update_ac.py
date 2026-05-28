import re

fr_map = {
    "AC11.01": "AC11.01 – Maîtriser les lois fondamentales de l'électricité afin d'intervenir sur des équipements de réseaux et télécommunications",
    "AC11.02": "AC11.02 – Comprendre l'architecture et les fondements des systèmes numériques, les principes du codage de l'information, des communications et de l'Internet",
    "AC11.03": "AC11.03 – Configurer les fonctions de base du réseau local",
    "AC11.04": "AC11.04 – Maîtriser les rôles et les principes fondamentaux des systèmes d'exploitation afin d'interagir avec ceux-ci pour la configuration et l'administration des réseaux et services fournis",
    "AC11.05": "AC11.05 – Identifier les dysfonctionnements du réseau local et savoir les signaler",
    "AC11.06": "AC11.06 – Installer un poste client, expliquer la procédure mise en place",

    "AC12.01": "AC12.01 – Mesurer, analyser et commenter les signaux",
    "AC12.02": "AC12.02 – Caractériser des systèmes de transmissions élémentaires et découvrir la modélisation mathématique de leur fonctionnement",
    "AC12.03": "AC12.03 – Déployer des supports de transmission",
    "AC12.04": "AC12.04 – Connecter les systèmes de ToIP",
    "AC12.05": "AC12.05 – Communiquer avec un tiers (client, collaborateur...) et adapter son discours et sa langue à son interlocuteur",

    "AC13.01": "AC13.01 – Utiliser un système informatique et ses outils",
    "AC13.02": "AC13.02 – Lire, comprendre, exécuter, corriger et modifier un programme",
    "AC13.03": "AC13.03 – Traduire un algorithme dans un langage et pour un environnement donné",
    "AC13.04": "AC13.04 – Connaître l'architecture et les technologies d'un site Web",
    "AC13.05": "AC13.05 – Utiliser les frameworks et bibliothèques",

    "AC14.01": "AC14.01 – Acquérir les principes fondamentaux de la cybersécurité",
    "AC14.02": "AC14.02 – Appliquer les politiques de sécurité des équipements réseau",
    "AC14.03": "AC14.03 – Déceler des compromissions dans un système informatique",
    "AC14.04": "AC14.04 – Respecter les réglementations en vigueur et les bonnes pratiques",

    "AC15.01": "AC15.01 – Mesurer et analyser les performances d'un réseau",
    "AC15.02": "AC15.02 – Caractériser et analyser le trafic réseau",
    "AC15.03": "AC15.03 – Maîtriser les outils de supervision réseau",
    "AC15.04": "AC15.04 – Documenter les réseaux et les activités de surveillance"
}

en_map = {
    "AC11.01": "AC11.01 – Master the fundamental laws of electricity to intervene on network and telecommunications equipment",
    "AC11.02": "AC11.02 – Understand the architecture and foundations of digital systems, the principles of information coding, communications and the Internet",
    "AC11.03": "AC11.03 – Configure the basic functions of the local network",
    "AC11.04": "AC11.04 – Master the roles and fundamental principles of operating systems to interact with them for the configuration and administration of networks and provided services",
    "AC11.05": "AC11.05 – Identify dysfunctions in the local network and know how to report them",
    "AC11.06": "AC11.06 – Install a client workstation, explain the implemented procedure",

    "AC12.01": "AC12.01 – Measure, analyze and comment on signals",
    "AC12.02": "AC12.02 – Characterize elementary transmission systems and discover the mathematical modeling of their operation",
    "AC12.03": "AC12.03 – Deploy transmission media",
    "AC12.04": "AC12.04 – Connect ToIP systems",
    "AC12.05": "AC12.05 – Communicate with a third party (client, collaborator...) and adapt discourse and language to the interlocutor",

    "AC13.01": "AC13.01 – Use a computer system and its tools",
    "AC13.02": "AC13.02 – Read, understand, execute, correct and modify a program",
    "AC13.03": "AC13.03 – Translate an algorithm into a language for a given environment",
    "AC13.04": "AC13.04 – Know the architecture and technologies of a website",
    "AC13.05": "AC13.05 – Use frameworks and libraries",

    "AC14.01": "AC14.01 – Acquire the fundamental principles of cybersecurity",
    "AC14.02": "AC14.02 – Apply security policies for network equipment",
    "AC14.03": "AC14.03 – Detect compromises in a computer system",
    "AC14.04": "AC14.04 – Comply with current regulations and best practices",

    "AC15.01": "AC15.01 – Measure and analyze network performance",
    "AC15.02": "AC15.02 – Characterize and analyze network traffic",
    "AC15.03": "AC15.03 – Master network supervision tools",
    "AC15.04": "AC15.04 – Document networks and monitoring activities"
}

def update_file(filepath, mapping):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_ac(match):
        ac_id = match.group(1)
        if ac_id in mapping:
            return f'<button class="accordion">{mapping[ac_id]}</button>'
        else:
            return match.group(0)

    # Replace mapped texts
    content = re.sub(r'<button class="accordion">(AC\d{2}\.\d{2}).*?</button>', replace_ac, content)
    
    # Remove extra unmapped AC blocks (like AC13.06, AC14.05, AC15.05)
    for extra_ac in ["AC13.06", "AC14.05", "AC15.05"]:
        pattern = re.compile(r'\s*<button class="accordion">' + extra_ac + r'.*?</button>\s*<div class="panel">\s*<div class="panel-content">[\s\S]*?</ul>\s*</div>\s*</div>\s*</div>')
        content = pattern.sub('', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_file('c:\\Users\\ps194\\OneDrive\\Téléchargements\\SAE14 BELGOUR Aicha Soulef\\Ma page web\\competences-fr.html', fr_map)
update_file('c:\\Users\\ps194\\OneDrive\\Téléchargements\\SAE14 BELGOUR Aicha Soulef\\Ma page web\\competences.html', en_map)
