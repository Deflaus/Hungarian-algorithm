import sqll
while(True):
    indata = input()
    if indata == "deleteW":
        id = input()
        sqll.delete_worker(id)
    if indata == "insertW":
        info = input()
        info = info.split()
        sqll.insert_workers(info[0], info[1], info[2])
    if indata == "printW":
        data = sqll.parse_alldata_workers()
        count = 0
        for element in data:
            count += 1
            print(str(count) + ' ' + str(element[0]) + ' ' + element[1] + ' ' + element[2])
    if indata == "countW":
        print(sqll.count_of_workers())



    if indata == "deleteT":
        id = input()
        sqll.delete_task(id)
    if indata == "insertT":
        info = input()
        info = info.split()
        sqll.insert_tasks(info[0], info[1])
    if indata == "printT":
        data = sqll.parse_alldata_tasks()
        count = 0
        for element in data:
            count += 1
            print(str(count) + ' ' + str(element[0]) + ' ' + element[1])
    if indata == "countT":
        print(sqll.count_of_tasks())

    if indata == "&&":
        print(sqll.get_time())

    if indata == "exit":
        break