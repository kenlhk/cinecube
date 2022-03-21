import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinecube.settings')

import django

django.setup()
from django.contrib.auth.models import User
from movies import load_info
from movies.models import Review, Movie


def populate():
    # Populate users
    if User.objects.all():
        for user in User.objects.all():
            user.delete()

    users = {
        "Alice": "alice@gmail.com",
        "Bernie": "bernie@gmail.com",
        "Cindy": "cindy@gmail.com",
        "Dandy": "dandy@gmail.com",
        "Edward": "edward@gmail.com",
        "Henry": "henry@gmail.com",
    }

    for user, email in users.items():
        add_user(user, email)

    # Populate movies
    load_info.get_movies()

    # Populate reviews
    if Review.objects.all():
        for review in Review.objects.all():
            review.delete()

    reviews = [None] * 18
    target = [None] * 10
    user = [None] * 6

    target[0] = Movie.objects.get(name="Uncharted")
    target[1] = Movie.objects.get(name="Marry Me")
    target[2] = Movie.objects.get(name="Moonfall")
    target[3] = Movie.objects.get(name="Blacklight")
    target[4] = Movie.objects.get(name="Kimi")
    target[5] = Movie.objects.get(name="Scream")
    target[6] = Movie.objects.get(name="Gold")
    target[7] = Movie.objects.get(name="The Batman")
    target[8] = Movie.objects.get(name="Turning Red")
    target[9] = Movie.objects.get(name="Pursuit")

    i = 0
    for userobject in User.objects.all():
        user[i] = userobject
        i = i + 1

    reviews[0] = [1, target[9], user[5],
                  "I like Tom Holland in movies like this. I wish the the action was a little a bit more exciting.", 2]
    reviews[1] = [2, target[8], user[5],
                  "The vibe of it is a little bit of throwback. It feels like the sort of silly, fun action movie we got a lot of in the 90s.",
                  4]
    reviews[2] = [3, target[7], user[0],
                  "This is a smart, character-driven romantic comedy that pulls at the heartstrings with confident flair.",
                  3]
    reviews[3] = [4, target[6], user[0],
                  "Marry Me doesn't quite follow through on all of its potential, but leading stars Jennifer Lopez and Owen Wilson will still make viewers swoon.",
                  4]
    reviews[4] = [5, target[5], user[1],
                  "Emmerich's storytelling is cluttered at best, incomprehensible at worst, but the camp does make it go down easy.",
                  1]
    reviews[5] = [6, target[4], user[1],
                  "Rarely makes any sense, but it's the kind of big dumb blockbuster that is fully self-aware of its own ridiculousness and embraces its inner goofiness.",
                  2]
    reviews[6] = [7, target[3], user[1],
                  "Plenty of fun is provided by trying to spot the local locations where the reckless car chases were filmed.",
                  5]
    reviews[7] = [8, target[2], user[1], "The script is, gross opportunism aside, dismally threadbare.", 5]
    reviews[8] = [9, target[1], user[2], "A timely, tense, and ethically rich high-tech thriller.", 4]
    reviews[9] = [10, target[9], user[2],
                  "A jumpy, jolty and ever-intensifying journey into the unknown, conducted under the expert filmmaking eye of Steven Soderbergh.",
                  2]
    reviews[10] = [11, target[8], user[2],
                   "Scream is smart. All that's lacking is a plot, or a heroine, capable of making us squeal.", 1]
    reviews[11] = [12, target[7], user[2], "With boredom, lets just scream for no more!", 3]
    reviews[12] = [13, target[6], user[3],
                   "Driven by a career-best Zac Efron performance, Gold is an effective if unremarkable survival thriller.",
                   4]
    reviews[13] = [14, target[5], user[3], "If only the film itself rose to Efron's extreme level of his commitment.",
                   2]
    reviews[14] = [15, target[4], user[3],
                   "As for special effects, they are very good, and Greig Fraser’s cinematography is epic.", 3]
    reviews[15] = [16, target[3], user[4],
                   "How you like this iteration of Batman may depend upon how you like your serial murderers served and if you like your casting on a binary of Black and White.",
                   2]
    reviews[16] = [17, target[2], user[4],
                   "A unique and entertaining effort that continues the studios recent hot streak.",
                   5]
    reviews[17] = [18, target[1], user[4],
                   "This messy, convoluted action movie is so incomprehensible that it's difficult to say what it's actually about, other than a whole bunch of characters shooting each other and blowing stuff up.",
                   1]

    for script in reviews:
        review_data = Review(
            id=script[0],
            target=script[1],
            reviewer=script[2],
            comment=script[3],
            score=script[4],
        )
        review_data.save()


def add_user(username, email):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.username = username
    user.email = email
    user.save
    print(user)
    return user


if __name__ == '__main__':
    print('Starting userfile population script...')
    populate()