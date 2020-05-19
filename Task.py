from urllib.request import urlopen
import json
#loading json from api
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

#Creating a list and adding both the conference data i.e paid and free
def concat_conf(conf_data):
    conf_dict = []
    paid_conf = conf_data['paid']
    conf_dict.append(paid_conf)
    free_conf = conf_data['free']
    conf_dict.append(free_conf)
    return paid_conf+free_conf

#getting exact and Semantic Duplicates
def checkIfDuplicates(data):
    new_dict = {}
    answer = []
    for item in data:
        s_tuple = item["conference_id"]  ,  item["confStartDate"] ,item['venue']
        if s_tuple in new_dict:
            new_dict[s_tuple] += 1
        else:
            new_dict[s_tuple] = 1
    for i in list(new_dict.keys()):
        if new_dict[i] > 1:
            answer.append(i)        
    print("Found ", len(answer),"Duplicate Conference \n")    
    print("Duplicate Conferences \n",*answer, sep="\n")
    
if __name__ == "__main__":
    url = ("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")
    conf_data = get_jsonparsed_data(url)
    conf_dict = concat_conf(conf_data)
    #printing in human readable format
    i=0
    for item in conf_dict:
        i=i+1
        print(i,item["conference_id"],". Name of the Conference:",item['confName'],"\n","Start Date:",item['confStartDate'],"\n","Venue:",item['venue'],"\n","Free or Paid:",item['entryType'],"\n","Register Here:",item['confUrl'],"\n")


    #Duplication
    print(checkIfDuplicates(conf_dict))
