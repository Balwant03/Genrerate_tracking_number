from flask import Flask, jsonify
import time
import redis
import uuid

app = Flask(__name__)


class TrackingNumberGenerator:
   def __init__(self, redis_host='localhost', redis_port=6379):
       try:
           self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
           self.redis_client.ping()  # Test connection
       except redis.ConnectionError:
           print("Could not connect to Redis. Make sure Redis is running on port 6379.")
           raise

   def generate_tracking_number(self):
       timestamp = int(time.time() * 1000)
       random_component = uuid.uuid4().hex
       tracking_number = f"{timestamp}-{random_component}"
       
       # Ensure the tracking number is unique
       if not self.redis_client.sadd("tracking_numbers", tracking_number):
           # Retry if duplicate
           return self.generate_tracking_number()
       
       return tracking_number

try:
   generator = TrackingNumberGenerator()
except redis.ConnectionError:
   print("Failed to create the tracking number generator due to Redis connection issues.")
   generator = None

@app.route('/generate', methods=['GET'])
def generate_tracking_number():
   if generator is None:
       return jsonify({'error': 'Redis connection error. Please try again later.'}), 500
   tracking_number = generator.generate_tracking_number()
   return jsonify({'tracking_number': tracking_number})


@app.route('/tracking_numbers', methods=['GET'])
def get_tracking_numbers():
   if generator is None:
       return jsonify({'error': 'Redis connection error. Please try again later.'}), 500
   tracking_numbers = generator.redis_client.smembers("tracking_numbers")
   return jsonify({'tracking_numbers': list(tracking_numbers)})



if __name__ == "__main__":
   app.run(debug=True)