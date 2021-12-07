from numpy import inf
import praw, re, time, sys, getopt
import pandas as pd
from praw.models import MoreComments
from datetime import datetime

quarantined_text = 'quarantined.txt'
non_quarantined_text = 'non_quarantined.txt'

def quarantined_subreddits():
    quarantined_subreddits = []
    quarantined_file = open("logs/"+quarantined_text, "r")
    for line in quarantined_file:
        quarantined_subreddits += re.findall(r'r/(.*)', line)
    quarantined_file.close()
    return quarantined_subreddits

def non_quarantined_subreddits():
    non_quarantined_subreddits = []
    non_quarantined_file = open("logs/"+non_quarantined_text, "r")
    for line in non_quarantined_file:
        non_quarantined_subreddits += re.findall(r'r/(.*)', line)
    non_quarantined_file.close()
    return non_quarantined_subreddits

def is_quarantined(s):
    """
    Given the string name of a subreddit, determine if it is quarantined
    """
    if s in quarantined_subreddits():
        return True
    elif s in non_quarantined_subreddits():
        return False
    else:
        raise ValueError('subreddit', s, 'does not exist in subreddit lists')
