
from random import randint
from time import sleep


paths={
    # Login Page Paths
    "username_input"    :   "//input [@name='username']",
    "password_input"    :   "//input[@name='password']",
    "login_button"      :   "//button[@type='submit']",

    # Home Page Paths
    "save_info"         :   "//button[@type='button' and contains(.,'Not Now')]",
    "notifications"     :   "//button[@tabindex='0' and contains(.,'Not Now')]",
    "dm_button"         :   "//a[@href='/direct/inbox/']",

    #Direct Message Page Paths
    "engagement_group"  :   "//*[text()='Small Businesses']",
    "group_chat_element":   "//div[@class='JiVIq _0NM_B']",
    "first_picture"     :   "//div[@class='eLAPa']",
    "exit_button"       :   '//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]',
    "like_button"       :   '//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Like"]',
    # "comment_textarea"  :   '//textarea[@class="Ypffh"]'
    "comment_textarea"  :   '//textarea[@aria-label="Add a comment…"]',
    "comment_post"      :   '//button[contains(@class, "sqdOP") and contains(@class, "yWX7d") and contains(@class, "y3zKF") and contains(@type, "submit")]',
    "messages"          :   'div.Igw0E.Xf6Yq.eGOV_.ybXk5._4EzTm',
    "like_message"      :   ".//span[@class='uTSKe']",
    "profile"           :   ".//a[contains(@class, '_2dbep') and contains(@class, 'qNELH') and contains(@class, 'kIKUG')]"






}

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

def sleep_rand():
    sleep(randint(1,3))

def random_time():
    return randint(4,6)