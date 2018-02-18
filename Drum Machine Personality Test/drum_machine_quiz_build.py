#drum_machine_build.py
#Generates the list of questions that the quizzee is asked

class Question:
	"""A class containing one quiz question, consisting of a question and a set of answers sorted by category."""
	def __init__(self, q_txt, a_li):
		self.q_text = q_txt
		self.a_list = a_li


class Endgame:
	"""A class containing personality diagnosis text, a Wikipedia link on a drum machine to scrape the summary paragraph from, and a link to a YouTube clip of a recording involving a drum machine"""
	def __init__(self, diagnosis, wiki, demo, song):
		self.diagnosis = diagnosis
		self.wiki = wiki
		self.demo = demo
		self.song = song


def addquestion(args, q_text, a_list): #makes a Question object and appends it to questions
	args[0].append(Question(q_text, a_list))


def main(args): #args is the questions array and the dictionary

	#CREATING THE QUESTIONS
	tmpli = ["Critic", "Teacher", "Programmer", "Celebrity", "Firefighter"]
	addquestion(args, "What job would you like to have?", tmpli)

	tmpli = ["Class", "Smiles", "Brainpower", "Booty", "Honesty"]
	addquestion(args, "What do you find most attractive?", tmpli)

	tmpli = ["Your birthday", "Valentine's Day", "Halloween", "Saturday", "Thanksgiving"]
	addquestion(args, "What is your favourite holiday?", tmpli)
	
	tmpli = ["Touring Europe", "Skiing", "Comic Conventions", "Las Vegas", "Camping"]
	addquestion(args, "How would you like to spend a vacation?", tmpli)

	tmpli = ["Skating", "Ice Cream", "Gaming", "Clubbing", "Concerts"]
	addquestion(args, "What is your favourite thing to do on a date?", tmpli)

	tmpli = ["Mystery", "YA", "Superhero", "Nope", "Thriller"]
	addquestion(args, "What is your favourite literary genre?", tmpli)
	
	tmpli = ["Alfred Hitchcock", "Hayao Miyazaki", "Peter Jackson", "Michael Bay", "Steven Spielberg"]
	addquestion(args, "Who is your favourite filmmaker?", tmpli)
	
	
	tmpli = ["Audi A7", "Volkswagen Beetle", "DeLorean DMC-12", "Cadillac Escalade", "Ford Mustang"]
	addquestion(args, "Which type of car would you like to own?", tmpli)

	tmpli = ["Tennis", "Ping-Pong", "StarCraft", "Basketball", "Soccer"]
	addquestion(args,"What's your favourite sport?",tmpli)

	tmpli = ["Art", "Biology", "Math", "Gym", "History"]
	addquestion(args,"What was your favourite subject in high school?",tmpli)

	tmpli = ["A fine suit", "Pajamas", "A humourous T-shirt", "Limited-edition sneakers", "Running shoes"]
	addquestion(args,"What is your favourite item of clothing?",tmpli)

	tmpli = ["Relaxing with a good book and a glass of wine", "Volunteering with a local charity", "Magic: The Gathering", "Hanging out with the squad", "Spending time with family"]
	addquestion(args, "What's your favourite way to spend a weekend?",tmpli)
	

	#CREATING THE ENDGAMES
	tmpstr = "You are a CR-78! Suave, smooth, and sophisticated, you pride yourself upon your appreciation of the finer things in life. You dress well, think ahead, and speak tactfully. As the scion of a long line of organ-accompaniment boxes, you sometimes come off as crusty or snobbish, but you make up for it with your impeccable grammar, inimitable fashion sense, and pioneering user-programmable pattern storage."
	args[1][0] = Endgame(tmpstr, 'https://en.wikipedia.org/wiki/Roland_CR-78', 'https://www.youtube.com/watch?v=Wd3HIdipohw', 'https://www.youtube.com/watch?v=Ti6qhk3tX2s')

	tmpstr = "You are a TR-606! Creative, awkward, and adorable, you regularly go out of your way to help others. The best people have no trouble seeing through your social ineptitude to find the wonderful human being underneath, and someday, if it hasn't happened already, one of them is going to fall hard for you. Better hope that they share your love of Disney films and that they can live with your poor signal-to-noise ratio and complete lack of any tone-shaping controls."
	args[1][1] = Endgame(tmpstr, 'https://en.wikipedia.org/wiki/Roland_TR-606', 'https://www.youtube.com/watch?v=LHbckGWz-fo', 'https://www.youtube.com/watch?v=wraDrKHP0tE')

	tmpstr = "You are a TR-707! Logical, obsessive, and unadventurous, your high school marks were excellent despite the fact that you spent half of your math classes playing Mario Kart DS. But when you find a topic truly interesting, you power through it with ruthless efficiency, pausing only to check Tumblr and eat your daily ration of Kraft Dinner. Your parents wish you would call more often and you are uncommonly terrible at making jokes, but your powerful brain and individual instrument output jacks make you a winner."
	args[1][2] = Endgame(tmpstr, 'https://en.wikipedia.org/wiki/Roland_TR-707', 'https://www.youtube.com/watch?v=gEnIFbrjHc8', 'https://www.youtube.com/watch?v=mG3jv2ObYMA')

	tmpstr = "You are a TR-808! Talkative, provocative, and confident, you find silence suffocating and are most at home in a large group of friends. You like slow beats, fast cars, and Kanye West, and your real-life friends are as impressively numerous as your Instagram followers. You haven't cried in over a year. Meanwhile, the whole world just can't seem to get enough of your irreverent verve and your wall-shaking kick drum."
	args[1][3] = Endgame(tmpstr, 'https://en.wikipedia.org/wiki/Roland_TR-808', 'https://www.youtube.com/watch?v=aoiDs41Pr_0', 'https://www.youtube.com/watch?v=n2MVzP4MaJ0')

	tmpstr = "You are a TR-909! Loyal, likable, and honest, you are a team player and a great friend. You like dogs, handshakes, and the Beatles. As a youngest sibling, you've done your best to learn from the mistakes of your forebears, but you allow people in your life to intrude upon spare time that you should really spend working toward your own goals. Meanwhile, your bright eyes, repitchable cymbals, and MIDI connectivity get you asked out more frequently than would be comfortable."
	args[1][4] = Endgame(tmpstr, 'https://en.wikipedia.org/wiki/Roland_TR-909', 'https://www.youtube.com/watch?v=SHrqQb03n4k', 'https://www.youtube.com/watch?v=GuJQSAiODqI')

if __name__ == '__main__':
	import sys
	main(sys.argv[1:]) #sys.argv[0] is the name of the script, so only argv[1:] is needed to run the main
