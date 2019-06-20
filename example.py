#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login="udemy_dm",  # Enter username (lowercase). Do not enter email!
    password="Oneplus135",
    like_per_day=5000,
    comments_per_day=100,
    tag_list=["follow4follow","blackchain", "AI", "f4f", "tutorial", "aesthetic",
            "tech", "programming", "art", "design", "blockchaintechnology","innovation","technology", "future", "education", "industry", "information"
            ,"solution", "development","business","webdevelopment", "datascience", "python", "javascript", "C++", "l:212999109"],
    tag_blacklist=["rain", "thunderstorm"],
    user_blacklist={},
    max_like_for_one_tag=192,
    follow_per_day=600,
    follow_time=1 * 60 * 60,
    unfollow_per_day=600,
    unlike_per_day=100,
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
    # We're giving away Udemy Courses for FREE👀 DM if interested🎉
    comment_list=[
        ["We're"],
        ["giving away", "giving out"],
        ["Udemy Courses"],
        ["for FREE👀"],
        ["DM"],
        ["if you want one🎉", "if interested🎉"]
    ],
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
    # end_at_h = 23, # Hour you want the bot to stop
    # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
    # start_at_h = 9, # Hour you want the bot to start
    # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
)

bot.mainloop()
