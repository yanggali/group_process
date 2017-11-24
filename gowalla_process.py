from plancast_file_process import initial_group_event,write_to_file
import pandas as pd
#input data file
checkin_file = "C:\\Users\\uqjyan18\\Documents\\datasets\\Gowalla\\Gowalla_totalCheckins.txt"
user_friend_file = "C:\\Users\\uqjyan18\\Documents\\datasets\\Gowalla\\Gowalla_edges.txt"

user_poi_file = "C:\\Users\\uqjyan18\\Documents\\datasets\\Gowalla\\user_poi.csv"
#output data file
poi_users_file = "C:\\Users\\uqjyan18\\Documents\\datasets\\Gowalla\\poi_users_file.dat"


if __name__=="__main__":
    initial_group_event(user_poi_file,user_friend_file,poi_users_file)