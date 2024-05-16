def main():
  MAX_TWEET_LENGTH = 140
  tweet = input()
  if len(tweet) <= MAX_TWEET_LENGTH:
    print('TWEET')
  else:
    print('MUTE')

if __name__ == '__main__':
  main()