from random import randint, choice
def story_gen():
    hra = {
    0: { # FORTNITE
        "She/her": {
            "start": ["Dropnula v Tilted Towers.", "Dropnula v Loot Laku.", "Dropnula ve Wailing Woods.", "Dropnula v Paradise Palms.", "Dropnula v Dusty Divot.", "Dropnula ve Snobby Shores."],
            "konec": ["Mezitím co těžila resources tak dostala Shotgunou od hráče co se nenápadně dostal za ní.", "Viděla droplej loot kterej se pokusila sebrat ale mezitím dostala headshot od hráče se Sniper rifelkou.", "Musela jít AFK tak ji zabil NoSkin s krumpáčem.", "Stavěla ve velké výšce ale náhle ji došli resources a spadnula z moc velké výšky.", "Pokusila se střelit z Rocket launcheru když náhle se před ni postavila zeď takže se zabila vlastní explozí.", "Dostala hned ban za to že řekla N-Slovíčko. "]
        },
        "He/him": {
            "start": ["Dropnul v Tilted Towers.", "Dropnul v Loot Laku.", "Dropnul ve Wailing Woods.", "Dropnul v Paradise Palms.", "Dropnul v Dusty Divot.", "Dropnul ve Snobby Shores."],
            "konec": ["Mezitím co těžil resources tak dostal Shotgunou od hráče co se nenápadně dostal za něj.", "Viděl droplej loot kterej se pokusil sebrat ale mezitím dostal headshot od hráče se Sniper rifelkou.", "Musel jít AFK tak ho zabil NoSkin s krumpáčem.", "Stavěl ve velké výšce ale náhle mu došli resources a spadnul z moc velké výšky.", "Pokusil se střelit z Rocket launcheru když náhle se před něj postavila zeď takže se zabil vlastní explozí.", "Dostal hned ban za to že řekl N-Slovíčko."],
        },
    },
    1: { # TEAM FORTRESS
        "She/her": {
            "start": ["Vybrala si za postavu Heavyho.", "Vybrala si za postavu Medica.", "Vybrala si za postavu Demomana.", "Vybrala si za postavu Scouta.", "Vybrala si za postavu Engineera.", "Vybrala si za postavu Spye.", "Vybrala si za postavu Snipera.", "Vybrala si za postavu Pyra.", "Vybrala si za postavu Soldiera."],
            "konec": ["Hned co vylezila ze spawnu dostala headshot od Snipera.", "Málem sebrala kufřík ale zabila ji Sentry nest který ten kufřík chránil.", "Snažila se zabrat Control Point ale nevšimnula si že nepřátelský Demoman na něj dal Stickybomby.", "Mezitím co se snažila tlačit bombu dostala nožem do zad od nepřátelského Spye.", "Málem začala dominovat nepřátelského Hoovyho ale dostala od Scouta Fish Kill a byla ztrapňena před celým týmem. "]
        },
        "He/him": {
            "start": ["Vybral si za postavu Heavyho.", "Vybral si za postavu Medica.", "Vybral si za postavu Demomana.", "Vybral si za postavu Scouta.", "Vybral si za postavu Engineera.", "Vybral si za postavu Spye. ""Vybral si za postavu Snipera.", "Vybral si za postavu Pyra.", "Vybral si za postavu Soldiera."],
            "konec": ["Hned co vylezil ze spawnu dostal headshot od Snipera.", "Málem sebral kufřík ale zabil ho Sentry nest který ten kufřík chránil.", "Snažil se zabrat Control Point ale nevšimnul si že nepřátelský Demoman na něj dal Stickybomby.", "Mezitím co se snažil tlačit bombu dostal nožem do zad od nepřátelského Spye.", "Málem začal dominovat nepřátelského Hoovyho ale dostal od Scouta Fish Kill a byl ztrapňen před celým týmem. "]
        },
    },
    2: { # CELESTE
        "She/her": {
            "start": ["Začala skákat v Forsaken City","Začala skákat v Old Site","Začala skákat v Celestial Resortu","Začala skákat v Golden Ridge","Začala skákat v Mirror Temple","Začala skákat v Reflection","Začala skákat v Summitu","Začala skákat v Core","Začala skákat v Farewellu"],
            "konec": ["a narazila na Badeline, ta ji brutálně zavraždila.","a narazila na Badeline, měli horký sex","ihned spadla do ostnů a zemřela","a úspěšně tuto kapitolu dokončila, může jít dál!","a udělala velký skok, avšak ji nedošlo že nemá doplněné dashe a spadla do díry.","a udělala velký skok a přežila. "]
        },
        "He/him": {
            "start": ["Začal skákat v Forsaken City","Začal skákat v Old Site","Začal skákat v Celestial Resortu","Začal skákat v Golden Ridge","Začal skákat v Mirror Temple","Začal skákat v Reflection","Začal skákat v Summitu","Začal skákat v Core","Začal skákat v Farewellu"],
            "konec": ["a narazil na Badeline, ta ho brutálně zavraždila.","a narazil na Badeline, měli horký sex.","ihned spadl do ostnů a zemřel","a úspěšně tuto kapitolu dokončil, může jít dál!","a udělal velký skok, avšak mu nedošlo že nemá doplněné dashe a spadl do díry.","a udělal velký skok a přežil. "]
        },
    },
    3: { # MINECRAFT
        "She/her": {
            "start": ["vytvořila nový svět","připojila se na náhodný server","připojila se na náhodný realm","připojila se na holkoklucicarny SMP"],
            "konec": ["někdo jí napadl a zabil, byl to hardcore takže se už nevrátí...", "někdo jí napadl a zabil, respawnula se zabila ho!", "po nějaké době hraní našla diamanty a teď má hodně diamantových hoes", "hrála tak dobře že porazila draka a teď dominuje celému světu.", "po chvíli ji to přestalo ji to bavit tak si šla honit pero", "snažila se ale nešlo jí to, třeba jí to pujde někdy příště... "]
        },
        "He/him": {
            "start": ["vytvořil nový svět","připojil se na náhodný server","připojil se na náhodný realm","připojil se na holkoklucicarny SMP"],
            "konec": ["někdo ho napadl a zabil, byl to hardcore takže se už nevrátí...", "někdo ho napadl a zabil, respawnul se zabila ji!", "po nějaké době hraní našel diamanty a teď má hodně diamantových hoes", "hrál tak dobře že porazil draka a teď dominuje celému světu.", "po chvíli ho to přestalo ji to bavit tak si šel honit pero", "snažil se ale nešlo mu to, třeba mu to pujde někdy příště... "]
        },
    },
    }

    postava = {
        "She/her":["Pavlí","Lena","Kiki","Adélka","Fena"],
        "He/him":["Šéf", "Archie", "Péťa", "Džimmy", "Fanoušek","Skyf","Ol*a "]
        }

    pronouns = choice(["He/him","She/her"])
    postava =choice(postava[pronouns])
    game = randint(0,3)
    start = choice(hra[game][pronouns]["start"])
    end = choice(hra[game][pronouns]["konec"])


    return (postava + " " + start + " " + end)