LOGS ANALYSIS AND MANAGEMENT USING MACHINE LEARNING

CONCEPT: 

* The main concept was to differentiate different log-levels like 'INFO', 'WARN', 'CRITICAL', 'DEBUG', 'ERROR'
* Prepare a data frame(DF) using those differentiated log-levels
* Grab out the 'ERROR' log-level and train the data set to recognise the obtained 'ERROR' log-level patterns such that whenever those types of 'ERROR' log-levels are hit, then     there would be some kind of alert or some type of recovery.

1. main.py: Runs the application using Flask and stores logs to a file in logs directory. 