
# TODO change this data parameter with your own data
def Find_Variability(data):
    beta = 0.9
    stop_bias_correction = 10
    Avg = 0
    Avg_of_square_data = 0

    length_of_data = len(data)

    # Counter can not start from zero, because 1/(1-beta^0) is undefined
    counter = 1

    for index in range(length_of_data):

        if index == 0:
            # TODO change this part with your own data
            x = pd.to_numeric(data.iat[index, -1])

            Avg = (1 - beta) * x
            Avg_of_square_data = (1 - beta) * x ** 2

            continue

        # TODO change this part with your own data
        x = pd.to_numeric(data.iat[index, -1])

        Avg = beta * Avg + (1 - beta) * x
        Avg_of_square_data = beta * Avg_of_square_data + (1 - beta) * x ** 2

        # At first 1/(1-beta) iterations do bias correction
        if counter < stop_bias_correction:
            variance = (1 / (1 - beta ** (counter + 1))) * Avg_of_square_data - (1 / (1 - beta ** (counter + 1)) * Avg) ** 2 
        else:
            variance = Avg_of_square_data - Avg ** 2

        counter += 1
