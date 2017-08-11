def list_sum(input_list):
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum

test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


def tag_count(list):
    count = 0
    for item in list:
        if item[0] == "<" and item[len(item)-1] == ">":
            count+=1
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))


names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones', 'philip diplodocus mallory']
capitalized_names = []
for name in names:
    capitalized_names.append(name.title())

print(capitalized_names)


def nearest_square(num):
    i=0
    while i*i<=num:
        i+=1
    return (i-1)*(i-1)


for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break