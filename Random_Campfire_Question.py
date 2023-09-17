# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:56:04 2023

@author: Admin
"""

import random

# Define your sentence pool
sentence_pool = [
    "1. If your character wasn’t an adventurer, what livelihood would they lead?",
    "2. Who in the party would your character trust the most with their life?",
    "3. What are your character’s core moral beliefs?",
    "4. What relationship does your character have with their parents and siblings?",
    "5. Does your character have any biases for or against certain races?",
    "6. What is your character’s opinion on nobility? On authority?",
    "7. Describe your character’s current appearance: clothes, armor, scars they’ve picked up along the journey, etc.",
    "8. What location encountered in the campaign has your character felt the most “at home” in, or just generally liked the most?",
    "9. What deity, if any, does your character worship? What’s their opinion on other people’s worship?",
    "10. If your character had time to pick up any artisan’s tools, game set, instrument, etc., what would it be?",
    "11. Describe your character’s current relationship with the player character sitting to your right.",
    "12. What is your character’s current goal, summed up in one sentence?",
    "13. Does your character ever want to “settle down” with a spouse, children, house, etc.?",
    "14. Has your character ever been in love?",
    "15. What battle in the campaign has been most memorable to your character?",
    "16. If your character wasn’t whatever class they are, what would they be instead?",
    "17. What is your character’s favorite season?",
    "18. What would your character’s Zodiac sign be, following stereotypical astrology?",
    "19. Where in the world does your character most want to visit?",
    "20. What is the biggest mistake your character has ever made?",
    "21. Does your character have any noticeable scars? If so, what are their stories?",
    "22. What animal best represents your character?",
    "23. If your character could go back in time and change one thing about their life, what would it be?",
    "24. Which other player character does your character find themselves having the most in common with?",
    "25. Does your character regret any particular choice the party has made?",
    "26. What would your character say their best trait would be?",
    "27. What is your character’s greatest fear? Deep, irrational?",
    "28. What is currently motivating your character to stay with the party?",
    "29. What are your character’s hobbies and interests outside of their class?",
    "30. What would most people think when they first see your character?",
    "31. What stereotypical group role does your character play in the party? (The Mom, the Mess, the Comic Relief, etc. Optionally: What role would your character play in the “Five Man Band” structure?)",
    "32. What is your character the most insecure about?",
    "33. What person does your character admire most?",
    "34. What does your character admire and dislike the most about the player character sitting to your left?",
    "35. Why is your character’s lowest stat their lowest (the in-character reason, not “because there’s no reason for a wizard to have 16 strength, duh”)?",
    "36. What would be your character’s theme song/favorite band/favorite genre of music?",
    "37. What stereotypical role would your character play in a high school AU/if they attended a normal high school? (Nerd, jock, bully, goth, etc.)",
    "38. What treasure/item/artifact that your character has collected during the adventure is the most important to them?",
    "39. Is there any particular weapon, item, etc. that your character longs to find?",
    "40. Where does your character feel the most at home?",
    "41. Does your character care about how they’re perceived by others? How do they change themselves to fit in with other people?",
    "42. What does your character think is the true meaning of life?",
    "43. What is your character’s scent? (Bonus points for a description that sounds like it could be from a bad [or awesome] fanfic.)",
    "44. Does your character think more with their heart or their brain?",
    "45. What is your character’s most recent or frequent nightmare?",
    "46. What opinion does your character have on [CERTAIN ESTABLISHED GROUPS/AUTHORITIES IN THE GAME WORLD]? (Dragonmarked Houses, royal crown, etc.)",
    "47. How did your character spend their childhood? Where did they grow up/who were their childhood friends?",
    "48. What aspect of your character’s future are they most curious about? (If they could know one thing about the future, what would it be?)",
    "49. What colors are associated with your character?",
    "50. Who in the party would your character prioritize rescuing, in dire circumstances?",
    "51. Is your character the most swayed by ethos, pathos, or logos?",
    "52. If your character was granted a single use of Wish, what would they use it for?",
    "53. What is your character’s favorite spell? If they don’t use spells: what is their favorite personal weapon/combat maneuver/skill/etc.?",
    "54. How does your character feel about keeping secrets from the rest of the party?",
    "55. What type of creature in the world is your character the most intrigued by?",
    "56. When they were a child, what did your character want to be, or think they were going to be, when they grew up?",
    "57. The player character to your left admits that they’re passionately in love with your character. How would your character respond?",
    "58. If somebody (an NPC, someone from their backstory, etc.) your character trusts/loves asked your character to do something against the party’s best interest, who would they side with?",
    "59. Does your character value their own best interest more than the party’s?",
    "60. What decision would the party have to make in order for your character to consider splitting off from the group?",
    "61. How does your character imagine the way they will die?",
    "62. What is your character’s greatest achievement?",
    "63. Is your character willing to risk the well-being of others in order to achieve their goal?",
    "64. What is your character’s opinion on killing others?",
    "65. What is your character’s favorite food? Beverage?",
    "66. How generous is your character? Especially to those they don’t know?",
    "67. What is your character the most envious about, regarding anyone in the party?",
    "68. The player character to your left and the player character to your right are both telling your character two different versions of the truth. Who does your character believe?",
    "69. What is your character’s sexuality/relationship with sex?",
    "70. What is your character’s biggest pet peeve?",
    "71. Describe how your character feels about the party’s current situation/objective/etc.",
    "72. Who in the party would your character trust the most to keep an important secret?",
    "73. If your character knew that they were going to die in a month, how would they spend the rest of their life?",
    "74. What makes your character feel safe?",
    "75. If your character had the chance to rename the party/give the party a name, no questions asked, what would it be?",
    "76. What memory does your character want to forget the most?",
    "77. If your character had to multiclass into a class they currently aren’t the next time they level up, what would it be and what reason would they have for doing so?",
    "78. What television/book/video game/etc. character would your character be best friends with? (Or: what media character is your character the most influenced by/similar to?)",
    "79. What unusual talents does your character possess?",
    "80. How does your character feel about receiving/giving orders? Are they more of a leader, or a follower?",
    "81. What does your character’s name represent to them? (Or: why as a player did you choose your character’s name?)",
    "82. Is your character more of an introvert, or an extrovert?",
    "83. How far is your character willing to go to pursue the 'greater good'? Do they believe in a greater good at all?",
    "84. What does your character want to be remembered by?",
    "85. What would be your character’s major in college?",
    "86. Does your character consider themselves a hero, villain, or something else?",
    "87. What major arcana tarot card best represents your character?",
    "88. Where does your character see themselves in 20 years?",
    "89. What is your character’s relationship with magic? Are they scared of it, wish to know more about it, indifferent to it?",
    "90. Who is your character’s biggest rival?",
    "91. What is your character’s guiltiest pleasure?",
    "92. What does your character hope for the afterlife?",
    "93. Who in the party does your character trust the least?",
    "94. What is your character’s biggest flaw?",
    "95. How did your character learn the languages that they speak?",
    "96. What is your character’s favorite school of magic/type of weaponry?",
    "97. What is most important to your character: health, wealth, or happiness?",
    "98. What advice would your character give to a younger version of themselves?",
    "99. Are there any social or political issues your character feels strongly about?",
    "100. What, currently, is your character the most curious about?",
    "101. What are you looking forward to at your next stop?",
    "102. What scares you about the direction you're taking?",
    "103. What does your present circumstance remind you of?",
    "104. What disturbs you about your past actions?",
    "105. What secret do you need to reveal about yourself?",
    "106. What did you always want to tell one of your companions?",
    "107. What is something you seek in a future journey?",
    "108. What friend do you miss?",
    "109. What location does your current location remind you of?",
    "110. What loved one do you miss?",
    "111. What was the most morally questionable choice you made?",
    "112. What villain do you remember?",
    "113. What location did you best enjoy?",
    "114. Where do you wish you were right now?",
    "115. Who did you leave behind?",
    "116. What villain is still out there?",
    "117. What happened with your last adventuring party?",
    "118. What is your fondest memory?",
    "119. What was your darkest moment?",
    "120. What was your favorite meal?"
]

# Function to get random sentences
def get_random_sentences(num_sentences):
    random_sentences = random.sample(sentence_pool, num_sentences)
    return random_sentences

# Number of sentences to display
num_sentences_to_display = 3

while True:
    # Get and display random sentences
    random_sentences = get_random_sentences(num_sentences_to_display)
    for i, sentence in enumerate(random_sentences, start=1):
        print(f"{sentence}\n")

    # Wait for user input to continue or exit
    user_input = input("Press Enter to display another set of sentences or 'q' to quit: ")
    print("\n---------------------------------------\n")
    if user_input.lower() == 'q':
        break
