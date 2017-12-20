from plancast_file_process import initial_group_event,get_event_group,group_statistic,group_statistic_v2,write_to_file
from file_process import get_train_groupid_user,get_train_user_event,generate_test_candi
import pandas as pd
import random
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

# 初始化groupid_eventid和groupid_userids
groupid_eventid_file = "F:/datasets/Event-based Social Networks/Plancast_network/formal/groupid_eventid.dat"
groupid_userids_file = "F:/datasets/Event-based Social Networks/Plancast_network/formal/map/groupid_userids.dat"
groupid_userid_file = "F:/datasets/Event-based Social Networks/Plancast_network/formal/groupid_userid.dat"
# 划分训练集测试集
train_groupid_eventid_file = "F:/codebase/python/group_model/data/dataset/plancast/train_groupid_eventid.dat"
test_groupid_eventid_file = "F:/codebase/python/group_model/data/dataset/plancast/test_groupid_eventid.dat"
train_userid_eventid_file = "F:/codebase/python/group_model/data/dataset/plancast/train_userid_eventid.dat"
train_groupid_userids_file = "F:/codebase/python/group_model/data/dataset/plancast/train_groupid_userids.dat"
test_groupid_userids_file = "F:/codebase/python/group_model/data/dataset/plancast/test_groupid_userids.dat"
test_groupid_eventid_candis = "F:/codebase/python/group_model/data/dataset/plancast/test_groupid_eventid_candis.dat"
# 从group_event中随机抽取20%作为测试集
def get_test_group_event(group_event,test_group_event,train_group_event):
    df = pd.read_csv(group_event,sep="\t",names=["group","event"],engine="python")
    l = len(df)
    test_groupid_eventid_str = ""
    train_groupid_eventid_str = ""
    record = 0
    test_index_set = set()
    while record < l*0.2:
        rand_index = random.randint(0, l - 1)
        if rand_index not in test_index_set:
            test_groupid_eventid_str += str(int(df[df.index == rand_index]["group"]))+"\t"+str(int(df[df.index == rand_index]["event"]))+"\n"
            record += 1
            test_index_set.add(rand_index)
    write_to_file(test_group_event,test_groupid_eventid_str)
    for index,row in df.iterrows():
        if index not in test_index_set:
            train_groupid_eventid_str += str(row["group"])+"\t"+str(row["event"])+"\n"
    write_to_file(train_group_event,train_groupid_eventid_str)

if __name__ == "__main__":
    #initial_group_event(user_event_file,user_subscription_file,event_users_file)
    #get_event_group(event_users_file,event_group_file)
    #group_statistic_v2(event_group_file,event_groupid_file,groupid_users_file)
    #user_event_to_id(user_event_file,user_id_file,event_id_file,userid_eventid_file)
    #group_event_to_id(event_groupid_file,event_id_file,groupid_eventid_file)
    #groupid_users_to_id(groupid_users_file,user_id_file,groupid_userids_file)
    #groupid_userid_tuple(groupid_userids_file,groupid_userid_file)
    # 划分训练集测试集
    #get_test_group_event(groupid_eventid_file,test_groupid_eventid_file,train_groupid_eventid_file)
    #get_train_groupid_user(test_groupid_eventid_file,groupid_userids_file,test_groupid_userids_file)
    #get_train_user_event(test_groupid_eventid_file,groupid_userids_file,userid_eventid_file,train_userid_eventid_file)
    generate_test_candi(test_groupid_eventid_file,groupid_eventid_file,train_userid_eventid_file,
                        test_groupid_userids_file,train_groupid_userids_file,test_groupid_eventid_candis)