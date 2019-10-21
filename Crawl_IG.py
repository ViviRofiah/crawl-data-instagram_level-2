# Import Library
import instaloader
import json
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()
            
L = instaloader.Instaloader()

# Login or load session
L.login("username", "password")        # (login)
print("instagram login succes\nInstaloader ready to use \n")

# Obtain profile metadata

queue = []
passed = []

target = ("username target")
queue.append(instaloader.Profile.from_username(L.context, target))

while len(queue) is not 0 :
    profile_target = queue.pop()
    
    #profile_target = instaloader.Profile.from_username(L.context, target)
    print("Instagram target found. username target:", profile_target)
    print("\n")


    if target in passed : continue

    
#follow_list = []
    file_json = open ("dataName.json", "a")
    save = [] #array for follower data from profle_target

    liked = set()
    kumpulan_kata = []
    print("process data retrieval... \n")
    #looping followers dari profile target
    for follower in profile_target.get_followers():
        follower_target = follower.username

        #looping one of follower post
        print("getting all datas from @" + follower_target)
        profile = instaloader.Profile.from_username(L.context, follower_target)
        #follow_list.append(follower_target)
        post_count = 1 #the count of post

    
        for post in profile.get_posts():
            caption_post = post.caption
            tag = post.caption_hashtags
            likes_count = post.likes
            liked = liked | set(post.get_likes())
       
            if caption_post is None: #if the post not have caption
                caption_post = None
                 
            if caption_post is not None: #if the post have caption
                datapost = caption_post.encode('ascii', 'ignore').decode('ascii')
                data_post = re.sub(r'[^\w\s]','',datapost)
                fix_caption = stemmer.stem(data_post)
                #test
                x = fix_caption.split(" ")
                for key in x :
                    kumpulan_kata.append(key)
                    #print (key)
                print("caption : ", x)

        #test
            print("hashtag : ", tag)
            print("count likes :", likes_count)

            comments_box = []
            for comment in post.get_comments():
                data_comment = comment.text.encode('ascii', 'ignore').decode('ascii')
                comments_box.append(data_comment)
                #test
            print("comment :", comments_box)
            print("\n")
            data = {"account" : follower_target, "caption": fix_caption, "hastag" : tag, "likes": likes_count, "komen": comments_box}
            save.append(data)
        
            post_count = post_count + 1

    print('Ghost followers of {}.'.format(profile.username))
    followerss = set(profile.get_followers())
    ghost = (followerss - liked)
    print(ghost)
       
    print(kumpulan_kata)

    data_dict = {}
    for words in kumpulan_kata :
        if words not in data_dict.keys():
            data_dict[words] = 0
            #print('berhasil menambahkan kata', words)
    print(data_dict)
    save.append(data_dict)
    print('\n')

    for follower in profile_target.get_followers():
        queue.append(follower)
    passed.append(profile_target)

    
    data_json = json.dumps(save)
    file_json.write(data_json)
    file_json.close()

