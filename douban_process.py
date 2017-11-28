from file_process import relation_to_dict,initial_adjacent_matrix,dfs,write_to_file,append_to_file
from plancast_file_process import group_statistic
import pandas as pd
import sys
sys.setrecursionlimit(100000)
#input
douban_user_follows_file = "F:\\datasets\\douban\\raw dataset\\user_follow.csv"
douban_user_event_file = "F:\\datasets\\douban\\raw dataset\\user_event.csv"
douban_event_users_file = "F:\\datasets\\douban\\raw dataset\\event_users.dat"
#output 无向
douban_event_group_file = "F:\\datasets\\douban\\raw dataset\\event_group.dat"
douban_big_event_file = "F:\\datasets\\douban\\raw dataset\\bigevent_users.dat"
douban_event_groupid_file = "F:\\datasets\\douban\\raw dataset\\event_groupid_0.dat"
douban_groupid_users_file = "F:\\datasets\\douban\\raw dataset\\groupid_users_0.dat"
#output 有向
douban_event_group_file_1 = "F:\\datasets\\douban\\raw dataset\\event_group_1.dat"
douban_big_event_file_1 = "F:\\datasets\\douban\\raw dataset\\bigevent_users_1.dat"

douban_event_groupid_file_1 = "F:\\datasets\\douban\\raw dataset\\event_groupid_1.dat"
douban_groupid_users_file_1 = "F:\\datasets\\douban\\raw dataset\\groupid_users_1.dat"

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
        if len(attendees_list) > 1000:
            big_event_file_str += str(row["event"])+"\t"
            for attendee in attendees_list:
                big_event_file_str += attendee+" "
            big_event_file_str += "\n"
            append_to_file(big_event_file,big_event_file_str)
            big_event_file_str = ""
            continue
        if index/1000 == 0:
            append_to_file(event_group_file,event_group_str)
            event_group_str = ""
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

if __name__=="__main__":
    #write_to_event_users_file(douban_user_event_file,douban_event_users_file)
    #initial_event_group(douban_event_users_file,douban_user_follows_file,douban_event_group_file_1,douban_big_event_file_1)
    group_statistic(douban_event_group_file_1, douban_event_groupid_file_1, douban_groupid_users_file_1)