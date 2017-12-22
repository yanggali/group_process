from plancast_file_process import initial_group_event


user_event_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/la_review.csv'
user_friend_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/la_user_friend.csv'
event_users_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/event_users.dat'
if __name__=="__main__":
    initial_group_event(user_event_file, user_friend_file, event_users_file)