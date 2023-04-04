from faker import Faker

monkey = Faker("pl_PL")


class Human:
    def __init__(self, first_name, last_name, firm, position, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.firm = firm
        self.position = position
        self.mail = mail
        pass


# using Fake Name Generator to create data
human_1 = Human(
    first_name="Dobrogost",
    last_name="Wieczorek",
    firm="Local account executive",
    position="Erol's",
    mail="DobrogostWieczorek@jourrapide.com",
)
human_2 = Human(
    first_name="Wioletta",
    last_name="Nowak",
    firm="Earl Abel's",
    position="Nurse specialist",
    mail="WiolettaNowak@rhyta.com",
)
human_3 = Human(
    first_name="Dorota",
    last_name="Czerwinska",
    firm="Builders Emporium",
    position="Apartment leasing agent",
    mail="DorotaCzerwinska@dayrep.com",
)
human_4 = Human(
    first_name="Klemens",
    last_name="Kowalczyk",
    firm="Starship Tapes & Records",
    position="Toolmaker",
    mail="KlemensKowalczyk@dayrep.com",
)
human_5 = Human(
    first_name="Janusz",
    last_name="Kwiatkowski",
    firm="Handy Andy",
    position="Small engine mechanic",
    mail="JanuszKwiatkowski@dayrep.com",
)
business_card_holder = [human_1, human_2, human_3, human_4, human_5]
[print(vars(human)) for human in business_card_holder]

# using Faker to create data for monkeys (allmost like humans) ;)
monkey_list = []
for _ in range(4):
    monkey_list.append(
        Human(
            first_name=monkey.first_name(),
            last_name=monkey.last_name(),
            firm=monkey.company(),
            position=monkey.job(),
            mail=monkey.email(),
        )
    )

[print(vars(monkeys)) for monkeys in monkey_list]
