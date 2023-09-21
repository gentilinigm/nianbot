"""
Loads bot configuration from environment variables and `.env` files.

By default, the values defined in the classes are used, these can be overridden by an env var with the same name.

`.env` and `.env.server` files are used to populate env vars, if present.
"""
import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvConfig(
    BaseSettings,
    env_file=(".env.server", ".env"),
    env_file_encoding="utf-8",
    env_nested_delimiter="__",
    extra="ignore",
):
    """Our default configuration for models that should load from .env files."""


class _Miscellaneous(EnvConfig):
    debug: bool = True
    file_logs: bool = False


Miscellaneous = _Miscellaneous()


FILE_LOGS = Miscellaneous.file_logs
DEBUG_MODE = Miscellaneous.debug


class _Bot(EnvConfig, env_prefix="bot_"):

    prefix: str = ">"
    sentry_dsn: str = ""
    token: str = ""
    trace_loggers: str = "*"


Bot = _Bot()


class _Channels(EnvConfig, env_prefix="channels_"):

    # Announcement
    welcome: int = 684040618196074522
    rules: int = 696333834697965618
    videos_streams: int = 684040996581015572
    server_news: int = 684787405554843649
    giveaway: int = 1068553259087822948
    roles_acquisition: int = 1073995608572039209

    # General-Talks
    general: int = 684045196484411412
    clips: int = 870306031337619456
    original_art: int = 736422743960191086
    food_flex: int = 801134650071580792
    media: int = 696346389331968011
    memes: int = 696347314561875979
    bot_spam: int = 684786580937900043

    # Ak-General
    ak_rules: int = 918903009184997459
    ak_game_news: int = 684405119840026734
    arknights: int = 684044989319479319
    ak_cn: int = 736630867300057178
    integrated_sss_strategies: int = 997150353055289414
    ak_handhold: int = 1074327862519279726
    ak_viewer_pulls: int = 1091326608780034068

    # Ak-Social-Hub
    ak_media_n_memes: int = 684111169211858948
    ak_salt_n_sugar: int = 684050926138687568
    ak_friends: int = 1074327019074093066
    weedy_bot: int = 1048576559365234728

    # Ak-Help
    information_corner: int = 1074327484859953233
    ak_help: int = 1074327484859953233
    ak_math_lab: int = 1074327833054285884

    # Genshin-Impact
    genshin_rules: int = 782937680568516628
    genshin_news: int = 802157913006145556
    genshin_impact: int = 745211643369095188
    genshin_guides: int = 764419321841057792
    genshin_help: int = 1026052675567099905
    gi_media_n_memes: int = 772215084733825085
    saltshin_impact: int = 758367359018205224
    genshin_wizard: int = 1045217823464632390
    gi_role_submission: int = 822412672834207755

    # Other-Games
    game_suggestions: int = 1074339171520479302
    honkai_star_rail: int = 1074406728143208498
    honkai_impact_3rd: int = 1074407711627813006
    fgo: int = 1074407795564232835
    azur_lane: int = 1074407830142079076
    blue_archive: int = 1074407754090946560
    snowbreak_containment_zone: int = 1132091238443659374
    project_neural_cloud: int = 1074406902697574510
    nier: int = 1074406999460163777
    pokemon: int = 1074666454839992340
    nikke: int = 1074407423865008228
    mobile_legends: int = 1074406840206626907
    counter_side: int = 1074407160336875580
    rhythm_games: int = 1074406959203233802
    league_of_legends: int = 1074666272329043988
    fps: int = 1074500144805982260
    project_moon: int = 1082649829387284620
    warframe: int = 1094064934284951562
    granblue_fantasy: int = 1096983744247775232
    princess_connect: int = 1108179250042912938
    wuthering_waves: int = 1108179401625063506
    chess: int = 1109139519300706355
    stardew_valley: int = 1110539675241824306
    aether_gazer: int = 1110580103655739522

    # Community-Content
    community_announcements: int = 729696553324904500
    community_ideas: int = 1006236098533527562
    nightcats_lounge: int = 761977915654537226

    # Degeneracy
    nsfw_rules: int = 783689432334336020
    nsfw: int = 685503748641914920
    nswf_chat_dome: int = 729737192292745358

    # Music
    music_jockie: int = 684046563219341368
    music_pancake: int = 882658387546996806

    # Outside-The-City
    outside_the_city: int = 951135069353947156

    # Voice-Channels
    voice_chat: int = 684796922170834958
    spam: int = 711218302214733834

    # Zenless-Zone-Zero
    zzz_news: int = 1114630717616427028
    zenless_zone_zero: int = 1114657118734254080

    # Logs
    log: int = 707608318692163617
    audit_log: int = 696333346577317998
    automod_logs: int = 934841792380149810
    message_log: int = 934852398822866975
    warn_ban: int = 727460706072526858

    # Dev
    github_updates: int = 1042183714312028250
    general_discussion: int = 1042187126743248936
    dev: int = 1042187126743248936
    testing_1: int = 743426792723054672
    testing_2: int = 743077096506523659


    # -----------VOICE----------- #

    # Community-Content
    nightcats_domain: int = 696349492135591986

    # Music
    music_only_1: int = 684743307087183904
    music_only_2: int = 685801962125393942

    # Outside-The-City
    hornt_mansion: int = 938651144966799410
    ultra_hornt_mansion: int = 982665301856509992

    # Voice-Channels
    doctors_bed: int = 1079062957914337441
    travellers_campfire: int = 696349409964982292
    team_game_vc1: int = 744634274560606239
    team_game_vc2: int = 744634382148436018
    crying_in_the_circle: int = 730895768247992401
    anime_corner: int = 951963205306023976
    afk: int = 687791818402037785

    # Dev
    devs_cafe: int = 743076855921508412

    # Moderator
    appeals: int = 1052634404226355240


Channels = _Channels()


class _Roles(EnvConfig, env_prefix = "roles_"):

    # Staff
    my_husband: int = 691248301529497671
    administrator: int = 684039437482590229
    moderator: int = 684797230758363137
    sub_mod: int = 703187683429842985

    # Assignable
    true_traveler_simp: int = 835845564008366121
    true_nahida_simp: int = 1036332991540117545
    true_tighnari_simp: int = 1012667803146399794
    true_nahida_guardian: int = 1036332991540117545
    true_alhaitham_simp: int = 1064809499543744572
    true_baizhu_simp: int = 1103581143812542474
    true_xiao_simp: int = 835845023919636510
    true_kazuha_simp: int = 851424806159384617
    true_venti_simp: int = 835845559746166834
    true_jean_simp: int = 835845565689364521
    true_wanderer_simp: int = 1050069470921629817
    true_zhongli_simp: int = 835845562732511243
    true_itto_simp: int = 898614048063639562
    true_albedo_simp: int = 835845561814220880
    true_diluc_simp: int = 835845560769708082
    true_hutao_simp: int = 835845557464334396
    true_klee_guardian: int = 835845705233989632
    true_yoimiya_simp: int = 851425618880102401
    true_dehya_simp: int = 1080316632406167583
    true_nilou_simp: int = 1012668632213491713
    true_mona_simp: int = 835845566365302804
    true_yelan_simp: int = 959370978922733579
    true_kokomi_simp: int = 883026441447571507
    true_tartaglia_simp: int = 835845707499569152
    true_ayato_simp: int = 958741398255972392
    true_ganyu_simp: int = 835845523729547286
    true_ayaka_simp: int = 851425118705942558
    true_eula_simp: int = 837676883616464906
    true_shenhe_simp: int = 927163481717886987
    true_qiqi_guardian: int = 835845702940229662
    true_raiden_simp: int = 883026095333593128
    true_yae_simp: int = 927164139107913749
    true_keqing_simp: int = 835845500602286080
    true_cyno_simp: int = 1024494814089203762

    # Self-Assignable
    arknights: int = 1074345356231454773
    genshin_impact: int = 1074345296093524049
    general: int = 1074345448615202846
    other_games: int = 1074345494081458237
    _18: int = 1074345416650391692
    stream_notification: int = 1083759737369268358

    # Factions
    rhodes_island: int = 691053209212682281
    glasgow: int = 691053515082039306
    lungmen: int = 691270263224008724
    rhine_lab: int = 691053926224756746
    abyssal_hunters: int = 692360428113887282
    penguin_logistics: int = 691054080079953961
    karlan_commercials: int = 835893668744265738
    blacksteel_worldwide: int = 691055670253977600
    ursus_government: int = 691054315720147054
    reunion: int = 691270705945378856
    no_faction: int = 691053610154328154

    # Community
    champion: int = 1004381868893945979
    nightcats: int = 749263980840747061

    # Subs
    twitch_subscriber: int = 1100030502360076328
    twitch_subscriber_tier_1: int = 1100030502360076329
    twitch_subscriber_tier_2: int = 1100030502360076330
    twitch_subscriber_tier_3: int = 1100030502360076331
    youtube_member: int = 905829711324807178
    youtube_member_meow: int = 905829711324807179
    server_booster: int = 688919183982985229

    # Bots
    music_bot: int = 684836940868354048
    testing_bot: int = 1047476989256286238
    pancake: int = 882657308792983612
    weedy: int = 1048580831251279953
    giveawaybot: int = 1068553173851177086
    carl_bot: int = 1074393998103420980
    phish_grabber: int = 934841440423542785
    dyno: int = 934852233340784651
    genshin_wizard: int = 1043823021300912160

    # Other
    black_room: int = 691265959302004797
    dj: int = 700344480779206717
    pingcord: int = 1092103735917940808  # TODO what is this??
    dev: int = 1042181285277339688


Roles = _Roles()


class _Categories(EnvConfig, env_prefix="categories_"):

    announcement: int = 684040094528700502
    general_talks: int = 696370842325745716
    ak_social_hub: int = 1074325438677123143
    ak_help: int = 1074325613738999878
    genshin_impact: int = 758366635849154570
    other_games: int = 1074324499564089396
    community_content: int = 729694893663846512
    degeneracy: int = 685503676030517255
    music: int = 684043938721693736
    outside_the_city: int = 1028169436122849280
    voice_channels: int = 684043783519862806
    zenless_zone_zero: int = 1114630631440261172

    logs: int = 713743909196660766
    bot_dev: int = 743076582796689409


Categories = _Categories()


class _Guild(EnvConfig, env_prefix="guild_"):

    id: int = 684039093927280664
    invite: str = "https://discord.gg/kyostinv"

    moderation_categories: tuple[int, ...] = (
        Categories.logs,
    )
    moderation_channels: tuple[int, ...] = ()
    modlog_blacklist: tuple[int, ...] = (
        Channels.log,
        Channels.message_log,
        Channels.automod_logs,
        Channels.message_log,
        Channels.warn_ban,
    )
    staff_roles: tuple[int, ...] = (Roles.administrator, Roles.moderator, Roles.sub_mod, Roles.my_husband,)


Guild = _Guild()


class Webhook(BaseModel):
    """A base class for all webhooks."""

    id: int
    channel: int


class _Webhooks(EnvConfig, env_prefix="webhooks_"):

    github: Webhook = Webhook(id=1042184254731341945, channel=Channels.github_updates)
    kyostinv_unwarn_appeals: Webhook = Webhook(id=680501655111729222, channel=Channels.appeals)


Webhooks = _Webhooks()


class _Database(EnvConfig, env_prefix="database_"):

    dbname: str
    database: str
    user: str
    password: str
    host: str
    port: int


Database = _Database()


class _CleanMessages(EnvConfig, env_prefix="clean_"):

    message_limit: int = 10_000


CleanMessages = _CleanMessages()


class _Cooldowns(EnvConfig, env_prefix="cooldowns_"):

    tags: int = 60


Cooldowns = _Cooldowns()


class _URLs(EnvConfig, env_prefix="urls_"):

    # Kyo
    youtube: str = "https://www.youtube.com/@KyoStinV"
    twitch: str = "https://www.twitch.tv/kyostinv"
    patreon: str = "https://www.patreon.com/kyostinv"
    discord: str = "https://discord.com/invite/kyostinv"

    # Discord
    bot_avatar: str = ""
    github_bot_repo: str = "https://github.com/gentilinigm/nianbot"


URLs = _URLs()

# FIXME: use the new style: "<:trashcan:637136429717389331>"
class _Emojis(EnvConfig, env_prefix="emojis_"):

    worryass: int = 1132314501195243520
    pink_rotate: int = 1131196229028675654
    pink_no_no_no: int = 1127752660007780432
    pink_boing: int = 1127294557026005142
    pink_rotate_tsk_tsk_tsk: int = 1127294535567953941
    pink_hair_tsk_tsk_tsk: int = 1127294520111931512
    pink_head_spin: int = 1127294509559062668
    pink_bald_tsk_tsk_tsk: int = 1127294499727614062
    rainbow_tsk_tsk_tsk: int = 1127294489678053438
    pink_hyper_tsk_tsk_tsk: int = 1127294475266424974
    pink_tsk_tsk_tsk: int = 1127294461068709939
    pika_tsk_tsk_tsk: int = 1127294451249852578
    kyostinv_pop: int = 1126990357729640581
    kyostinv_hyper_pat: int = 1126879442812272660
    kyostinv_pat_the_kyo: int = 1126855494695403611
    kyostinv_stare_right: int = 1126855492254314587
    kyostinv_stare_left: int = 1126855490656276551
    kyostinv_pout: int = 1126855489079226458
    kyostinv_oh_nooo: int = 1126855487674138685
    kyostinv_disgusted: int = 1126855486457778249
    kyostinv_kyome: int = 1126855485182722089
    kyostinv_kyomega_lul: int = 1126855483744063489
    kyome: int = 1126846796774248488
    kyomegalul: int = 1126846780592640131
    cock: int = 1126452598401142837
    balls: int = 1112665717364506634
    ultra_mad: int = 1104672719146078209
    strongge: int = 1104672713458593915
    ome: int = 1104672711160111196
    kyosti_2_kyopium: int = 1101884721983651881
    kyosti_2_bonk: int = 1101854262004289597
    kyosti_2_derp: int = 1100463079927599104
    kyosti_2_pog: int = 1100463075989147649
    kyosti_2_spin_derp: int = 1100463067533418527
    kyosti_2_poooooooooooog: int = 1100463066510020708
    gardenman: int = 1094254399041327184
    chadfish: int = 1094249260289106051
    pepe_la: int = 1079447919645687809
    pepe_ok: int = 1079447905162764379
    kyoko_bonk: int = 1069120448635338824
    kyoko_pout: int = 1069120430079746191
    kyoko_disgust: int = 1069120401541697556
    kyoko_oh_no: int = 1069120379680981084
    kyoko_stare_2: int = 1068538599403954266
    kyoko_stare: int = 1068537481496100925
    kyopium: int = 1057919194466877470
    worry_brick_throw: int = 1056241726945230999
    yep: int = 1056215539699167242
    cum: int = 1056215131782135818
    kek_wait: int = 1051523548667187350
    skadi_daijoubu: int = 1050690544822648873
    clueless: int = 1043480327135432785
    gladge: int = 1043480324430114826
    aware: int = 1043480321737359420
    madge: int = 1040203985967140894
    icant: int = 1040203264739774524
    raiden_poke: int = 1039528100263895040
    pepespit: int = 1033753984357367898
    pepe_flushed: int = 1033319558045507604
    huh: int = 1033319541108916288
    pat_the_kyo: int = 1030943703235297431
    crow_of_judgement: int = 1020020074041589770
    pepe_cringe: int = 1006832987754741760
    thonk: int = 1006192673406865438
    poog: int = 1005143266024489132
    binoculars: int = 976478719499718757
    based_halt: int = 971839936732995584
    based: int = 971829532258615306
    susge: int = 949193824658415656
    wokege: int = 948433100512329749
    bedge: int = 948433025367179284
    worry_ecchi: int = 947872676456841286
    pepe_point: int = 947548063063486545
    trollface: int = 947539035876896888
    monka_w: int = 947538500423680020
    sadge: int = 947538459436937226
    omegalul: int = 947538391090749591
    _5_head: int = 947538350120763482
    coom: int = 941753746763956285
    ok_man: int = 938817138792210452
    hot_dog: int = 936708417496698950
    pepega: int = 936316551370530936
    wicked: int = 936248992470269963
    fuck_copium: int = 936248932701450270
    worry_wants_boobas: int = 936007837363081216
    makeitspin: int = 933683924926877747
    hi: int = 926833363761889380
    trolldespair: int = 917064518478233610
    guoba_hypetwerk: int = 895631886716649472
    speed_r: int = 895631886595018772
    speed_l: int = 895631886578241576
    guoba_twerk: int = 893900481649319976
    worry_tired_of_your_shit: int = 893116082607497256
    prayge: int = 892360871454580798
    pogcrazy: int = 891281033054523392
    bonk: int = 891281005992886293
    booba: int = 891280992558514218
    ez: int = 891280938137452595
    mod_check: int = 891280856109424671
    pepega_swipe: int = 890449526350024744
    kanna_point: int = 888868072134414358
    worry_eating_popcorn: int = 888117708447690753
    kyoko_pet_pet: int = 884527630764871751
    kyoko_molest: int = 884527630257389579
    nezuko_ping: int = 875809698983579719
    kyoko_derp: int = 871014004162723841
    kyoko_pog: int = 871014003617460265
    kyoko_blush: int = 871014003495796797
    kyoko_sad: int = 871014003466457098
    kyoko_lul: int = 871014003428691988
    kyoko_mad: int = 871014003009277952
    onee_san_nose_pick: int = 870598858072281169
    pepe_oh: int = 866427412308426773
    sad_pepega_taking_a_shit: int = 865927386583400498
    sad_vermeil: int = 865654691416637500
    lagg: int = 860488807996456970
    ceobe_ok: int = 855805335553966080
    pat_skadi: int = 855226796261244930
    lapp_math: int = 855218224153362484
    cat_eat: int = 854633999523119154
    cat_disapprove: int = 853361483690147890
    cat_nod: int = 853351342046183425
    nanji: int = 852834519786717215
    wtffff: int = 848616374217867265
    wcry: int = 848207998752784385
    cat_baby: int = 844912224699285514
    flamy_approve: int = 839898309723422790
    pepe_smug_cofee: int = 836191981893058600
    lappy_laugh: int = 834092520141094963
    peepocuteeyes: int = 829165091521167370
    pepe_fight: int = 826042223044198400
    you_thorni: int = 823898352243441745
    copium: int = 817740687263924245
    keksip: int = 817055802812268595
    poggiessssss: int = 814871970805973033
    natasha_smash: int = 814479033973866506
    tachanka_watch: int = 814478638158053428
    poggies: int = 811185876586725396
    cuddle: int = 809107036025258044
    spicyoil: int = 805466035452772352
    i_didnt_want_to: int = 805395038708301865
    pepe_ew: int = 805052268600623184
    dumb_nian: int = 805051115095457793
    peepohappy: int = 803422576416129094
    karen_lmao: int = 800348224723877910
    pika_ew: int = 800346314168336384
    dumb_kyoko: int = 799657215933677578
    dumb_thorns: int = 799310717483220992
    youcantdodis: int = 797873913115574302
    doggo_kek: int = 795242694301057044
    kek_l: int = 794980929227063386
    peepopopcorn: int = 794550407565279232
    kekhands: int = 783675182136950786
    skaderppp: int = 779910678014197820
    worry_card: int = 778661629646602280
    worry_sad: int = 778660543522406410
    worry_pop_corn: int = 778572667896594433
    worry_thonk: int = 778572667644805121
    worry_sweat: int = 778572667594342400
    worry_pog: int = 778572667346878504
    worry_knows: int = 778572667031912478
    worry_detective: int = 778572666881572874
    kekw: int = 778571043639394314
    lapp_triggered: int = 776645282141962280
    pog_o: int = 772120528014147596
    ceobe_mad: int = 751115610087358634
    pepe_noob: int = 748607919184019477
    pepe_send_nudes: int = 748194080173064202
    kurumi_run: int = 745329053736632364
    dance: int = 743081294283407380
    worry_happy_hug: int = 732207457253851178
    fish_man: int = 730804192423182411
    amiya_stahp: int = 726068334222639136
    angry_bork: int = 722488824101339256
    eyja_whyyyy: int = 720214128387555428
    manticore_look: int = 720214127980707901
    red_shinelook: int = 720214127959605259
    ifrit_burnnn: int = 720214127485780070
    exu_sad: int = 720214126630010911
    bp_blusshed: int = 720214123744460842
    worry_knife: int = 719596151527178260
    stabby_sneak: int = 716672406097363054
    sneak_peek: int = 716672404612579428
    pepe_molest: int = 716358626968731688
    _02_pat_fast: int = 715834155870715944
    worry_rock_hit: int = 714821825749844058
    worry_rock: int = 714821656731975700
    cute_squeezz: int = 713830872805277767
    confusedog: int = 713830575647227946
    awkward_smile: int = 712957863529545758
    iseenothing: int = 712603379108413440
    yussplz: int = 712603359919734845
    deku_head_bang: int = 712572801588133968
    worry_originium_hit: int = 712563348969095199
    worry_dodge: int = 711890916503191572
    worry_want_hug: int = 711890151621787659
    worrykawai: int = 711889881743491093
    worry_love: int = 711888214918692926
    ricarbonk: int = 711886838301720616
    worrybrickhit: int = 711886661600149607
    yelledcat: int = 711886205956128848
    teehehe: int = 711886192706191450
    worrysleep: int = 711886156962201681
    danceloli: int = 711884244938653817
    dancericardo: int = 711883672386797608
    dancedoge_2: int = 711883540458897419
    cat_love: int = 711861436573286410
    worry_my_originium: int = 711237828016603206
    worry_unsee: int = 711199436847710258
    worry_heart_tear: int = 710805600493371442
    dancekirby: int = 710428326438895679
    dancedoge: int = 710426073124569119
    pepe_yeehaw: int = 710421326527070209
    danceblob: int = 710421008707747893
    bongoslap: int = 710419945892347986
    dancevibing: int = 710419563140874240
    bongo_cat: int = 710419037049585757
    castle_dance: int = 710418098804752444
    angy_mid_finger: int = 710416328846213220
    liclic: int = 710414068883914872
    worry_bleach: int = 710410177266057286
    ifrit_shake: int = 710067051959418941
    bp_hug: int = 707575085606764595
    lapp_laugh: int = 707310904827707475
    pepe_think: int = 706865976616157184
    surprised_pikachu: int = 706836785753358346
    pepe_sip: int = 706788602885177414
    owohehe: int = 706470343132315688
    w_love_you: int = 706118554495221881
    gun_right: int = 705875059780092015
    panda_love: int = 705748647505297449
    chika_nani: int = 705453047551229972
    narucutor: int = 705453008917495869
    narubonk: int = 705452996879843379
    kanna_kms: int = 705449233905483834
    pepe_pantsu: int = 705418218126180465
    worry_haging_1: int = 704444564156579901
    worry_haging_2: int = 704444563984744560
    pepe_hmmmmmmmmmmmmmmmmmmm: int = 704394527888375879
    baka: int = 704300066856239364
    facepalm: int = 704300066306916362
    worry_huggle: int = 704253457057579088
    worry_leave: int = 704252834488778832
    cryyyymin: int = 702564172537528381
    pepe_wow: int = 702424708158586901
    watame_shake: int = 701747965584474112
    ruuun: int = 701394787672129597
    oneec_popcorn: int = 699593948334653462
    worry_woke: int = 698130102634151936
    worry_cry: int = 698130102214721647
    bunny_lurk: int = 697833405831839845
    flamy_refuse: int = 697407014690881634
    where_is_my_lmd: int = 697372652700041247
    bruh: int = 696314089772941312
    panikkk: int = 696303994041270272
    red_sleeping: int = 695351526331383838
    dokta_hyper_slap: int = 695350035516489750
    harisa_pat_kasumi: int = 695240511413420132
    pat_pat: int = 695240106835181619
    rangers_popcorn: int = 695225674142842880
    dumb_lapp: int = 694990279991885884
    lapp_kek: int = 694989715903873065
    red_crying: int = 694086435136995389
    pepe_pat: int = 693897849229934594
    pepeonkillrage: int = 692847868259729448
    dancecat: int = 691959935562547251
    pepeplz: int = 691745520963813386
    pepecry: int = 691745285038276768
    yay: int = 691741131360174160
    wt_fman: int = 691615357118709800
    pepe_cry_with_headphones: int = 689212395021009027
    look_from_the_prison: int = 689212388863770637
    tom: int = 689212388834279548
    pepe_gun: int = 689137658945077315
    ifrit_burn: int = 689137654188474389
    novy_pat: int = 689137650657263691
    pepefuckingkillyou: int = 689137648379625531
    gun: int = 689095965545988110
    subarashi: int = 689095964706996226
    lapp_lick_candy: int = 689095964706865211
    skadi_peek: int = 685821281744191489
    kyeew: int = 685812554752458754
    hoshigu_spinner: int = 685151728148021278
    exutatatatata: int = 685151716362289193
    shaw_cumming: int = 685151704966234172
    shining: int = 685151695910469688
    kal_consoles_dokutah_for_no_sanity: int = 685151686054248454
    jessica_rich_cat: int = 685151676617064450
    amiya_beat_on_table: int = 685151653988663428
    originium_cancelled: int = 685151622321668210
    sanity_cancelled: int = 685151505778737184
    frost_leaf_love: int = 685151438040727710
    theresa_broke: int = 685151310882144284
    theresa_look: int = 685151293219930266
    texas_shame: int = 685151271396573326
    jessica_sad_cat: int = 685151247724052541
    dokutah_nice: int = 685151162260783122
    dokutah_nooo: int = 685151146322690114
    texas_hype: int = 685150904261148680
    texas_pat: int = 685150884774412298
    exu_love: int = 685150851261792277
    exu_hype_stare: int = 685150826724982798
    pti_thinking: int = 685150552623022114
    skadi_mad: int = 685150501792120862
    dokutah_stonks: int = 685150420032946236
    dokutah_not_stonks: int = 685150396616146967

    check_mark: str = "\u2705"
    cross_mark: str = "\u274C"

    ok_hand: str = ":ok_hand:"


Emojis = _Emojis()


BOT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(BOT_DIR, os.pardir))

# Default role combinations
STAFF_ROLES = Guild.staff_roles

# Channel combinations
MODERATION_CHANNELS = Guild.moderation_channels

# Category combinations
MODERATION_CATEGORIES = Guild.moderation_categories
