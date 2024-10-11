from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    # Home page with the main form for regex matching
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string')
    regex_pattern = request.form.get('regex_pattern')
    matches = []
    
    # Find all matches and include start/end positions
    for match in re.finditer(regex_pattern, test_string):
        match_details = {
            'match': match.group(),
            'start': match.start(),
            'end': match.end()
        }
        matches.append(match_details)
    
    return render_template('results.html', matches=matches, test_string=test_string, regex_pattern=regex_pattern)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    email = ''
    is_valid = None

    if request.method == 'POST':
        email = request.form.get('email')
        # Simple regex for email validation
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = bool(re.match(regex, email))
    
    return render_template('email_validation.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
