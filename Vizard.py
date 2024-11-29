#insert modules
import viz 
import vizshape
import vizfx
import vizact

#create empty world
viz.go() 

#import the 3D model
room = viz.addChild("tavern.osgb") 

#starting position
viz.MainView.move([0,2,-15])
viz.MainWindow.fov(100)
vizshape.addAxes()

#grass
ground = viz.addChild("ground_grass.osgb")

#sky
env = viz.addEnvironmentMap("sky.jpg")
sky = viz.add("skydome.dlc")
sky.texture(env)

#stop collisions and puts gravity
viz.MainView.collision(viz.ON)
viz.MainView.gravity(10)

#scene headlight
headlight = viz.MainView.getHeadLight() 

#CANDLE
flame = room.getChild("CANDLE_HOLDER058", flags=viz.CHILD_REPLACE_TRANSFORM)
flame_position = flame.getPosition()
print(flame_position)

candle_light = vizfx.addPointLight(color=viz.RED, pos=flame_position)
candle_light_position = candle_light.getPosition()
print(candle_light_position)

candle_light.quadraticAttenuation(1)
candle_light.intensity(50)

flame.specular(viz.YELLOW)
flame.shininess(10)


#Open / close the door
door1=room.getTransform("PivotDoor001")


#spinAction= vizact.spin(0,1,0,40)
#door1.addAction(spinAction)

#vizact.onkeydown("c",spinDoor,door1,-40)


# Add and walk avatar
#vicky=viz.add("vcc_female.cfg",euler=(180,0,0))
#vicky.setPosition([-1,0,15],viz.ABS_GLOBAL)
#vicky.execute(5)
#vicky.state(14)
#
#def walkAvatar():
#walk1=vizact.walkTo([1.4,0,0])
#vicky.addAction(walk1)
#
#vizact.onkeydown("w",walkAvatar)
#
#def picker():
#object=viz.pick(info=True)
#if(object.valid):
#print(object.name)


#TEXT INFO
text3d= viz.addText3D("My House 3d" , pos=[0,5,-10], align= viz.ALIGN_CENTER_BOTTOM)
text2d= viz.addText("My House 2d" , pos=[0,6,-10], align= viz.ALIGN_CENTER_BOTTOM)
textScreen= viz.addText("My House on Screen" , parent=viz.ORTHO, pos=[20,20,0])

text3d.addAction(vizact.spin (0,1,0,15))
text2d.addAction(vizact.spin (0,1,0,-15))

#slider
cfg=vizconfig.BasicConfigurable("My House 3d")
cgf.addFloatRangeItem("Thickness", [0.01, 0.5], fset=text3d.setThickness, fget=text3d.getThickness)
vizconfig.register(cfg)
vizconfig.getConfigWindow().setWindowVisible(True)

#addVideo
myvideo=viz.addVideo("kati.mpg")
myscreen=room.getChild("onoma screen")
myscreen.texture(myvideo)

myvideo.play()
myvideo.loop()
myvideo.setRate(0.51)

#addSound
mysound=viz.addSound("kati.mid")
vizact.onkeydown("p", mysound.play)
vizact.onkeydown("s", mysound.stop)

#see other file for flashlight