# design-data utilities

DESCRIPTION
In July of 2017, Reveal from The Center for Investigative Reporting requested a data set from the Oklahoma Department of Corrections, and has published it in its raw format.

Code for Tulsa and Asemio will be hosting an event at 36°N in Tulsa, OK to review the dataset, understand what's in it, and begin to organize the data so that it is meaningful and useful to journalists, policy analysts, lawyers, and anyone else working in criminal justice.  [Go here if you are interested in attending the event.](https://www.eventbrite.com/e/designdata-criminal-justice-in-ok-tickets-39290102755?utm_source=eb_email&utm_medium=email&utm_campaign=order_confirmation_email&utm_term=eventname&ref=eemailordconf)

## Contributing to this repo:
1. There are no restrictions to the language you use for a utility.
1. Please document the usage of the utility in this or a separate readme file.
1. If possible, a utility should start by opening zip file and complete it's tasks without manual intervention.
1. If you output the data, please remove names.
1. Please do not add the offender zip files to this repo.  The files contain personal information and we don't want too many copies available. For the same reason, please do not add new data files either.

# Files
## zip2json.py (work in progress):
Reads the contents of the zip file and (eventually) scans each line and converts to a stream of json objects.
