import csv
a=1
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        #print(row[2])
        #row[2]-name
        #row[3]-person
        #row[4]-contact
        #row[5]-date_time
        #row[6]-link
        #row[7]-disc
        #row[9]-req
        #row[10]-cost
        #row[11]-venue
        image=a
        event_name=row[2]
        date_time=row[5]
        link=row[6]
        disc=row[7]
        req=row[9]
        cost=row[10]
        contact=row[4]
        person=row[3]
        venue=row[11]
        print(' <div class="event-container"> ')
        print(f'<div class="event-box"  style="background-image: url(\'images/{image}.png\')">')
        print(f'<h3 class="event-title">{event_name}</h3>')
        print(f'<p class="event-details">{date_time}</p>')
        print('<p class="event-details"><a href="javascript:void(0);" class="details-button">More details</a></p>')
        print('<div class="details-popup" id="details-popup">')
        print('<div class="details-content" style="background-image: url(\'common.jpg\')">')
        print(f'<a class="register-button" href="{link}">Register Now</a>')
        print(f'<h3 class="event-title">{event_name}</h3>')
        print(f'<p class="event-details">{date_time}</p>')
        print(f'<p class="event-details">{venue}</p>')
        print(f'<p class="event-details">{person}</p>')
        print(f'<p class="event-description">{disc}</p>')
        print(f'<p class="event-requirements">Requirements:{req}</p>')
        print(f'<p class="event-cost">Cost: {cost}</p>')
        print(f'<p class="event-contact">Contact: {contact}</p>')
        print('<a href="javascript:void(0);" class="close-button">Close</a>')
        print(" </div>")
        print("</div>")
        print("</div>")
        print("</div>")
        a=a+1

        
        
