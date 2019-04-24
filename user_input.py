import pandas
import time
import funcs as f


# Currently just gives us one row of first names in the data set
df_10k = pandas.read_csv("MOCK_10000.csv", usecols=[2])
df_100k = pandas.read_csv("MOCK_100000.csv", usecols=[2])
df_1m = pandas.read_csv("MOCK_1000000.csv", usecols=[2])

# Dictionary for calling functions by user input
funcs = {
    1: f.row_by_len,
    2: f.row_by_char
}


def user_func():
    func_num = int(input("Enter function number from file in directory (ie. 1, 2, 5 etc.): "))
    data_amt = input("Enter amount of data to apply function to (available choices are: 10k, 100k, 1m, or all): ")
    pieces = str()
    start = time.time()

    if data_amt == "10k":
        funcs[func_num](df_10k)
        pieces = "10,000"

    elif data_amt == "100k":
        funcs[func_num](df_100k)
        pieces = "100,000"

    elif data_amt == "1m":
        funcs[func_num](df_1m)
        pieces = "1,000,000"

    elif data_amt == "all":
        funcs[func_num](df_10k)
        funcs[func_num](df_100k)
        funcs[func_num](df_1m)
        pieces = "all the data"

    else:
        print("That was not a valid input. Please type one of the following: '10k', '100k', '1m', or 'all': ")

    end = time.time()
    print("Your function processed " + pieces + " over " + str((end - start)) + " seconds.")


user_func()
