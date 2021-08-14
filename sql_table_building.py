from Globals import Globals


def idk():
    c = Globals.conn.cursor()
    c.execute("""CREATE TABLE server_preference(
    guild_id integer UNIQUE,
    prefix CHAR(5),
    report_mod_channel_id integer,
    mods_role_id integer,
    helpers_role_id integer,
    join_to_create_a_room_category_id integer,
    join_to_create_a_room_channel_id integer,
    member_count_category_id integer,
    tempmute_role_id integer,
    audit_log_channel_id integer,
    commands_log_channel_id integer,
    pug_player_role integer,
    moderation varchar(5)
    )""")
    c.execute("""CREATE TABLE voice_user_data(
    voice_owner_id integer UNIQUE,
    voice_name text(100),
    voice_limit integer)""")
    c.execute("""CREATE TABLE voice_data(
    voice_owner_id integer,
    voice_channel_id integer  UNIQUE,
    guild_id integer)""")
    c.execute("""CREATE TABLE member_count(
    guild_id integer PRIMARY KEY UNIQUE,
    member_count_channel_id integer)""")
    c.execute("""CREATE TABLE offences(
    member_id integer,
    member_name tinytext,
    guild_id integer,
    kind tinytext,
    start_date datetime,
    end_date datetime,
    reason mediumtext,
    treated varchar(5),
    moderator_id integer)""")
    c.execute("""create table pug_limit_5(
    match_id integer UNIQUE,
    guild_id integer,
    cat_id integer,
    red_team_player_1 integer,
    red_team_player_2 integer,
    red_team_player_3 integer,
    red_team_player_4 integer,
    red_team_player_5 integer,
    blue_team_player_1 integer,
    blue_team_player_2 integer,
    blue_team_player_3 integer,
    blue_team_player_4 integer,
    blue_team_player_5 integer,
    result varchar(2)
    )
    """)
    c.execute("""create table pug_limit_6(
    match_id integer PRIMARY KEY UNIQUE,
    guild_id integer,
    cat_id integer,
    red_team_player_1 integer,
    red_team_player_2 integer,
    red_team_player_3 integer,
    red_team_player_4 integer,
    red_team_player_5 integer,
    red_team_player_6 integer,
    blue_team_player_1 integer,
    blue_team_player_2 integer,
    blue_team_player_3 integer,
    blue_team_player_4 integer,
    blue_team_player_5 integer,
    blue_team_player_6 integer,
    result varchar(2)
    )
    """)
    c.execute("""create table pug_queue(
    guild_id integer,
    member_id integer,
    pug_limit integer,
    cat_id integer
    )""")
    c.execute("""create table pug_channels(
    guild_id integer,
    cat_id integer,
    commands_channel_id integer,
    voice_channel_id integer,
    pug_limit integer,
    time_to_approve integer,
    picks_by_roles varchar(5),
    api varchar(5),
    auto varchar(5)
    )""")
    c.execute("""create table ow_users(
    member_id integer unique,
    battle_tag varchar(20) unique,
    ip_address varchar(15))
    """)
    Globals.conn.commit()
