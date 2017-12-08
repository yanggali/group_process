from file_process import group_event_to_id,groupid_users_to_id,groupid_userid_tuple,get_train_user_event,get_train_groupid_user
from plancast_file_process import group_statistic
user_friends = "F:\\datasets\\group_recommendation\\user_friends.csv\\user_friends.csv"
event_attendees = "F:\\datasets\\group_recommendation\\event_attendees.csv\\event_attendees.csv"
#output
user_event = "F:\\datasets\\group_recommendation\\formal\\raw data\\user_event.dat"
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
groupid_userids_file = "F:\\datasets\\group_recommendation\\formal\\map\\groupid_userids.dat"
groupid_userid_file = "F:\\datasets\\group_recommendation\\formal\\groupid_userid.dat"
#无向
event_groupid_file = "F:\\datasets\\group_recommendation\\undirected\\event_groupid_file.dat"
groupid_users_file = "F:\\datasets\\group_recommendation\\undirected\\groupid_users_file.dat"
#有向
event_groupid_file_1 = "F:\\datasets\\group_recommendation\\formal\\event_groupid_file_1.dat"
groupid_users_file_1 = "F:\\datasets\\group_recommendation\\formal\\groupid_users_file_1.dat"

# 划分训练集
groupid_users = "F:\\datasets\\group_recommendation\\formal\\raw data\\groupid_users_file.dat"
test_event_group = "F:\\datasets\\group_recommendation\\formal\\test\\test_groupid_event.dat"
train_event_group = "F:\\datasets\\group_recommendation\\formal\\train\\train_groupid_event.dat"
train_user_event = "F:\\datasets\\group_recommendation\\formal\\train\\train_user_event.dat"
groupid_users = "F:\\datasets\\group_recommendation\\formal\\raw data\\groupid_users_file.dat"
train_groupid_users = "F:\\datasets\\group_recommendation\\formal\\train\\train_groupid_users.dat"
if __name__=="__main__":
    #get_train_user_event(test_event_group,groupid_users,user_event,train_user_event)
    get_train_groupid_user(train_event_group,groupid_users,train_groupid_users)