from flask import Flask
from flask_caching import Cache
import random
import redis

application = Flask(__name__)
application.config['CACHE_TYPE'] = 'RedisCache'
application.config['CACHE_REDIS_URL'] = 'redis://our-very-own-cluster:6379'

cache = Cache(app=application)

print("iniciando")
cache.init_app(application)

redis_client = redis.Redis(host='our-very-own-cluster', port=6379, db=0)

@application.route("/")
@cache.cached(timeout=10)

def route():
    data = str(random.randint(0,100))  + '\n'
    return data

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8084)