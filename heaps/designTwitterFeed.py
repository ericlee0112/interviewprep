'''
Follow
- userId1
- userId2

Tweet
- userId
- tweetId





'''
import collections
class Tweet:
    def __init__(self, tweetId, time):
        self.time = time
        self.tweetId = tweetId

class Twitter:
    def __init__(self):
        self.tweetCounter = 0
        self.follows = collections.defaultdict(set)
        # userId -> [userThatTheyFollow1, userThatTheyFollow2, ...]
        self.tweets = collections.defaultdict(list)
        # userId -> [tweet1, tweet2 ...]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(tweetId, self.tweetCounter)
        self.tweetCounter += 1

        self.tweets[userId].append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # get users tweets
        usersTweets = self.tweets[userId]
        for tweet in usersTweets:
            heapq.heappush(heap, (-1 * tweet.time, tweet.tweetId))

        # get users that userId follows
        otherUsers = self.follows[userId]
        # for every
        for otherUserId in otherUsers:
            if otherUserId == userId:
                continue
            else:

                otherTweets = self.tweets[otherUserId]
                for tweet in otherTweets:
                    heapq.heappush(heap, (-1 * tweet.time, tweet.tweetId))
        
        content = []
        i = 0
        while i < 10 and len(heap) > 0:
            time, tweetId = heapq.heappop(heap)
            content.append(tweetId)
            i += 1
        
        return content

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        
