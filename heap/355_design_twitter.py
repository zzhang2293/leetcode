from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list) # user id -> list of [count, tweet_id]
        self.follow_map = defaultdict(set) # user id -> set of followee_id


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([tweetId, self.count])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        for ids in self.follow_map[userId]:
            index = len(self.tweet_map[ids]) - 1
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
