class User:
  def __init__(self, user_data):
        self.username = user_data["username"] 
        self.name = user_data["name"] 
        self.followers_count = user_data["followers_count"] 
        self.following_count = user_data["following_count"] 
        self.language = user_data["language"] 
        self.region = user_data["region"]
        self.tweets = user_data["tweets"] 
        self.following = user_data["following"] 
        self.followers = user_data["followers"] 