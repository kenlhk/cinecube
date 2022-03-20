from movies.models import Movie, Review
from userprofile.models import UserProfile
from django.contrib.auth.models import User

def populate_reviews():
    
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
    
    reviews[0] = [target[0], user[0], "I like Tom Holland in movies like this. I wish the the action was a little a bit more exciting.", 6]
    reviews[1] = [target[0], user[1], "The vibe of it is a little bit of throwback. It feels like the sort of silly, fun action movie we got a lot of in the 90s.", 7]
    reviews[2] = [target[1], user[2], "This is a smart, character-driven romantic comedy that pulls at the heartstrings with confident flair.", 9]
    reviews[3] = [target[1], user[3], "Marry Me doesn't quite follow through on all of its potential, but leading stars Jennifer Lopez and Owen Wilson will still make viewers swoon.", 6]
    reviews[4] = [target[2], user[4], "Emmerich's storytelling is cluttered at best, incomprehensible at worst, but the camp does make it go down easy.", 5]
    reviews[5] = [target[2], user[5], "Rarely makes any sense, but it's the kind of big dumb blockbuster that is fully self-aware of its own ridiculousness and embraces its inner goofiness.", 8]
    reviews[6] = [target[3], user[0], "Plenty of fun is provided by trying to spot the local locations where the reckless car chases were filmed.", 7]
    reviews[7] = [target[3], user[1], "The script is, gross opportunism aside, dismally threadbare.", 3]
    reviews[8] = [target[4], user[3], "A timely, tense, and ethically rich high-tech thriller.", 8]
    reviews[9] = [target[4], user[4], "A jumpy, jolty and ever-intensifying journey into the unknown, conducted under the expert filmmaking eye of Steven Soderbergh.", 6]
    reviews[10] = [target[5], user[5], "Scream is smart. All that's lacking is a plot, or a heroine, capable of making us squeal.", 6]
    reviews[11] = [target[5], user[0], "With boredom, lets just scream for no more!", 3]
    reviews[12] = [target[6], user[2], "Driven by a career-best Zac Efron performance, Gold is an effective if unremarkable survival thriller.", 7]
    reviews[13] = [target[6], user[3], "If only the film itself rose to Efron's extreme level of his commitment.", 5]
    reviews[14] = [target[7], user[5], "As for special effects, they are very good, and Greig Fraser’s cinematography is epic.", 6]    
    reviews[15] = [target[7], user[0], "How you like this iteration of Batman may depend upon how you like your serial murderers served and if you like your casting on a binary of Black and White.", 6]
    reviews[16] = [target[8], user[1], "A unique and entertaining effort that continues the studios recent hot streak.", 9]
    reviews[17] = [target[9], user[2], "This messy, convoluted action movie is so incomprehensible that it's difficult to say what it's actually about, other than a whole bunch of characters shooting each other and blowing stuff up.", 4]
    
    for script in reviews:
        review_data = Review(
                target = script[0],
                reviewer = script[1],
                comment = script[2],
                score = script[3],
        )
        review_data.save()
    
    