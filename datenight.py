#!/usr/bin/python

from datetime import date
import rpy2.robjects as robjects

getdate = robjects.r('function(year,month,day){ return(c(year=year, month=month, day=day))}')

thedate = getdate(2012,6,20)

cara_and_jake_available = set([date(thedate[0],thedate[1],thedate[2])])
cjellrun_and_luke_available = cara_and_jake_available #set([])
sam_and_sam_available = set([date(year=2012, month=6, day=20),
                             date(year=2012, month=6, day=16)])

cj_babysitter =cara_and_jake_available #set([])
kl_babysitter =cara_and_jake_available #set([])
ss_babysitter =cara_and_jake_available #set([])

def print_dates(dates):
    for d in dates:
        print d.strftime("%m/%d/%Y")

def main():
    global cara_and_jake_available, cjellrun_and_luke_available, sam_and_sam_available
    global cj_babysitter, kl_babysitter, ss_babysitter

    possible_dates = reduce(lambda x,y: x.intersection(y),
                            [sam_and_sam_available,
                             cara_and_jake_available,
                             cjellrun_and_luke_available])

    if possible_dates == None or len(possible_dates) == 0:
        print "Could not find any dates for the babysitters"
        return

    print "Here are some dates to ask the babysitters:"
    print_dates(possible_dates)
    print
    
    possible_dates = map(lambda x: x.intersection(possible_dates), [cj_babysitter,
                                                                    kl_babysitter,
                                                                    ss_babysitter])

    possible_dates = reduce(lambda x,y: x.intersection(y), possible_dates)

    if possible_dates == None or len(possible_dates) == 0:
        return

    print "DATE NIGHT!!!:"
    print_dates(possible_dates)

if __name__ == "__main__":
    main()
