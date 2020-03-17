import redis


class Instance:
    def __init__(self,addr='127.0.0.1',port=6379,db=0,passwd=''):
        self.addr=addr
        self.port=port
        self.db=db
        self.passwd=passwd
    
    def connect(self):
        if self.passwd == '':
            return redis.StrictRedis(host=self.addr,port=self.port,db=self.db)
        else:
            return redis.StrictRedis(host=self.addr,port=self.port,db=self.db,password=self.passwd)
    
        