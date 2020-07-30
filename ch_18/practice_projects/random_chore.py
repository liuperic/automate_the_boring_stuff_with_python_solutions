# random_chore.py - Randomly assigns chore and emails the person.
# Keeps record of last week's chore assignments so person does not do same chore
# two weeks in a row. Script runs once a week from time of initial run.

import csv, os, random, schedule, time

def chore():
    # Edit list of names / emails to assign chores to
    emails = {'bob':'bob@example.com', 'alice':'alice@example.com', 'james':'james@exmaple.com', 'timothy':'timothy@example.com'}

    # Edit list of chores below.
    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

    last_assignment = []

    # Read last week assignment so no repeat chores for person
    if os.path.exists('chore-assignment.csv'):
        with open('chore-assignment.csv', 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                last_assignment.append(','.join(row))
        
    
    with open('chore-assignment.csv', 'w') as f:
        csv_writer = csv.writer(f)
    
        # Keep assigning chores until all chores assigned
        while chores:

            random_chore = random.choice(chores)
            random_person = random.choice(list(emails))

            check = random_chore + ',' + random_person

            # Ensure no repeat chore from last week
            while check in last_assignment:
                random_chore = random.choice(chores)
                random_person = random.choice(list(emails))
                check = random_chore + ',' + random_person

            chores.remove(random_chore)
            emails.pop(random_person, None)

            csv_writer.writerow([random_person, random_chore])

        print('Assigned chores listed in chore-assignment.csv...')
            
chore()

# Runs once a week
schedule.every().week.do(chore)

while True:
    schedule.run_pending()
    time.sleep(1)