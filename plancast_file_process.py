import pandas as pd
from file_process import initial_adjacent_matrix,dfs,write_to_file
import sys
sys.setrecursionlimit(10000) #例如这里设置为一百万
#获取朋友关系
def initial_friends_relationship(user_subscription_file):
    col_names = ["user","subscription"]
    df = pd.read_csv(user_subscription_file,names=col_names)
    user_friends_dict = dict()
    for index,row in df.iterrows():
        if str(row["user"]) not in user_friends_dict:
            user_friends_dict[str(row["user"])] = [str(row["subscription"])]
        else:
            user_friends_dict[str(row["user"])].append(str(row["subscription"]))
    return user_friends_dict

#初始化group-user,group-event
def initial_group_event(user_event_file,user_subscription_file,event_users_file):
    event_group_str = ""
    group_user_str = ""
    group_users_dict = dict()
    group_event_dict = dict()
    user_friends_dict = initial_friends_relationship(user_subscription_file)
    print("initial friends relationship finished")
    col_names = ["user","event"]
    df = pd.read_csv(user_event_file,names=col_names)
    event_set = set(df["event"].unique())
    for event in event_set:
        users_list = [str(i) for i in list(df["user"][df.event==event])]
        vertex = len(users_list)
        user_index_dict = dict()
        index_user_dict = dict()
        for user in users_list:
            user_index_dict[user] = int(len(user_index_dict))
            index_user_dict[len(index_user_dict)] = user
        #初始化邻接矩阵
        adjacent_matrix = initial_adjacent_matrix(users_list,user_index_dict,user_friends_dict)
        visited_list = [0 for i in range(vertex)]

        # 计算连通分图
        connect_set = set()
        for i in range(vertex):
            if visited_list[i] != 1:
                connect_set.clear()
                visited_list[i] = 1
                #找到一个group
                dfs(i, vertex, visited_list, adjacent_matrix, index_user_dict, connect_set)
                #print(connect_set)
                # if connect_set not in group_users_dict.values():
                #     group_users_dict[len(group_users_dict)] = connect_set
                users_str = ""
                for user in connect_set:
                    users_str += str(user)+" "
                event_group_str += str(event)+"::"+users_str+"\n"
        print("event " + str(event) + " finished")
    write_to_file(event_users_file,event_group_str)

#将group人数超过2个的挑选出来
def get_event_group(event_users_file,event_group_file):
    col_names = ["event","users"]
    event_group_str = ""
    df = pd.read_csv(event_users_file,sep="::",header=None,names=col_names,engine='python')
    for index,row in df.iterrows():
        if len(str(row["users"]).split(" ")) > 1:
            event_group_str += str(row["event"])+"::"+str(row["users"])+"\n"
    write_to_file(event_group_file,event_group_str)

#统计group数目
def group_statistic(event_group_file,event_groupid_file,groupid_users_file):
    col_names = ["event","group"]
    df = pd.read_csv(event_group_file,header=None,sep="\t",names=col_names,engine="python")
    group_list = []
    for index,row in df.iterrows():
        group = set(str(row["group"]).split(" "))
        if group not in group_list:
            group_list.append(group)
    event_groupid_str = ""
    groupid_users_str = ""
    for index,row in df.iterrows():
        id = group_list.index(set(str(row["group"]).split(" ")))
        event_groupid_str += str(row["event"])+"\t"+str(id)+"\n"
        groupid_users_str += str(id)+"\t"+str(row["group"])+"\n"
    write_to_file(event_groupid_file,event_groupid_str)
    write_to_file(groupid_users_file,groupid_users_str)


#得到set的hash值
def get_hash_code(group):
    hash_code = ""
    for user in group:
        hash_code += str(user)
    return hash_code
