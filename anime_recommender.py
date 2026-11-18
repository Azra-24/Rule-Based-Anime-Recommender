import time
import random
from termcolor import colored
def print_pause(message):
    #print(message)
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    #time.sleep(2)
def recom():
    print_pause(colored("These are the genre's avaible right now:\n","cyan"))
    genre={'1.SHONEN':'1',
           '2.FANSTASY':'2',
           '3.ACTION':'3',
           '4.COMEDY':'4',
           '5.ADVENTURE':'5',
           '6.SUPER POWER':'6',
           '7.MARTIAL ARTS':'7',
           '8.PSYCHOLOGICAL':'8',
           '9.POLICE/DETECTIVE':'9',
           '10.THRILLER':'10',
           '11.SUPERNATURAL':'11',
           }
    for i, item in enumerate(genre):
        time.sleep(0.03)
        print(colored(item,"blue"))
        print("\n")
    #a=input("enter the number of the corresponding genre")
    print_pause(colored("would you like the anime to be short or long\n","cyan"))
    srl=input().lower()
    if srl=='short':
        #a=input(colored("enter the number of the corresponding genre\n","cyan"))
        print_pause(colored("enter the number of the corresponding genre\n","cyan"))
        a=input()

        #SHORT SHONEN ANIME
        if a=='1':
            print_pause(colored("Here is a SHONEN anime recommendation that has less episodes:\n","cyan"))
            short_shonen_anime=['Noragami',
                                'Deadman Wonderland',
                                'Mob Psycho 100',
                                'Baccano!',
                                'The Devil is a Part-Timer! (Hataraku Maou-sama!)',
                                'Kekkai Sensen (Blood Blockade Battlefront)',
                                'Barakamon',
                                'No Game No Life',
                                'Angel Beats!',
                                'Charlotte']
            ran= random.choice(short_shonen_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_shonen_anime[0]
            c=short_shonen_anime[1]
            d=short_shonen_anime[2]
            f=short_shonen_anime[3]
            g=short_shonen_anime[4]
            h=short_shonen_anime[5]
            o=short_shonen_anime[6]
            j=short_shonen_anime[7]
            k=short_shonen_anime[8]
            l=short_shonen_anime[9]
            
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Supernatural, Comedy\n","red"))
                print_pause(colored('Synopsis: Follows the adventures of Yato, a minor deity and his adventures with a human girl named Hiyori and a spirit weapon named ',"yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Horror, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: Ganta Igarashi is framed for the brutal slaughter of his classmates and sent to a twisted prison where inmates must participate in deadly games to survive.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Supernatural, Comedy\n","red"))
                print_pause(colored("Synopsis: Shigeo 'Mob' Kageyama is an incredibly powerful psychic who tries to lead a normal life while suppressing his emotions","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Mystery, Supernatural\n","red"))
                print_pause(colored("Synopsis: Set in the 1930s, this anime follows multiple interconnected storylines involving immortals, gangsters, and alchemists aboard the luxury transcontinental train, the Flying Pussyfoot.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Comedy, Fantasy\n","red"))
                print_pause(colored("Synopsis: The Devil King, Satan, is forced to work at a fast-food restaurant in modern-day Tokyo after being transported from his fantasy world.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Fantasy, Supernatural\n","red"))
                print_pause(colored("Synopsis: In Hellsalem's Lot, formerly New York City, where a portal to the 'Beyond' opened three years ago, the Libra organization fights to maintain peace between humans and otherworldly beings.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Slice of Life, Comedy\n","red"))
                print_pause(colored("Synopsis: Seishuu Handa, a calligrapher, moves to a remote island after punching an elderly curator who criticized his work. He finds new inspiration and forms relationships with the islanders.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Adventure, Comedy, Fantasy\n","red"))
                print_pause(colored("Synopsis: Siblings Sora and Shiro are transported to a world where everything is decided by games. They aim to conquer this world by defeating the god of games.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Action, Comedy, Drama\n","red"))
                print_pause(colored("Synopsis: In the afterlife, Otonashi awakens with no memories and joins a rebel group fighting against a girl named Angel, who enforces the rules in this mysterious world.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Drama, Supernatural\n","red"))
                print_pause(colored("Synopsis:Yuu Otosaka gains the ability to possess anyone for five seconds. He is recruited into a student council to track down others with supernatural abilities.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))   
            print_pause(colored("\n\nENJOY!!","cyan"))
            
        #SHORT FANTASY ANIME
        elif a=='2':
            print_pause(colored("Here is a reccommendation FANTASY anime that has less episodes:\n","cyan"))
            short_fantasy_anime=['Madoka Magica',
                                 'No Game No Life',
                                 'The Ancient Magus Bride(Mahoutsukai no Yome)',
                                 'Made in Abyss',
                                 'Grimgar:Asher and Illusions(Hai to Gensou no Grimgar)']
            ran=random.choice(short_fantasy_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_fantasy_anime[0]
            c=short_fantasy_anime[1]
            d=short_fantasy_anime[2]
            e=short_fantasy_anime[3]
            f=short_fantasy_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Dark Fantasy, Magical Girl\n","red"))
                print_pause(colored("Synopsis: Madoka Kaname is approached by a mysterious creature and offered the chance to become a magical girl, granting her powers to fight witches. However, she soon discovers the dark and dangerous reality behind this seemingly glamorous role.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Fantasy, Game\n","red"))
                print_pause(colored("Synopsis:Siblings Sora and Shiro are master gamers who are transported to a world where all conflicts are settled through games. Using their gaming prowess, they aim to conquer the world of Disboard and challenge its god, Tet.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Fantasy, Romance\n","red"))
                print_pause(colored("Synopsis:Chise Hatori, a troubled orphan girl, is bought at an auction by Elias Ainsworth, a mage with a skull for a head. Elias announces that Chise will become his apprentice and eventually his bride, leading her into a world of magic, mythical creatures, and self-discovery.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Fantasy, Adventure\n","red"))
                print_pause(colored("Synopsis:In a city built around the edge of a gigantic abyss, orphaned girl Riko dreams of becoming a Cave Raider like her mother and exploring its depths. When she encounters a mysterious robot boy named Reg, they embark on a perilous journey into the abyss, encountering strange creatures and uncovering its mysteries.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Fantasy, Adventure\n","red"))
                print_pause(colored("Synopsis:A group of strangers awaken in the fantasy world of Grimgar with no memory of their past lives. Forced to adapt and survive, they join the Volunteer Soldiers to earn a living and explore the dangerous lands, discovering their own strengths and weaknesses along the way.","yellow"))
            else:
                print(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))
        #short action anime
        elif a=='3':
            print_pause(colored("Here is a recommendation ACTION anime that has less episodes:","cyan"))
            short_action_anime=['Attack on Titan : Junior High',
                                'FLCL(Fooly Cooly)',
                                'Wind Breaker',
                                'Tokyo Ghoul',
                                'Cowboy Bebop',
                                'Trigun']
            ran=random.choice(short_action_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_action_anime[0]
            c=short_action_anime[1]
            d=short_action_anime[2]
            e=short_action_anime[3]
            f=short_action_anime[4]
            g=short_action_anime[5]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Comedy, Parody\n","red"))
                print_pause(colored("Synopsis: This spin-off of the popular *Attack on Titan* series reimagines the characters as junior high school students in a comedic and lighthearted setting. Eren Yeager and his friends navigate the challenges of school life while dealing with the occasional Titan invasion.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Comedy, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: Naota Nandaba's mundane life in a quiet town is turned upside down when a mysterious woman on a Vespa runs him over, then hits him with a bass guitar. This event triggers a series of bizarre and surreal events involving giant robots, aliens, and eccentric characters.","yellow"))   
            elif ran==d:
                print_pause(colored("Sub Genre: Sports, Action, Slice of Life\n","red"))
                print_pause(colored("Synopsis:A high school student joins an elite group of bikers, discovering camaraderie and rivalry while navigating the thrills and challenges of competitive cycling.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Horror, Supernatural\n","red"))
                print_pause(colored("Synopsis:In modern Tokyo, ghouls—creatures who look like humans but survive on human flesh—live among humans in secret. Ken Kaneki, a college student, becomes half-ghoul after a deadly encounter and must navigate between the human and ghoul worlds while facing deadly conflicts.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Sci-Fi, Space Western\n","red"))
                print_pause(colored("Synopsis:Spike Spiegel and Jet Black are bounty hunters aboard the spaceship Bebop. They are joined by femme fatale Faye Valentine, hacker prodigy Edward, and a corgi named Ein as they chase bounties across the galaxy while confronting their own troubled pasts.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Action, Sci-Fi, Comedy\n","red"))
                print_pause(colored("Synopsis:In a futuristic desert wasteland, Vash the Stampede is a skilled gunslinger with a mysterious past and a bounty on his head. Despite his reputation as a destructive force, Vash is actually a pacifist who avoids killing, leading to comedic and action-packed encounters.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))
        # short comedic anime
        elif a=='4':
            print_pause(colored("Here is a reccommendation COMEDIC anime that has less episodes:\n","cyan"))
            short_comedy_anime=['The Devil is a Part-Timer!',
                                 'Nichijou: My Ordinary Life',
                                 'Monthly Girls Nozaki-kun',
                                 "Haven't You Heard? I'm Sakamoto",
                                 'Asobi Asobase',
                                 'Barakamon',
                                 'Detroit Metal City',
                                 'Space Patrol Luluco',
                                 "Aggretsuko",
                                 'Anohana: The Flower We Saw That Day'
                                 ]
            ran=random.choice(short_comedy_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_comedy_anime[0]
            c=short_comedy_anime[1]
            d=short_comedy_anime[2]
            f=short_comedy_anime[3]
            g=short_comedy_anime[4]
            h=short_comedy_anime[5]
            o=short_comedy_anime[6]
            j=short_comedy_anime[7]
            k=short_comedy_anime[8]
            l=short_comedy_anime[9]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print(colored("Sub Genre: Comedy, Fantasy, Slice of Life\n","red"))
                print(colored('Synopsis: A demon lord ends up in modern Tokyo and must work at a fast-food restaurant to make ends meet while plotting his return to power.',"yellow"))
            elif ran==c:
                print(colored("Sub Genre: Comedy, Slice of Life\n","red"))
                print(colored("Synopsis: The everyday lives of three high school girls and their eccentric friends unfold in a series of bizarre and whimsical events","yellow"))
            elif ran==d:
                print(colored("Sub Genre: Comedy, Romance, Slice of Life\n","red"))
                print(colored("Synopsis: A high school girl confesses to her crush, only to become his assistant as he secretly works as a popular shoujo manga artist.","yellow"))
            elif ran==f:
                print(colored("Sub Genre: Comedy, School, Slice of Life\n","red"))
                print(colored("Synopsis: The coolest and most unflappable high school student handles every situation with style and perfection, baffling everyone around him.","yellow"))
            elif ran==g:
                print(colored("Sub Genre: Comedy, School, Slice of Life\n","red"))
                print(colored("Synopsis: Three schoolgirls with contrasting personalities form a club dedicated to playing games, leading to outrageous and hilarious antics.",'yellow'))
            elif ran==h:
                print_pause(colored("Sub Genre: Comedy, Slice of Life\n","red"))
                print_pause(colored("Synopsis: A calligrapher moves to a rural village to find inspiration and ends up bonding with the quirky locals, especially an energetic little girl.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Comedy, Music\n","red"))
                print_pause(colored("Synopsis: A mild-mannered musician secretly fronts a death metal band with outrageously vulgar lyrics and wild performances.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Comedy, Sci-Fi, Action\n","red"))
                print_pause(colored("Synopsis:  A middle school girl becomes an unwilling space patrol officer to save her father, leading to a series of zany adventures.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre:  Comedy, Slice of Life, Music\n","red"))
                print_pause(colored("Synopsis: A red panda copes with her thankless office job and frustrations through death metal karaoke sessions.",'yellow'))
            elif ran==l:
                print_pause(colored("Sub Genre: Comedy, Drama, Slice of life\n","red"))
                print_pause(colored("Synopsis: A group of childhood friends reunites to help the ghost of their deceased friend find peace.","yellow"))
            else:
                print(colored("INVALID","grey"))   
            print_pause(colored("\n\nENJOY!!","cyan"))
        #short adventure anime
        elif a=='5':
            print_pause(colored("Here is a reccommendation of ADVENTUROUS anime that has less episodes:","cyan"))
            short_adventure_anime=['Samurai Champloo',
                                 'The Rising of the Shield Hero',
                                 'Katanagatari',
                                 "Erased (Boku dake ga Inai Machi)",
                                 'A Place Further than the Universe',
                                 'Angels of Death (Satsuriku no Tenshi)',
                                 'Elfen Lied',
                                 'Space Dandy',
                                 ]
            ran=random.choice(short_adventure_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_adventure_anime[0]
            c=short_adventure_anime[1]
            d=short_adventure_anime[2]
            e=short_adventure_anime[3]
            f=short_adventure_anime[4]
            g=short_adventure_anime[5]
            h=short_adventure_anime[6]
            o=short_adventure_anime[7]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Historical\n","red"))
                print_pause(colored("Synopsis: A samurai epic that follows three mismatched companions on a quest across Edo-era Japan.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis:An ordinary man is summoned to another world as the Shield Hero and must fight to protect the realm.","yellow")) 
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Adventure, Romance\n","red"))
                print_pause(colored("Synopsis:: A swordless swordsman and a strategist set out to collect twelve unique swords.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Mystery, Psychological, Supernatural\n","red"))
                print_pause(colored("Synopsis: A man with the ability to time-travel tries to prevent a series of kidnappings and murders.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Adventure, Slice of Life\n","red"))
                print_pause(colored("Synopsis: Four girls embark on an expedition to Antarctica, seeking adventure and self-discovery.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre:  Adventure, Horror, Psychological\n","red"))
                print_pause(colored("Synopsis: A girl wakes up in a strange building and must escape with the help of a serial killer.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Horror, Psychological\n","red"))
                print_pause(colored("Synopsis:  A genetically mutated girl with deadly powers escapes from a facility and struggles to find a place in the world.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Adventure, Comedy, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: A dandy space explorer travels the galaxy in search of rare aliens.","yellow"))
            else:
                print(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!"),"cyan")
#SHORT SUPER POWER  ANIME
        elif a=='6':
            print_pause(colored("Here is a recommendation anime in which characters have SUPERPOWERS that has less episodes:","cyan"))
            short_superpower_anime=['The Disastrous Life of Saiki K." (Saiki Kusuo no Psi-nan)',
                                   'Parasyte -the maxim-(Kiseijuu: Sei no Kakuritsu)',
                                   'Darker than Black',
                                   'Tokyo ESP',
                                   'Bungo Stray Dogs',
                                   'Blue Exorcist" (Ao no Exorcist)',
                                   'Code',
                                   'InuYasha',
                                   'One Punch Man',
                                   'Akame ga Kill!'
                                ]
            ran=random.choice(short_superpower_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_superpower_anime[0]
            c=short_superpower_anime[1]
            d=short_superpower_anime[2]
            f=short_superpower_anime[3]
            g=short_superpower_anime[4]
            h=short_superpower_anime[5]
            o=short_superpower_anime[6]
            j=short_superpower_anime[7]
            k=short_superpower_anime[8]
            l=short_superpower_anime[9]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Comedy, School, Supernatural\n","red"))
                print_pause(colored('Synopsis: A high school student with immense psychic powers tries to live a normal life.',"yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Horror, Supernatural\n","red"))
                print_pause(colored("Synopsis: A high school student battles parasitic aliens that take over human hosts.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Mystery, Sci-Fi, Super Power\n","red"))
                print_pause(colored("Synopsis: In a world where contractors gain supernatural abilities, a masked man with electric powers works as a spy.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Sci-Fi, Super Power\n","red"))
                print_pause(colored("Synopsis: A high school girl gains the ability to phase through objects and fights against other espers.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Action, Mystery, Supernatural\n","red"))
                print_pause(colored("Synopsis: A young man joins a detective agency staffed by individuals with literary-inspired superpowers.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Fantasy, Supernatural\n","red"))
                print_pause(colored("Synopsis: A teenager discovers he's the son of Satan and trains to become an exorcist to fight demons.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Action, Super Power, Supernatural\n","red"))
                print_pause(colored("Synopsis: A high school girl discovers a secret organization of super-powered individuals who serve as vigilantes.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Super Power\n","red"))
                print_pause(colored("Synopsis: A modern girl travels back in time and teams up with a half-demon to collect powerful shards.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Action, Comedy, Super Power\n","red"))
                print_pause(colored("Synopsis: A superhero who can defeat any opponent with a single punch struggles with the boredom of invincibility.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Super Power\n","red"))
                print_pause(colored("Synopsis: A group of assassins with unique weapons and abilities fights to overthrow a corrupt empire.","yellow"))
            else:
                print(colored("INVALID","grey"))  
            print_pause(colored("\n\nENJOY!!","cyan"))
#SHORT MARTIAL ART ANIME   
        elif a=='7':
            print_pause(colored("Here is a recommendation of a MARTIAL ARTS anime with less episodes:","cyan"))
            short_martialart_anime=['Afro Samurai',
                                   'Kenichi: The Mightiest Disciple" (Shijou Saikyou no Deshi Kenichi)',
                                   'Ben-To',
                                   'C: The Money of Soul and Possibility Control',
                                   'Tenjou Tenge',
                                   'Air Master',
                                   'Hajime no Ippo',
                                   'Megalo Box',
                                   'The God of High School',
                                   'Basilisk: The Kouga Ninja Scrolls'
                                ]
            ran=random.choice(short_martialart_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_martialart_anime[0]
            c=short_martialart_anime[1]
            d=short_martialart_anime[2]
            f=short_martialart_anime[3]
            g=short_martialart_anime[4]
            h=short_martialart_anime[5]
            o=short_martialart_anime[6]
            j=short_martialart_anime[7]
            k=short_martialart_anime[8]
            l=short_martialart_anime[9]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Samurai\n","red"))
                print_pause(colored('Synopsis: A warrior seeks revenge on the man who killed his father in a futuristic feudal Japan.',"yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Comedy, Martial Arts\n","red"))
                print_pause(colored("Synopsis: A bullied teen trains under six martial arts masters to protect himself and his friends.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Comedy, Martial Arts\n","red"))
                print_pause(colored("Synopsis: High school students fight in martial arts battles over discounted bento boxes.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Mystery, Super Power\n","red"))
                print_pause(colored("Synopsis: A student enters a parallel world where money and martial arts determine one's fate.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Action, Martial Arts, Super Power\n","red"))
                print_pause(colored("Synopsis: Two delinquent boys enroll in a high school known for its martial arts curriculum and face formidable opponents.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Martial Arts, Seinen\n","red"))
                print_pause(colored("Synopsis: A former gymnast uses her acrobatic skills to become a formidable street fighter.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Action, Comedy, Drama, Martial Arts, Sports\n","red"))
                print_pause(colored("Synopsis: A bullied teen discovers a passion for boxing and trains to become a champion.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Action, Sci-Fi, Sports\n","red"))
                print_pause(colored("Synopsis:  A boxer in a dystopian future uses enhanced gear to fight his way to the top of the Megalonia tournament.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Action, Fantasy, Martial Arts\n","red"))
                print_pause(colored("Synopsis: High school students compete in an epic martial arts tournament that reveals hidden powers and ancient secrets.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Action, Adventure, Historical, Martial Arts, Supernatural\n","red"))
                print_pause(colored("Synopsis: Two rival ninja clans engage in a deadly battle to determine the next shogun's successor.","yellow"))
            else:
                print(colored("INVALID","grey"))  
            print_pause(colored("\n\nENJOY!!","cyan"))
#SHORT PSYCHOLOGICAL ANIME
        elif a=='8':
            print_pause(colored("Here is a PSYCHOLOGICAL anime recommendation that has less episodes:\n","cyan"))
            short_psychological_anime=['Paranoia Agent',
                                'Death Parade',
                                'Serial Experiments Lain',
                                'Flowers of Evil" (Aku no Hana)',
                                'Another',
                                'Re',
                                'Kaiba',
                                'Texhnolyze',
                                'Welcome to the NHK',
                                'The Perfect Insider (Subete ga F ni Naru)']
            ran= random.choice(short_psychological_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_psychological_anime[0]
            c=short_psychological_anime[1]
            d=short_psychological_anime[2]
            f=short_psychological_anime[3]
            g=short_psychological_anime[4]
            h=short_psychological_anime[5]
            o=short_psychological_anime[6]
            j=short_psychological_anime[7]
            k=short_psychological_anime[8]
            l=short_psychological_anime[9]
            print("some additional information about",ran,":")
            print("\n")
            
            if ran==b:
                print_pause(colored("Sub Genre: Drama, Mystery, Psychological, Supernatural\n","red"))
                print_pause(colored("Synopsis:  A mysterious attacker known as Lil' Slugger terrorizes Tokyo, causing chaos and revealing hidden truths about his victims.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Drama, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: Souls are judged in a mysterious bar where they play games that reveal their true nature.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Dementia, Drama, Mystery, Psychological, Sci-Fi, Supernatural\n","red"))
                print_pause(colored("Synopsis:  A teenage girl delves into the virtual world, uncovering disturbing truths about reality and herself.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre:  Drama, Psychological, Romance, School\n","red"))
                print_pause(colored("Synopsis: A middle school student is blackmailed by a classmate after she discovers his darkest secret.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Horror, Mystery, Psychological, Supernatural, Thriller\n","red"))
                print_pause(colored("Synopsis: A transfer student uncovers the eerie history of his new class, where death is a constant companion.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Fantasy, Psychological\n","red"))
                print_pause(colored("Synopsis: Characters from various stories come to life and confront their creators in the real world.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Adventure, Drama, Romance, Sci-Fi, Psychological\n","red"))
                print_pause(colored("Synopsis: In a world where memories can be transferred between bodies, a man with amnesia searches for his identity.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Action, Drama, Psychological, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: In a dystopian underground city, a boxer with cybernetic limbs becomes involved in a conflict that could determine the fate of the world.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Comedy, Drama, Psychological, Romance\n","red"))
                print_pause(colored("Synopsis: A reclusive young man battles his social anxiety and delusions with the help of a mysterious girl.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Mystery, Psychological\n","red"))
                print_pause(colored("Synopsis: A professor and a student investigate a locked-room murder in a secluded research facility","yellow"))
            else:
                print(colored("INVALID","grey"))   
            print_pause(colored("\n\nENJOY!!","cyan"))

# SHORT POLICE / DETECTIVE ANIME                                #need to change
        elif a=='9': 
            print_pause(colored("Here is a DETECTIVE/POLICE anime recommendation that has less episodes:\n","cyan"))
            short_detective_anime=['Paranoia Agent (Mousou Dairinin)',
                                'Psycho-Pass',
                                'The Millionaire Detective – Balance: UNLIMITED',
                                'Hyouka',
                                'Ghost in the Shell: Stand Alone Complex',
                                'Death Note',
                                'ID: Invaded',
                                'Beautiful Bones: Sakurako’s Investigation (Sakurako-san no Ashimoto ni wa Shitai ga Umatteiru)',
                                'Rampo Kitan: Game of Laplace',
                                'Case File nº221: Kabukicho']
            ran= random.choice(short_detective_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_detective_anime[0]
            c=short_detective_anime[1]
            d=short_detective_anime[2]
            f=short_detective_anime[3]
            g=short_detective_anime[4]
            h=short_detective_anime[5]
            o=short_detective_anime[6]
            j=short_detective_anime[7]
            k=short_detective_anime[8]
            l=short_detective_anime[9]
            
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: A series of seemingly random attacks by a boy with a golden baseball bat perplexes the detectives as they uncover the dark truths behind the victims' lives.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Sci-Fi, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: In a dystopian future where a computer system dictates societal order, a police force tackles crimes by assessing individuals' psychological states.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Mystery, Comedy, Crime\n","red"))
                print_pause(colored("Synopsis: A wealthy detective with unlimited resources teams up with a justice-driven officer to solve high-profile cases in unconventional ways.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Mystery, Slice of Life, School\n","red"))
                print_pause(colored("Synopsis: A high school student with a knack for deduction joins his school's Classic Literature Club and solves various mysteries, both trivial and serious.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Sci-Fi, Cyberpunk, Mystery\n","red"))
                print_pause(colored("Synopsis: In a future where cybernetic enhancements are common, a special police unit investigates cyber-crimes and terrorist activities.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Mystery, Supernatural, Thriller\n","red"))
                print_pause(colored("Synopsis:  A high school student discovers a supernatural notebook that allows him to kill anyone by writing their name, leading to a high-stakes cat-and-mouse game with a brilliant detective.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Mystery, Sci-Fi, Psychological\n","red"))
                print_pause(colored("Synopsis:  A detective with a tragic past dives into the minds of killers to solve crimes in a futuristic setting.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Mystery, Slice of Life, Thriller\n","red"))
                print_pause(colored("Synopsis: A brilliant osteologist with a fascination for bones teams up with a high school student to solve mysterious cases involving skeletal remains.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Mystery, Psychological, Horror\n","red"))
                print_pause(colored("Synopsis: Inspired by the works of Edogawa Rampo, a middle school student and a genius detective solve bizarre and gruesome crimes.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre:  Mystery, Drama\n","red"))
                print_pause(colored("Synopsis: Set in Tokyo's red-light district, a group of detectives, each with unique skills and backgrounds, tackle various criminal cases and personal challenges.","yellow"))
            else:
                print(colored("INVALID","grey"))  
            print_pause(colored("\n\nENJOY!!","cyan")) 
    
    
    #SHORT THRILLER ANIME
        if a=='10':
            print_pause(colored("Here is a THRILLER anime recommendation that has less episodes:\n","cyan"))
            short_thriller_anime=['Another',
                                'Paranoia Agent (Mousou Dairinin)',
                                'Terror in Resonance (Zankyou no Terror)',
                                'Devilman Crybaby',
                                'Elfen Lied',
                                'Shiki',
                                'Highschool of the Dead',
                                'The Promised Neverland (Yakusoku no Neverland)',
                                'The Future Diary (Mirai Nikki)',
                                'Higurashi: When They Cry (Higurashi no Naku Koro ni)']
            ran= random.choice(short_thriller_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_thriller_anime[0]
            c=short_thriller_anime[1]
            d=short_thriller_anime[2]
            f=short_thriller_anime[3]
            g=short_thriller_anime[4]
            h=short_thriller_anime[5]
            o=short_thriller_anime[6]
            j=short_thriller_anime[7]
            k=short_thriller_anime[8]
            l=short_thriller_anime[9]
            
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Horror, Mystery\n","red"))
                print_pause(colored('Synopsis:  A transfer student and his classmates try to unravel the mystery behind a series of gruesome deaths linked to a cursed class.',"yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Psychological, Mystery\n","red"))
                print_pause(colored("Synopsis:  A series of bizarre assaults by a young boy with a golden baseball bat unearth dark secrets among the victims.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre:  Psychological, Mystery\n","red"))
                print_pause(colored("Synopsis:  Two teenage terrorists orchestrate bombings in Tokyo and challenge the police with cryptic clues.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Horror\n","red"))
                print_pause(colored("Synopsis: A teenager gains the powers of a demon to protect humanity from an apocalyptic war between demons and humans.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Horror, Psychological\n","red"))
                print_pause(colored("Synopsis: A mutant girl with deadly telekinetic powers escapes from a lab and brings chaos to those around her.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Horror, Mystery, Supernatural\n","red"))
                print_pause(colored("Synopsis:  A small village is plagued by mysterious deaths, leading the local doctor and a monk to uncover a terrifying secret about the new residents.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Action, Horror, Supernatural\n","red"))
                print_pause(colored("Synopsis: A group of high schoo","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Mystery, Horror, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: Orphans discover the dark secret behind their idyllic orphanage and plan a daring escape.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Psychological, Mystery, Thriller\n","red"))
                print_pause(colored("Synopsis: A survival game involving future-predicting diaries pits twelve participants against each other in a deadly battle.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Horror, Mystery, Psychological\n","red"))
                print_pause(colored("Synopsis:A series of mysterious and gruesome events plague a rural village, leading to repeated cycles of murder and paranoia.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))   
            print_pause(colored("\n\nENJOY!!","cyan")) 
        
        
        elif a=='11':
            print_pause(colored("Here is a SUPERNATURAL anime recommendation that has less episodes:\n","cyan"))
            short_supernatural_anime=["Natsume's Book of Friends (Natsume Yuujinchou)",
                                'Blue Exorcist (Ao no Exorcist)d',
                                'Durarara!!',
                                'Beyond the Boundary (Kyoukai no Kanata)',
                                'Mekakucity Actors',
                                'Tokyo Ravens',
                                'Inu x Boku SS',
                                'Dusk Maiden of Amnesia (Tasogare Otome x Amnesia)',
                                'Fate/Stay Night: Unlimited Blade Works',
                                ' Kamisama Dolls']
            ran= random.choice(short_supernatural_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=short_supernatural_anime[0]
            c=short_supernatural_anime[1]
            d=short_supernatural_anime[2]
            f=short_supernatural_anime[3]
            g=short_supernatural_anime[4]
            h=short_supernatural_anime[5]
            o=short_supernatural_anime[6]
            j=short_supernatural_anime[7]
            k=short_supernatural_anime[8]
            l=short_supernatural_anime[9]
            
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Slice of Life, Drama\n","red"))
                print_pause(colored('Synopsis: A boy who can see spirits inherits a book that contains the names of spirits bound by his grandmother, and he seeks to return their names and grant them freedom.',"yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Fantasy\n","red"))
                print_pause(colored("Synopsis: The son of Satan decides to become an exorcist to fight against his biological father’s forces.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Mystery\n","red"))
                print_pause(colored("Synopsis: In the district of Ikebukuro, a headless rider and various colorful characters navigate the intertwining supernatural events.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Fantasy, Romance\n","red"))
                print_pause(colored("Synopsis: A high school student with a curse that prevents him from dying meets a spirit warrior girl who must kill evil spirits.","yellow"))
            elif ran==g:
                print_pause(colored("Sub Genre: Sci-Fi, Supernatural\n","red"))
                print_pause(colored("Synopsis:  A group of teenagers with special powers come together to unravel the mysteries behind their abilities.","yellow"))
            elif ran==h:
                print_pause(colored("Sub Genre: Action, Romance\n","red"))
                print_pause(colored("Synopsis: A boy from a prestigious onmyouji family must protect Tokyo from dark supernatural forces.","yellow"))
            elif ran==o:
                print_pause(colored("Sub Genre: Romance, Comedy\n","red"))
                print_pause(colored("Synopsis: A girl with supernatural lineage is protected by a bodyguard who has a past connection with her.","yellow"))
            elif ran==j:
                print_pause(colored("Sub Genre: Horror, Mystery, Romance\n","red"))
                print_pause(colored("Synopsis: A high school boy joins a supernatural investigation club and meets the ghost of a girl who has lost her memories.","yellow"))
            elif ran==k:
                print_pause(colored("Sub Genre: Action, Fantasy\n","red"))
                print_pause(colored("Synopsis: Seven mages summon heroic spirits to battle in a secret war for the Holy Grail, a powerful artifact that grants wishes.","yellow"))
            elif ran==l:
                print_pause(colored("Sub Genre: Action, Drama\n","red"))
                print_pause(colored("Synopsis:A university student gets involved in a conflict involving powerful ancient gods controlled by humans.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))   
            print_pause(colored("\n\nENJOY!!","cyan"))

    
    elif srl=='long':
        print_pause(colored("enter the number of the corresponding genre\n","cyan"))
        a=input()

        # LONG SHONEN ANIME
        if a == '1':
            print_pause(colored("Here is a SHONEN anime recommendation that has more episodes:\n", "cyan"))

            long_shonen_anime = [
                'Naruto',
                'One Piece',
                'Bleach',
                'Dragon Ball Z',
                'Hunter x Hunter (2011)',
                'Black Clover',
                'Fairy Tail',
                'My Hero Academia',
                'D.Gray-man',
                'Gintama',
                'JoJo\'s Bizarre Adventure'
            ]

            ran = random.choice(long_shonen_anime)
            print_pause(colored(ran, "blue"))
            print("\n")

            b = long_shonen_anime[0]
            c = long_shonen_anime[1]
            d = long_shonen_anime[2]
            e = long_shonen_anime[3]
            f = long_shonen_anime[4]
            g = long_shonen_anime[5]
            h = long_shonen_anime[6]
            o = long_shonen_anime[7]
            j = long_shonen_anime[8]
            k = long_shonen_anime[9]
            l = long_shonen_anime[10]

            print("some additional information about", ran, ":")
            print("\n")

            if ran == b:
                print_pause(colored("Sub Genre: Action, Adventure, Martial Arts, Super Power\n", "red"))
                print_pause(colored("Synopsis: Naruto Uzumaki, a young ninja who dreams of becoming the strongest ninja and the leader of his village, faces powerful enemies while seeking recognition and friendship.", "yellow"))

            elif ran == c:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Super Power\n", "red"))
                print_pause(colored("Synopsis: Monkey D. Luffy and his pirate crew travel across dangerous seas in search of the legendary treasure known as One Piece, encountering powerful enemies and unforgettable adventures.", "yellow"))

            elif ran == d:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n", "red"))
                print_pause(colored("Synopsis: Ichigo Kurosaki, a teenager who can see spirits, gains the powers of a Soul Reaper and protects humans from evil spirits while uncovering secrets about the spiritual world.", "yellow"))

            elif ran == e:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Martial Arts\n", "red"))
                print_pause(colored("Synopsis: Goku and his friends defend Earth and the universe against increasingly powerful enemies while discovering new transformations and abilities.", "yellow"))

            elif ran == f:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n", "red"))
                print_pause(colored("Synopsis: Gon Freecss sets out to become a Hunter and find his missing father. Along the way, he meets friends and faces dangerous challenges that test his strength and determination.", "yellow"))

            elif ran == g:
                print_pause(colored("Sub Genre: Action, Fantasy, Magic\n", "red"))
                print_pause(colored("Synopsis: Asta, a boy born without magic in a world where magic is everything, dreams of becoming the Wizard King and works hard to prove that determination can overcome any limitation.", "yellow"))

            elif ran == h:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Magic\n", "red"))
                print_pause(colored("Synopsis: Lucy Heartfilia joins the Fairy Tail wizard guild and embarks on magical adventures with Natsu and their friends while completing missions and facing powerful enemies.", "yellow"))

            elif ran == o:
                print_pause(colored("Sub Genre: Action, School, Super Power\n", "red"))
                print_pause(colored("Synopsis: In a world where most people possess superpowers called Quirks, Izuku Midoriya dreams of becoming a great hero despite being born without one.", "yellow"))

            elif ran == j:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n", "red"))
                print_pause(colored("Synopsis: Allen Walker joins the Black Order, an organization of exorcists fighting against the Millennium Earl and his army of demonic weapons known as Akuma.", "yellow"))

            elif ran == k:
                print_pause(colored("Sub Genre: Action, Comedy, Historical, Sci-Fi\n", "red"))
                print_pause(colored("Synopsis: In an alternate version of Edo-era Japan, Gintoki Sakata and his friends take on unusual jobs while dealing with aliens, samurai conflicts, and hilarious everyday situations.", "yellow"))

            elif ran == l:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n", "red"))
                print_pause(colored("Synopsis: JoJo's Bizarre Adventure follows the Joestar family across generations as they battle supernatural enemies using unique abilities and extraordinary fighting techniques.", "yellow"))

            else:
                print_pause(colored("INVALID", "grey"))

            print_pause(colored("\n\nENJOY!!", "cyan"))



        elif a=='2':
            print_pause(colored("Here is a FANTASY anime recommendation that has more episodes:\n","cyan"))
            long_fantasy_anime=[
                'Inuyasha',
                'The Twelve Kingdoms',
                'Magi: The Labyrinth of Magic',
                'Fairy Tail',
                'The Seven Deadly Sins'
            ]
            ran=random.choice(long_fantasy_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_fantasy_anime[0]
            c=long_fantasy_anime[1]
            d=long_fantasy_anime[2]
            e=long_fantasy_anime[3]
            f=long_fantasy_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Kagome, a modern-day schoolgirl, is transported to the past and joins the half-demon Inuyasha on a quest to collect the shards of a powerful jewel.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Adventure, Drama, Fantasy\n","red"))
                print_pause(colored("Synopsis: Yoko Nakajima is transported to another world where she must learn to survive and discover her place among kingdoms ruled by supernatural beings.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Aladdin travels across a world filled with mysterious dungeons and powerful Djinn, meeting allies and uncovering the secrets of the Magi.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Magic\n","red"))
                print_pause(colored("Synopsis: Lucy joins the Fairy Tail wizard guild and takes on missions with Natsu and their friends, facing powerful enemies along the way.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Princess Elizabeth searches for the legendary Seven Deadly Sins to help reclaim her kingdom from the corrupt Holy Knights.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='3':
            print_pause(colored("Here is a ACTION anime recommendation that has more episodes:\n","cyan"))
            long_action_anime=[
                'Naruto Shippuden',
                'One Piece',
                'Bleach',
                'Dragon Ball Z',
                'Black Clover'
            ]
            ran=random.choice(long_action_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_action_anime[0]
            c=long_action_anime[1]
            d=long_action_anime[2]
            e=long_action_anime[3]
            f=long_action_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Martial Arts\n","red"))
                print_pause(colored("Synopsis: Naruto returns to his village after years of training and faces dangerous enemies while trying to rescue his friend Sasuke and protect the people he cares about.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Monkey D. Luffy and his pirate crew travel across dangerous seas in search of the legendary treasure known as One Piece.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n","red"))
                print_pause(colored("Synopsis: Ichigo Kurosaki becomes a Soul Reaper and protects the living world from dangerous spirits while discovering the secrets of the Soul Society.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Adventure, Martial Arts\n","red"))
                print_pause(colored("Synopsis: Goku and his friends defend Earth and the universe against powerful enemies, pushing their abilities beyond their limits.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Asta, born without magic, works hard to become the Wizard King in a world where magical ability determines a person's status.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='4':
            print_pause(colored("Here is a COMEDY anime recommendation that has more episodes:\n","cyan"))
            long_comedy_anime=[
                'Gintama',
                'KochiKame',
                'Doraemon',
                'Crayon Shin-chan',
                'The Disastrous Life of Saiki K.'
            ]
            ran=random.choice(long_comedy_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_comedy_anime[0]
            c=long_comedy_anime[1]
            d=long_comedy_anime[2]
            e=long_comedy_anime[3]
            f=long_comedy_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Comedy, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: In an alternate Edo-era Japan occupied by aliens, Gintoki Sakata and his friends take on unusual jobs and get caught in hilarious adventures.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Comedy, Police, Slice of Life\n","red"))
                print_pause(colored("Synopsis: The daily life of a reckless police officer, Kankichi Ryotsu, is filled with unusual schemes and comical situations at the local police station.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Comedy, Sci-Fi, Family\n","red"))
                print_pause(colored("Synopsis: A robotic cat from the future helps Nobita with futuristic gadgets, but their adventures often lead to unexpected trouble.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Comedy, Slice of Life\n","red"))
                print_pause(colored("Synopsis: Shinnosuke Nohara, a mischievous young boy, creates funny situations for his family, friends, and everyone around him.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Comedy, School, Supernatural\n","red"))
                print_pause(colored("Synopsis: Kusuo Saiki has extraordinary psychic powers and constantly tries to live an ordinary life while avoiding attention.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='5':
            print_pause(colored("Here is a ADVENTURE anime recommendation that has more episodes:\n","cyan"))
            long_adventure_anime=[
                'One Piece',
                'Hunter x Hunter (2011)',
                'Dragon Ball',
                'Inuyasha',
                'Magi: The Kingdom of Magic'
            ]
            ran=random.choice(long_adventure_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_adventure_anime[0]
            c=long_adventure_anime[1]
            d=long_adventure_anime[2]
            e=long_adventure_anime[3]
            f=long_adventure_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Monkey D. Luffy gathers a pirate crew and explores the Grand Line in search of the legendary treasure called One Piece.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Gon Freecss becomes a Hunter and travels across dangerous places to find his father, making friends and facing difficult challenges.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Adventure, Comedy\n","red"))
                print_pause(colored("Synopsis: Young Goku sets out on adventures with Bulma to find the seven Dragon Balls, encountering new friends and powerful opponents.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Kagome travels to feudal Japan and joins Inuyasha on a journey to recover the scattered shards of the Shikon Jewel.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy\n","red"))
                print_pause(colored("Synopsis: Aladdin and his friends travel through different kingdoms, facing challenges and learning about the world's mysterious magical powers.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='6':
            print_pause(colored("Here is a SUPER POWER anime recommendation that has more episodes:\n","cyan"))
            long_superpower_anime=[
                'My Hero Academia',
                'One Punch Man',
                'A Certain Scientific Railgun',
                "JoJo's Bizarre Adventure",
                'Mob Psycho 100'
            ]
            ran=random.choice(long_superpower_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_superpower_anime[0]
            c=long_superpower_anime[1]
            d=long_superpower_anime[2]
            e=long_superpower_anime[3]
            f=long_superpower_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, School, Super Power\n","red"))
                print_pause(colored("Synopsis: Izuku Midoriya dreams of becoming a hero in a world where most people have special abilities called Quirks, despite being born without one.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Comedy, Super Power\n","red"))
                print_pause(colored("Synopsis: Saitama can defeat any opponent with a single punch, but his overwhelming strength leaves him searching for a meaningful challenge.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Sci-Fi, Super Power\n","red"))
                print_pause(colored("Synopsis: Mikoto Misaka, one of the strongest espers in Academy City, investigates strange incidents involving the city's advanced technology and superpowers.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Adventure, Super Power\n","red"))
                print_pause(colored("Synopsis: The Joestar family battles supernatural enemies across generations using unique powers and extraordinary fighting techniques.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Comedy, Supernatural\n","red"))
                print_pause(colored("Synopsis: Shigeo 'Mob' Kageyama is a powerful psychic who tries to live a normal life while learning to understand and control his emotions.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='7':
            print_pause(colored("Here is a MARTIAL ARTS anime recommendation that has more episodes:\n","cyan"))
            long_martialarts_anime=[
                'Dragon Ball Z',
                'Hajime no Ippo',
                'Kenichi: The Mightiest Disciple',
                'Ranma 1/2',
                'Yu Yu Hakusho'
            ]
            ran=random.choice(long_martialarts_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_martialarts_anime[0]
            c=long_martialarts_anime[1]
            d=long_martialarts_anime[2]
            e=long_martialarts_anime[3]
            f=long_martialarts_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Martial Arts\n","red"))
                print_pause(colored("Synopsis: Goku and his friends train and fight powerful opponents to protect Earth and the universe.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Sports, Drama, Martial Arts\n","red"))
                print_pause(colored("Synopsis: Ippo Makunouchi discovers boxing after being bullied and trains hard to become a professional boxer.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Comedy, Martial Arts\n","red"))
                print_pause(colored("Synopsis: A bullied high school student trains under several martial arts masters and gradually becomes a skilled fighter.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Comedy, Martial Arts\n","red"))
                print_pause(colored("Synopsis: Ranma Saotome studies martial arts and deals with a strange curse that changes his body whenever he is splashed with cold water.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Adventure, Martial Arts, Supernatural\n","red"))
                print_pause(colored("Synopsis: Yusuke Urameshi becomes a Spirit Detective and battles dangerous supernatural beings while protecting the human world.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='8':
            print_pause(colored("Here is a PSYCHOLOGICAL anime recommendation that has more episodes:\n","cyan"))
            long_psychological_anime=[
                'Monster',
                'Legend of the Galactic Heroes',
                'Death Note',
                'Kaiji: Ultimate Survivor',
                'Psycho-Pass'
            ]
            ran=random.choice(long_psychological_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_psychological_anime[0]
            c=long_psychological_anime[1]
            d=long_psychological_anime[2]
            e=long_psychological_anime[3]
            f=long_psychological_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Drama, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: Dr. Kenzo Tenma saves a young boy's life, but years later discovers that the boy has become a dangerous criminal.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Drama, Sci-Fi, Psychological\n","red"))
                print_pause(colored("Synopsis: Two brilliant military leaders from opposing sides face each other in a long war while questioning politics, power, and the cost of conflict.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Mystery, Psychological, Supernatural, Thriller\n","red"))
                print_pause(colored("Synopsis: Light Yagami discovers a notebook that can kill anyone whose name is written in it, leading to a battle of intelligence with detective L.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Drama, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: Kaiji is forced into dangerous gambling games where he must use strategy and courage to survive and escape debt.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Crime, Psychological, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: In a future society, a system measures people's likelihood of committing crimes, and inspectors must decide how justice should be carried out.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='9':
            print_pause(colored("Here is a POLICE/DETECTIVE anime recommendation that has more episodes:\n","cyan"))
            long_policedetective_anime=[
                'Detective Conan',
                'Psycho-Pass',
                'Lupin the Third',
                'Kindaichi Case Files',
                'Ghost in the Shell: Stand Alone Complex'
            ]
            ran=random.choice(long_policedetective_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_policedetective_anime[0]
            c=long_policedetective_anime[1]
            d=long_policedetective_anime[2]
            e=long_policedetective_anime[3]
            f=long_policedetective_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Adventure, Comedy, Mystery\n","red"))
                print_pause(colored("Synopsis: High school detective Shinichi Kudo is transformed into a child and secretly solves crimes while searching for the organization responsible.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Crime, Mystery, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: Police officers use a system that measures people's mental states to identify and stop potential criminals in a controlled future society.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Action, Adventure, Comedy, Mystery\n","red"))
                print_pause(colored("Synopsis: Master thief Arsène Lupin III travels around the world with his companions, pulling off daring heists while being chased by Inspector Zenigata.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Mystery, Detective, Thriller\n","red"))
                print_pause(colored("Synopsis: High school student Hajime Kindaichi uses his sharp reasoning skills to solve complicated murders and mysterious cases.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Crime, Sci-Fi\n","red"))
                print_pause(colored("Synopsis: Major Motoko Kusanagi and Public Security Section 9 investigate cybercrime and complex threats in a technologically advanced future.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='10':
            print_pause(colored("Here is a THRILLER anime recommendation that has more episodes:\n","cyan"))
            long_thriller_anime=[
                'Monster',
                'Higurashi: When They Cry',
                'The Promised Neverland',
                'Death Note',
                'Future Diary'
            ]
            ran=random.choice(long_thriller_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_thriller_anime[0]
            c=long_thriller_anime[1]
            d=long_thriller_anime[2]
            e=long_thriller_anime[3]
            f=long_thriller_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Drama, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: A doctor searches for a former patient who has become a serial killer, uncovering a disturbing chain of events.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Horror, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: A group of friends in a quiet village become connected to a series of mysterious deaths and disturbing events that repeat over time.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Dark Fantasy, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: Children living in a seemingly perfect orphanage discover a horrifying secret and plan to escape.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Mystery, Psychological, Supernatural, Thriller\n","red"))
                print_pause(colored("Synopsis: A student uses a mysterious notebook to judge criminals, while a brilliant detective tries to uncover his identity.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Action, Mystery, Psychological, Thriller\n","red"))
                print_pause(colored("Synopsis: A teenager becomes part of a deadly survival game in which participants use diaries that predict the future.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        elif a=='11':
            print_pause(colored("Here is a SUPERNATURAL anime recommendation that has more episodes:\n","cyan"))
            long_supernatural_anime=[
                'Inuyasha',
                'Yu Yu Hakusho',
                "Natsume's Book of Friends",
                'Bleach',
                'GeGeGe no Kitaro'
            ]
            ran=random.choice(long_supernatural_anime)
            print_pause(colored(ran,"blue"))
            print("\n")
            b=long_supernatural_anime[0]
            c=long_supernatural_anime[1]
            d=long_supernatural_anime[2]
            e=long_supernatural_anime[3]
            f=long_supernatural_anime[4]
            print("some additional information about",ran,":")
            print("\n")
            if ran==b:
                print_pause(colored("Sub Genre: Action, Adventure, Fantasy, Supernatural\n","red"))
                print_pause(colored("Synopsis: Kagome travels to feudal Japan and joins the half-demon Inuyasha on a quest involving a powerful jewel and supernatural enemies.","yellow"))
            elif ran==c:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n","red"))
                print_pause(colored("Synopsis: After an unexpected death, Yusuke becomes a Spirit Detective and investigates supernatural cases involving dangerous demons.","yellow"))
            elif ran==d:
                print_pause(colored("Sub Genre: Drama, Fantasy, Slice of Life, Supernatural\n","red"))
                print_pause(colored("Synopsis: A boy who can see spirits inherits a book containing the names of spirits and tries to return their names and free them.","yellow"))
            elif ran==e:
                print_pause(colored("Sub Genre: Action, Adventure, Supernatural\n","red"))
                print_pause(colored("Synopsis: Ichigo Kurosaki gains the powers of a Soul Reaper and protects humans from evil spirits while uncovering the secrets of the spirit world.","yellow"))
            elif ran==f:
                print_pause(colored("Sub Genre: Comedy, Horror, Supernatural\n","red"))
                print_pause(colored("Synopsis: Kitaro, a young yokai, helps maintain peace between humans and supernatural creatures while dealing with strange cases.","yellow"))
            else:
                print_pause(colored("INVALID","grey"))
            print_pause(colored("\n\nENJOY!!","cyan"))

        else:
            print_pause(colored("INVALID","grey"))

print_pause(colored("Hey What's your name?\n","cyan"))
name=input()
res=["yes","no","skip"]
print("Hello",name,"Would you like an anime recommendation?")
ans=input().lower()
if ans==res[0]:
    print_pause(colored("Alright! But before we start, is it your first time watching anime?\n","cyan"))
    ans1=input().lower()
    if ans1==res[0] :
        print_pause(colored("Oh well,it's good that you want to start watching anime!\n","cyan"))
        print_pause(colored("Since you are new would you like to learn more about the world of anime(yes,skip)?\n","cyan"))
        ans2=input()
        if ans2==res[0] :
            print_pause(colored("1. Anime is a Japanese animated art form known for its diverse genres and captivating storytelling.\n","magenta"))
            print_pause(colored("2. It features distinctive art styles, often characterized by colorful visuals and expressive characters.\n","magenta"))
            print_pause(colored("3. Anime explores a wide range of themes, from action-packed adventures to profound reflections on life and humanity.\n","magenta"))
            print_pause(colored("4. With a global fanbase, anime's influence extends beyond Japan, shaping pop culture and inspiring creativity worldwide\n","magenta"))
            print_pause(colored("5. Whether through its imaginative worlds or compelling characters, anime offers an immersive and entertaining experience for viewers of all ages.\n","magenta"))
            print_pause(colored("alright then! lets get started\n","light_green"))
            recom()
        if ans2== res[2] :
            print_pause(colored("alright,then lets get started!\n","light_green"))
            recom()
            
    elif ans1==res[1]:
        print_pause(colored("Nice! then you must have wanted to watch something new\n","cyan"))
        ans1=input().lower()
        if ans1==res[0] :
            print_pause(colored("okay! How long has it been since you started watching anime?\n","cyan"))
            ans2=input().lower()
            print("Oh wow!",ans2,"!")
        print_pause(colored("Okay then lets get started!\n","light_green"))
        recom()  
else:
    print_pause(colored("Okay then...see you next time!","light_cyan"))



    
