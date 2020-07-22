from random import randint

comments= [
    "I love your page! Keep up the good Work🔥🔥🔥",
    "This is a great post!!",
    "I love your content 🧡🧡",
    "I'm learning so much from you :)) ",
    "Great post 💯💯💯",
    "Wow! Thank! this is very eduational",
    "Great Content!",
    "This is a great idea 📚📚📚",
    " I love it 👍👍 ",
    "Nice Post. I like it 👍👍",
    "Your account looks really nice!",
    "I just learned something new today!! Thanks 🧡🧡🧡🧡",
    "Learned something new 🧡🧡 Great Content!",
    "I appreciate your posts! Great Job 🧡🧡",
    "This is such a great Post 🔥🔥. ",
    "very educational 🔥🔥 Great Job🔥🔥",
    "yo chill, gonna blow people away with knowledge 🔥🔥",
    "I have been enlightened 🔥🔥",
    "The More you know 🔥🔥",
    "Daily content is found here thx 🔥🔥"
    "This account makes me learn every day! Great Job"
    "love your posts! 🔥🔥"
    




]


def get_random_comment():
    size = len(comments)-1;
    return comments[randint(0, size)]