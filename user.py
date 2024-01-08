import instaloader
user = input("Enter your username: ")
L= instaloader.Instaloader()
L.download_profile(user, profile_pic_only=False)