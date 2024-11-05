# This function calculates the mean, that is the division of the sum of all elements by the number of elements in the dataset
def my_mean(data):
    
    # This variable holds the sum of the elements in the dataset
    sumtotal = 0
    n = len(data)
    
    # The for loop iterates through all values in the dataset
    for element in data:
        sumtotal += element
    return sumtotal/n

# This function calculates the median, that is the central element in a sorted dataset (Or the mean of the two central ones if the number of elements in the dataset is even)
def my_median(data):
    n = len(data)
    
    # Adding this line of code to sort the data
    data.sort()
    
    # This condition checks weather the dataset is even or odd
    if n % 2 == 1:
        
        # Return the central element
        return sorted_data[n//2]
    else:
        middle_1, middle_2 = n//2 - 1, n//2
        
        # Return the mean between the two central elements
        return (sorted_data[middle_1] + sorted_data[middle_2]) / 2
    
# This function calculates how many times a specific element repeats in the dataset
def my_count(data, item):
    occurences = 0
    
    # Iterates through all the elements in the dataset
    for element in data:
        if element == item:
            occurences += 1
    return occurences

# This function calculates the mode, that is the number that repeats the most number of times. To do this, it uses the previous function "my_count"
def my_mode(data):
    max_count = 0
    max_item = None
    
    # Iterates through all the elements in the dataset
    for element in data:
        
        # Counts the number of occurences of "element" in the dataset and stores it in "current_count"
        current_count = my_count(data, element)
        
        # Checks if the current counting is the biggest one encountered, if so, register it as "max_count" and the element as "max_item"
        if current_count > max_count:
            max_count = current_count
            max_item = element

    return max_item

# This function calculates the standard deviation of the dataset, that is a measure of spread and is calculated by the square root of the division of the squared sum of the difference between all the elements and the mean by the number of elements
def my_sample_SD(data):
    
    # variable to store the sum of all the squares of the difference between the value and the mean
    sum_of_squares = 0
    n = len(data)
    mean = my_mean(data)
    
    # Iterates through all elements
    for element in data:
        sum_of_squares += (element - mean)**2
        
    # Return the square root of the sum of all squares divided by the number of elements
    return (sum_of_squares/(n-1))**0.5

# This function gets the range of the dataset, that is the difference between the highest and the lowest value in the dataset
def my_range(data):
    
    #I added this line to make sure that the dataset is sorted from lowest to highest in order to use the indexes "[-1]" and "[0]" in the next line
    data.sort()
    
    # This function assumes that the dataset is already sorted
    return data[-1] - data[0]
