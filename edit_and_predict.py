import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


def edit_df(df):
    for index, row in df.iterrows():
        if float(row['day 1'].replace("$", "")) == 0:
            df.drop(index, inplace=True)
    return df


def one_dim_chart_rarity(df):
    list_of_lists = []
    rarity_list = df['rarity'].tolist()
    rarity_list = list(set(rarity_list))
    val_list_day1 = []
    val_list_day2 = []
    val_list_day3 = []
    val_list_day4 = []
    val_list_day5 = []
    val_list_day6 = []
    val_list_day7 = []
    val_list_day8 = []
    val_list_day9 = []
    counter = []

    for i in range(0, len(rarity_list)):
        val_list_day1.append(0)
        val_list_day2.append(0)
        val_list_day3.append(0)
        val_list_day4.append(0)
        val_list_day5.append(0)
        val_list_day6.append(0)
        val_list_day7.append(0)
        val_list_day8.append(0)
        val_list_day9.append(0)
        counter.append(0)

    for index, row in df.iterrows():
        i = 0
        for search in rarity_list:
            if row["rarity"] == search:
                val_list_day1[i] = val_list_day1[i] + float(row['day 1'].replace("$", ""))
                val_list_day2[i] = val_list_day2[i] + float(row['day 2'].replace("$", ""))
                val_list_day3[i] = val_list_day3[i] + float(row['day 3'].replace("$", ""))
                val_list_day4[i] = val_list_day4[i] + float(row['day 4'].replace("$", ""))
                val_list_day5[i] = val_list_day5[i] + float(row['day 5'].replace("$", ""))
                val_list_day6[i] = val_list_day6[i] + float(row['day 6'].replace("$", ""))
                val_list_day7[i] = val_list_day7[i] + float(row['day 7'].replace("$", ""))
                val_list_day8[i] = val_list_day8[i] + float(row['day 8'].replace("$", ""))
                val_list_day9[i] = val_list_day9[i] + float(row['day 9'].replace("$", ""))
                counter[i] = counter[i] + 1
            i = i + 1

    for i in range(0, len(rarity_list)):
        val_list_day1[i] = val_list_day1[i] / max(counter[i], 1)
        val_list_day2[i] = val_list_day2[i] / max(counter[i], 1)
        val_list_day3[i] = val_list_day3[i] / max(counter[i], 1)
        val_list_day4[i] = val_list_day4[i] / max(counter[i], 1)
        val_list_day5[i] = val_list_day5[i] / max(counter[i], 1)
        val_list_day6[i] = val_list_day6[i] / max(counter[i], 1)
        val_list_day7[i] = val_list_day7[i] / max(counter[i], 1)
        val_list_day8[i] = val_list_day8[i] / max(counter[i], 1)
        val_list_day9[i] = val_list_day9[i] / max(counter[i], 1)
    list_of_lists.append(val_list_day1)
    list_of_lists.append(val_list_day2)
    list_of_lists.append(val_list_day3)
    list_of_lists.append(val_list_day4)
    list_of_lists.append(val_list_day5)
    list_of_lists.append(val_list_day6)
    list_of_lists.append(val_list_day7)
    list_of_lists.append(val_list_day8)
    list_of_lists.append(val_list_day9)
    '''plot'''
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.xlabel("days")
    plt.ylabel("prices")
    plt.title("A test graph")
    plt.ylim(0, 300)
    y = []
    for i in range(0, len(rarity_list)):
        for j in range(0, 9):
            y.append(list_of_lists[j][i])
        plt.plot(x, y, label='%s' % rarity_list[i])
        y.clear()
    plt.legend()
    plt.show()

    '''bar plot'''
    plt.ylim(0, 300)
    X_axis = np.arange(len(x))
    for i in range(0, len(rarity_list)):
        for j in range(0, 9):
            y.append(list_of_lists[j][i])
        plt.bar(X_axis + (i * 0.1), y, 0.1, label='%s' % rarity_list[i])
        y.clear()

    plt.xticks(X_axis, x)
    plt.xlabel("days")
    plt.ylabel("prices")
    plt.title("A test graph bar")
    plt.legend()
    plt.show()

    '''scatter plot'''
    plt.ylim(0, 300)
    X_axis = np.arange(len(x))
    for i in range(0, len(rarity_list)):
        for j in range(0, 9):
            y.append(list_of_lists[j][i])
        plt.scatter(x, y, label='%s' % rarity_list[i])
        y.clear()
    plt.xticks(X_axis, x)
    plt.xlabel("days")
    plt.ylabel("prices")
    plt.title("A test graph bar")
    plt.legend()
    plt.show()


def linear_regression(x, y):
    data = pd.DataFrame({"days": x, "price": y})
    reg = linear_model.LinearRegression()
    reg.fit(data[['days']], data.price)
    return reg.coef_[0], reg.intercept_


def predict_day_9(df):
    day_9 = list()
    x = (1, 2, 3, 4, 5, 6, 7, 8)
    for index, row in df.iterrows():
        y = (float(row['day 1'].replace("$", "")), float(row['day 2'].replace("$", "")),
             float(row['day 3'].replace("$", "")), float(row['day 4'].replace("$", "")),
             float(row['day 5'].replace("$", "")), float(row['day 6'].replace("$", "")),
             float(row['day 7'].replace("$", "")), float(row['day 8'].replace("$", "")))
        coef, intercept = linear_regression(x, y)
        day_9.append("{:.2f}".format(9 * coef + intercept) + "$")
    return day_9
