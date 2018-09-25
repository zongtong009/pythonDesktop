import pandas  as pd
user_feature_data = []
flag = 1
print("landing")
with open("userFeature.data","r",encoding="utf-8") as f :
    for i,line in enumerate(f) :
        line = line.strip().split("|")
        dict_list = {}
        for each in line :
            each_list = each.split(" ")
            dict_list[each_list[0]] = " ".join(each_list[1:])#这里会给value添加一个空格和，//但是好像dataframe帮我解决了他们，dont worry
            #print(dict_list)
        user_feature_data.append(dict_list)
        if i/flag >= 100000 :
            user_feature = pd.DataFrame(user_feature_data)
            user_feature.to_csv("userFeature_%d_part_bat.csv" % (i), index=False)
            #print("finish:userFeature_part_bat.csv")
            user_feature_data = []
            flag += 1