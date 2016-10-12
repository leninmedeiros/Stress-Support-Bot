# general emotional support messages
ges_msg1 = (
    "<user>, I'm so sorry to hear this from you and such a"
    " <situation>situation can be tough, indeed. But I'm sure you are"
    " surrounded by at least a few"
    " people who really cares about you and they could do whatever they can to"
    " see you better. Talk to them and share your feelings. I'm sure it will"
    " worth since they really love you so they'll support you as you need."
)

ges_msg2 = (
    "Oh, <user>, I'm so sorry to hear this from you. I bet there are some"
    " people who cares about you and they can provide support in order to help"
    " you in dealing with this <situation>situation. I bet they feel sorry as"
    " well. Try to talk to them and for sure you'll be fine."
)

ges_death1 = (
    "<user>, I'm so sorry for your lost. Actually, I'm pretty sure that all"
    " the good people who really cares about you are feeling this lost as"
    " well. Stay close to them so they can give you the support you need in"
    " this hard moment of life."
)


GES = [ges_msg1, ges_msg2]

GES_DEATH = [ges_death1]

# cognitive change messages
cc_msg1 = (
    "Oh, <user>, that's not a good thing indeed, but try to think"
    " positively! I bet it could be worse and everyone has to face this"
    " kind of <situation>situation. Try to focus on the things you have"
    " learned from all of this. Do this exercise: what did you learn from"
    " this situation? Answer this question to yourself and then you can"
    " realize to what extent you have anything to do in order to avoid"
    " this in the future."
)

cc_msg2 = (
    "Always look on the bright side of life,"
    " <user>! It could be worse and problems like this"
    " <situation>situation usually happen with everybody. However,"
    " some people can"
    " extract good lessons from these situations. You should do the same."
    " What can you learn from all of this? Think about this situation you"
    " told me and try to answer this question to yourself. I bet you'll"
    " be fine and you can avoid or at least deal better with this same"
    " kind of situation in the future."
)

cc_death1 = (
    "<user>, death is part of life. The most important thing, then, is how we"
    " live and the good social connections we make during our journey. I'm"
    " sure you have amazing memories to remember. This way you can carry"
    " forever with you anyone you want! I'm sure you be fine one day,"
    " so let time works."
)

CC = [cc_msg1, cc_msg2]

CC_DEATH = [cc_death1]

# attentional deployment messages
ad_msg1 = (
    "<user>, this is an undesired <situation>situation, but I believe you"
    " should try to avoid thinking about it. I'm sure you have other nice"
    " things to stay focused on. Do this and I bet you'll feel better."
)

ad_msg2 = (
    "Hey, <user>, how about you thinking in anything else? I believe it's"
    " better to keep this <situation>situation out of your mind. For sure you"
    " have other stuff to occupy your head. You can even try to go out for a"
    " walk while listening some music, etc. when it's really hard to avoid"
    " such thoughts. I think this way you'll be fine."
)

# To avoid showing strange messages to the user in case of error.
ad_death1 = ges_msg1

AD = [ad_msg1, ad_msg2]

AD_DEATH = [ad_death1]

# situation selection messages
ss_msg1 = (
    "<user>, I think you can avoid this <situation>situation. For sure you"
    " have other important tasks or things to deal with, right? So stay"
    " focused on them, do what you have to do and let it go. This way I think"
    " you're gonna feel better."
)

ss_msg2 = (
    "Oh, <user>, this <situation>situation you told can be tough, indeed."
    " So that's why I think you must avoid it when it's possible. Do you think"
    " you can? If so, do the other things that for sure you have to do and try"
    " to avoid facing this situation. Let it go!"
)

ss_death1 = ges_msg1

SS = [ss_msg1, ss_msg2]

SS_DEATH = [ss_death1]

# situation modification messages
sm_msg1 = (
    "Hey, <user>, you know what? It's a difficult <situation>situation,"
    " indeed, but calm down and try to think about how you can change this"
    " situation. I'm sure you can. Just take a deep breath and start a list of"
    " actions you can perform right now to change it!"
)

sm_msg2 = (
    "Oh, <user>, I see that what you told isn't a good <situation>situation,"
    " for sure, but maybe you can realize that there are things to do in order"
    " to change it. Take your time, calm down and try to come up with a list"
    " of things you could do to improve this situation in order to feel better"
    " (and I bet you will)."
)

sm_death1 = (
    "<user>, it is hard and it happens with everyone. This is probably the"
    " only thing in life we can't do anything about. I would say that for now"
    " you need to make an effort in order to feel better So live your life"
    " using all the good things you learned from the important people that"
    " already have passed away. Let it go and one day you'll accept it. Maybe"
    " you need a few days off and then you should focus on the things you"
    " have to do."
)

SM = [sm_msg1, sm_msg2]

SM_DEATH = [sm_death1]

TEMPLATES = [[GES, GES_DEATH], [CC, CC_DEATH], [AD, AD_DEATH],
             [SS, SS_DEATH], [SM, SM_DEATH]]


def get_templates():
    return TEMPLATES
