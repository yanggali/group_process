from plancast_file_process import initial_group_event,group_statistic_v2
from plancast_group_process import get_test_group_event
from file_process import user_event_to_id,group_event_to_id,groupid_users_to_id,groupid_userid_tuple,\
    group_event_to_id,groupid_users_to_id,get_train_groupid_user,get_train_user_event,generate_test_candi

user_event_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/la_review.csv'
user_friend_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/la_user_friend.csv'
event_users_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/event_users.dat'
groupid_event_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/groupid_event.dat'
groupid_users_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/groupid_users.dat'
user_id_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/map/user_id.dat'
event_id_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/map/event_id.dat'
userid_eventid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/userid_eventid.dat'
groupid_eventid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/groupid_eventid.dat'
groupid_userids_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/groupid_userids.dat'
groupid_userid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/groupid_userid.dat'
# 划分训练集测试集
test_groupid_eventid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/test/test_groupid_eventid'
test_groupid_userids_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/test/test_groupid_userids.dat'
test_groupid_eventid_candis = 'C:/Users/uqjyan18/Documents/datasets/yelp/test/test_groupid_eventids.dat'
train_groupid_eventid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/train/train_groupid_eventid'
train_userid_eventid_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/train/train_userid_eventid'
train_groupid_userids_file = 'C:/Users/uqjyan18/Documents/datasets/yelp/train/train_groupid_eventid_candis.dat'

if __name__=="__main__":
    #initial_group_event(user_event_file, user_friend_file, event_users_file)
    #group_statistic_v2(event_users_file,groupid_event_file,groupid_users_file)
    #user_event_to_id(user_event_file,user_id_file,event_id_file,userid_eventid_file)
    #group_event_to_id(groupid_event_file,event_id_file,groupid_eventid_file)
    #groupid_users_to_id(groupid_users_file,user_id_file,groupid_userids_file)
    #groupid_userid_tuple(groupid_userids_file, groupid_userid_file)
    # 划分训练集测试集
    #get_test_group_event(groupid_eventid_file,test_groupid_eventid_file,train_groupid_eventid_file)
    #get_train_groupid_user(test_groupid_eventid_file,groupid_userids_file,test_groupid_userids_file)
    #get_train_user_event(test_groupid_eventid_file,groupid_userids_file,userid_eventid_file,train_userid_eventid_file)
    generate_test_candi(test_groupid_eventid_file, groupid_eventid_file, train_userid_eventid_file,
                        test_groupid_userids_file, train_groupid_userids_file, test_groupid_eventid_candis)