from Repository.Simulation import Simulation
from Repository.Json import Json
from Repository.Database import Database
from Views.View import View

class ETLController:
    def __init__(self):
        self.model = None
        self.view = View()
        self.data_source = "" # avoids name shadowing with source() and sink()
        self.data_sink = ""


    def source(self, source):
        self.data_source = source

        return self

    def sink(self, sink):
        self.data_sink = sink

        return self

    def run_sink(self):
        if self.data_sink == "stdout":
            self.view.print_data(self.model)

            if self.data_source == "simulation":
                while True:  # will ask until input is "n"
                    repeat = self.view.repeat()

                    if repeat == "n":
                        break
                    elif repeat == "y":
                        self.model = Simulation().generate_random_data()
                        self.view.print_data(self.model)
                    else:
                        print("Input is not valid!")

        if self.data_sink == "postgres":
            host = self.view.ask_host()
            database = self.view.ask_database()
            user = self.view.ask_user()
            password = self.view.ask_password()
            port = self.view.ask_port()

            Database().write_data(self.model, host, database, user, password, port)
            if self.data_source == "simulation":

                while True:  # will ask until input is "n"
                    repeat = self.view.db_repeat()

                    if repeat == "n":
                        break
                    elif repeat == "y":
                        self.model = Simulation().generate_random_data()
                        Database().write_data(self.model, host, database, user, password, port)
                    else:
                        print("Input is not valid!")

        return self

    def get_filepath(self):
        filepath = View().ask_filepath()

        return filepath

    def run(self):

        if self.data_source == "simulation":
            self.model = Simulation().generate_random_data()

        if self.data_source == "json":
            self.model = Json.create_models(self.get_filepath())
        self.run_sink()


