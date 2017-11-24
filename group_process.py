from file_process import write_to_tuple,test,relation_to_dict,initial_user_friends,relation_to_tuple
from plancast_file_process import group_statistic
user_friends = "F:\\datasets\\group_recommendation\\user_friends.csv\\user_friends.csv"
event_attendees = "F:\\datasets\\group_recommendation\\event_attendees.csv\\event_attendees.csv"
user_event = "F:\\datasets\\group_recommendation\\user_event.dat"
user_friend_tuple_file = "F:\\datasets\\group_recommendation\\user_friend.dat"
event_group_file = "F:\\datasets\\group_recommendation\\test_event_group_file.dat"
event_groupid_file = "F:\\datasets\\group_recommendation\\event_groupid_file.dat"
groupid_users_file = "F:\\datasets\\group_recommendation\\groupid_users_file.dat"
if __name__=="__main__":
    #write_to_tuple(event_users,user_event)
    #group_statistic(event_group_file,event_groupid_file,groupid_users_file)
    initial_user_friends(event_attendees,user_friends,event_group_file)
