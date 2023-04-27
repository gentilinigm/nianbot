/* NOTE:
 * We use discord's default
 * user ids as they should
 * be unique.
 * They have a fixed length
 * of 18 characters.
 */
CREATE DOMAIN MEMBER_ID_TYPE AS VARCHAR(18);
CREATE TABLE members (
member_id MEMBER_ID_TYPE PRIMARY KEY,
member_name TEXT UNIQUE,
member_nickname TEXT,
member_level REAL,
member_karma REAL,
messages_count INTEGER,
commands_count INTEGER,
first_joined DATE,
last_message DATE
);

CREATE TABLE giveaways (
giveaway_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
giveaway_title TEXT UNIQUE,
giveaway_description TEXT,
giveaway_notes TEXT,
giveaway_start DATE,
giveaway_end DATE,
max_winners SMALLINT,
fk_member_creator MEMBER_ID_TYPE REFERENCES members(member_id)
);

CREATE TABLE r_giveaways_members (
r_giveaways_members_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
winner_rank SMALLINT DEFAULT -1,
fk_member MEMBER_ID_TYPE REFERENCES members(member_id),
fk_giveaways INTEGER REFERENCES giveaways(giveaway_id)
);

CREATE TABLE qotds (
qotd_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
qotd_text TEXT,
qotd_date DATE,
anonymous BOOL,
approved BOOL,
approved_date DATE,
picked BOOL,
picked_date DATE,
qotd_likes INT,
qotd_dislikes INT,
message_id TEXT UNIQUE,
fk_member_approver MEMBER_ID_TYPE REFERENCES members(member_id),
fk_member_issuer MEMBER_ID_TYPE REFERENCES members(member_id)
);

CREATE TABLE nicknames (
nickname_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nickname_date_start DATE,
nickname_date_end DATE,
fk_member_updated_by MEMBER_ID_TYPE REFERENCES members(member_id),
fk_member MEMBER_ID_TYPE REFERENCES members(member_id)
);

CREATE TABLE punishments (
punishment_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
reason TEXT,
active BOOL,
dm_sent BOOL,
inserted_at DATE,
punishment_type TEXT CHECK(punishment_type IN ('ban', 'kick', 'mute', 'warn')),
expires_at DATE,
fk_member_issuer MEMBER_ID_TYPE REFERENCES members(member_id),
fk_member MEMBER_ID_TYPE REFERENCES members(member_id)
);

/* NOTE:
 * since kyo makes titles like:
 * [Genshin] [Arkinights] it is
 * possible to categorize them,
 * could be useful for some features
 */
CREATE TABLE video_types(
video_type_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
video_type_name TEXT CHECK(video_type_name IN ('genshin', 'arknights', 'other')),
video_type_priority INTEGER CHECK(video_type_priority >= 0 AND video_type_priority <= 10)
);

/* NOTE:
 * We use youtube default ids,
 * which should have a fixed
 * lenght of 11 characters
 * in case of videos.
 */
CREATE DOMAIN VIDEO_ID_TYPE AS VARCHAR(11);
CREATE TABLE videos(
video_id VIDEO_ID_TYPE PRIMARY KEY,
video_url TEXT UNIQUE,
video_title TEXT,
video_creation_date DATE,
is_live BOOL,
fk_video_type INTEGER REFERENCES video_types(video_type_id)
);

/* NOTE:
 * We use youtube default ids,
 * which should have a fixed
 * lenght of 34 characters
 * in case of playlists.
 */
CREATE DOMAIN PLAYLIST_ID_TYPE AS VARCHAR(34);
CREATE TABLE playlists(
playlist_id PLAYLIST_ID_TYPE PRIMARY KEY,
playlist_title TEXT
);

CREATE TABLE r_videos_playlists(
r_videos_playlists_id INT PRIMARY KEY,
fk_video VIDEO_ID_TYPE REFERENCES videos(video_id),
fk_playlist PLAYLIST_ID_TYPE REFERENCES playlists(playlist_id)
);
