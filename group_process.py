from file_process import write_to_tuple,test,relation_to_dict,initial_user_friends,relation_to_tuple
from plancast_file_process import group_statistic
user_friends = "F:\\datasets\\group_recommendation\\user_friends.csv\\user_friends.csv"
event_attendees = "F:\\datasets\\group_recommendation\\event_attendees.csv\\event_attendees.csv"
#output
user_event = "F:\\datasets\\group_recommendation\\user_event.dat"
user_friend_tuple_file = "F:\\datasets\\group_recommendation\\user_friend.dat"
event_group_file = "F:\\datasets\\group_recommendation\\undirected\\test_event_group_file.dat"
event_group_file_1 = "F:\\datasets\\group_recommendation\\directed\\event_group_file_1.dat"
#有向无向同时进行构造event_group
event_group_file_0 = "F:\\datasets\\group_recommendation\\test\\test_event_group_file_0.dat"
event_group_file_1 = "F:\\datasets\\group_recommendation\\test\\test_event_group_file_1.dat"

#无向
event_groupid_file = "F:\\datasets\\group_recommendation\\undirected\\event_groupid_file.dat"
groupid_users_file = "F:\\datasets\\group_recommendation\\undirected\\groupid_users_file.dat"
#有向
event_groupid_file_1 = "F:\\datasets\\group_recommendation\\directed\\event_groupid_file_1.dat"
groupid_users_file_1 = "F:\\datasets\\group_recommendation\\directed\\groupid_users_file_1.dat"

if __name__=="__main__":
    #write_to_tuple(event_users,user_event)
    #group_statistic(event_group_file_1,event_groupid_file_1,groupid_users_file_1)
    initial_user_friends(event_attendees,user_friends,event_group_file_1,1)
