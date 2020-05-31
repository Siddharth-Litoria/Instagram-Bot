# Instagram-Bot
Instagram Bot to like and comment on any of the followers in list

Description:this bot likes all the pic of the person from your followers list and also comments on all the pics.

Methods:-
login: login methods helps to login to instagram using your username and password and takes you to the main page of instagram after login.

profile: takes the parameter(USERNAME-OF-the person whose pics you want to like and comment on)

first_pic:takes you to  the first pic

like_pic:Likes pic if it was not liked previously

next_pic:next-pic.

continue_liking:to loop through all the pictures of the profile.

comment-has a list of comment which can be edited and takes random comments from  this list.


To run the project:

1.install selenium using -pip install selenium
2.Enter id and password in the my_bot
2.I would recommend to run this project on interactive mode in python :-

python -i Python_bot.py
Run the methods in the following order:
1.run the profile method using my_bot.login()
2.run the profile method using my_bot.profile("USERNAME OF person whose pics you want to like")
3.run the profile method using my_bot.first_pic()
4.run the profile method using my_bot.like_pic()
5.run the profile method using my_bot.comment()
6.run the profile method using my_bot.continue_Liking()




