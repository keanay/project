from graphics import *
import time,os,glob
#################
win_width,win_height=500,800
parent_path=os.getcwd() #WHERE ARE WEEEEE

###################

def inside(point, rectangle):
    """ the the given Point(x,y) is inside the rectangle?
    this func is used with the data returned from WIN.getMouse() to determine if the user is clicking on an object or not"""

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def closeGr(win):
 	win.close()
def rec_fill(rec,m_win,color):
	rec.setFill(color)
	rec.draw(m_win)
#####################################################

def welcome():
	'''
	the first window to show 
	it ask the user for what type is he to determine what is his propose of using this app 
	'''
	main=GraphWin("mainapp",win_width,win_height)
	main.setBackground('white')
	img=Image(Point(250,400),os.path.join(parent_path,'pic.png'))
	img.draw(main)
	text=Text(Point(250,100),"you are ...")
	text.draw(main)
	org_box=Rectangle(Point(100,600),Point(200,650))
	org_box.draw(main)
	vol_box=Rectangle(Point(300,600),Point(400,650))
	vol_box.draw(main)
	txt=Text(Point(150,620),"an organizer")
	txt.draw(main)
	del txt
	txt=Text(Point(350,620),'a volunteer')
	txt.draw(main)
	del txt
	usr_def=Text(Point(250, 320),'')
	usr_def.draw(main)
	while True:
		pass
		click=main.getMouse()
		if inside(click, org_box):
			#the user wants to advertise his organization 
			usr_def.setText("you're an organizer")
			Text(Point(250,600),'you will be directed right now to organizers interface...').draw(main)
			closeGr(main)
			org_first()
			break
		elif inside(click,vol_box):
			#the user is a vol_user
			usr_def.setText("you're a volunteer")
			time.sleep(0.5)
			Text(Point(250,600),'you will be directed right now to volunteers interface...').draw(main)
			time.sleep(1)
			closeGr(main)
			chosen_keys=vol_first()
			vol_second(vol_interested_into(chosen_keys))

			break

#########################################################
'''
volunteers section
'''

def vol_first():
	'''take the type of services the vol_user is interested into giving help with '''
	page=GraphWin('volunteer',win_width,win_height)
	page.setBackground('white')
	img=Image(Point(250,400),'pic.png')
	img.draw(page)
	Text(Point(250,100),'select your fields of interest:').draw(page)
	#### choices boxes 
	hel_care=Rectangle(Point(100,200),Point(200,250))
	hel_care.draw(page)
	Text(Point(150,220),'Health Care').draw(page)
	
	don=Rectangle(Point(300,200),Point(400,250))
	don.draw(page)
	Text(Point(350,220),"Donation").draw(page)

	edu=Rectangle(Point(100,300),Point(200,350))
	edu.draw(page)
	Text(Point(150,320),'Education').draw(page)

	env=Rectangle(Point(300,300),Point(400,350))
	env.draw(page)
	Text(Point(350,320),'Environmental').draw(page)

	soc=Rectangle(Point(200,400),Point(300,450))
	soc.draw(page)
	Text(Point(250,420),"Social").draw(page)

	####
	Qw=Rectangle(Point(390,740),Point(490,790))
	Qw.draw(page)
	Text(Point(440,760),'Done').draw(page)
	ck=[]
	chosen_keys=[]
	while True:
		click=page.getMouse()
		if inside(click,hel_care):
			ck.append('healthcare')
			hel_care.setFill('red')
		if inside(click,don):
			ck.append('donation')
			don.setFill('red')
		if inside(click,edu):
			ck.append('education')
			edu.setFill('red')
		if inside(click,env):
			ck.append('enviromnental')
			env.setFill('red')
		if inside(click,soc):
			ck.append('social')
			soc.setFill('red')
		if inside(click,Qw):
			break
	Text(Point(200,760),"you will be redirected to the main page right now").draw(page)
	for i in ck:
		if i not in chosen_keys:
			chosen_keys.append(i)
	closeGr(page)
	return chosen_keys



def vol_interested_into(chosen_keys):
	'''this func shows boxes containing infos of each orgs that need help the vol_user can give'''
	F_T_S=[] #files i will hold directories  to files the program will show to the vol_user 
	for key in chosen_keys:
		if os.path.exists(os.path.join('orgs_data/',key)):
			os.chdir(os.path.join('orgs_data/',key))
			for file0 in glob.glob('*.orgd'):
				F_T_S.append(os.path.join(key+'/'+file0))
			os.chdir(parent_path)

		

	return(F_T_S)


def vol_second(files_list):
	sec_page=GraphWin('organizations',win_width,win_height)
	sec_page.setBackground('white')
	img=Image(Point(250,400),os.path.join(parent_path,'pic.png'))
	img.draw(sec_page)
	Text(Point(250,50),'organizations that needs help').draw(sec_page)
	r1=Rectangle(Point(50,100),Point(450,250))
	r_1_sub=Rectangle(Point(400,200),Point(440,240))
	r2=Rectangle(Point(50,300),Point(450,450))
	r_2_sub=Rectangle(Point(400,400),Point(440,440))
	r3=Rectangle(Point(50,500),Point(450,650))
	r_3_sub=Rectangle(Point(400,600),Point(440,640))

	qwt=Rectangle(Point(225,700),Point(275,750))
	qwt.draw(sec_page)
	Text(Point(250,725),"quite").draw(sec_page)

	


	count=1
	if not files_list==[]:
		for i in files_list:
			if count==1:
				in_x,in_y1,in_y2,in_y3=220,110,160,210
				mem1=database_reader(i)
				rec_fill(r1,sec_page,color_rgb(234, 234, 234))
				rec_fill(r_1_sub,sec_page,'white')
				Text(Point(420,220),'>>').draw(sec_page)
			elif count==2:
				in_x,in_y1,in_y2,in_y3=220,310,360,410
				mem2=database_reader(i)
				rec_fill(r2,sec_page,color_rgb(234, 234, 234))
				rec_fill(r_2_sub,sec_page,'white')
				Text(Point(420,420),">>").draw(sec_page)
			if count==3:
				in_x,in_y1,in_y2,in_y3=220,510,560,610
				mem3=database_reader(i)
				rec_fill(r3,sec_page,color_rgb(234, 234, 234))
				rec_fill(r_3_sub,sec_page,'white')

				Text(Point(420,620),">>").draw(sec_page)
			per_org_dt=database_reader(i)
			Text(Point(in_x,in_y1),"organization name: "+per_org_dt[0]).draw(sec_page)
			Text(Point(in_x,in_y2),"Located in :"+per_org_dt[5]).draw(sec_page)
			Text(Point(in_x,in_y3),"needs help related with :"+per_org_dt[2]).draw(sec_page)
			if i==files_list[-1]:
				while True:
					click=sec_page.getMouse()
					if inside(click,r_1_sub):
						r_1_win=GraphWin('organization description',500,500)
						r_1_win.setBackground('white')
						img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
						img.draw(r_1_win)
						tit1=Text(Point(250,50),mem1[0])
						tit1.setSize(25)
						tit1.draw(r_1_win)
						Text(Point(150,100),'mission description: '+mem1[3]).draw(r_1_win)
						Text(Point(150,150),'goal :'+mem1[1]).draw(r_1_win)
						stit1=Text(Point(250,220),'Contact the organizers')
						stit1.setSize(20)
						stit1.draw(r_1_win)
						Text(Point(150,280),"email: "+mem1[4]).draw(r_1_win)
						Text(Point(150,340),'website: '+mem1[6]).draw(r_1_win)


					if inside(click,r_2_sub):
						r_2_win=GraphWin('organization description',500,500)
						r_2_win.setBackground('white')
						img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
						img.draw(r_2_win)
						tit2=Text(Point(250,50),mem2[0])
						tit2.setSize(25)
						tit2.draw(r_2_win)
						Text(Point(150,100),'mission description: '+mem2[3]).draw(r_2_win)
						Text(Point(150,150),'goal :'+mem2[1]).draw(r_2_win)
						stit2=Text(Point(250,220),'Contact the organizers')
						stit2.setSize(20)
						stit2.draw(r_2_win)
						Text(Point(150,280),"email: "+mem2[4]).draw(r_2_win)
						Text(Point(150,340),'website: '+mem2[6]).draw(r_2_win)

					if inside(click,r_3_sub):
						r_3_win=GraphWin('organization description',500,500)
						r_3_win.setBackground('white')
						img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
						img.draw(r_3_win)
						tit3=Text(Point(250,50),mem3[0])
						tit3.setSize(25)
						tit3.draw(r_3_win)
						Text(Point(150,100),'mission description: '+mem3[3]).draw(r_3_win)
						Text(Point(150,150),'goal :'+mem3[1]).draw(r_3_win)
						stit3=Text(Point(250,220),'Contact the organizers')
						stit3.setSize(20)
						stit3.draw(r_3_win)
						Text(Point(150,280),"email: "+mem3[4]).draw(r_3_win)
						Text(Point(150,340),'website: '+mem3[6]).draw(r_3_win)
					if inside(click,qwt):
						sec_page.close()
						welcome()

						break

			count+=1
	else:
		Text(Point(250,500),'nothing to show here currently').draw(sec_page)
	
#'<name>0','<goal>1','<need>2','<desc>3','<email>4','<city>5','<website>6





####################
'''
organization section
'''
def col_ent(en_b,m_win):
	en_b.setFill(color_rgb(170, 255, 255))
	en_b.draw(m_win)

def org_first():
	org_form1=GraphWin('orgs infos',win_width,win_height)
	org_form1.setBackground('white')
	img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
	img.draw(org_form1)
	Text(Point(250,100),"please fill in the entry boxes below ").draw(org_form1)
	Text(Point(150,150),"what's your organization name?").draw(org_form1)
	org_name=Entry(Point(150,200),30)
	col_ent(org_name,org_form1)
	
	Text(Point(150,350),'tell us about your organization').draw(org_form1)
	org_desc=Entry(Point(150,400),30)
	col_ent(org_desc,org_form1)

	Text(Point(165,550),'what goal your organization is trying to reach?').draw(org_form1)
	org_goal=Entry(Point(150,600),30)
	col_ent(org_goal,org_form1)
	nxt_box=Rectangle(Point(350,740),Point(450,790))
	nxt_box.draw(org_form1)
	Text(Point(400,760),'next').draw(org_form1)
	while True:
		click=org_form1.getMouse()
		if inside(click,nxt_box):
			name,desc,goal,=org_name.getText(),org_desc.getText(),org_goal.getText()
			org_form1.close()
			break
	###########

	org_form2=GraphWin('orgs infos',win_width,win_height)
	org_form2.setBackground('white')
	img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
	img.draw(org_form2)
	Text(Point(250,100),'what type of help does your organization need from volunteers?').draw(org_form2)
	hel_care=Rectangle(Point(100,200),Point(200,250))
	hel_care.draw(org_form2)
	Text(Point(150,220),'Health Care').draw(org_form2)
	
	don=Rectangle(Point(300,200),Point(400,250))
	don.draw(org_form2)
	Text(Point(350,220),"Donation").draw(org_form2)

	edu=Rectangle(Point(100,300),Point(200,350))
	edu.draw(org_form2)
	Text(Point(150,320),'Education').draw(org_form2)

	env=Rectangle(Point(300,300),Point(400,350))
	env.draw(org_form2)
	Text(Point(350,320),'Environmental').draw(org_form2)

	soc=Rectangle(Point(200,400),Point(300,450))
	soc.draw(org_form2)
	Text(Point(250,420),"Social").draw(org_form2)
	shown=False
	while True:

		if shown==True:
			nxt_box=Rectangle(Point(350,740),Point(450,790))
			nxt_box.draw(org_form2)
			Text(Point(400,760),'next').draw(org_form2)
			while True:
			 	click_s=org_form2.getMouse()
			 	if inside(click_s,nxt_box):
			 		break
			break
		org_need=''
		click=org_form2.getMouse()
		if inside(click,hel_care):
			org_need='healthcare'
			hel_care.setFill('red')
			shown=True
		elif inside(click,don):
			org_need='donation'
			don.setFill('red')
			shown=True
		elif inside(click,edu):
			org_need='education'
			edu.setFill('red')
			shown=True
		elif inside(click,env):
			org_need='enviromnental'
			env.setFill('red')
			shown=True
		elif inside(click,soc):
			org_need='social'
			soc.setFill('red')
			shown=True
	need=org_need
	org_form2.close()

	org_form3=GraphWin('orgs infos',win_width,win_height)
	org_form3.setBackground('white')
	img=Image(Point(250,250),os.path.join(parent_path,'pic.png'))
	img.draw(org_form3)
	Text(Point(250,100),"contacting your organization infos")
	Text(Point(205,150),"which city or cities your organization office is located in ?").draw(org_form3)
	org_city=Entry(Point(150,200),30)
	col_ent(org_city,org_form3)
	Text(Point(200,350),"organization's website or socialnetwork page").draw(org_form3)
	org_webs=Entry(Point(150,400),30)
	col_ent(org_webs,org_form3)

	Text(Point(165,550),'email').draw(org_form3)
	org_email=Entry(Point(150,600),30)
	col_ent(org_email,org_form3)
	nxt_box=Rectangle(Point(350,740),Point(450,790))
	nxt_box.draw(org_form3)
	done_Text=Text(Point(400,760),'done')
	done_Text.draw(org_form3)
	while True:
		click=org_form3.getMouse()
		if inside(click,nxt_box):
	 		webs,email,city=org_webs.getText(),org_email.getText(),org_city.getText()
	 		Text(Point(250,650),"you've succesfully filled your organization advertising.").draw(org_form3)
	 		Text(Point(250,700),"now just wait for volunteers to contact you through email or your website").draw(org_form3)
	 		done_Text.setText('Exit')
	 		org_form3.getMouse()
	 		break
	database_writter(goal,need,desc,email,city,webs,name)
	org_form3.close()
	welcome()
###################
'''
working with data section
'''
def database_writter(goal,need,description,email,city,webs,org_name):
	if not os.path.exists(os.path.join('orgs_data/',need)):
		if not os.path.exists('orgs_data/'):
			os.mkdir(os.path.join('orgs_data/'))
		os.mkdir(os.path.join('orgs_data/',need))
	os.chdir(os.path.join('orgs_data/',need))
	file=open(org_name+'.orgd','w')
	print(org_name,'<name>',goal,'<goal>',need,'<need>',description,'<desc>',email,'<email>',city,'<city>',webs,'<website>',file=file)
	file.close()
	os.chdir(parent_path)

def database_reader(file):
	#this func gets the org name and return a list containing data about it  'donation/????.orgd'
	os.chdir(parent_path)
	os.chdir('orgs_data')
	os.chdir(file.split('/')[0])
	pre_sp=''
	data_list=[]
	for i in ['<name>','<goal>','<need>','<desc>','<email>','<city>','<website>']:
		data_1=open(file.split('/')[-1],'r').read().split(i)[0]
		if pre_sp=='':
			data_2=data_1
			pre_sp=i
		else:
			data_2=data_1.split(pre_sp)[-1]
		data_list.append(data_2)
		pre_sp=i
	return data_list



######
'''jump start'''
if __name__=='__main__':
	welcome()
