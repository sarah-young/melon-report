def melon_count():
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        print  "Delivered {} {}s for total of ${}".format(
        count, melon, amount)

print "Day 1"
the_file = open("um-deliveries-20140519.txt")
melon_count()
the_file.close()


print "Day 2"
the_file = open("um-deliveries-20140520.txt")
melon_count()
the_file.close()


print "Day 3"
the_file = open("um-deliveries-20140521.txt")
melon_count()
the_file.close()
