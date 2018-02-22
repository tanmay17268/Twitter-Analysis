from django.shortcuts import render

def ans(n):
	if (n.lower()=='america'):
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(35)+r"% in BBC News", str(45)+r"% in FOX News",str(20)+r"% in Various News Sources",str(45.2)+r"% in Tweets", "NEUTRAL",str(45)+r"% in BBC News",str(45)+r"% in FOX News",str(70)+r"% in Various News Sources", str(31.9)+r"% in Tweets","NEGATIVE",str(20)+r"% in BBC News",str(10)+r"% in FOX News", str(10)+r"% in Various News Sources",str(22.9)+r"% in Tweets"]
	    return tb
	elif (n.lower()=='army'):
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(15)+r"% in BBC News", str(15)+r"% in FOX News",str(0)+r"% in Various News Sources",str(46.3)+r"% in Tweets", "NEUTRAL",str(70)+r"% in BBC News",str(55)+r"% in FOX News",str(100)+r"% in Various News Sources", str(45.9)+r"% in Tweets","NEGATIVE",str(15)+r"% in BBC News",str(30)+r"% in FOX News", str(0)+r"% in Various News Sources",str(7.8)+r"% in Tweets"]
	    return tb
	elif (n.lower()=='asian'):
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(15)+r"% in BBC News", str(5)+r"% in FOX News",str(0)+r"% in Various News Sources",str(65.9)+r"% in Tweets", "NEUTRAL",str(80)+r"% in BBC News",str(75)+r"% in FOX News",str(100)+r"% in Various News Sources", str(22.3)+r"% in Tweets","NEGATIVE",str(5)+r"% in BBC News",str(20)+r"% in FOX News", str(0)+r"% in Various News Sources",str(11.8)+r"% in Tweets"]
	    return tb
	elif (n.lower()=='florida'):
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(10)+r"% in BBC News", str(35)+r"% in FOX News",str(10)+r"% in Various News Sources",str(40.6)+r"% in Tweets", "NEUTRAL",str(85)+r"% in BBC News",str(55)+r"% in FOX News",str(80)+r"% in Various News Sources", str(37.7)+r"% in Tweets","NEGATIVE",str(5)+r"% in BBC News",str(10)+r"% in FOX News", str(10)+r"% in Various News Sources",str(21.7)+r"% in Tweets"]
	    return tb
	elif (n.lower()=='trump'):
	    tb=['',"Sentiment Analysis for "+n,'',"POSITIVE", str(0)+r"% in BBC News", str(30)+r"% in FOX News",str(10)+r"% in Various News Sources",str(36.7)+r"% in Tweets", "NEUTRAL",str(95)+r"% in BBC News",str(65)+r"% in FOX News",str(85)+r"% in Various News Sources", str(46)+r"% in Tweets","NEGATIVE",str(5)+r"% in BBC News",str(5)+r"% in FOX News", str(5)+r"% in Various News Sources",str(17.3)+r"% in Tweets"]
	    return tb
	else:
	    return(["Sorry not a named entity"])

def index(request):
	return render(request,'personal/home.html')

def search(request):
    if 'q' in request.GET:
    	message = ans(request.GET['q'])
    else:
        message = ['You submitted an empty form.']
    return render(request,'personal/basic.html',{'content':message})