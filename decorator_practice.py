def my_name(additional_info):
    def my_info():
        print("jainendra")
        additional_info()
        print("iitg")
    return my_info

@my_name
def my_lastname():
    print("kumar")





if __name__ == '__main__':
    my_lastname()