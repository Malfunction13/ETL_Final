from Controllers.ETLController import ETLController

ETL = ETLController
ETL().source("json").sink("postgres").run()
#source args can be "json" or "simulation" and sink args can be "postgres" or "stdout"
