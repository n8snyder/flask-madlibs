from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)

# change homepage to select which story
# submitting selected story should do get with story name to /questions?store-name=silly-story
# /question view look up the story from a global STORIES dictionary

STORIES = {"silly story": silly_story, "excited story": excited_story}
# STORIES.keys()

# story_name = request.args["store-name"]
# story = STORIES[story_name]


@app.get("/")
def home():
    """Home page of Madlib"""

    return render_template("questions.html", prompts=silly_story.prompts)


@app.get("/results")
def story_result():
    """Story page with submitted words"""

    text = silly_story.generate(request.args)

    return render_template("story.html", story=text)


# TODO: include in docstring for home that we show form
