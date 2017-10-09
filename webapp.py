from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis')), port=6379

@app.route('/')
def hello():
    redis.incr('hit')
    return 'Hello container world! I have been seen %s times./n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
