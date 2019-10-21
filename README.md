# crawl-data-instagram_level-2
This Instagram crawl contains how we get data from target followers using the BFS algorithm, then search for bag of words from the caption post, and look for ghost followers


#This is instagram crawl
 what you can do with this program :
 - get instagram post/profile/hastag/comment/likes data without using Instagram API. the code in 'Crawl_IG.py'
 - get bag of words from the caption 
 - crawl data followers target with the BFS algoritm
 - get ghost follower
 
#Install
 - install instaloader, 'pip Install Instaloader'
 - install json if you want to save data with json like this code. 'pip install jsonlib'
 - install regex tu remove punctuation. 'pip install regex'
 - install sastrawi to remove conjuction. 'pip install Sastrawi'

##Crawler
###Usage
  - positional arguments :
    mode options : [post(caption), hashtag, likes, komen]
  - 
  - optional arguments :
     username         --- instagram's username 
     hashtag          --- istagram's tag name/hashtag
     likes            --- count of how much post likes
     comment          --- comment of instagram's post
     ghost followers  --- get the ghost follower from user
     
  - Output :
    output file name(json format)


   #####
   you must login with instagram's account what you have to run instaloader library in this program.
   write username and password

   if login succes, you need the user target to get the data
   'target' is who the instagram's account target you want, write username target

   after that, the program will check the follower of target to put into the list
   program will open the profile of user target and get the follower of user target.
   and then open one by one follower of user target to get data as post caption, hashtag, likes and comment, and ghost followers. then, the program will do the same to get the followers of target's followers
   
   this program crawl the followers with BFS algorithm

   if the looping finish, the data will be saved to json format

 
