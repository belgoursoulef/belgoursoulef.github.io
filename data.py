import re

# Data structure: AC_ID: (French_Dict, English_Dict)
data = {
    "AC11.03": {
        "fr": {
            "Ce que j’ai fait :": "J'ai configuré des commutateurs (switchs) et des routeurs Cisco directement via l'interface en ligne de commande (CLI). Mes interventions ont porté sur l'attribution d'adresses IP, la création de VLANs, la mise en place de routage statique et la configuration du protocole DHCP.",
            "Pourquoi je l’ai fait :": "C'est véritablement la compétence cœur du technicien réseau. Sans savoir configurer correctement un réseau local à la base, il est tout simplement impossible d'assurer sa disponibilité et son bon fonctionnement pour les utilisateurs.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Dans le cadre de la SAE 1.03 (Dispositif de Transmission), j'ai commencé par des simulations sur Packet Tracer pour valider mes topologies, puis je suis passé sur des équipements physiques en TP. Je me suis beaucoup appuyé sur la documentation officielle Cisco et les supports du cours R103.",
            "Mes difficultés :": "Le routage inter-VLAN et la compréhension du fonctionnement des interfaces virtuelles (SVI) m'ont posé pas mal de problèmes au début. La logique n'était pas évidente et j'ai dû effacer et recommencer mes configurations plusieurs fois avant que le ping ne passe.",
            "Ce que j’en ai appris :": "Aujourd'hui, je maîtrise les commandes de base du système IOS de Cisco, et la logique de segmentation d'un réseau par VLAN est devenue très claire et naturelle pour moi.",
            "Ce que je ferais autrement :": "La prochaine fois, je prendrai le temps de documenter chaque étape de ma configuration dans un journal de bord, avec des captures d'écran, pour pouvoir rejouer les manipulations beaucoup plus facilement sans devoir tout mémoriser."
        },
        "en": {
            "What I did:": "I configured Cisco switches and routers directly via the Command Line Interface (CLI). My interventions included assigning IP addresses, creating VLANs, setting up static routing, and configuring the DHCP protocol.",
            "Why I did it:": "This is truly the core skill of a network technician. Without knowing how to properly configure a local network at the base, it is simply impossible to ensure its availability and proper functioning for users.",
            "How I did it (method, tools, resources):": "As part of SAE 1.03 (Transmission Device), I started with simulations on Packet Tracer to validate my topologies, then I moved on to physical equipment during practicals. I relied heavily on official Cisco documentation and R103 course materials.",
            "My difficulties:": "Inter-VLAN routing and understanding how virtual interfaces (SVI) work caused me quite a few problems at the beginning. The logic was not obvious and I had to erase and restart my configurations several times before the ping went through.",
            "What I learned from it:": "Today, I master the basic commands of the Cisco IOS system, and the logic of network segmentation via VLAN has become very clear and natural to me.",
            "What I would do differently:": "Next time, I will take the time to document each step of my configuration in a logbook, with screenshots, so that I can replay the manipulations much more easily without having to memorize everything."
        }
    },
    "AC11.04": {
        "fr": {
            "Ce que j’ai fait :": "J'ai utilisé des environnements Linux (Ubuntu) en ligne de commande pour effectuer des tâches d'administration système : gestion de l'arborescence des fichiers, attribution des droits utilisateurs, configuration des interfaces réseau (via `ifconfig` et `ip`) et gestion des services avec `systemd`.",
            "Pourquoi je l’ai fait :": "La très grande majorité des serveurs réseau dans le monde fonctionnent sous Linux. Maîtriser le terminal n'est pas une option, c'est un prérequis incontournable pour pouvoir administrer et déployer des services réseau en entreprise.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai travaillé sur ces compétences lors des TP Systèmes du semestre 1, en installant et configurant un serveur Ubuntu. J'ai complété cet apprentissage par des tutoriels en ligne et beaucoup de pratique personnelle sur des machines virtuelles via VirtualBox.",
            "Mes difficultés :": "La gestion des permissions avec les commandes `chmod` et `chown`, ainsi que la compréhension du fonctionnement des processus en arrière-plan (les daemons), ont été les points les plus difficiles à assimiler au départ.",
            "Ce que j’en ai appris :": "Je me sens désormais à l'aise dans un terminal Linux pour effectuer des tâches d'administration basiques et je comprends précisément le rôle des principaux services réseau au sein du système d'exploitation.",
            "Ce que je ferais autrement :": "Si c'était à refaire, j'installerais un serveur Linux chez moi (ou sur un vieux PC) dès le premier jour de la formation pour m'obliger à pratiquer quotidiennement, et pas uniquement pendant les heures de TP."
        },
        "en": {
            "What I did:": "I used command-line Linux environments (Ubuntu) to perform system administration tasks: file tree management, user rights assignment, network interface configuration (via `ifconfig` and `ip`), and service management with `systemd`.",
            "Why I did it:": "The vast majority of network servers worldwide run on Linux. Mastering the terminal is not an option; it is an essential prerequisite for administering and deploying enterprise network services.",
            "How I did it (method, tools, resources):": "I worked on these skills during the Semester 1 Systems practicals, installing and configuring an Ubuntu server. I supplemented this learning with online tutorials and extensive personal practice on virtual machines via VirtualBox.",
            "My difficulties:": "Managing permissions with the `chmod` and `chown` commands, as well as understanding how background processes (daemons) work, were the most difficult points to grasp initially.",
            "What I learned from it:": "I now feel comfortable in a Linux terminal performing basic administration tasks and I precisely understand the role of the main network services within the operating system.",
            "What I would do differently:": "If I had to do it again, I would install a Linux server at home (or on an old PC) from the very first day of training to force myself to practice daily, and not just during practical hours."
        }
    },
    "AC11.05": {
        "fr": {
            "Ce que j’ai fait :": "J'ai pratiqué le diagnostic réseau en utilisant des utilitaires de dépannage classiques (`ping`, `traceroute`, `nslookup`) ainsi que Wireshark pour localiser avec précision des pannes simulées en laboratoire (câbles défectueux, erreurs IP, boucles de commutation).",
            "Pourquoi je l’ai fait :": "Savoir identifier la source d'un problème et le signaler correctement est essentiel. C'est ce qui permet de rétablir rapidement la disponibilité des services et de collaborer efficacement avec le reste de l'équipe technique.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Lors des TP de diagnostic (R103), j'ai été confronté à divers scénarios de pannes. J'ai dû appliquer une méthodologie d'investigation stricte, basée sur les couches du modèle OSI, puis rédiger des rapports d'incident détaillés.",
            "Mes difficultés :": "Au début, sans méthode vraiment rigoureuse, j'avais beaucoup de mal à distinguer rapidement une panne de couche 2 (problème de switch ou de MAC) d'une panne de couche 3 (problème de routage ou d'IP). Je testais un peu au hasard.",
            "Ce que j’en ai appris :": "J'ai fini par intégrer une méthode de diagnostic systématique : je vérifie d'abord la couche physique, puis la liaison, le réseau et enfin le transport. Cette rigueur accélère considérablement mon temps de résolution.",
            "Ce que je ferais autrement :": "Je mettrais en place un système de tickets fictifs entre étudiants pour m'entraîner à la rédaction formelle et professionnelle des incidents dès le début de l'année."
        },
        "en": {
            "What I did:": "I practiced network diagnostics using standard troubleshooting utilities (`ping`, `traceroute`, `nslookup`) as well as Wireshark to accurately locate simulated laboratory failures (faulty cables, IP errors, switching loops).",
            "Why I did it:": "Knowing how to identify the source of a problem and report it correctly is essential. This allows for the rapid restoration of service availability and effective collaboration with the rest of the technical team.",
            "How I did it (method, tools, resources):": "During the diagnostic practicals (R103), I was faced with various failure scenarios. I had to apply a strict investigation methodology based on the OSI model layers, then write detailed incident reports.",
            "My difficulties:": "At first, without a truly rigorous method, I had a hard time quickly distinguishing a Layer 2 failure (switch or MAC problem) from a Layer 3 failure (routing or IP problem). I tested a bit randomly.",
            "What I learned from it:": "I ended up integrating a systematic diagnostic method: I first check the physical layer, then the data link, network, and finally the transport layer. This rigor considerably accelerates my resolution time.",
            "What I would do differently:": "I would set up a mock ticketing system among students to practice formal and professional incident writing right from the start of the year."
        }
    },
    "AC11.06": {
        "fr": {
            "Ce que j’ai fait :": "J'ai procédé à l'installation et à la configuration complète de postes de travail sous Windows et Linux : gestion du partitionnement des disques, installation de l'OS, paramétrage du réseau et déploiement des logiciels métiers et des pilotes.",
            "Pourquoi je l’ai fait :": "La préparation et l'installation de postes clients font partie du quotidien de base d'un technicien. Savoir non seulement le faire, mais aussi être capable d'expliquer et de documenter sa procédure est indispensable pour la transmission d'informations au sein d'une équipe.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai acquis cette expérience principalement lors de mes stages en entreprise (Surface Informatique et DNL Informatique), où j'ai préparé de nombreuses machines en conditions réelles, ainsi que lors des TP à l'IUT.",
            "Mes difficultés :": "Le plus dur n'a pas été l'installation technique en elle-même, mais l'effort de documenter clairement chaque étape. Rédiger une procédure suffisamment précise pour qu'un autre technicien puisse la reproduire sans aide extérieure m'a demandé beaucoup de rigueur.",
            "Ce que j’en ai appris :": "J'ai réellement pris conscience de l'importance capitale de la documentation technique : une procédure bien rédigée sur le moment fait gagner un temps précieux lors des interventions futures.",
            "Ce que je ferais autrement :": "À l'avenir, je prendrai le réflexe de faire des captures d'écran systématiquement à chaque clic ou étape importante, et ce dès le tout début de l'installation, pour faciliter la rédaction de mes guides."
        },
        "en": {
            "What I did:": "I carried out the complete installation and configuration of Windows and Linux workstations: managing disk partitioning, OS installation, network configuration, and deployment of business software and drivers.",
            "Why I did it:": "Preparing and installing client workstations is part of a technician's basic daily routine. Knowing not only how to do it but also being able to explain and document the procedure is essential for knowledge transfer within a team.",
            "How I did it (method, tools, resources):": "I gained this experience mainly during my corporate internships (Surface Informatique and DNL Informatique), where I prepared many machines under real conditions, as well as during IUT practicals.",
            "My difficulties:": "The hardest part wasn't the technical installation itself, but the effort to clearly document each step. Writing a procedure precise enough for another technician to reproduce without outside help required a lot of rigor.",
            "What I learned from it:": "I truly realized the paramount importance of technical documentation: a well-written procedure on the spot saves precious time during future interventions.",
            "What I would do differently:": "In the future, I will make it a habit to systematically take screenshots at every click or important step, right from the very beginning of the installation, to facilitate writing my guides."
        }
    },
    "AC12.01": {
        "fr": {
            "Ce que j’ai fait :": "J'ai réalisé des câblages Ethernet RJ45 en respectant les normes T568A et T568B. J'ai ensuite vérifié mes réalisations à l'aide d'un testeur de câble, tout en étudiant les caractéristiques physiques et les performances des catégories de câbles (Cat5e, Cat6).",
            "Pourquoi je l’ai fait :": "Le câblage structuré est la fondation physique de tout réseau. Si cette base est mauvaise, un câble mal serti peut provoquer des pannes intermittentes et des pertes de paquets qui sont ensuite très difficiles à diagnostiquer au niveau logiciel.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai mis cela en pratique lors des TP de câblage du semestre 1, ainsi que dans le cadre de la SAE 1.03. J'ai manipulé des pinces à sertir, des testeurs de paires, et je me suis appuyé sur des guides de câblage structuré.",
            "Mes difficultés :": "Aligner parfaitement les petits fils de cuivre dans le bon ordre à l'intérieur du connecteur RJ45, sans qu'ils ne bougent au moment du sertissage, m'a demandé pas mal d'essais avant d'avoir un geste fluide.",
            "Ce que j’en ai appris :": "Je sais désormais réaliser proprement des câbles droits et croisés. J'ai aussi compris concrètement pourquoi le choix de la catégorie du câble a un impact direct sur la bande passante et la distance maximale de transmission.",
            "Ce que je ferais autrement :": "Je m'entraînerais sur des chutes de câbles supplémentaires avant les évaluations pour gagner en vitesse d'exécution et en précision lors du sertissage."
        },
        "en": {
            "What I did:": "I made RJ45 Ethernet cables respecting the T568A and T568B standards. I then verified my work using a cable tester, while studying the physical characteristics and performance of cable categories (Cat5e, Cat6).",
            "Why I did it:": "Structured cabling is the physical foundation of any network. If this base is poor, a poorly crimped cable can cause intermittent failures and packet loss that are very difficult to diagnose at the software level later.",
            "How I did it (method, tools, resources):": "I put this into practice during the Semester 1 cabling practicals, as well as part of SAE 1.03. I handled crimping tools, pair testers, and relied on structured cabling guides.",
            "My difficulties:": "Perfectly aligning the small copper wires in the correct order inside the RJ45 connector, without them moving during crimping, took quite a few attempts before I had a fluid motion.",
            "What I learned from it:": "I now know how to cleanly make straight-through and crossover cables. I also concretely understood why the choice of cable category has a direct impact on bandwidth and maximum transmission distance.",
            "What I would do differently:": "I would practice on extra cable scraps before assessments to gain execution speed and precision during crimping."
        }
    },
    "AC12.02": {
        "fr": {
            "Ce que j’ai fait :": "J'ai étudié les différentes normes WiFi (802.11 a/b/g/n/ac) et configuré des points d'accès (AP) en mode infrastructure. J'ai également procédé à l'analyse des signaux et des canaux WiFi à l'aide d'un logiciel de scan.",
            "Pourquoi je l’ai fait :": "Le sans-fil est aujourd'hui omniprésent dans les entreprises. Comprendre ses mécanismes de diffusion et d'interférence est obligatoire pour pouvoir déployer et sécuriser des réseaux WiFi fiables et performants.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Lors du cours R112 et des TP associés, j'ai configuré un Access Point Cisco. J'ai utilisé l'outil inSSIDer pour réaliser une analyse de spectre WiFi sur les bandes 2.4 GHz et 5 GHz afin d'optimiser le plan de canaux.",
            "Mes difficultés :": "La gestion des interférences et la logique de sélection des canaux non-chevauchants (comme les canaux 1, 6 et 11 en 2.4 GHz) n'étaient pas très intuitives au départ et m'ont demandé un effort de conceptualisation.",
            "Ce que j’en ai appris :": "Je comprends aujourd'hui les compromis techniques qu'il faut faire entre la portée du signal, le débit attendu et la sécurité, en fonction du standard WiFi choisi et de l'environnement physique de déploiement.",
            "Ce que je ferais autrement :": "Pour rendre cet apprentissage encore plus concret, je réaliserais une cartographie thermique de la couverture radio (heatmap) directement dans les couloirs du bâtiment de l'IUT."
        },
        "en": {
            "What I did:": "I studied the different WiFi standards (802.11 a/b/g/n/ac) and configured access points (APs) in infrastructure mode. I also analyzed WiFi signals and channels using scanning software.",
            "Why I did it:": "Wireless is ubiquitous in businesses today. Understanding its broadcasting and interference mechanisms is mandatory to be able to deploy and secure reliable and high-performing WiFi networks.",
            "How I did it (method, tools, resources):": "During the R112 course and associated practicals, I configured a Cisco Access Point. I used the inSSIDer tool to perform a WiFi spectrum analysis on the 2.4 GHz and 5 GHz bands to optimize the channel plan.",
            "My difficulties:": "Interference management and the logic of selecting non-overlapping channels (like channels 1, 6, and 11 in 2.4 GHz) were not very intuitive initially and required conceptualization effort.",
            "What I learned from it:": "I now understand the technical compromises that must be made between signal range, expected throughput, and security, depending on the chosen WiFi standard and the physical deployment environment.",
            "What I would do differently:": "To make this learning even more concrete, I would create a thermal map of radio coverage (heatmap) right in the hallways of the IUT building."
        }
    },
    "AC12.03": {
        "fr": {
            "Ce que j’ai fait :": "J'ai conçu et déployé des topologies réseau complètes en partant de zéro. Cela incluait la création du plan d'adressage IP, le câblage physique, la configuration logicielle des équipements actifs, et les tests finaux de connectivité.",
            "Pourquoi je l’ai fait :": "Mettre en place un réseau de bout en bout est l'aboutissement qui regroupe toutes les compétences de la spécialité. C'est l'application réelle et concrète de tous les apprentissages théoriques vus en cours.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai travaillé sur ces déploiements en binôme lors des TP et pour la SAE 1.03. Nous avons utilisé Packet Tracer pour la phase de maquettage et de conception, avant de tout transposer sur du vrai matériel dans les baies de brassage.",
            "Mes difficultés :": "La gestion et le calcul du plan d'adressage m'ont demandé plusieurs itérations. Il fallait s'assurer d'avoir une organisation logique et évolutive tout en évitant les conflits d'adresses IP entre les différentes machines.",
            "Ce que j’en ai appris :": "J'ai surtout appris qu'il faut planifier avant d'agir. Un bon plan d'adressage, réfléchi et bien documenté sur papier, permet d'éviter la très grande majorité des problèmes lors de la phase de configuration.",
            "Ce que je ferais autrement :": "Je m'imposerais de rédiger un document de conception complet (avec un schéma d'architecture propre et un tableau d'adressage finalisé) avant même d'allumer ou de toucher le moindre équipement."
        },
        "en": {
            "What I did:": "I designed and deployed complete network topologies from scratch. This included creating the IP addressing plan, physical cabling, software configuration of active equipment, and final connectivity testing.",
            "Why I did it:": "Setting up an end-to-end network is the culmination that brings together all the skills of the specialty. It is the real and concrete application of all theoretical learning seen in class.",
            "How I did it (method, tools, resources):": "I worked on these deployments in pairs during practicals and for SAE 1.03. We used Packet Tracer for the mock-up and design phase before transposing everything onto real hardware in the server racks.",
            "My difficulties:": "Managing and calculating the addressing plan required several iterations. It was necessary to ensure a logical and scalable organization while avoiding IP address conflicts between the different machines.",
            "What I learned from it:": "Above all, I learned that planning must precede action. A good addressing plan, thought out and well-documented on paper, prevents the vast majority of problems during the configuration phase.",
            "What I would do differently:": "I would force myself to write a complete design document (with a clean architecture diagram and a finalized addressing table) even before turning on or touching any equipment."
        }
    },
    "AC12.04": {
        "fr": {
            "Ce que j’ai fait :": "J'ai configuré un serveur de téléphonie sur IP (ToIP) sous Asterisk, en créant des utilisateurs (extensions SIP) et en définissant des plans de numérotation (dialplan).",
            "Pourquoi je l’ai fait :": "La téléphonie sur IP est essentielle en entreprise pour centraliser et gérer les communications vocales de manière économique et évolutive.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai installé Asterisk sur un serveur Linux. J'ai configuré les fichiers sip.conf et extensions.conf, puis j'ai utilisé des softphones (MicroSIP) pour tester et valider l'établissement des appels.",
            "Mes difficultés :": "La configuration syntaxique des fichiers Asterisk, notamment la logique du dialplan (extensions.conf) avec les priorités et les contextes, a été difficile à appréhender au départ.",
            "Ce que j’en ai appris :": "J'ai compris le fonctionnement des protocoles de signalisation (SIP) et de transport de flux média (RTP), ainsi que l'importance de la gestion des codecs pour la qualité de la voix.",
            "Ce que je ferais autrement :": "Je testerais plus systématiquement les configurations avec des outils de capture comme Wireshark pour analyser les échanges de paquets SIP en cas de dysfonctionnement."
        },
        "en": {
            "What I did:": "I configured an IP telephony (ToIP) server using Asterisk, creating SIP extensions (users) and defining dial plans (dialplan).",
            "Why I did it:": "IP telephony is essential in companies to centralize and manage voice communications economically and scalably.",
            "How I did it (method, tools, resources):": "I installed Asterisk on a Linux server. I configured the sip.conf and extensions.conf files, then I used softphones (MicroSIP) to test and validate call establishment.",
            "My difficulties:": "The syntax configuration of Asterisk files, especially the dialplan logic (extensions.conf) with priorities and contexts, was difficult to understand at first.",
            "What I learned from it:": "I understood how signaling (SIP) and media stream transport (RTP) protocols work, as well as the importance of codec management for voice quality.",
            "What I would do differently:": "I would test configurations more systematically with capture tools like Wireshark to analyze SIP packet exchanges in case of issues."
        }
    },
    "AC12.05": {
        "fr": {
            "Ce que j’ai fait :": "J'ai assuré l'assistance technique directe auprès d'utilisateurs. J'ai dû leur expliquer la nature des pannes et les interventions que je réalisais, et j'ai également rédigé des comptes-rendus d'intervention professionnels.",
            "Pourquoi je l’ai fait :": "Un bon technicien réseau n'est pas uniquement un expert qui configure des machines dans son coin. Savoir vulgariser et communiquer clairement avec des personnes non-techniques est une compétence humaine (soft-skill) indispensable en entreprise.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai pu mettre cela en pratique lors de mes stages professionnels (chez Surface Informatique et DNL Informatique), où j'ai dû apprendre sur le tas à reformuler des problèmes informatiques complexes dans un langage accessible.",
            "Mes difficultés :": "Le plus dur a été d'apprendre à jauger mon interlocuteur pour adapter mon niveau de langage. Il fallait vulgariser pour les novices sans paraître condescendant, tout en restant précis face à des collègues plus techniques.",
            "Ce que j’en ai appris :": "J'ai réalisé que la communication compte presque autant que la technique : un utilisateur qui se sent écouté, rassuré et bien informé fera naturellement confiance au technicien, ce qui facilite grandement l'intervention.",
            "Ce que je ferais autrement :": "Je trouverais intéressant de faire des jeux de rôle simulant des situations \"client/technicien\" pendant les cours, afin de s'entraîner à gérer des utilisateurs stressés ou à expliquer des concepts compliqués simplement."
        },
        "en": {
            "What I did:": "I provided direct technical assistance to users. I had to explain the nature of failures and the interventions I was performing, and I also wrote professional intervention reports.",
            "Why I did it:": "A good network technician is not just an expert configuring machines in isolation. Knowing how to demystify and communicate clearly with non-technical people is an indispensable human skill (soft-skill) in business.",
            "How I did it (method, tools, resources):": "I was able to put this into practice during my professional internships (at Surface Informatique and DNL Informatique), where I had to learn on the job how to rephrase complex IT problems into accessible language.",
            "My difficulties:": "The hardest part was learning to gauge my interlocutor to adapt my language level. It was necessary to simplify for novices without sounding condescending, while remaining precise with more technical colleagues.",
            "What I learned from it:": "I realized that communication matters almost as much as technique: a user who feels heard, reassured, and well-informed will naturally trust the technician, which greatly facilitates the intervention.",
            "What I would do differently:": "I would find it interesting to do role-playing games simulating \"client/technician\" situations during classes, in order to practice dealing with stressed users or explaining complicated concepts simply."
        }
    },
    "AC13.01": {
        "fr": {
            "Ce que j’ai fait :": "J'ai pris en main et j'utilise quotidiennement un environnement de développement complet : l'éditeur VS Code, l'outil de versioning Git avec GitHub, le terminal Linux, ainsi que les outils de développement intégrés au navigateur (DevTools).",
            "Pourquoi je l’ai fait :": "Maîtriser son espace de travail et ses outils est la toute première étape indispensable pour être organisé, efficace et productif lors des phases de développement ou de scripting.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "C'est la pratique quotidienne lors du développement de mon propre portfolio qui m'a formé. J'ai lu la documentation officielle des outils et suivi des tutoriels spécifiques pour la prise en main de Git.",
            "Mes difficultés :": "La gestion des conflits sur Git au moment de fusionner des modifications (merges) et la compréhension abstraite du modèle de branches (branching) ont été des concepts assez complexes à intégrer au début.",
            "Ce que j’en ai appris :": "Je maîtrise aujourd'hui les commandes essentielles de Git et je me sens totalement à l'aise pour travailler dans un environnement de développement standardisé et professionnel.",
            "Ce que je ferais autrement :": "Je me forcerais à utiliser Git dès la toute première ligne de code d'un projet, plutôt que d'essayer de l'introduire en cours de route quand le développement est déjà bien avancé."
        },
        "en": {
            "What I did:": "I familiarized myself with and daily use a complete development environment: the VS Code editor, the Git versioning tool with GitHub, the Linux terminal, as well as integrated browser developer tools (DevTools).",
            "Why I did it:": "Mastering your workspace and tools is the very first essential step to being organized, efficient, and productive during development or scripting phases.",
            "How I did it (method, tools, resources):": "Daily practice while developing my own portfolio trained me. I read official tool documentation and followed specific tutorials to get started with Git.",
            "My difficulties:": "Handling Git conflicts when merging changes and conceptually understanding the branching model were rather complex concepts to grasp at first.",
            "What I learned from it:": "I now master the essential Git commands and feel completely comfortable working in a standardized, professional development environment.",
            "What I would do differently:": "I would force myself to use Git from the very first line of code of a project, rather than trying to introduce it midway when development is already well underway."
        }
    },
    "AC13.02": {
        "fr": {
            "Ce que j’ai fait :": "J'ai analysé, lu et modifié du code source existant (notamment le JavaScript du template SnapFolio) dans le but de l'adapter à mes propres besoins, tout en identifiant et en corrigeant divers bugs d'affichage.",
            "Pourquoi je l’ai fait :": "Dans le monde professionnel, on crée rarement un logiciel de zéro (from scratch). La réalité du métier implique très souvent de reprendre le code de quelqu'un d'autre ; savoir le lire et le modifier est donc une compétence clé.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Pour mon projet de Portfolio Web, j'ai épluché le code source du template, utilisé les DevTools du navigateur pour déboguer pas à pas, et effectué des recherches ciblées sur la documentation MDN et Stack Overflow.",
            "Mes difficultés :": "Comprendre la logique d'un code JavaScript (notamment pour l'animation Canvas) dont je n'étais pas l'auteur a été rude. Les notions de fermetures (closures) et la gestion de la boucle d'animation (`requestAnimationFrame`) m'ont posé des problèmes.",
            "Ce que j’en ai appris :": "J'ai développé une vraie méthode pour aborder du code inconnu : j'identifie d'abord les fonctions principales, je trace mentalement l'exécution du programme, et j'isole les variables pour trouver les bugs.",
            "Ce que je ferais autrement :": "À l'avenir, quand je découvre un nouveau script complexe, je prendrai le temps d'ajouter mes propres commentaires au-dessus de chaque bloc de code au fur et à mesure de ma lecture pour garder une trace claire de ma compréhension."
        },
        "en": {
            "What I did:": "I analyzed, read, and modified existing source code (notably the JavaScript of the SnapFolio template) to adapt it to my own needs, while identifying and fixing various display bugs.",
            "Why I did it:": "In the professional world, software is rarely created from scratch. The reality of the job very often involves taking over someone else's code; knowing how to read and modify it is therefore a key skill.",
            "How I did it (method, tools, resources):": "For my Web Portfolio project, I pored over the template's source code, used browser DevTools to debug step by step, and conducted targeted research on MDN documentation and Stack Overflow.",
            "My difficulties:": "Understanding the logic of JavaScript code (especially for the Canvas animation) that I hadn't written was tough. The concepts of closures and animation loop management (`requestAnimationFrame`) caused me problems.",
            "What I learned from it:": "I developed a real method for tackling unknown code: I first identify the main functions, I mentally trace the program's execution, and I isolate variables to find bugs.",
            "What I would do differently:": "In the future, when discovering a new complex script, I will take the time to add my own comments above each code block as I read it to keep a clear record of my understanding."
        }
    },
    "AC13.03": {
        "fr": {
            "Ce que j’ai fait :": "J'ai codé et implémenté des algorithmes classiques (comme le tri et la recherche) en utilisant la syntaxe de deux langages très différents : Python (dans le cadre de la certification Python Essentials 1) et le langage C.",
            "Pourquoi je l’ai fait :": "L'algorithme représente la logique pure, tandis que le langage n'est que l'outil pour l'exprimer. Savoir transposer une même logique d'un environnement à un autre est la base d'un bon esprit de programmation.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai suivi les cours de programmation du S1 et les exercices pratiques du cursus Cisco Python Institute. J'ai utilisé l'IDE Thonny pour expérimenter le Python et compilé mes programmes en C pour comparer les comportements.",
            "Mes difficultés :": "Passer de la simplicité de Python à la rigueur du C a été un choc. La gestion manuelle de la mémoire en C (avec les pointeurs et l'allocation dynamique) a été un concept particulièrement abstrait et difficile à dompter.",
            "Ce que j’en ai appris :": "J'ai réellement assimilé le fait que la logique algorithmique prime sur la syntaxe. Une fois que l'algorithme est clair dans ma tête, son implémentation dans n'importe quel langage devient beaucoup plus facile.",
            "Ce que je ferais autrement :": "Je prendrais le réflexe de dessiner l'organigramme de mon algorithme sur une feuille de papier avant de toucher au clavier. Cela permet de séparer la réflexion purement logique des contraintes de syntaxe du code."
        },
        "en": {
            "What I did:": "I coded and implemented classic algorithms (like sorting and searching) using the syntax of two very different languages: Python (for the Python Essentials 1 certification) and the C language.",
            "Why I did it:": "An algorithm represents pure logic, while the language is just the tool to express it. Knowing how to transpose the same logic from one environment to another is the foundation of a good programming mindset.",
            "How I did it (method, tools, resources):": "I followed S1 programming courses and Cisco Python Institute curriculum practical exercises. I used the Thonny IDE to experiment with Python and compiled my C programs to compare behaviors.",
            "My difficulties:": "Going from Python's simplicity to C's rigor was a shock. Manual memory management in C (with pointers and dynamic allocation) was a particularly abstract and difficult concept to master.",
            "What I learned from it:": "I truly assimilated the fact that algorithmic logic takes precedence over syntax. Once the algorithm is clear in my head, implementing it in any language becomes much easier.",
            "What I would do differently:": "I would get into the habit of drawing my algorithm's flowchart on a piece of paper before touching the keyboard. This separates purely logical thinking from code syntax constraints."
        }
    },
    "AC13.04": {
        "fr": {
            "Ce que j’ai fait :": "J'ai conçu et développé des applications web complètes. D'une part, un portfolio statique (HTML5, CSS3, JS, Bootstrap) et d'autre part, une plateforme web dynamique en PHP reliée à une base de données MySQL (Plateforme ESGIS).",
            "Pourquoi je l’ai fait :": "Les interfaces web sont le standard de l'industrie, y compris pour administrer des équipements réseau (interfaces d'administration, tableaux de bord de supervision). Il est donc très utile de comprendre comment elles sont construites.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Je me suis appuyé sur les cours de développement web de la SAE 14, la documentation MDN, et des tutoriels. J'ai développé la logique côté serveur (backend) en PHP et la structure de données pour gérer des notes scolaires.",
            "Mes difficultés :": "Faire communiquer proprement le PHP avec MySQL (notamment via les requêtes préparées) et sécuriser les formulaires contre les failles courantes (comme les injections SQL) ont été les défis techniques les plus intenses.",
            "Ce que j’en ai appris :": "J'ai démystifié le modèle client-serveur. Je fais désormais très bien la distinction entre le rôle du frontend (l'interface) et du backend (la logique et les données), et je suis sensibilisé aux enjeux de base de la sécurité web.",
            "Ce que je ferais autrement :": "Avant de me lancer dans le code PHP, je modéliserais de façon beaucoup plus stricte la structure de ma base de données (MCD/MLD) pour m'éviter de devoir restructurer mes tables en plein milieu du projet."
        },
        "en": {
            "What I did:": "I designed and developed complete web applications. On one hand, a static portfolio (HTML5, CSS3, JS, Bootstrap) and on the other, a dynamic PHP web platform linked to a MySQL database (ESGIS Platform).",
            "Why I did it:": "Web interfaces are the industry standard, including for administering network equipment (admin interfaces, monitoring dashboards). It is therefore very useful to understand how they are built.",
            "How I did it (method, tools, resources):": "I relied on SAE 14 web development courses, MDN documentation, and tutorials. I developed server-side logic (backend) in PHP and the data structure to manage school grades.",
            "My difficulties:": "Making PHP communicate cleanly with MySQL (especially via prepared statements) and securing forms against common vulnerabilities (like SQL injections) were the most intense technical challenges.",
            "What I learned from it:": "I demystified the client-server model. I can now easily distinguish between the role of the frontend (interface) and the backend (logic and data), and I am aware of basic web security issues.",
            "What I would do differently:": "Before jumping into PHP code, I would model my database structure (MCD/MLD) much more strictly to avoid having to restructure my tables in the middle of the project."
        }
    },
    "AC13.05": {
        "fr": {
            "Ce que j’ai fait :": "J'ai intégré plusieurs outils tiers dans mes projets : le framework Bootstrap 5 pour assurer une mise en page responsive, la bibliothèque AOS pour gérer les animations au défilement, et Bootstrap Icons/Font Awesome pour l'iconographie.",
            "Pourquoi je l’ai fait :": "En entreprise, on ne réinvente pas la roue à chaque projet. L'utilisation de frameworks permet d'accélérer considérablement le développement tout en garantissant un code robuste, maintenable et visuellement professionnel.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Pour la création de mon Portfolio (SAE 14), je me suis plongé dans la documentation officielle de Bootstrap. J'ai analysé les exemples fournis par la communauté pour comprendre comment imbriquer les classes proprement.",
            "Mes difficultés :": "Le plus délicat a été de réussir à surcharger les styles CSS imposés par défaut par Bootstrap pour personnaliser le design, sans pour autant \"casser\" le comportement responsive et le système de grille natif du framework.",
            "Ce que j’en ai appris :": "J'ai appris à naviguer efficacement dans une documentation technique officielle et, surtout, j'ai appris à distinguer ce qui relève de ma propre logique de code de ce que le framework gère automatiquement en arrière-plan.",
            "Ce que je ferais autrement :": "Avant d'importer un framework et de commencer à bidouiller, je prendrais le temps de lire sa documentation dans son ensemble pour avoir une vue globale de toutes ses capacités et de sa philosophie."
        },
        "en": {
            "What I did:": "I integrated several third-party tools into my projects: the Bootstrap 5 framework for responsive layout, the AOS library for scroll animations, and Bootstrap Icons/Font Awesome for iconography.",
            "Why I did it:": "In business, you don't reinvent the wheel for every project. Using frameworks significantly accelerates development while guaranteeing robust, maintainable, and visually professional code.",
            "How I did it (method, tools, resources):": "For my Portfolio creation (SAE 14), I delved into the official Bootstrap documentation. I analyzed community-provided examples to understand how to nest classes cleanly.",
            "My difficulties:": "The trickiest part was successfully overriding the default CSS styles imposed by Bootstrap to customize the design, without \"breaking\" the responsive behavior and the framework's native grid system.",
            "What I learned from it:": "I learned how to effectively navigate official technical documentation and, above all, I learned to distinguish what belongs to my own code logic from what the framework automatically manages in the background.",
            "What I would do differently:": "Before importing a framework and starting to tinker, I would take the time to read its documentation as a whole to get an overview of all its capabilities and philosophy."
        }
    },
    "AC14.01": {
        "fr": {
            "Ce que j’ai fait :": "J'ai suivi et validé le MOOC SecNumacadémie de l'ANSSI (dans le cadre de la SAE 1.01). J'ai étudié les règles de création de mots de passe, les bases du chiffrement, la gestion des risques et la réaction face aux incidents.",
            "Pourquoi je l’ai fait :": "La cybersécurité est le domaine vers lequel je souhaite me spécialiser. Posséder et maîtriser ces fondamentaux théoriques est le prérequis absolu avant de mettre en place la moindre architecture ou intervention sécurisée.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai travaillé en autonomie sur la plateforme de l'ANSSI, en validant les différents quiz des modules (sécurité des systèmes, protection des données personnelles, cryptographie) et en étudiant les fiches pratiques associées.",
            "Mes difficultés :": "L'assimilation des concepts liés à la cryptographie asymétrique (le fonctionnement des PKI, la gestion des clés publiques/privées et les certificats X.509) a été dense et m'a obligé à faire des recherches complémentaires pour tout comprendre.",
            "Ce que j’en ai appris :": "J'ai vraiment pris conscience que la cybersécurité n'est pas qu'une question de pare-feu et de technique : c'est un enjeu organisationnel. J'ai compris que le facteur humain reste de loin le maillon le plus faible de la chaîne.",
            "Ce que je ferais autrement :": "Pour accompagner la lecture parfois ardue du MOOC, je chercherais d'emblée des vidéos de vulgarisation ou des schémas explicatifs sur la cryptographie pour visualiser les concepts théoriques plus facilement."
        },
        "en": {
            "What I did:": "I followed and validated the ANSSI SecNumacadémie MOOC (as part of SAE 1.01). I studied password creation rules, encryption basics, risk management, and incident response.",
            "Why I did it:": "Cybersecurity is the field I want to specialize in. Possessing and mastering these theoretical fundamentals is the absolute prerequisite before implementing any secure architecture or intervention.",
            "How I did it (method, tools, resources):": "I worked independently on the ANSSI platform, validating various module quizzes (system security, personal data protection, cryptography) and studying associated practical sheets.",
            "My difficulties:": "Assimilating concepts related to asymmetric cryptography (PKI functioning, public/private key management, and X.509 certificates) was dense and forced me to do additional research to understand everything.",
            "What I learned from it:": "I truly realized that cybersecurity isn't just about firewalls and technology: it's an organizational issue. I understood that the human factor remains by far the weakest link in the chain.",
            "What I would do differently:": "To accompany the sometimes arduous MOOC reading, I would immediately look for popularization videos or explanatory diagrams on cryptography to visualize theoretical concepts more easily."
        }
    },
    "AC14.02": {
        "fr": {
            "Ce que j’ai fait :": "J'ai mis en pratique la sécurisation d'infrastructures en configurant des listes de contrôle d'accès (ACL) sur des routeurs Cisco pour filtrer le trafic. J'ai aussi activé des protections de niveau 2 sur les switchs, comme le *Port Security*.",
            "Pourquoi je l’ai fait :": "Un réseau sans politique de sécurité active est une porte ouverte aux attaques. Appliquer ces configurations, c'est traduire concrètement les grands principes théoriques de sécurité directement dans le matériel de l'entreprise.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "J'ai réalisé des TP spécifiques de sécurisation réseau en m'entraînant d'abord sur Packet Tracer pour concevoir mes ACL (standard et étendues), puis je me suis basé sur la documentation Cisco pour les appliquer sur les switchs.",
            "Mes difficultés :": "Saisir la logique stricte des ACL n'a pas été simple : comprendre la différence entre les standards et les étendues, gérer la numérotation, l'ordre de lecture des règles, et surtout ne pas oublier le *deny any* implicite à la fin qui bloquait tout mon trafic.",
            "Ce que j’en ai appris :": "J'ai appris que la mise en place de la sécurité réseau exige une méthode infaillible : il faut identifier précisément les flux légitimes nécessaires, les autoriser, et bloquer absolument tout le reste (c'est le principe du moindre privilège).",
            "Ce que je ferais autrement :": "Je ne tapperai plus mes commandes à l'aveugle. Je modéliserai systématiquement une matrice des flux sur papier (qui communique avec qui et sur quel port) avant de commencer à écrire mes règles ACL."
        },
        "en": {
            "What I did:": "I practiced securing infrastructures by configuring Access Control Lists (ACLs) on Cisco routers to filter traffic. I also enabled Layer 2 protections on switches, such as *Port Security*.",
            "Why I did it:": "A network without an active security policy is an open door to attacks. Applying these configurations concretely translates overarching theoretical security principles directly into enterprise hardware.",
            "How I did it (method, tools, resources):": "I completed specific network security practicals by first practicing on Packet Tracer to design my ACLs (standard and extended), then I relied on Cisco documentation to apply them on switches.",
            "My difficulties:": "Grasping the strict logic of ACLs wasn't simple: understanding the difference between standard and extended, managing numbering, rule reading order, and above all not forgetting the implicit *deny any* at the end that blocked all my traffic.",
            "What I learned from it:": "I learned that implementing network security requires a foolproof method: you must precisely identify the necessary legitimate flows, allow them, and absolutely block everything else (this is the principle of least privilege).",
            "What I would do differently:": "I will no longer type my commands blindly. I will systematically model a flow matrix on paper (who communicates with whom and on what port) before I start writing my ACL rules."
        }
    },
    "AC14.03": {
        "fr": {
            "Ce que j’ai fait :": "J'ai effectué des analyses techniques sur des journaux d'événements (logs) système sous Linux et inspecté des captures Wireshark dans le but de repérer des indicateurs de compromission, comme des scans de ports ou des tentatives de connexion par force brute.",
            "Pourquoi je l’ai fait :": "Être capable de détecter une attaque le plus tôt possible permet de réduire drastiquement son impact sur l'entreprise. C'est le cœur de la cybersécurité défensive (Blue Team).",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Lors d'un TP dédié à l'analyse de logs et à l'introduction à l'investigation numérique (forensique), j'ai utilisé des commandes d'extraction textuelle (`grep`, `awk`) pour fouiller les fichiers système, en croisant ces données avec des captures Wireshark.",
            "Mes difficultés :": "Se retrouver face à des milliers de lignes de logs bruts et essayer de distinguer un trafic anormal d'une simple connexion légitime inhabituelle s'est avéré extrêmement chronophage sans l'aide d'outils d'automatisation.",
            "Ce que j’en ai appris :": "Cette expérience pratique m'a fait comprendre pourquoi les entreprises investissent dans des outils SIEM (gestion des événements de sécurité). Centraliser et corréler les logs automatiquement est indispensable à grande échelle.",
            "Ce que je ferais autrement :": "Pour aller plus loin, je mettrais en place un petit laboratoire personnel (home-lab) avec des solutions open source comme la stack ELK ou Snort, afin de m'entraîner à l'analyse et à la détection en dehors des heures de cours."
        },
        "en": {
            "What I did:": "I performed technical analysis on Linux system event logs and inspected Wireshark captures to identify indicators of compromise, such as port scans or brute force login attempts.",
            "Why I did it:": "Being able to detect an attack as early as possible drastically reduces its impact on the business. This is the core of defensive cybersecurity (Blue Team).",
            "How I did it (method, tools, resources):": "During a practical dedicated to log analysis and introduction to digital forensics, I used text extraction commands (`grep`, `awk`) to search system files, cross-referencing this data with Wireshark captures.",
            "My difficulties:": "Facing thousands of raw log lines and trying to distinguish abnormal traffic from a simple unusual legitimate connection proved extremely time-consuming without automation tools.",
            "What I learned from it:": "This practical experience made me understand why companies invest in SIEM (Security Information and Event Management) tools. Centralizing and correlating logs automatically is essential on a large scale.",
            "What I would do differently:": "To go further, I would set up a small personal lab (home-lab) with open-source solutions like the ELK stack or Snort, to practice analysis and detection outside of class hours."
        }
    },
    "AC14.04": {
        "fr": {
            "Ce que j’ai fait :": "J'ai étudié le cadre légal du numérique, notamment le RGPD et les exigences strictes de l'ANSSI concernant les Opérateurs d'Importance Vitale (OIV). J'ai veillé à appliquer ces bonnes pratiques de sécurité dans mes propres projets (SAE 1.01).",
            "Pourquoi je l’ai fait :": "Un administrateur réseau n'évolue pas dans une bulle technique : il est soumis à un cadre légal. Ignorer ces réglementations expose l'entreprise (et soi-même) à des failles graves et à de lourdes sanctions pénales et financières.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Je me suis basé sur les cours de Droit du Numérique, sur le guide de sensibilisation au RGPD fourni par la CNIL, et sur le guide d'hygiène informatique édité par l'ANSSI.",
            "Mes difficultés :": "Le jargon juridique n'est pas toujours simple à appréhender. Comprendre les obligations spécifiques à certains secteurs critiques (santé, finance) et délimiter clairement les responsabilités juridiques entre un client et son sous-traitant a été complexe.",
            "Ce que j’en ai appris :": "J'ai compris que la conformité légale (compliance) ne doit pas être vue comme une contrainte administrative, mais comme un standard de qualité qui protège efficacement les données des utilisateurs et la réputation de l'organisation.",
            "Ce que je ferais autrement :": "Pour être sûr de ne rien oublier, je me créerais une \"checklist\" ou une grille de conformité personnelle que je validerais systématiquement à chaque nouvelle étape de conception de mes projets informatiques."
        },
        "en": {
            "What I did:": "I studied the digital legal framework, notably the GDPR and the strict ANSSI requirements concerning Operators of Vital Importance (OIV). I made sure to apply these security best practices in my own projects (SAE 1.01).",
            "Why I did it:": "A network administrator does not operate in a technical bubble: they are subject to a legal framework. Ignoring these regulations exposes the company (and oneself) to serious flaws and heavy penal and financial sanctions.",
            "How I did it (method, tools, resources):": "I based my work on Digital Law courses, the GDPR awareness guide provided by the CNIL, and the IT hygiene guide published by ANSSI.",
            "My difficulties:": "Legal jargon is not always easy to grasp. Understanding the specific obligations of certain critical sectors (health, finance) and clearly defining legal responsibilities between a client and their subcontractor was complex.",
            "What I learned from it:": "I learned that legal compliance should not be seen as an administrative constraint, but as a quality standard that effectively protects user data and the organization's reputation.",
            "What I would do differently:": "To make sure I don't forget anything, I would create a personal \"checklist\" or compliance grid that I would systematically validate at each new design stage of my IT projects."
        }
    },
    "AC15.01": {
        "fr": {
            "Ce que j’ai fait :": "J'ai manipulé divers outils de métrologie réseau (comme `iperf`, `ping`, `traceroute`) pour mesurer précisément des indicateurs de performance clés sur une liaison, tels que la bande passante réelle, la latence et la gigue (jitter).",
            "Pourquoi je l’ai fait :": "Surveiller les performances physiques d'une infrastructure permet de détecter une dégradation silencieuse avant qu'elle ne se transforme en panne pour les utilisateurs, et aide à anticiper les futurs besoins en équipement.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Lors des TP de supervision du semestre 1, j'ai simulé des transferts de charge avec `iperf3` et analysé les paquets avec Wireshark pour comparer le comportement du réseau en situation normale puis en situation dégradée.",
            "Mes difficultés :": "Interpréter correctement les chiffres renvoyés par `iperf` (par exemple la différence de comportement entre un flux TCP et UDP face à la gigue) et comprendre l'écart inévitable entre le débit théorique du câble et le débit utile mesuré m'a demandé de la réflexion.",
            "Ce que j’en ai appris :": "J'ai compris qu'une métrique isolée ne veut pas dire grand-chose : la performance dépend d'une multitude de facteurs (la charge instantanée, le protocole utilisé, le matériel). L'analyse doit être globale.",
            "Ce que je ferais autrement :": "Plutôt que de faire des mesures ponctuelles uniquement quand il y a un problème, je mettrais en place des tests automatisés réguliers (benchmarks) pour établir une base de référence saine (baseline) et repérer facilement les dérives."
        },
        "en": {
            "What I did:": "I handled various network metrology tools (like `iperf`, `ping`, `traceroute`) to accurately measure key performance indicators on a link, such as actual bandwidth, latency, and jitter.",
            "Why I did it:": "Monitoring an infrastructure's physical performance helps detect silent degradation before it turns into a user outage, and helps anticipate future equipment needs.",
            "How I did it (method, tools, resources):": "During Semester 1 monitoring practicals, I simulated load transfers with `iperf3` and analyzed packets with Wireshark to compare network behavior under normal and degraded conditions.",
            "My difficulties:": "Correctly interpreting the figures returned by `iperf` (for example, the difference in behavior between a TCP and UDP flow against jitter) and understanding the inevitable gap between the cable's theoretical speed and the measured useful speed required some thought.",
            "What I learned from it:": "I learned that an isolated metric doesn't mean much: performance depends on a multitude of factors (instantaneous load, protocol used, hardware). The analysis must be holistic.",
            "What I would do differently:": "Rather than making ad-hoc measurements only when there is a problem, I would implement regular automated tests (benchmarks) to establish a healthy baseline and easily spot drifts."
        }
    },
    "AC15.02": {
        "fr": {
            "Ce que j’ai fait :": "J'ai capturé du trafic en direct à l'aide de Wireshark pour l'analyser en profondeur. J'ai identifié les protocoles en jeu, reconstruit des flux TCP complets (Follow TCP Stream) et cherché à détecter des comportements de communication anormaux.",
            "Pourquoi je l’ai fait :": "Analyser le trafic est comme observer la circulation sur une autoroute : cela permet de savoir exactement quel type de données transite, de repérer les goulets d'étranglement qui ralentissent le réseau et de déceler les activités malveillantes.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Je me suis familiarisé avec la syntaxe des filtres de capture et d'affichage de Wireshark lors des TP, en décortiquant des sessions d'échanges HTTP, des requêtes de résolution DNS et des paquets de diagnostic ICMP.",
            "Mes difficultés :": "Face à une capture de plusieurs minutes contenant des centaines de milliers de trames, j'ai d'abord été complètement noyé. Apprendre à utiliser les bons filtres pour faire le tri sans perdre d'informations pertinentes a été laborieux.",
            "Ce que j’en ai appris :": "Aujourd'hui, je suis capable de nettoyer visuellement une capture Wireshark en isolant très rapidement la conversation ou le protocole qui m'intéresse, ce qui m'aide énormément à pointer du doigt une anomalie.",
            "Ce que je ferais autrement :": "Je ferais l'effort d'apprendre la syntaxe avancée des filtres de capture (BPF - Berkeley Packet Filter) dès le départ, ce qui m'éviterait d'enregistrer des fichiers de capture énormes et illisibles."
        },
        "en": {
            "What I did:": "I captured live traffic using Wireshark for in-depth analysis. I identified the protocols involved, reconstructed complete TCP streams (Follow TCP Stream), and looked for abnormal communication behaviors.",
            "Why I did it:": "Analyzing traffic is like observing traffic on a highway: it lets you know exactly what type of data is transiting, spot bottlenecks that slow down the network, and detect malicious activities.",
            "How I did it (method, tools, resources):": "I familiarized myself with the syntax of Wireshark capture and display filters during practicals, dissecting HTTP exchange sessions, DNS resolution requests, and ICMP diagnostic packets.",
            "My difficulties:": "Faced with a multi-minute capture containing hundreds of thousands of frames, I was completely overwhelmed at first. Learning to use the right filters to sort things out without losing relevant information was tedious.",
            "What I learned from it:": "Today, I am able to visually clean up a Wireshark capture by quickly isolating the conversation or protocol that interests me, which helps me enormously in pinpointing an anomaly.",
            "What I would do differently:": "I would make the effort to learn the advanced syntax of capture filters (BPF - Berkeley Packet Filter) right from the start, which would save me from saving huge and unreadable capture files."
        }
    },
    "AC15.03": {
        "fr": {
            "Ce que j’ai fait :": "J'ai découvert, installé et pris en main des solutions de supervision professionnelles (comme Nagios et PRTG). J'ai configuré les hôtes à surveiller, paramétré les services à interroger et créé des règles d'alertes automatiques.",
            "Pourquoi je l’ai fait :": "La supervision proactive est ce qui permet à l'équipe réseau d'être alertée d'une panne (ou d'un risque de panne) de jour comme de nuit, bien avant que les utilisateurs ne s'en plaignent. C'est l'outil de base du \"NOC\" (Network Operations Center).",
            "Comment je l’ai fait (méthode, outils, ressources) :": "Après une introduction théorique, j'ai déployé le système Nagios Core sur une machine virtuelle Ubuntu en TP. En m'aidant de la documentation, j'ai activé la surveillance de nos équipements et paramétré l'envoi d'alertes par email.",
            "Mes difficultés :": "La logique de configuration textuelle de Nagios (associer les commandes, les hôtes, les groupes de services et les contacts) m'a semblé très abstraite et rigide au début, ce qui a causé pas mal d'erreurs de syntaxe.",
            "Ce que j’en ai appris :": "J'ai assimilé l'architecture de fonctionnement d'un serveur de supervision (le principe du \"polling\") et j'ai compris à quel point il est crucial de bien calibrer ses seuils d'alerte (Warning vs Critical) pour éviter la fatigue d'alerte.",
            "Ce que je ferais autrement :": "Pour avoir une vision plus moderne et comparer les approches, je déploierais de mon côté des outils plus récents et visuels (comme Zabbix, ou un couple Prometheus/Grafana) pour bien cerner l'évolution du marché de la supervision."
        },
        "en": {
            "What I did:": "I discovered, installed, and learned to use professional monitoring solutions (like Nagios and PRTG). I configured the hosts to monitor, set up the services to poll, and created automatic alert rules.",
            "Why I did it:": "Proactive monitoring is what allows the network team to be alerted to an outage (or risk of outage) day and night, long before users complain about it. It is the core tool of the NOC (Network Operations Center).",
            "How I did it (method, tools, resources):": "After a theoretical introduction, I deployed the Nagios Core system on an Ubuntu virtual machine during a practical. With the help of documentation, I enabled monitoring for our equipment and configured email alert sending.",
            "My difficulties:": "Nagios' text-based configuration logic (linking commands, hosts, service groups, and contacts) seemed very abstract and rigid at first, causing quite a few syntax errors.",
            "What I learned from it:": "I assimilated the functional architecture of a monitoring server (the \"polling\" principle) and understood how crucial it is to properly calibrate alert thresholds (Warning vs Critical) to avoid alert fatigue.",
            "What I would do differently:": "To get a more modern view and compare approaches, I would deploy newer, more visual tools on my own (like Zabbix, or a Prometheus/Grafana combo) to fully grasp the evolution of the monitoring market."
        }
    },
    "AC15.04": {
        "fr": {
            "Ce que j’ai fait :": "J'ai réalisé des schémas topologiques clairs (via Packet Tracer et draw.io), maintenu des tableaux d'adressage IP détaillés, et rédigé des descriptions techniques et des rapports d'incident structurés (notamment pour mon portfolio et mes stages).",
            "Pourquoi je l’ai fait :": "Un réseau qui fonctionne mais qui n'est pas documenté est un réseau impossible à dépanner et à faire évoluer sereinement. La documentation est littéralement la mémoire collective et le patrimoine technique d'une entreprise.",
            "Comment je l’ai fait (méthode, outils, ressources) :": "C'est un travail continu que j'ai appliqué sur chaque projet et TP. J'ai utilisé des outils de dessin vectoriel pour l'architecture logique et physique, et j'ai rédigé les objectifs, méthodes et résultats pour alimenter mon portfolio.",
            "Mes difficultés :": "Le plus grand défi est de réussir à maintenir la documentation à jour. Dans le feu de l'action, on modifie souvent une configuration sans mettre à jour le schéma, ce qui m'a souvent conduit à avoir des documents obsolètes par rapport à la réalité.",
            "Ce que j’en ai appris :": "J'ai retenu qu'une bonne documentation doit être synthétique, très visuelle et, surtout, qu'elle doit être produite en temps réel au fur et à mesure du travail, et non pas gardée comme une corvée pour la fin du projet.",
            "Ce que je ferais autrement :": "Je me tournerais vers des méthodologies de type \"Documentation as Code\", en utilisant par exemple des scripts qui génèrent l'architecture ou en versionnant mes fichiers de schémas avec Git pour tracer et forcer la mise à jour à chaque modification technique."
        },
        "en": {
            "What I did:": "I created clear topological diagrams (via Packet Tracer and draw.io), maintained detailed IP addressing tables, and wrote technical descriptions and structured incident reports (especially for my portfolio and internships).",
            "Why I did it:": "A working network that is not documented is a network impossible to troubleshoot and evolve peacefully. Documentation is literally the collective memory and technical heritage of a company.",
            "How I did it (method, tools, resources):": "This is continuous work that I applied to every project and practical. I used vector drawing tools for logical and physical architecture, and I wrote down objectives, methods, and results to feed my portfolio.",
            "My difficulties:": "The biggest challenge is managing to keep documentation up to date. In the heat of the moment, you often modify a configuration without updating the diagram, which often led me to having outdated documents compared to reality.",
            "What I learned from it:": "I learned that good documentation must be concise, very visual, and above all, it must be produced in real-time as the work progresses, not kept as a chore for the end of the project.",
            "What I would do differently:": "I would turn to \"Documentation as Code\" type methodologies, using for example scripts that generate the architecture or versioning my diagram files with Git to track and force updates with every technical modification."
        }
    }
}
