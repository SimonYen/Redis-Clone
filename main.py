import fire
import instance

def hello(src_addr='127.0.0.1',src_port=6379,src_db=0,src_passwd='',dst_addr='127.0.0.1',dst_port=6379,dst_db=0,dst_passwd=''):
    src=instance.Instance(src_addr,src_port,src_db,src_passwd).connect()
    dst=instance.Instance(dst_addr,dst_port,dst_db,dst_passwd).connect()


    for key in src.keys():
        print(key)
        hash_keys=src.hkeys(key)
        for k in hash_keys:
            v = src.hget(key,k)
            dst.hset(key,k,v)
    print('Complete!')

if __name__ == "__main__":
    fire.Fire(hello)