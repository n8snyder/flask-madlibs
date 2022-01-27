from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

debug = DebugToolbarExtension(app)
chosen_story = None
# change homepage to select which story
# submitting selected story should do get with story name to /questions?store-name=silly-story
# /question view look up the story from a global STORIES dictionary

STORIES = {"silly story": silly_story, "excited story": excited_story}
# STORIES.keys()

# story_name = request.args["store-name"]
# story = STORIES[story_name]


@app.get("/")
def story_type():
    """Page to choose the story template"""

    return render_template("chooseStory.html", storynames=STORIES.keys())

    

@app.get("/story")
def question():
    """Question page to recieve input for completing story from user """
    global story_name
    story_name = request.args.get("story-name")
    chosen_story = STORIES[story_name]


    return render_template("questions.html", prompts=chosen_story.prompts)




@app.get("/results")
def story_result():
    """Story page with submitted words"""

    text = chosen_story.generate(request.args)

    return render_template("story.html", story=text)


# TODO: include in docstring for home that we show form
