import pytz
import datetime

#for x in pytz.all_timezones:
#    myCountry = x
#    tzOfMyCountry = pytz.timezone(myCountry)
#    print("*"*50)
#    print(tzOfMyCountry)
#    currentTimeInMyCounter = datetime.datetime.now(tzOfMyCountry)
#    print(currentTimeInMyCounter)

print(pytz.country_names)
# for x in pytz.country_names:
    # this below give error because BV have no timezone defined, so we used .get method in dictionary
    #print(x + ": " + pytz.country_names[x] + ": " + str(pytz.country_timezones[x]))
#    print(x + ": " + pytz.country_names[x] + ": " + str(pytz.country_timezones.get(x)))
    # BV: Bouvet Island: None
#    print("\n")



for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x] + ": ", end="")
    if x in pytz.country_timezones.keys():
        for myZone in sorted(pytz.country_timezones[x]):
            tzOfMyCountry = pytz.timezone(myZone)
            currentTimeInMyCountry = datetime.datetime.now(tz=tzOfMyCountry)
            print("\t\t" + str(myZone) +":  " + str(currentTimeInMyCountry))

    else:
        print("\t\t NO TimeZone Defined For This Country")