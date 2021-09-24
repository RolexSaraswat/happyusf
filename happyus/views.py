from django.shortcuts import render
from django.http import HttpResponse
from .models import team ,intrn
from django.core.mail import send_mail

def home(request):

	

		team1 = team()
		team1.name='Kshitij Vaibhav'
		team1.img='kv.png'
		team1.role='Operations Head'
		team.link="https://www.linkedin.com/in/kshitij-vaibhav-8692861ba"
		team2 = team()
		team2.name='Apoorav Jain'
		team2.img='ap.png'
		team2.role='Chief Executive Officer '
		team2.link="https://www.linkedin.com/in/apoorav-jain-84ba9018b"
		team3 = team()
		team3.name='Shivam Verma'
		team3.img='shi.png'
		team3.role='Chief Technical Officer'
		team3.link="https://www.linkedin.com/in/shivam-verma-978b5718b"
		team4 = team()
		team4.name='Rithik Bhandari'
		team4.img='ri.png'
		team4.role='Technical Head'
		team4.link=""
		team5 = team()
		team5.name='Chetna Dua'
		team5.img='ch.png'
		team5.role='Creative Head'
		team5.link=""
		team6 = team()
		team6.name='Aashie Chaudhary'
		team6.img='aa.png'
		team6.role='Communication Head'
		team6.link="https://www.linkedin.com/in/aashie-chaudhary-1a6566214"
		team7 = team()
		team7.name='Rishab Pandey'
		team7.img='ris.png'
		team7.role='Social Media Head'
		team7.link=""
		team8 = team()
		team8.name='Bhanvi Aggarwal'
		team8.img='bh.png'
		team8.role='HR Head'
	
		team9 = team()
		team9.name='Shubham Mittal'
		team9.img='sh.png'
		team9.role='Design Head'
		team9.link="https://www.linkedin.com/in/shubham-mittal-bb694918b"
		teamc=[team2,team3,team9,team8,team1,team4,team6,team5,team7]


		intrn1=intrn()
		intrn1.name='Raaghav Bhasin'
		intrn1.quote="Sometimes people don't realise that the person who you vent out to could also use some venting out. For people like me who usually listen to others, I was glad to know I have a listener by the name of 'Happy Us' too"
		intrn1.img='rag.jpg'
		intrn2=intrn()
		intrn2.name='PRIYANSHU KASHYAP'
		intrn2.quote="Happy us foundation showers love and support to all young generation and as well as old , irrespective to any caste creed and religion. It's my pleasure to be a part of it."
		intrn2.img='pri.jpg'
		intrn3=intrn()
		intrn3.name='Aditi Kumari '
		intrn3.quote='Accept what life brings on the table and keep working to create better days than all the " yesterdays". And never feel shy to express yourself ,dump all that mental baggage, allow yourself to breathe freely,'
		intrn3.img='adi.jpg'
		intrn4=intrn()
		intrn4.name='Harshit Tiwari'
		intrn4.quote='Happy Us is a Very nice and good platform to share your inner thoughts and feelings with someone and Happy Us allows you to know others feelings so you can know and share their new stories and feelings as well.'
		intrn4.img='har.jpg'
		intrn5=intrn()
		intrn5.name='Vinayak'
		intrn5.quote='Its a very great experience working with Happy Us it made me Happy.'
		intrn5.img='vin.jpg'
		intrn6=intrn()
		intrn6.name='Divyansh Palia'
		intrn6.quote='Everyday is so positive at Happy Us! Apoorav and all the co-heads are fantastic workers who are dedicated to serve their part for the community which is fascinating and wants me to do the same as well.'
		intrn6.img='div.jpg'
		intrn7=intrn()
		intrn7.name='Shreya Chatterjee'
		intrn7.quote='Being a part of happy us is an elite thing you can do to yourself. They hear you out! You are sad, depressed, anxious, they help you out get through it. Till now, they have helped a lot of people going through the same. '
		intrn7.img='shr.jpg'
		intrn8=intrn()
		intrn8.name='Mansi Gupta'
		intrn8.quote='My experience with Happy Us has been great till now.I worked with the technical team and did my part in developing the website for Happy Us.The Happy Us team is very encouraging and supportive which provides a great environment for working.'
		intrn8.img='man.jpg'
		intrn9=intrn()
		intrn9.name='Srishti'
		intrn9.quote='HAPPY US is creating awareness about mental health and Spreading happiness which is really a good initiative and idea. Interning at happy us was a really wonderful experience. All colleagues were friendly and very helpful. I have learned a lot working here.'
		intrn9.img='sri.jpg'
		intrn10=intrn()
		intrn10.name='Megha'
		intrn10.quote='Happy us doing a great work.. It help those student who feel lonely and unheard. And I am very happy to work in this organisation.'
		intrn10.img='meg.jpg'
		intrn11=intrn()
		intrn11.name='Akshat'
		intrn11.quote="Working with Happy us had a great experience for me as I have got to know how a team works together to achieve something. A special mention for Apoorva Jain our boss who worked all day/night which made Happy us what it is today. At last it's just an immense pleasure to work with Happy us."
		intrn11.img='aks.jpg'
		intrn12=intrn()
		intrn12.name='Bhawna'
		intrn12.quote="it's commendable how Apoorav and his amazingly Hard working team makes an idea a huge success. I am glad I've been chosen to become a part of this journey and make new amazing friends despite of the pandemic and being behind the screens.Happy us brings me joy just like it's name."
		intrn12.img='bha.jpg'
		intrn13=intrn()
		intrn13.name='Naaz Verma'
		intrn13.quote='Happy us is actually something which is in no doubt bringing out a little shine of joy and peace around.With its features of volunteers it is a great way to communicate without the fear of judgment and get your mind and heart cleared.The posts and activities are highly intriguing and totally bring out a self.'
		intrn13.img='naa.jpg'
		intrn14=intrn()
		intrn14.name='Adhya Gupta'
		intrn14.quote="Everyone goes though downward curve in their life and want someone to be with to listen. I am glad to know I have a listener by the name of 'Happy Us' where i can share all my feelings without even a fear of disclosing .Thank you for coming out with such a comfortable platform for all people out there."
		intrn14.img='adh.jpg'
		intrn15=intrn()
		intrn15.name='Geet'
		intrn15.quote='I have been working with happy us for quite some time now, and I have had a very good experience with them. I work as a creative content creator in the team and work on template designing, editing videos, etc. the create a very healthy environment to work in.'
		intrn15.img='gee.jpg'
		intrn16=intrn()
		intrn16.name='Danish'
		intrn16.quote="This pandemic as a whole was already too much too handle. But I got to know about happy us at the same time.Then I was intrigued by the apps feature that i can post and even talk people about my feeling. I didn't know talking could be such relieving task. Even if sometimes the app stops working, you can't be mad cause those beep beep bop message makes you laugh."
		intrn16.img='dan.jpg'
		intrn17=intrn()
		intrn17.name='Aastha Sinha'
		intrn17.quote='I was introduced to happy us by my brother who is a core head in the organisation and honestly this was a wonderful experience I have edited several videos for them and the ideas these people have are awesome and I would love to create more for them.'
		intrn17.img='aas.jpg'
		intrn18=intrn()
		intrn18.name='Rolex Saraswat'
		intrn18.quote='Happy us came to me as an internship opportunity introduced to me by my batchmate but its become so much more I learnt a lot about the initiative while designing this very website and would like to stay here for a long time to come'
		intrn18.img='rol.jpg'
		intrn19=intrn()
		intrn19.name='Akshat Rastogi'
		intrn19.img='aksh.jpg'
		intrn19.quote="The app helped me cope up with work stress and professional jealously. I was trilled when I worked on the iOS deployment of the appm"
		intrn20=intrn()

		intrn20.name='Ankita'
		intrn20.quote="I am happy to learn that you don’t have to struggle in silence. You can be UN-SILENT and live with a mental health condition as long as you open up to somebody like ‘Happy Us’ about it."
		intrn20.img="ank.jpg"
		interns=[intrn15,intrn18,intrn17,intrn16,intrn14,intrn13,intrn12,intrn19,intrn20,intrn11,intrn10,intrn9,intrn8,intrn7,intrn6,intrn5,intrn4,intrn3,intrn2,intrn1]
		

		
        

		context={
			'teamc':teamc,
			'interns':interns

		}
		

		return render(request,"home.html", context)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'content': content
        }
        

        send_mail(
            data['name'],
            'Name: '
            + data['name']
            + '\nEmail: '
            + data['email']
            + '\nMobile: '
            + data['phone']
            + '\n\nMessage:\n'
            + data['content'],
            'happyus404@gmail.com',
            ['happyus404@gmail.com'],
            fail_silently=False
        )


        return render(request, 'home.html', {'name':name})
    else:
        return render(request, 'contact.html')
