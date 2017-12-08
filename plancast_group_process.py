from plancast_file_process import initial_group_event,get_event_group,group_statistic,group_statistic_v2
from file_process import user_event_to_id,group_event_to_id,groupid_users_to_id,groupid_userid_tuple
user_event_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\plancast_user_event.csv"
user_subscription_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\plancast_user_subscription.csv"
groupid_users_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\groupid_users_file.dat"
event_groupid_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_groupid_file.dat"
event_users_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_users_file.dat"
event_group_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_group_file.dat"
#user to id,event to id,user_event to userid_eventid
user_id_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\map\\user_id.dat"
event_id_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\map\\event_id.dat"
userid_eventid_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\userid_eventid.dat"

#初始化groupid_eventid和groupid_userids
groupid_eventid_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\groupid_eventid.dat"
groupid_userids_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\map\\groupid_userids.dat"
groupid_userid_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\formal\\groupid_userid.dat"
if __name__ == "__main__":
    #initial_group_event(user_event_file,user_subscription_file,event_users_file)
    #get_event_group(event_users_file,event_group_file)
    #group_statistic_v2(event_group_file,event_groupid_file,groupid_users_file)
    #user_event_to_id(user_event_file,user_id_file,event_id_file,userid_eventid_file)
    #group_event_to_id(event_groupid_file,event_id_file,groupid_eventid_file)
    #groupid_users_to_id(groupid_users_file,user_id_file,groupid_userids_file)
    groupid_userid_tuple(groupid_userids_file,groupid_userid_file)