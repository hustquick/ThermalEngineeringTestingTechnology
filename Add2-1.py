A_min = 1.2
A_max = 2.5
Delta = 0.01

R = Delta / (A_max - A_min)

# 精度等级列表
acc_list = [0.1, 0.2, 0.5, 1.0, 1.5, 2.5, 5.0]


def find_min_class(value, class_list):
    # 先猜最大的精度等级，如果还能取更小，则取更小值
    classification = class_list[-1]
    # 使用class_list[::-1]实现倒序遍历
    for class_value in class_list[::-1]:
        if value * 100 <= class_value:
            classification = class_value
    return classification


print("该电流表的精度等级为{}级".format(find_min_class(R, acc_list)))
