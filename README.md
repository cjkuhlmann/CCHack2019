# CCHack2019
Respoitry for team FAFF of the 2019 Cambridge Consultants gHackathon

All files except the pi_source_code file are to be used on the server. (with the pi_souce_code to be launched on the pi)

The pi will constantly take readings and try to send them to the server. If connection is lost it will try to re-establish connection.

The server will take input from the pi and then update its grid of devices with each device's data.

## In a real-world scenario
If this was to run in a real-world scenario then the PIs ssould upload data every 5-10 mins allowing time for all the data to be processed. Additionally GPS and radio communication would be used to map can communitate with the PIs.
Data for detecting fires would be collected on each upload but only every hour would the data be added to the history of each device. This is to save storage and processing however on  a larger system it may be suitable to store all data received.

The fire spread simulation would aonly be run when at least one fire is detected. After this condition is met it would be run on every update.
