from Globals import Globals


def idk():
    c = Globals.conn.cursor()
    c.execute("""CREATE TABLE server_preference(
    guild_id integer PRIMARY KEY UNIQUE,
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
    pug_match_user_limit integer
    )""")
    c.execute("""CREATE TABLE voice_user_data(
    voice_owner_id integer PRIMARY KEY UNIQUE,
    voice_name text(100),
    voice_limit integer)""")
    c.execute("""CREATE TABLE voice_data(
    voice_owner_id integer,
    voice_channel_id integer PRIMARY KEY UNIQUE,
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
    match_id integer,
    red_team_player_1 integer,
    red_team_player_2 integer,
    red_team_player_3 integer,
    red_team_player_4 integer,
    red_team_player_5 integer,
    blue_team_player_1 integer,
    blue_team_player_2 integer,
    blue_team_player_3 integer,
    blue_team_player_4 integer,
    blue_team_player_5 integer)
    """)
    c.execute("""create table pug_limit_6(
    match_id integer,
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
    blue_team_player_6 integer
    )
    """)
    c.execute("""create table ow_user(
    user_id integer PRIMARY KEY UNIQUE,
    battle_tag mediumtext,
    ip_address mediumtext)
    """)
    Globals.conn.commit()
