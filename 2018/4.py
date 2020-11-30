while True:
    try:
        weight = input("请输入航天员的体重:")
        if weight == 'q' or weight == 'Q':
            break
        else:
            new_weight = eval(weight)
            earth_weight = new_weight + 0.5 * 10
            moon_weight = 0.165 * earth_weight
            print("10年后航天员在地球上的体重为：{}".format(earth_weight))
            print("10年后航天员在月球上的体重为：{}".format(moon_weight))
    except:
        print("输入格式有误")