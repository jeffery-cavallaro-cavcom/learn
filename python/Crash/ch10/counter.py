def increment_counter(filename):
    count = 0
    with open(filename, 'a+') as counter_file:
        if counter_file.tell():
            counter_file.seek(0, 0)
            count = int(counter_file.readline().strip())
            counter_file.seek(0, 0)
            counter_file.truncate()
        count += 1
        counter_file.write(str(count) + '\n')


counter_file_name = 'data/counter.txt'

increment_counter(counter_file_name)
