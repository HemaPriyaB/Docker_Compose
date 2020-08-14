import time
from flask import Flask
from redis import Redis

project= Flask(__name__)
redis = Redis(host='redis', port=6379)

@project.route('/')
def hello():
   redis.incr('hits')
   return 'This Compose/Flask demo got%s time(s).' % redis.get('hits')

if __name__=="__main__":
  
    project.run(host="0.0.0.0", debug=True)

