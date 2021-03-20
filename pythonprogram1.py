five_km = []
ten_km =[]
fifteen_km =[]
final_list =[]
output = []

def milestones(running_events):
    for elemnts in range(1,len(running_events )):
        if running_events[elemnts][-1] == 5:
            five_km.append(running_events[elemnts][-2])
        elif running_events[elemnts][-1] == 10:
            ten_km.append(running_events[elemnts][-2])
        else:
            fifteen_km.append(running_events[elemnts][-2])


running_events=[[ 'date_of_run', 'finish_time_in_minutes', 'length_of_run_in_kms' ],
         	[ "29-5-2017", 15, 5],
         	[ "9-3-2017", 35, 10],
         	[ "29-3-2017", 13, 5]]
milestones(running_events)
final_list.append(five_km)
final_list.append(ten_km)
final_list.append(fifteen_km)

for data in final_list :
    if len(data) == 0 :
        output.append(0)
    else:
        output.append(min(data))
print(output)
