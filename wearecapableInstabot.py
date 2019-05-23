#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login="chronicallycapable",  # Enter username (lowercase). Do not enter email!
    password="groupten123",
    like_per_day=1000,
    comments_per_day=0,
    tag_list=["chronicillness",	"chronicpain",	"chronicillness",	"chronicpain",	"chronicdisease",	"wfh",	"lymewarrior",	"lymedisease",	"invisibleillness",	"painsucks",	"cancersucks",	"autoimmunedisease",	"cancerawareness",	"beatcancer",	"cancersupport",	"chrons",	"lupus",	"healthanxiety",	"fibrowarrior",	"healthanxiety",	"chronickidneydisease",	"tickbornedisease",	"painsucks",	"spoonie",	"butyoudontlooksick",	"workfromhome",	"lupus",	"themighty",	"friendsinthefight",	"fastcompany",	"fuckcancer",	"sufferingthesilence",	"spooniestrong",	"remission",	"autoimmune",	"chronicpainwarrior",	"autoimmunewarrior",	"spoonielife",	"spooniesisters",	"lymedontkillmyvibe",	"lyme",	"endo",	"anxiety",	"chronicpainawareness",	"invisibleillnesswarrior",	"spooniesupport",	"chronicfatigue",	"youdontlooksick",	"ehlersdanlos",	"selfcarematters",	"chroniclife",	"disability",	"spooniewarrior",	"mentalhealthday",	"butyoudontlooksick",	"communitymatters",	"chronicillnesslife",	"invisibleillnessawareness",	"selfcarematters",	"spooniesister",	"invisibledisability",	"sufferingthesilence",	"asl",	"deafcommunity",	"americansignlanguage",	"therapy",	"depression",	"mentalillnessawareness",	"speakyourtruth",	"healthcareisahumanright",	"bethechange",	"diabetesawareness",	"accessibility",	"type1diabetes",	"type1life",	"womenshealth",	"insulinpump",	"disabled",	"imapreexistingcondition",	"potsie",	"dysautonomia",	"crps",	"wheelchairlife",	"disabledandcute",	"depressionwareness",	"anxietyquote",	"chronicdisease"],
    tag_blacklist=["rain", "thunderstorm", "sex", "porn", "adulting",	"alone",	"americangirl",	"ariefmirna2015",	"armparty",	"asia",	"asiandick",	"attractive",	"babyrp",	"bacak",	"badbitcztwerk",	"baddie",	"balenciaga",	"balls",	"bang",	"bangbang",	"batikate",	"beaty",	"belfie",	"bi",	"bigdickboy",	"bikinibody",	"bombshell",	"bootay",	"bootybounce",	"bra",	"brain",	"breast",	"buns",	"butt",	"butts",	"cam",	"carving",	"catsau",	"cesitone",	"cheeky",	"citycentre",	"commentschivettes",	"costumes",	"cph",	"cpr",	"csun",	"cumfession",	"curvesfordays",	"curvy",	"damngirl",	"datass",	"date",	"dating",	"desk",	"direct",	"dm",	"dominant",	"dripping",	"dutchgirl",	"dxb",	"easter",	"ebonyandivory",	"edm",	"edmbabes",	"eggplant",	"eggplants",	"eggporn",	"elevator",	"escilepernatale",	"estellaseraphim",	"everybodyisbeautiful",	"excitada",	"expose",	"fapstagram",	"feetofatlanta",	"fishnets",	"foreplay",	"freakshow",	"freethenipple",	"gays",	"gilofashion",	"girlsonly",	"gloves",	"goddess",	"hamishnadine",	"happythanksgiving",	"hardsummer",	"hijabiba",	"hooters",	"hornyyyyyyasf",	"hotgirls",	"hotguy",	"hots",	"hottie",	"humpday",	"iamgay",	"instagirl",	"instamood",	"istanbulgay",	"italiano",	"jugs",	"kansas",	"kickoff",	"kik",	"kikgirl",	"kikmessenger",	"killingit",	"kissing",	"lesbian",	"lesbiansofinstagram",	"lilmandingo",	"lingerie",	"lust",	"marcoreus",	"master",	"mebelim",	"medicina",	"mexicangirl",	"mirrorphoto",	"mixedgirls",	"models",	"mr40club",	"mrsandmrsbordeaux",	"mrtox",	"nacket",	"nasty",	"newyears",	"newyearsday",	"ngento",	"oovoo",	"petite",	"piroka",	"pixie",	"poop",	"pornfood",	"printic",	"publicrelations",	"pushups",	"rack",	"ravebabes",	"roleplay",	"russiangirl",	"russianmilf",	"saltwater",	"sexlife",	"shebad",	"shesquats",	"shit",	"shower",	"single",	"singlelife",	"skype",	"slimthick",	"snap",	"snapback",	"snapchat",	"snapchatgay",	"snapme",	"sokus",	"sopretty",	"spanishgirl",	"sparklingnudes",	"stopdropandyoga",	"stranger",	"streetphoto",	"stud",	"submission",	"sultry",	"sunbathing",	"swole",	"tag4like",	"takeitoff",	"teens",	"tgif",	"thatasstho",	"thick",	"thought",	"todayimwearing",	"treviso",	"twerk",	"twerker",	"undies",	"valentinesday",	"vatine",	"weed",	"weedstagram",	"weezmoney",	"wet",	"whitegirl",	"woman",	"womancrushwednesday",	"women",	"workflow"],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60 * 60,
    unfollow_per_day=350,
    unlike_per_day=0,
    unfollow_recent_feed=True,
    # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
    time_till_unlike=3 * 24 * 60 * 60,  # 3 days
    unfollow_break_min=15,
    unfollow_break_max=30,
    user_max_follow=0,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=0,
    log_mod=0,
    proxy="",
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        "second",
        "stuff",
        "art",
        "project",
        "love",
        "life",
        "food",
        "blog",
        "free",
        "keren",
        "photo",
        "graphy",
        "indo",
        "travel",
        "art",
        "shop",
        "store",
        "sex",
        "toko",
        "jual",
        "online",
        "murah",
        "jam",
        "kaos",
        "case",
        "baju",
        "fashion",
        "corp",
        "tas",
        "butik",
        "grosir",
        "karpet",
        "sosis",
        "salon",
        "skin",
        "care",
        "cloth",
        "tech",
        "rental",
        "kamera",
        "beauty",
        "express",
        "kredit",
        "collection",
        "impor",
        "preloved",
        "follow",
        "follower",
        "gain",
        ".id",
        "_id",
        "bags",
    ],
    unfollow_whitelist=["example_user_1", "example_user_2"],
    # Enable the following to schedule the bot. Uses 24H
     end_at_h = 23, # Hour you want the bot to stop
     end_at_m = 30, # Minute you want the bot stop, in this example 23:30
     start_at_h = 9, # Hour you want the bot to start
     start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
)

bot.mainloop()
