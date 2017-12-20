from file_process import relation_to_dict,initial_adjacent_matrix,dfs,write_to_file,append_to_file,user_event_to_id,group_event_to_id,groupid_users_to_id,groupid_userid_tuple,get_train_groupid_user,get_train_user_event,generate_test_candi
from plancast_file_process import group_statistic,group_statistic_v2
import pandas as pd
import sys
sys.setrecursionlimit(100000)
#input
douban_user_follows_file = "F:\\datasets\\douban\\raw dataset\\user_follow.csv"
douban_user_event_file = "F:\\datasets\\douban\\raw dataset\\user_event.csv"
douban_event_users_file = "F:\\datasets\\douban\\raw dataset\\event_users.dat"
user_event_file = "F:\\datasets\\douban\\raw dataset\\formal\\user_event.dat"

#output
#user\event to id map
userid_eventid_file = "F:\\datasets\\douban\\raw dataset\\formal\\userid_eventid.dat"
user_id_file = "F:\\datasets\\douban\\raw dataset\\formal\\user_id.dat"
event_id_file = "F:\\datasets\\douban\\raw dataset\\formal\\event_id.dat"

#output 有向
douban_event_group_file_1 = "F:\\datasets\\douban\\raw dataset\\directed\\event_group_1.dat"
douban_big_event_file_1 = "F:\\datasets\\douban\\raw dataset\\bigevent_users_1.dat"

#用group_statistic_v2来统计
test_event_groupid_file_1 = "F:\\datasets\\douban\\raw dataset\\formal\\test_event_groupid_1.dat"
test_groupid_users_file_1 = "F:\\datasets\\douban\\raw dataset\\formal\\test_groupid_users_1.dat"


douban_event_groupid_file_1 = "F:\\datasets\\douban\\raw dataset\\formal\\event_groupid_1.dat"
douban_groupid_users_file_1 = "F:\\datasets\\douban\\raw dataset\\formal\\groupid_users_uniq.dat"
#将event_groupid映射到groupid_eventid,groupid_users映射到groupid_userids
douban_groupid_eventid_file = "F:\\datasets\\douban\\raw dataset\\formal\\groupid_eventid_1.dat"
douban_groupid_userids_file = "F:\\datasets\\douban\\raw dataset\\formal\\map\\groupid_userids.dat"
douban_groupid_userid_file = "F:\\datasets\\douban\\raw dataset\\formal\\groupid_userid.dat"
def write_to_event_users_file(user_events_file,event_users_file):
    df = pd.read_csv(user_events_file)
    event_users_str = ""
    event_users_dict = dict()
    for index, row in df.iterrows():
        for event in str(row["event_id"]).split(" "):
            if event not in event_users_dict:
                event_users_dict[event] = [str(row["uid"])]
            else:
                event_users_dict[event].append(str(row["uid"]))
    for event,users in event_users_dict.items():
        event_users_str += event+"\t"
        for user in users:
            event_users_str += user+" "
        event_users_str+="\n"
    write_to_file(event_users_file,event_users_str)
def initial_event_group(event_users_file,user_follows_file,event_group_file,big_event_file):
    user_friends_dict = relation_to_dict(user_follows_file)
    event_group_str = ""
    big_event_file_str = ""
    df = pd.read_csv(event_users_file,sep="\t",header=None,names=["event","users"],engine="python")

    for index,row in df.iterrows():
        if index%2000 == 0:
            append_to_file(event_group_file,event_group_str)
            event_group_str = ""
        attendees_list = str(row["users"]).split(" ")
        vertex = len(attendees_list)
        attendee_index_dict = {attendee:attendees_list.index(attendee) for attendee in attendees_list}
        index_attendee_dict = {attendees_list.index(attendee):attendee for attendee in attendees_list}
        # 初始化邻接矩阵
        adjacent_matrix = initial_adjacent_matrix(attendees_list, attendee_index_dict, user_friends_dict,1)
        visited_list = [0 for i in range(vertex)]
        connect_set = set()
        # 计算连通分图
        for i in range(vertex):
            if visited_list[i] != 1:
                connect_set.clear()
                visited_list[i] = 1
                dfs(i, vertex, visited_list, adjacent_matrix, index_attendee_dict, connect_set)
                if len(connect_set) > 1:
                    users_str = ""
                    for user in connect_set:
                        users_str += str(user) + " "
                    events = str(row["event"]).split(" ")
                    if len(events) == 1:
                        event_group_str += str(row["event"]) + "\t" + users_str + "\n"
                    else:
                        for event in events:
                            event_group_str += event + "\t" + users_str + "\n"
        print("event "+str(row["event"])+" finished")
    append_to_file(event_group_file,event_group_str)

train_groupid_eventid = "F:/codebase/python/group_model/data/dataset/douban/train_groupid_eventid.dat"
test_groupid_eventid = "F:/codebase/python/group_model/data/dataset/douban/test_groupid_eventid.dat"
groupid_userids = "F:/codebase/python/group_model/data/dataset/douban/groupid_userids.dat"
train_groupid_userids = "F:/codebase/python/group_model/data/dataset/douban/train_groupid_userids.dat"
test_groupid_userids = "F:/codebase/python/group_model/data/dataset/douban/test_groupid_userids.dat"
user_event = "F:/codebase/python/group_model/data/dataset/douban/userid_eventid.dat"
train_user_event = "F:/codebase/python/group_model/data/dataset/douban/train_userid_eventid.dat"
groupid_eventid = "F:/codebase/python/group_model/data/dataset/douban/groupid_eventid.dat"
test_groupid_eventid_candis = "F:/codebase/python/group_model/data/dataset/douban/test_groupid_eventid_candis.dat"
if __name__=="__main__":
    #write_to_event_users_file(douban_user_event_file,douban_event_users_file)
    #initial_event_group(douban_event_users_file,douban_user_follows_file,douban_event_group_file_1,douban_big_event_file_1)
    #group_statistic_v2(douban_event_group_file_1, test_event_groupid_file_1, test_groupid_users_file_1)
    #user_event_to_id(user_event_file,user_id_file,event_id_file,userid_eventid_file)
    #group_event_to_id(douban_event_groupid_file_1,event_id_file,douban_groupid_eventid_file)
    #groupid_users_to_id(douban_groupid_users_file_1,user_id_file,douban_groupid_userids_file)
    # 抽取train groupid_userids
    #get_train_groupid_user(test_groupid_eventid,groupid_userids,test_groupid_userids)
    # 根据train_groupid_event抽取train_user_event
    # get_train_user_event(test_groupid_eventid,groupid_userids,user_event,train_user_event)
    generate_test_candi(test_groupid_eventid, groupid_eventid, train_user_event, test_groupid_userids,
                        train_groupid_userids,test_groupid_eventid_candis)