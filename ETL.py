from Controllers.ETLController import ETLController

ETL = ETLController
ETL().source("json").sink("postgres").run()