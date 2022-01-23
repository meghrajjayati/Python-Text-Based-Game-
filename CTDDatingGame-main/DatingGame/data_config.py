class data_config():

    def __init__(self):
        self.colors = {
                        'white':    "\033[1;37m",
                        'yellow':   "\033[1;33m",
                        'green':    "\033[1;32m",
                        'blue':     "\033[1;34m",
                        'cyan':     "\033[1;36m",
                        'red':      "\033[1;31m",
                        'magenta':  "\033[1;35m",
                        'black':      "\033[1;30m",
                        'darkwhite':  "\033[0;37m",
                        'darkyellow': "\033[0;33m",
                        'darkgreen':  "\033[0;32m",
                        'darkblue':   "\033[0;34m",
                        'darkcyan':   "\033[0;36m",
                        'darkred':    "\033[0;31m",
                        'darkmagenta':"\033[0;35m",
                        'darkblack':  "\033[0;30m",
                        'off':        "\033[0;0m"
                    }
        self.player_profile_questions =  {
                                            "gender" : ['What is your gender?\n\n[M] Male\n[F] Female\n\nChoice: ', ['M','F']],
                                            "partner_gender" : ['Who are you interested in?\n\n[M] Male Partner\n[F] Female Partner\n\nChoice: ', ['M','F']],
                                            "name" : "What's your Name?\n\nName: ",
                                            "age" : "What's your Age?\n\nAge: "
                                        }

        self.partner_preference_questions = [
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Athletic\n[2] Artistic\n\nChoice: ", ['1','2']],
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Introvert\n[2] Extrovert\n\nChoice: ", ['1','2']],
                                                ["What do you prefer more in a partner?\nMy partner has to be:\n\n[1] Adventurous\n[2] Conservative\n\nChoice: ",['1','2']]
                                            ]

        self.lose_scenes =  [
                                "Unfortunately, _partner_ is not interested in hanging with you anymore… Game Over",
                                "Rejection hurts, and you hurt _partner_! There are no second chances in life... Game over",
                                "_partner_: Sorry.. but I'm already married. K THX BYE_br_Ouch.. Game over",
                                "_partner_: Sorry.. but I'm already married. K THX BYE_br_Ouch.. Game over",
                                "_partner_: Sorry.. You're not really my type.._br_Game over",
                                "_partner_: It's not you, it's me.. Actually.. It's not me. It's you!_br_Game over",
                                "After trying to contact _partner_ for several days, you realized _partner_ has blocked you._br_Too bad.. Game Over.",
                            ]

        self.win_scenes =  {
                                        1 : "That was fun texting _partner_!\nGet ready now for your big date with _partner_!!\nAll the best _player_!!",
                                        2 : "OMG!!! That was a pretty cool date!! \nNow it's time for your big final date with _partner_!!\nGood Luck _player_!!!!",
                                        3 : "Seems like you and _partner_ will be going on more dates together!!\nThings are magical with you two!\nBoth of you are a match made in heaven!!"
                                    }

        self.list_of_all_types = [['Athletic', 'Artistic'], 
                    ['Introvert','Extrovert'], 
                    ['Adventurous','Conservative']]

        self.list_of_jobs = ['Accountant', 
                    'Social worker', 
                    'Computer Scientist', 
                    'Teacher', 
                    'Sales manager', 
                    'Architect', 
                    'Research scientist', 
                    'Entreprenuer', 
                    'Doctor', 
                    'Nurse', 
                    'Cafe Owner', 
                    'Model', 
                    'Dentist',
                    "Interior Designer",
                    "Engineer",
                    "Influencer",
                    "Freelance Photographer"]
                    
        self.list_of_male_names = ['Justin', 
                        'Xavier', 
                        'Damien',
                        'Adrian',
                        'Ryan',
                        'Nicholas',
                        'Alex',
                        'Joshua',
                        'De Ren',
                        'Joseph',
                        'Zi Long',
                        'Wei Jie',
                        'Karthik',
                        'Muhammad',
                        'Danial',
                        'Ahmad',
                        'Rohit',
                        'Sean',
                        'Michael',
                        'Wen Hao',
                        'Zhen Rong',
                        'Isaac',
                        'Hasrul',
                        'Eric',
                        'Ian',
                        'Christopher']

        self.list_of_female_names = ['Melody',
                            'Melodie',
                            'Hui Min',
                            'Rachel',
                            'Jia Wen',
                            'Jasmine',
                            'Michelle',
                            'Ashley',
                            'Jayati',
                            'Maya',
                            'Nichole',
                            'Sarah',
                            'Atika',
                            'Anyana',
                            'Jing Yi',
                            'Grace',
                            'Jing Wen',
                            'Emily',
                            'Mei ling',
                            'Joyce',
                            'Samatha',
                            'Isabelle',
                            'Suraya',
                            'Trishna']

        self.list_of_male_pickup_lines = ["malepickupline1","malepickupline2","malepickupline3"]  # Melodee fill this in!
        self.list_of_female_pickup_lines = ["femalepickupline1","femalepickupline2","femalepickupline3"]  # Melodee fill this in!

        self.plotline = open('game_story.json', 'r').read()
