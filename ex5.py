name = 'Zed A. Shaw'
age = 35  #not a lie
height = 74 * 0.0254  #meters
weight = 180 * 0.453592 #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %r." % name)
print ("He's %r meters tall." % height)
print ("He's %r kilograms heavy." % weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)

#this line is tricky, try to get it exactly right
print ("If I add %d, %r, and %r I get %d." % (
	age, height, weight, age + height + weight))