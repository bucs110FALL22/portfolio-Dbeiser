article = "U.S. business and media publication Fast Company said it shut down its website on Tuesday evening after the site was hacked and sent “obscene and racist” notifications to Apple users via the iPhone maker’s Apple News service. News publishers using the Apple News aggregation app can connect their digital publishing tools to Apple News to send push notifications to Apple customers who subscribe to the publisher’s channel. Fast Company said hackers broke into those publishing tools. Hackers sent two “obscene and racist push notifications” about a minute apart, Fast Company said in a tweet, adding it had suspended the Apple News feed until the situation was resolved. “We are investigating the situation and have suspended the feed & shut down FastCompany.com until we are certain the situation has been resolved,” the publication added. Fast Company’s website was down and the page displayed a 404 error when viewed by Reuters on Tuesday evening. In a subsequent tweet after the shutdown, Fast Company said that its content management system - software used by news outlets to publish and manage their stories - had been hacked to send the notifications. Apple News said in a tweet that it had disabled Fast Company’s channel. Fast Company said it had earlier suffered an “apparently related” hack of its website on Sunday afternoon, when similar language appeared on its home page, causing it to shut the site down for about two hours. Fast Company is owned by publishing firm Mansueto Ventures LLC"

replace= {"Fast": "Slow","Company":"Turtle", "Apple":"Pair", "site": "seat", "Website":"webseat"}

for key, value in replace.items():  
  article = article.replace(key,value)
print(article)