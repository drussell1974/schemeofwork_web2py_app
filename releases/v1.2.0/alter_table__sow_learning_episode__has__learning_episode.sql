ALTER TABLE sow_learning_objective__has__learning_episode
ADD COLUMN is_key_objective bool NOT NULL default 1 after learning_episode_id;