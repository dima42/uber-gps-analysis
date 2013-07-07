README: Uber GPS Traces (June 2011)

This collection contains gps logs from black car pickups in San Francisco. It is intended for data visualization purposes (e.g. for traffic) but can be easily adapted for other purposes (e.g. training ETA algorithms).

The Uber business model revolves around dispatching black cars to pick up clients. In total, GPS traces from 25,000 such pickups are used to build this dataset. Line in each trace is spaced at about 4 seconds apart. The exception is if a car is stationary, in which case we discard redundant points until the car moves again.

The logs are kept as "raw" as possible - bad traces and/or missing data (e.g. from radio interference) is preserved. However, the logs have been altered to protect the privacy of our clients. Specifically, we truncated the start and end legs of each trace and also occluded the specific date of the pickup. Rather than their true original dates, all pickups in the dataset are shown to have started during the first week of January 2007. The weekday and time of day is preserved, however. Finally, traces deemed too short to effectively truncate have been excluded from the dataset.

We provide tab seperated flat files, with each line in the following format:

  <trip id>\t<iso timestamp>\t<latitude>\t<longitude>

The iso timestamp is in UTC.

For more details, please contact henry at uber dot com.
