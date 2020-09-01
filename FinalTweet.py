import json


class TweetFinal:
    def final_tweet(self):
        finalTweet = ''
        final_path = 'E:\\FinalData\\Tweet'
        id_path = 'E:\\FinalData\\Config.txt'
        with open(id_path, 'r') as fp:
            CurrentpoemId = fp.read()
        with open(final_path, 'r') as fp:
            data = json.loads(fp.read())
            CurrentpoemId = int(CurrentpoemId) + 1
            tweetInfo = data[CurrentpoemId]
            poemId = tweetInfo['id']
            title = tweetInfo['title']
            author = tweetInfo['author']
            poem = str(tweetInfo['lines']).strip('[,]')
            finalTweet = poem + '\n' + '\n' + 'Author: ' + author + '\n' + 'Poem: '+title + '\n' + '#poems' + '#truth' + '#life'
            print(finalTweet)
            print(len(finalTweet))
        with open(id_path, 'w') as fp:
            fp.truncate()
            fp.write(str(CurrentpoemId))
        return finalTweet
