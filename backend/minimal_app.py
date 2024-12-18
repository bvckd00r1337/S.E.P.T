from flask import Flask

app = Flask(__name__)

# Initialize a flag to track if the setup has been done
app.setup_done = False

@app.before_request
def before_first_request_func():
    if not app.setup_done:
        print("This runs before the first request.")
        # Perform any initialization tasks here
        # For example, creating tables or starting a scheduler
        # Once done, set the flag to True to prevent future executions
        app.setup_done = True

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    with app.app_context():
        # Perform initialization tasks here if necessary
        # For example:
        # db.create_all()
        pass  # Replace with actual initialization if needed
    app.run(debug=True)
