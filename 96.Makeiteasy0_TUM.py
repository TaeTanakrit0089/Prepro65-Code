"""Never Gonna Give You Up"""


def my_main():
    """Never Gonna Give You Up"""

    input_count = int(input())
    output_list = list()

    customer_list = input().split(" ")
    #print("customer_list = ", customer_list)

    output_list.append(customer_list[2].upper())
    temp_list = list()
    temp_list.append(customer_list[1])
    temp_list.append(customer_list[0])
    answer_list = list()
    answer_list.append(temp_list)
    output_list.append(answer_list)
    #print("output_list = ", output_list)

    i = 2
    while i <= input_count:
        customer_list = input().split(" ")
        #print("customer_list = ", customer_list)
        xxx = 0
        output_count = len(output_list)
        is_same = False
        same_position = 0
        while xxx < output_count:
            if output_list[xxx] == customer_list[2].upper():
                is_same = True
                same_position = xxx
            xxx = xxx + 2

        # Exist while loop
        if is_same:
            #print("same job append customer = ", customer_list[1], " age = ", customer_list[0])
            temp_list = list()
            temp_list.append(customer_list[1])
            temp_list.append(customer_list[0])
            output_list[same_position+1].append(temp_list)
            #print("output_list =", output_list)
        else:
            #print("new job customer = ", customer_list[1], " age = ", customer_list[0])
            output_list.append(customer_list[2].upper())
            temp_list = list()
            temp_list.append(customer_list[1])
            temp_list.append(customer_list[0])
            answer_list = list()
            answer_list.append(temp_list)
            output_list.append(answer_list)
            #print("output_list =", output_list)

        i = i + 1

    #print("final output = ", output_list)
    output_list = sort_list(output_list)
    #print("sorted output = ", output_list)
    i = 0
    output_count = len(output_list)
    while i < output_count:
        print("OCCUPATION :", output_list[i])
        customer_list = output_list[i+1]
        #print("customer_list =", customer_list)
        customer_count = len(customer_list)
        j = 0
        while j < customer_count:
            print(str(j+1) + ". " +
                  customer_list[j][0] + ", " + customer_list[j][1])
            j += 1
        i += 2


def sort_list(my_list):
    """Never Gonna Give You Up"""
    return_list = list()
    job_list = list()
    my_count = len(my_list)
    aaa = 0

    # Create Job List
    while aaa < my_count:
        job_list.append(my_list[aaa])
        aaa = aaa + 2

    job_list.sort()
    #print("job_list sorted = ", job_list)
    job_count = len(job_list)

    bbb = 0

    # Check job_list with my_list
    while bbb < job_count:
        aaa = 0
        while aaa < my_count:
            if job_list[bbb] == my_list[aaa]:
                return_list.append(my_list[aaa])
                return_list.append(sort_customer_list(my_list[aaa + 1]))
                aaa = my_count  # go out from loop while aaa < my_count
            aaa = aaa + 2
        bbb = bbb + 1

    #print("return_list = ", return_list)
    return return_list


def sort_customer_list(my_list):
    """Never Gonna Give You Up"""
    my_count = len(my_list)
    customer_name_list = list()
    return_list = list()
    i = 0
    while i < my_count:
        customer_name_list.append(my_list[i][0])
        i = i + 1

    #print("customer_name_list = ", customer_name_list)
    customer_name_list.sort()
    customer_name_count = len(customer_name_list)
    #print("SORT customer_name_list = ", customer_name_list)
    i = 0
    while i < customer_name_count:
        j = 0
        while j < my_count:
            if customer_name_list[i] == my_list[j][0]:
                return_list.append(my_list[j])
            j = j + 1
        i = i + 1
    #print("return sorted customer_name_list = ", return_list)
    return return_list


my_main()
