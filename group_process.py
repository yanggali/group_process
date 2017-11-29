from file_process import group_event_to_id,groupid_users_to_id
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
#user\event id map
userid_eventid_file = "F:\\datasets\\group_recommendation\\formal\\userid_eventid.dat"
user_id_file = "F:\\datasets\\group_recommendation\\formal\\user_id.dat"
event_id_file = "F:\\datasets\\group_recommendation\\formal\\event_id.dat"
#user-group-event to id map
groupid_eventid_file = "F:\\datasets\\group_recommendation\\formal\\groupid_eventid.dat"
#groupid_users to groupid_userids
groupid_userids_file = "F:\\datasets\\group_recommendation\\formal\\groupid_userids.dat"
#无向
event_groupid_file = "F:\\datasets\\group_recommendation\\undirected\\event_groupid_file.dat"
groupid_users_file = "F:\\datasets\\group_recommendation\\undirected\\groupid_users_file.dat"
#有向
event_groupid_file_1 = "F:\\datasets\\group_recommendation\\formal\\event_groupid_file_1.dat"
groupid_users_file_1 = "F:\\datasets\\group_recommendation\\formal\\groupid_users_file_1.dat"

if __name__=="__main__":
    #write_to_tuple(event_attendees,user_event)
    #group_statistic(event_group_file_1,event_groupid_file_1,groupid_users_file_1)
    #initial_user_friends(event_attendees,user_friends,event_group_file_1,1)
    #user_event_to_id(user_event,user_id_file,event_id_file,userid_eventid_file)
    #group_event_to_id(event_groupid_file,event_id_file,groupid_eventid_file)
    groupid_users_to_id(groupid_users_file,user_id_file,groupid_userids_file)
