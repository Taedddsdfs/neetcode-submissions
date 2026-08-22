class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1

    # users = 팔로우한_사람들 | 나 union set 집합임
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        feed = []
        for user in users:
            feed.extend(self.tweets[user])
            feed.sort(reverse = True)

        return [tweetId for time,tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
