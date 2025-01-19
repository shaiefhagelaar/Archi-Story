### -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - Start of General Documentation - -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ###

# Archi-story is based off of: https://archipelago.gg/

# Archi-story is a game randomizer which reorganizes in-game items. Instead of a typical linear experience it will become like a puzzle. So items will be spawned in new locations. See: https://archipelago.gg/faq/en/ for FAQ

# Glossary of Archipelago will be used for several variables to keep it consistent with their guide and support: https://archipelago.gg/glossary/en/

# Several tutorials you can have a look at: https://archipelago.gg/tutorial/

# You can join the discord by clicking the DISCORD box on their website located in the top right corner (12:15 19/01/2025). This may change in the future

# We'll be using the AGPL v3 license whenever the product is released to the public see:  https://www.gnu.org/licenses/agpl-3.0.en.html

# Why the AGPL v3 license? So you or anyone else can change the code to your liking and adjust it to your needs. Also because me and others might contribute and move on to newer projects.

# We wish you the best of luck and if you have any questions you can always reach out.
### -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- End of General Documentation -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ###

### -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- Start Pseudo code -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ###

# Program makes a document (.txt .yml .json) file
# The stored file needs to save the story of the player.
# Set the starting values to initiate the randomizer (do it different for each and every player to make it more personal)
# Set start value
# Saves document
# Program opens a local webui (with a basic webui interface written with: HTML/CSS/Java/Javascript
# Counts the players words that the player typed
# Counter keeps track of words being used (aka hint points)
# After threshold (x amount of words written) initiate randomizer
# Saves the state of the program and new variables
# Reset counter
#

### -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- End Pseudo code -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ###

### -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  Start of the actual code in Python -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - ###

from flask import Flask, render_template, request, jsonify
import requests  # Use this to call the API

app = Flask(__name__)

# API Base URL of Archipelago
ARCHIPELAGO_API_BASE_URL = "https://github.com/ArchipelagoMW/Archipelago"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_data():
    try:
        # Data recieved from frontend
        request_data = request.json
        # Make an API-call to Archipelago
        response = requests.get(f"{ARCHIPELAGO_API_BASE_URL}/your-endpoint", params=request_data)
        response_data = response.json()

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

