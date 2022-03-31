import shelve  #  (pri metode pickl i shelv vosmoshno vnesti virus)

monday_schedule = ['Math', 'English language', 'System programming', 'Python']
tuesday_schedule = ['English language', 'HTML', 'Python', 'Football']
wednesday_schedule = ['Physics', 'English language', 'Python']
thursday_schedule = ['Math', 'Chemistry', 'Java']
friday_schedule = ['Running', 'Math', 'Python']

with shelve.open('schedules', writeback=True) as schedules:
     schedules['monday_schedule'] = monday_schedule
     schedules['tuesday_schedule'] = tuesday_schedule
     schedules['wednesday_schedule'] = wednesday_schedule
     schedules['thursday_schedule'] = thursday_schedule
     schedules['friday_schedule'] = friday_schedule

    # schedules['thursday_schedule'].append('Swimming')  #  v spisok ne dobavljaetsja, togda sleduyshee

    # temp_list = schedules['thursday_schedule']  # 1-i sposob
    # temp_list.append('Swimming')
    # schedules['thursday_schedule'] = temp_list

    # schedules['thursday_schedule'].append('Python')  # 2-i sposob, no nushno dobavit 'writeback=True'

      for key in schedules:
          print(key, schedules[key])
        #  monday_schedule ['Math', 'English language', 'System programming', 'Python']
        # tuesday_schedule ['English language', 'HTML', 'Python', 'Football']
        # wednesday_schedule ['Physics', 'English language', 'Python']
        # thursday_schedule ['Math', 'Chemistry', 'Java']
        # friday_schedule ['Running', 'Math', 'Python']
