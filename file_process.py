import pandas as pd
import numpy as np

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
        # print(row["yes"])
        user_list = str(row["yes"]).split(' ')
        if len(user_list) == 1:
            continue
        for user in user_list:
            write_str += user+" "+str(row["event"])+"\n"
    write_to_file(user_event_file,write_str)

#根据event_attendees和朋友关系获取group以及group参加的活动
def initial_user_friends(event_attedees_file,user_friends_file,event_group_file):
    user_friends_dict = relation_to_dict(user_friends_file)
    event_group_str = ""
    df = pd.read_csv(event_attedees_file)
    for index,row in df.iterrows():

        attendees_list = str(row["yes"]).split(" ")
        vertex = len(attendees_list)
        attendee_index_dict = dict()
        index_attendee_dict = dict()
        for attendee in attendees_list:
            attendee_index_dict[attendee] = int(len(attendee_index_dict))
            index_attendee_dict[len(index_attendee_dict)] = attendee
        #初始化邻接矩阵
        adjacent_matrix = initial_adjacent_matrix(attendees_list,attendee_index_dict,user_friends_dict)
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
                        event_group_str += str(row["event"]) + "::"+users_str+"\n"
                    else:
                        for event in events:
                            event_group_str += event + "::" + users_str + "\n"

        print("event "+ str(row["event"])+" finished.")
    write_to_file(event_group_file,event_group_str)


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
def initial_adjacent_matrix(attendee_list,attendee_index_dict,user_friends_dict):
    adjacent_matrix = np.zeros((len(attendee_list),len(attendee_list)))
    for u in attendee_list:
        for v in attendee_list[attendee_index_dict[u]+1:]:
            v_friends = user_friends_dict.get(v, 'nan')
            u_friends = user_friends_dict.get(u, 'nan')
            test_friends = user_friends_dict.get("1013376584")
            if (u in v_friends) or (v in u_friends):
                adjacent_matrix[attendee_index_dict[u]][attendee_index_dict[v]] = 1
                adjacent_matrix[attendee_index_dict[v]][attendee_index_dict[u]] = 1
    return adjacent_matrix

#将朋友关系初始化到dict中
def relation_to_dict(user_friends_file):
    df = pd.read_csv(user_friends_file)
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

#将字符串写入文件
def write_to_file(filename,str):
    with open(filename,'w') as fw:
        fw.write(str)