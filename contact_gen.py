############################
# iBen contacts genereator #
############################

import random
import sys

# lists of contact info to randomize
def generate_contact():
    first_names = ["John", "Emma", "Michael", "Sophia", "Robert", "Olivia", "William", "Ava", "David", "Mia","Daniel", "Elad", "Michael", "Noa", "Maytal", "Taliya", "Natali"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Kadosh", "Levi", "Cohen", "Amsalem", "Arbiv", "Sofer"]
    phone_prefixes = ["+1", "+44", "+61", "+81", "+86", "+971", "+33", "+90", "+972"]
    email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com", "walla.co.il"]
    street_names = ["Main St", "Park Ave", "Elm St", "Maple Ave", "Oak St", "Cedar Ln", "Pine St", "Washington Blvd", "Hillside Avenue", "Willow Lane", "Oakwood Drive", "Elmwood Avenue", "Pinecrest Road", "Meadow Lane", "Forest Street", "Cedar Avenue", "Birchwood Lane"]
    cities = ["New York", "London", "Sydney", "Tokyo", "Paris", "Berlin", "Rome", "Madrid", "Moscow", "Toronto", "Tel Aviv", "Dubai", "Miami Beach", "Los Angeles"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    phone_prefix = random.choice(phone_prefixes)
    phone_number = str(random.randint(100000000, 999999999))
    email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}"
    street_number = str(random.randint(1, 999))
    street_name = random.choice(street_names)
    city = random.choice(cities)
    address = f"{street_number} {street_name}, {city}"
    
    contact = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name} {last_name}\nTEL;TYPE=CELL:{phone_prefix}{phone_number}\nEMAIL;TYPE=HOME,INTERNET:{email}\nADR;TYPE=HOME:;;{address};;;;\nEND:VCARD\n"
    return contact

# args to create contact files  
def generate_contacts(filename, num_contacts):
    contacts = []
    for _ in range(num_contacts):
        contact = generate_contact()
        contacts.append(contact)
    
    with open(filename, "w") as f:
        f.writelines(contacts)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\n Usage: python.exe contacts_gen.py <filename.vcf> <number of contacts you want to generate>\n\n So something like this: -- python.exe contacts_gen.py name.vcf 500 -- \n")
        sys.exit(1)

    filename = sys.argv[1]
    num_contacts = int(sys.argv[2])
    generate_contacts(filename, num_contacts)
    print(f"\n{num_contacts} contacts generated and saved to {filename} \n\n")
