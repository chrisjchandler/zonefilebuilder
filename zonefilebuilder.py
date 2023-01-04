# prompt the user to enter the domain name
domain_name = input("Enter the domain name: ")

# create an empty dictionary to store the DNS records
records = {}

# prompt the user to enter the DNS records
while True:
  # prompt the user to enter the record type (A, CNAME, MX, etc.)
  record_type = input("Enter the record type (A, CNAME, MX, etc.) or type 'done' to finish: ")
  
  # check if the user is finished entering records
  if record_type.lower() == "done":
    break
  
  # prompt the user to enter the record value
  record_value = input("Enter the record value: ")
  
  # add the record to the dictionary
  records[record_type] = record_value

# create the zone file
zone_file = ""

# add the domain name to the zone file
zone_file += "$ORIGIN " + domain_name + "\n"

# add the DNS records to the zone file
for record_type, record_value in records.items():
  zone_file += record_value + " " + record_type + "\n"

# print the zone file
print(zone_file)
