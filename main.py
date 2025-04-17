from flask import Flask, render_template, request

app = Flask(__name__)

# Example data for sections
sections = {
    "about_me": ["This is the About Me section."],
    "projects": ["Project 1", "Project 2", "Project 3"],
    "contact": ["Contact me at example@example.com"]
}

@app.route('/')
def home():
    # Get the current section from the query parameter (default is 'about_me')
    section = request.args.get('section', 'about_me')
    items = sections.get(section, ["Section not found."])
    return render_template('index.html', items=items, section=section, sections=sections)

if __name__ == '__main__':
    app.run(debug=True, port=5001)