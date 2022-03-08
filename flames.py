from collections import Counter

def flames(name1, name2):
    total = len(name1) + len(name2)
    common_letters = Counter(name1) & Counter(name2)
    count = sum(common_letters.values())*2
    offset1 = total - count
    print(offset1)
    flames_list = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

    for i in range(0, 5):
        if offset1 > len(flames_list):
            offset = offset1 % len(flames_list)
        if offset1 >= len(flames_list) and offset1%len(flames_list) == 0:
            offset = len(flames_list)
        if offset1 < len(flames_list):
            offset = offset1
        list1 = flames_list[(offset-1)+1:]
        list2 = flames_list[:(offset-1)]
        list1.extend(list2)
        flames_list = list1

    return flames_list[0]
        
if __name__ == '__main__':
    print("***********************Welcome to the Flames Calculator!***********************")
    name1 = input("Enter name 1: ")
    name2 = input("Enter name 2: ")
    print("Result: ", flames(name1, name2))
    print("***********************Thank you for using the Flames Calculator!***********************")