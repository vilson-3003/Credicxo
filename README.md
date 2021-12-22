# Credicxo
# Credicxo
Project Name: credicxo_task
app name: authentication

Super Admin :
	username: vilson
	password: 12345

1: Urls to check:
	
	url for Login: localhost:8000/login   (use POST request)
	
	1: For Login please fill the details in the body section in the json format inside postman
	
	{
 	   "username":"vk",
 	   "password":"admin@12345"
	}   

              

	url for Admin registration: localhost:8000/registration/admin/   (use POST request)
	
	1: For registration please fill the details in the body section in the json format inside postman
	
		{
               "username":"vk",
    		"first_name":"vilson",
   		"last_name":"kumar",
   		"email":"correct_email@gmail.com",
		"password1":"admin@12345",
		"password2":"admin@12345"
		}
		

	url for Teacher Registration:  localhost:8000/registration/teacher/   (use POST request)
	
	1: For registration please fill the details in the body section in the json format inside postman
	
		{
               "username":"vk",
    		"first_name":"vilson",
   		"last_name":"kumar",
   		"email":"correct_email@gmail.com",
		"password1":"admin@12345",
		"password2":"admin@12345"
		}

	url for Student Registration:  localhost:8000/registration/student/   (use POST request):
	
	1: For registration please fill the details in the body section in the json format inside postman
	
		{
               "username":"vk",
    		"first_name":"vilson",
   		"last_name":"kumar",
   		"email":"correct_email@gmail.com",
		"password1":"admin@12345",
		"password2":"admin@12345"
		}
 

	url for Forgot password: localhost:8000/api/password_reset/     (use POST request) :
		
	1:After hitting the url the user will get a link to reset the password
	2:Copy the link and paste in the postman and type the current password in the body in the form of jason
	3:A link to reset password will received on the email from email named "wilsonkumar518@gmail.com", subject will Password Reset : Credixo Forgot Password, then after the passsword will changed
	4:Now login with new credentials. 

	

	url for list of students: localhost:8000/liststudents
		1: to get the list of students first we have to login with postman in above 1st step. After login it provide access keys. 
		2: We have to copy the access key and have to paste it into authorization tab and type should be bearer token 
		3: Then it will show the all the data.


	url for list of students: localhost:8000/listteachers
		1: to get the list of students first we have to login with postman in above 1st step. After login it provide access keys. 
		2: We have to copy the access key and have to paste it into authorization tab and type should be bearer token 
		3: Then it will show the all the data.
		


