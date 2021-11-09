QI_INDEX = [0, 3]
IS_CAT = [True, False]
SA_INDEX = 1
__DEBUG = False


def read_data():
    """
    read microdata for *.txt and return read data

    # Note that Mondrian can only handle numeric attribute
    # So, categorical attributes should be transformed to numeric attributes
    # before anonymization. For example, Male and Female should be transformed
    # to 0, 1 during pre-processing. Then, after anonymization, 0 and 1 should
    # be transformed to Male and Female.
    """
    import os

    os.system('shuf data/ex05-fake-registration-2.csv > data/ex05-fake-registration-shuffled.csv')
    QI_num = len(QI_INDEX)
    data = []
    # oder categorical attributes in intuitive order
    # here, we use the appear number
    intuitive_dict = []
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_dict.append(dict())
        intuitive_number.append(0)
        intuitive_order.append(list())
    data_file = open('data/ex05-fake-registration-shuffled.csv', 'rU')
    for line in data_file:
        line = line.strip()
        # remove double spaces
        line = line.replace(' ', '')
        temp = line.split(',')
        ltemp = []
        for i in range(QI_num):
            index = QI_INDEX[i]
            if IS_CAT[i]:
                try:
                    ltemp.append(intuitive_dict[i][temp[index]])
                except KeyError:
                    intuitive_dict[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
                    intuitive_order[i].append(temp[index])
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[SA_INDEX])
        data.append(ltemp)
    print(data)
    print("-------------")
    print(intuitive_order)
    return data, intuitive_order
