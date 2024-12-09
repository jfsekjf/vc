from flask import Flask
from threading import Thread
import time

# Create the Flask application instance
app = Flask('')

# Flask route to ensure the server is running
@app.route('/')
def home():
    return "I'm alive!"

# Function to run the Flask server
def run():
    app.run(host='0.0.0.0', port=8080)

# Function to start the Flask server in a separate thread
def keep_alive():
    t = Thread(target=run)
    t.start()

# Function to send a "Hello" message to the terminal every 30 seconds
def print_hello():
    try:
        while True:
            print("Hello - The script is running")
            time.sleep(30)  # Wait for 30 seconds before printing again
    except KeyboardInterrupt:
        print("Stopping the application...")

# Start the keep_alive server and the message loop
if __name__ == "__main__":
    keep_alive()   # Start Flask server to keep the application alive
    print_hello()  # Continuously send a message every 30 seconds
