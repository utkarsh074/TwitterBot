import json

#This class contains method to identify and pull poem from a locally maintained JSON file 
class TweetFinal:
    def final_tweet(self):
        finalTweet = ''
        #path where I have compiled poems from different sources in a way structured way i.e. JSON
        final_path = 'E:\\FinalData\\Tweet'
        #To keep track of poems which have been tweeted earlier
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
