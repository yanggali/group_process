import pandas as pd
import numpy as np
import random
import sys
import os
sys.setrecursionlimit(100000) #例如这里设置为一百万
def test(event_attendee_file):
    df = pd.read_csv(event_attendee_file)
    user_set = set()
    for index,row in df.iterrows():
        user_list = str(row["yes"]).split(" ")
        for user in user_list:
            user_set.add(user)
    print("total user num: %d" % len(user_set))

#将活动转换成<user,event>二元组
def write_to_tuple(event_attendee_file,user_event_file):
    df = pd.read_csv(event_attendee_file)
    print("total event number:%d" % len(df))
    write_str = ''
    for index,row in df.iterrows():
        event_list = str(row["event"]).split(" ")
        user_list = str(row["yes"]).split(' ')
        if len(user_list) == 1 and str(row["yes"])!="nan":
            continue
        for event in event_list:
            for user in user_list:
                write_str += user+" "+event+"\n"
    write_to_file(user_event_file,write_str)

#根据event_attendees和朋友关系获取group以及group参加的活动
def initial_user_friends(event_attedees_file,user_friends_file,event_group_file,direct):
    user_friends_dict = relation_to_dict(user_friends_file)
    event_group_str = ""
    df = pd.read_csv(event_attedees_file)
    for index,row in df.iterrows():
        if index%1000 == 0:
            append_to_file(event_group_file,event_group_str)
            event_group_str = ""
        attendees_list = str(row["yes"]).split(" ")
        vertex = len(attendees_list)
        attendee_index_dict = dict()
        index_attendee_dict = dict()
        for attendee in attendees_list:
            attendee_index_dict[attendee] = int(len(attendee_index_dict))
            index_attendee_dict[len(index_attendee_dict)] = attendee
        #初始化邻接矩阵
        #好友关系无向
        adjacent_matrix = initial_adjacent_matrix(attendees_list,attendee_index_dict,user_friends_dict,direct)
        visited_list = [0 for i in range(vertex)]
        connect_set = set()
        #计算连通分图
        for i in range(vertex):
            if visited_list[i] != 1:
                connect_set.clear()
                visited_list[i] = 1
                dfs(i,vertex,visited_list,adjacent_matrix,index_attendee_dict,connect_set)
                if len(connect_set) > 1:
                    users_str = ""
                    for user in connect_set:
                        users_str += str(user)+" "
                    events = str(row["event"]).split(" ")
                    if len(events) == 1:
                        event_group_str += str(row["event"]) + "\t"+users_str+"\n"
                    else:
                        for event in events:
                            event_group_str += event + "\t" + users_str + "\n"

        print("event "+ str(row["event"])+" finished.")
    append_to_file(event_group_file,event_group_str)


#深度优先搜索查找
def dfs(root,vertex,visited_list,adjacent_matrix,index_attendee_dict,connect_set):
    #print(index_attendee_dict.get(root)+" ")
    connect_set.add(index_attendee_dict.get(root))
    for i in range(vertex):
        if visited_list[i] != 1 and adjacent_matrix[root][i] == 1:
            visited_list[i] = 1
            dfs(i,vertex,visited_list,adjacent_matrix,index_attendee_dict,connect_set)
    #return index_attendee_dict[root] + " "

#初始化邻接矩阵并返回
def initial_adjacent_matrix(attendee_list,attendee_index_dict,user_friends_dict,direct = 0):
    adjacent_matrix = np.zeros((len(attendee_list),len(attendee_list)))
    #朋友关系之间是无向的
    if direct == 0:
        for u in attendee_list:
            for v in attendee_list[attendee_index_dict[u]+1:]:
                v_friends = user_friends_dict.get(v, 'nan')
                u_friends = user_friends_dict.get(u, 'nan')
                if (u in v_friends) or (v in u_friends):
                    adjacent_matrix[attendee_index_dict[u]][attendee_index_dict[v]] = 1
                    adjacent_matrix[attendee_index_dict[v]][attendee_index_dict[u]] = 1
    #朋友关系之间是有向的
    else:
        for u in attendee_list:
            for v in attendee_list[attendee_index_dict[u]+1:]:
                v_friends = user_friends_dict.get(v, 'nan')
                u_friends = user_friends_dict.get(u, 'nan')
                if (u in v_friends) and (v in u_friends):
                    adjacent_matrix[attendee_index_dict[u]][attendee_index_dict[v]] = 1
                    adjacent_matrix[attendee_index_dict[v]][attendee_index_dict[u]] = 1
    return adjacent_matrix

#将朋友关系初始化到dict中
def relation_to_dict(user_friends_file,col_names = ["user","friends"]):
    df = pd.read_csv(user_friends_file,names = col_names)
    user_friends_dict = dict()
    for index,row in df.iterrows():
        if str(row["friends"])!="nan":
            friends = str(row["friends"]).split(" ")
            if str(row["user"]).split(" ") == 1:
                user_friends_dict[str(row["user"])] = friends
            else:
                for user in str(row["user"]).split(" "):
                    user_friends_dict[user] = friends
    print("user_friends' user set size: %d" % len(user_friends_dict))
    return user_friends_dict

#将朋友关系转换成二元组到文件
def relation_to_tuple(user_friends_file,user_friend_tuple_file):
    user_friend_tuple = ''
    df = pd.read_csv(user_friends_file)
    for index,row in df.iterrows():
        users = str(row["user"]).split(" ")
        friends = str(row["friends"]).split(" ")
        if len(users) == 1:
            for friend in friends:
                user_friend_tuple += users[0]+" "+friend+"\n"
        else:
            for user in users:
                for friend in friends:
                    user_friend_tuple += user+" "+friend+"\n"
    write_to_file(user_friend_tuple_file,user_friend_tuple)

#将user和event映射到id，将user_event表映射到userid_eventid表
def user_event_to_id(user_event_file,user_id_map_file,event_id_map_file,userid_eventid_map_file):
    #df = pd.read_csv(user_event_file,sep="\t",names=["user","event"],engine="python")
    df = pd.read_csv(user_event_file,names=["user","event"])
    user_set = set(df["user"].unique())
    event_set = set(df["event"].unique())
    user_id_dict = {}
    event_id_dict = {}
    for user in user_set:
        user_id_dict[user] = len(user_id_dict)
    print("user id dict finished")
    for event in event_set:
        event_id_dict[event] = len(event_id_dict)
    print("event id dict finished")
    user_id_str = ""
    event_id_str = ""
    for user,id in user_id_dict.items():
        user_id_str += str(user)+"\t"+str(id)+"\n"
    write_to_file(user_id_map_file,user_id_str)
    user_id_str = ""
    print("user id map finished")
    for event,id in event_id_dict.items():
        event_id_str += str(event)+"\t"+str(id)+"\n"
    write_to_file(event_id_map_file,event_id_str)
    event_id_str = ""
    print("event id map finished")

    #将user_event转换成userid_eventid
    if os.path.exists(userid_eventid_map_file):
        os.remove(userid_eventid_map_file)
    userid_eventid_str = ""
    for index,row in df.iterrows():
        if index%1000 == 0:
            append_to_file(userid_eventid_map_file,userid_eventid_str)
            userid_eventid_str = ""
        userid_eventid_str += str(user_id_dict[row["user"]])+"\t"+str(event_id_dict[row["event"]])+"\n"
    append_to_file(userid_eventid_map_file,userid_eventid_str)


# 将event_groupid保存到groupid_eventid
def group_event_to_id(event_groupid_file,event_id_file,groupid_eventid_file):
    event_id_df = pd.read_csv(event_id_file,sep="\t",names=["event","id"],engine="python")
    event_id_dict = dict()
    # 从event_id映射表中读取event_id映射关系
    for index,row in event_id_df.iterrows():
        event_id_dict[row["event"]] = row["id"]
    # 将event_groupid改写成groupid_eventid
    event_groupid_df = pd.read_csv(event_groupid_file,sep="\t",names=["event","groupid"],engine="python")
    if os.path.exists(groupid_eventid_file):
        os.remove(groupid_eventid_file)
    groupid_eventid_str = ""
    for index,row in event_groupid_df.iterrows():
        if index%1000 == 0:
            append_to_file(groupid_eventid_file,groupid_eventid_str)
            groupid_eventid_str = ""
        groupid_eventid_str += str(row["groupid"])+"\t"+str(event_id_dict[row["event"]])+"\n"
    append_to_file(groupid_eventid_file,groupid_eventid_str)


# 将groupid_users改写成groupid_userids
def groupid_users_to_id(groupid_users_file,user_id_file,groupid_userids_file):
    user_id_df = pd.read_csv(user_id_file, sep="\t", names=["user", "id"], engine="python")
    user_id_dict = dict()
    # 从event_id映射表中读取event_id映射关系
    for index, row in user_id_df.iterrows():
        user_id_dict[row["user"]] = row["id"]
    # 将groupid_users映射到groupid_userids
    groupid_users_df = pd.read_csv(groupid_users_file,sep="\t",names=["groupid","users"],engine="python")
    groupid_userids_str = ""
    if os.path.exists(groupid_userids_file):
        os.remove(groupid_userids_file)
    for index,row in groupid_users_df.iterrows():
        if index%1000 == 0:
            append_to_file(groupid_userids_file,groupid_userids_str)
            groupid_userids_str = ""
        userids_str = ""
        for user in str(row["users"]).strip().split(" "):
            userids_str += str(user_id_dict[int(user)])+" "
        groupid_userids_str += str(row["groupid"])+"\t"+userids_str.strip()+"\n"
    append_to_file(groupid_userids_file,groupid_userids_str)


# 统计数据集信息
# 将groupid_userids转换成groupid_userid二元组
def groupid_userid_tuple(groupid_userids_file,groupid_userid_file):
    df = pd.read_csv(groupid_userids_file,sep="\t",names=["groupid","userids"],engine="python")
    if os.path.exists(groupid_userid_file):
        os.remove(groupid_userid_file)
    groupid_userid_str = ""
    for index,row in df.iterrows():
        if index%1000 ==0:
            append_to_file(groupid_userid_file,groupid_userid_str)
            groupid_userid_str = ""
        for userid in str(row["userids"]).strip().split(" "):
            groupid_userid_str += str(row["groupid"])+"\t"+userid+"\n"
    append_to_file(groupid_userid_file,groupid_userid_str)


# 划分训练集
# 根据test_event_groupid,group_users将user_event中的test event去除
def get_train_user_event(test_group_event,groupid_users,user_event,train_user_event):
    event_groupid_df = pd.read_csv(test_group_event,sep="\t",names=["groupid","event"],engine="python")
    groupid_users_df = pd.read_csv(groupid_users,sep="\t",names=["groupid","users"],engine="python")
    user_event_df = pd.read_csv(user_event,sep="\t",names=["user","event"],engine="python")
    group_users_dict = dict()
    for index,row in groupid_users_df.iterrows():
        group_users_dict[row["groupid"]] = [int(user) for user in str(row["users"]).strip().split(" ")]
    event_groups_dict = dict()
    for index,row in event_groupid_df.iterrows():
        if row["event"] not in event_groups_dict:
            event_groups_dict[row["event"]] = [row["groupid"]]
        else:
            event_groups_dict[row["event"]].append(row["groupid"])
    train_user_event_str = ""
    test_events = set(event_groupid_df["event"].unique())
    if os.path.exists(train_user_event):
        os.remove(train_user_event)
    for index,row in user_event_df.iterrows():
        if index%10000 == 0:
            append_to_file(train_user_event,train_user_event_str)
            train_user_event_str = ""
        if row["event"] not in test_events:
            train_user_event_str += str(row["user"])+"\t"+str(row["event"])+"\n"
        else:
            groups = event_groups_dict.get(row["event"])
            users = set()
            for group in groups:
                users.update(group_users_dict.get(group))
            if int(row["user"]) not in users:
                train_user_event_str += str(row["user"]) + "\t" + str(row["event"]) + "\n"
        print("%d row finshed" % index)
    append_to_file(train_user_event,train_user_event_str)


# 获取训练集的group以及user
def get_train_groupid_user(train_group_event,groupid_users,train_groupid_users):
    event_groupid_df = pd.read_csv(train_group_event, sep="\t", names=["groupid", "event"], engine="python")
    groupid_users_df = pd.read_csv(groupid_users, sep="\t", names=["groupid", "users"], engine="python")
    train_groupid_user_str = ""
    groupid_set = set(event_groupid_df["groupid"].unique())
    if os.path.exists(train_groupid_users):
        os.remove(train_groupid_users)
    for index,row in groupid_users_df.iterrows():
        if index%10000 == 0:
            append_to_file(train_groupid_users,train_groupid_user_str)
            train_groupid_user_str = ""
        if row["groupid"] in groupid_set:
            train_groupid_user_str += str(row["groupid"]) + "\t"
            for user in str(row["users"]).strip().split(" "):
                train_groupid_user_str += user+" "
            train_groupid_user_str = train_groupid_user_str.strip()+"\n"
    append_to_file(train_groupid_users,train_groupid_user_str)


def get_group_users(inputfile,col_names=["groupid","users"],sep="\t"):
    df = pd.read_csv(inputfile,sep=sep,names=col_names,engine="python")
    group_users = dict()
    for index,row in df.iterrows():
        group_users[row["groupid"]] = [int(member) for member in list(str(row["users"]).strip().split(" "))]
    return group_users


def read_file(inputfile,col_names,flag = 1,sep="\t"):
    df = pd.read_csv(inputfile,sep=sep,names=col_names,engine="python")
    if flag == 1:
        col1 = col_names[0]
        col2 = col_names[1]
    else:
        col1 = col_names[1]
        col2 = col_names[0]
    ver1_neighbours = dict()
    for index,row in df.iterrows():
        if row[col1] not in ver1_neighbours:
            ver1_neighbours[row[col1]] = [row[col2]]
        else:
            ver1_neighbours[row[col1]].append(row[col2])
    return ver1_neighbours


# 生成1000个测试样例
def generate_test_candi(test_group_event_file,group_event_file,train_user_event_file,test_group_users_file,train_group_users_file,test_group_event_candi_file):
    if os.path.exists(test_group_event_candi_file):
        os.remove(test_group_event_candi_file)
    test_group_users = get_group_users(test_group_users_file)
    group_events_dict = read_file(group_event_file,["group","event"],1)
    user_events_dict = read_file(train_user_event_file,["user","event"],1)
    user_event_df = pd.read_csv(train_user_event_file,sep="\t",names=["user","event"],engine="python")
    candi_events = list(user_event_df["event"].unique())
    print("event number:%d" % len(candi_events))
    # 找到所有被训练过的user
    train_group_users_df = pd.read_csv(train_group_users_file,sep="\t",names=["group","users"],engine="python")
    trained_users = set()
    for index,row in train_group_users_df.iterrows():
        trained_users.update([int(user) for user in str(row["users"]).strip().split(" ")])
    test_group_event_df = pd.read_csv(test_group_event_file,sep="\t",names=["group","event"],engine="python")
    for index, row in test_group_event_df.iterrows():
        print("index %d" % index)
        if row["event"] not in candi_events:
            continue
        test_group_event_candis = str(row["group"])+"\t"+str(row["event"])+"\t"
        members = test_group_users.get(row["group"])
        members_events = set()
        group_candi_events = set()
        num = 0
        # 首先看该group内所有成员是否都被训练
        for member in members:
            if member not in trained_users:
                break
            num += 1
            members_events.update(user_events_dict.get(member))
        if num < len(members): continue
        # 挑选1000个该group和group成员都未参加过的event
        candi_num = 0
        while candi_num < 1000:
            event = draw_candi(candi_events)
            if event not in group_events_dict.get(row["group"]) and event not in members_events\
                    and event not in group_candi_events:
                group_candi_events.add(event)
                test_group_event_candis += str(event)+" "
                candi_num += 1
        test_group_event_candis += "\n"
        append_to_file(test_group_event_candi_file,test_group_event_candis)


def draw_candi(candi_events):
    r = random.randint(0,len(candi_events)-1)
    return candi_events[r]
#
def test_train_user_event(test_train_user_event_file,train_user_event_file,train_group_event):
    train_group_event_df = pd.read_csv(train_group_event,sep="\t",names=["event","groupid"],engine="python")
    group_events = set(train_group_event_df["event"].unique())
    train_user_event_df = pd.read_csv(train_user_event_file,sep="\t",names=["user","event"],engine="python")
    test_train_user_event_str = ""
    if os.path.exists(test_train_user_event_file):
        os.remove(test_train_user_event_file)
    for index,row in train_user_event_df.iterrows():
        if index%10000 == 0:
            append_to_file(test_train_user_event_file,test_train_user_event_str)
            test_train_user_event_str = ""
        if row["event"] in group_events:
            test_train_user_event_str += str(row["user"])+"\t"+str(row["event"])+"\n"
    append_to_file(test_train_user_event_file,test_train_user_event_str)


# 将字符串写入文件
def write_to_file(filename,str):
    with open(filename,'w') as fw:
        fw.write(str)


# 将字符串追加至文件
def append_to_file(filename,str):
    with open(filename,'a') as fw:
        fw.write(str)

