from plancast_file_process import initial_group_event,get_event_group,group_statistic

user_event_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\plancast_user_event.csv"
user_subscription_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\plancast_user_subscription.csv"
groupid_users_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\groupid_users_file.dat"
event_groupid_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_groupid_file.dat"
event_users_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_users_file.dat"
event_group_file = "F:\\datasets\\Event-based Social Networks\\Plancast_network\\event_group_file.dat"
if __name__ == "__main__":
    #initial_group_event(user_event_file,user_subscription_file,event_users_file)
    get_event_group(event_users_file,event_group_file)
    group_statistic(event_group_file,event_groupid_file,groupid_users_file)