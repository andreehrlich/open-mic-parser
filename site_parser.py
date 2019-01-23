
# from bs4 import BeautifulSoup
# import urllib2

# chicago_comedy_open_mic_list_url = "http://www.comedyofchicago.com/p/chicago-open-mic-list.html"


# page = urllib2.urlopen(chicago_comedy_open_mic_list_url)

days = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "end"  ]
days_indices = []
day_counter = 0

current_day = None
last_update = None
mics_dict = { day: [] for day in days }

line_event_start = -1

lines = []


''' Read file into a list of strings'''
with open("mic_list.txt") as f:
    lines = f.readlines()

''' lowercase all '''
lines = [l.lower() for l in lines]

for i, line in enumerate(lines):
    if "last update" in line:
        last_update = line.split("last update")[1]
    # print i, line


    ''' Events in segments by day '''
    if days[day_counter] in line:
        # current_day = days[day_counter]
        days_indices.append(i)
        # print "CURRENT_DAY: ", current_day
        if day_counter < 7:
            day_counter += 1
        else:
            break

print(len(lines))
days_indices.append(len(lines))
print "days_indices", days_indices

''' Get the index number of any line that is a line break '''
line_break_indices = [i for i, x in enumerate(lines) if x == "\n" and i > days_indices[0]]

print "LINE_BREAKS", line_break_indices
print "DAYS_INDICES", days_indices


day_counter = 0
day_lb = days_indices[day_counter]
day_ub = days_indices[day_counter+1]

for i, line_break in enumerate(line_break_indices):

    if i >= len(line_break_indices) - 1:
        break

    current_line_break = line_break
    next_line_break = line_break_indices[i+1]
    # print "current_line_break", current_line_break
    # print "next_line_break", next_line_break

    if line_break > days_indices[day_counter+1]:
        day_counter += 1

    current_day = days[day_counter]

    lines_in_event = lines[current_line_break:next_line_break]

    if "\n" in lines_in_event:
        lines_in_event.remove("\n")
    event_str = "".join(lines_in_event)
    mics_dict[days[day_counter]].append(event_str)


for day in mics_dict:
    list_of_event_strings = mics_dict[day]
    for event_string in list_of_event_strings:
        event_string = OpenMic(event_string)

print "mics_dict['sunday']"
for event in mics_dict["sunday"]:
    print event

class OpenMic:

    def __init__(event_string):

        event_lines = event.split("\n")

        mic_name = event_lines[0])

        # if "open mic" in mic_name:
        #     mic_name = mic_name.split()
        #     mic_name.remove("open")
        #     mic_name.remove("mic")
        #     mic_name = " ".join(mic_name)
        # elif "mic" in mic_name:
        #     mic_name = mic_name.split()
        #     mic_name.remove("mic")
        #     mic_name = " ".join(mic_name)

        self.mic_name = mic_name

        for word in ["at", "@"]:
            if word in event_lines[1]:
                new_event.club = event_lines[1].split(word)
                break
        self.address = event_lines[2]


        for line in event_lines:
            if "sign up" in line:
                split_line = line.split("sign up")
                event.sign_up = split_line[0] + split_line[1]
            # if "start" or ""

         # club_name, address, sign_up_time, start_time, notes):

        # self.club_name = club_name
        # self.address = address
        # self.sign_up_time = sign_up_time
        # self.start_time = start_time
        # self.notes = notes
