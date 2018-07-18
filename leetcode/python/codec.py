import random


class Codec(object):
    def __init__(self):
        self.tiny_url_base="http://tinyurl.com/"
        self.characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.url_to_hash={}
        self.hash_to_url={}

    def encode(self, longUrl):
        hash_code=""
        if longUrl in self.url_to_hash:
            return self.tiny_url_base+self.url_to_hash[longUrl]
        for i in range(0,6):
            hash_code+=self.characters[random.randint(0,len(self.characters)-1)]
        while hash_code in self.url_to_hash.values():
            hash_code=""
            for i in range(0,6):
                hash_code+=self.characters[random.randint(0,len(self.characters)-1)]
        self.url_to_hash[longUrl]=hash_code
        self.hash_to_url[hash_code]=longUrl
        return self.tiny_url_base+hash_code

    def decode(self, shortUrl):
        return self.hash_to_url[shortUrl[len(self.tiny_url_base):]]

if __name__ == '__main__':
    url="https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    print(codec.decode(codec.encode(url)))