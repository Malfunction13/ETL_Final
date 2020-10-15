class View:

    def ask_filepath(self):
        filepath = input("Please insert filepath for JSON source: ")

        return filepath

    def ask_host(self):
        host = input("Please insert host: ")

        return host

    def ask_database(self):
        database = input("Please insert Database name: ")

        return database

    def ask_user(self):
        user = input("Please insert user: ")

        return user

    def ask_password(self):
        password = input("Please insert password: ")

        return password

    def ask_port(self):
        port = input("Please insert port: ")

        return port


    def print_data(self, data):

        if len(data) > 1:
            print(f"There is total of {len(data)} entries!")

            for i in data:
                print(f"key: {i.key}, value: {i.value}, ts: {i.ts}")
            print("No more data to display!")

        else:
            print(f"key: {data[0].key}, value: {data[0].value}, ts: {data[0].ts}")

    def repeat(self):
        print("Would you like to see more entries?")
        repeat = input("Insert Y for YES and N for NO: ").lower()

        return repeat

    def db_repeat(self):
        print("Would you like to write more entries?")
        repeat = input("Insert Y for YES and N for NO: ").lower()

        return repeat
