import random

class InterestAnalyzer:

    def analyze_interests(self, tweets):
        all_tweets = " ".join(tweets)

        possible_interests = ["spor", "müzik", "teknoloji", "film", "kitap", "seyahat",
                              "moda", "yemek", "sağlık", "eğitim", "sanat", "bilim",
                              "gezi", "otomobil", "oyun", "girişimcilik", "tarih", "siyaset",
                              "doğa", "evlilik", "ilişkiler", "televizyon", "sinema",
                              "dans", "müze", "konser", "felsefe", "fotoğraf", "yazılım",
                              "yabancı dil", "astroloji", "spor arabalar", "yoga", "kozmetik",
                              "video oyunları", "bisiklet", "denizcilik", "basketbol", "futbol",
                              "koşu", "bisiklet", "maraton", "zeka oyunları", "motorsporları",
                              "golf", "dövüş sanatları", "havacılık", "diyabet", "hayvan hakları"]
        
        num_interests = random.randint(1, min(5, len(possible_interests)))
        random_interests = random.sample(possible_interests, num_interests)

        return random_interests
    
    def getInterestList(self):
        return ["spor", "müzik", "teknoloji", "film", "kitap", "seyahat",
                              "moda", "yemek", "sağlık", "eğitim", "sanat", "bilim",
                              "gezi", "otomobil", "oyun", "girişimcilik", "tarih", "siyaset",
                              "doğa", "evlilik", "ilişkiler", "televizyon", "sinema",
                              "dans", "müze", "konser", "felsefe", "fotoğraf", "yazılım",
                              "yabancı dil", "astroloji", "spor arabalar", "yoga", "kozmetik",
                              "video oyunları", "bisiklet", "denizcilik", "basketbol", "futbol",
                              "koşu", "bisiklet", "maraton", "zeka oyunları", "motorsporları",
                              "golf", "dövüş sanatları", "havacılık", "diyabet", "hayvan hakları"]
