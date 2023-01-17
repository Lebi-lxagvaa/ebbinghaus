def ebbinghausIllusion(breite=600, hoehe=400, r_mitte=20,
                 r_kleiner=10, r_grosser=30, anzahl_kleiner=10, anzahl_grosser=6,
                 distanz_kleiner=40, distanz_grosser=70,
                 Farbe_mitte='purple', farbe_umringende='black',
                 graph_distanz=200):
    
    #Dependencies 
    import math
    import ipyturtle3 as turtle
    from ipyturtle3 import hold_canvas
    myCanvas=turtle.Canvas(width=breite,height=hoehe)
    display(myCanvas)
    myTS=turtle.TurtleScreen(myCanvas)

    myTS.bgcolor("lightblue")
    myPen=turtle.Turtle(myTS)
    
    #Koordinaten von mittleren kreisen
    x1, y1 = -distanz_grosser, 0
    x2, y2 = x1 + graph_distanz, y1
    
    def zeichneKreis(x, y, radius, farbe, myPen):
        myPen.setheading(0)
        myPen.penup()
        myPen.color(farbe)
        myPen.fillcolor(farbe)
        myPen.goto(x,y-radius)
        myPen.begin_fill()
        myPen.circle(radius)
        myPen.end_fill()
        myPen.pendown()
        myPen.speed(500)
        
    def umringen(umring_radius, r, x0, y0, anzahl_kreise):
        
        for i in range(anzahl_kreise):
            grad = 2 * math.pi * i / anzahl_kreise
            x = x0 + umring_radius * math.cos(grad)
            y = y0 + umring_radius * math.sin(grad)
            zeichneKreis(x, y, r, farbe_umringende, myPen)
    
    zeichneKreis(x1,y1,r_mitte,Farbe_mitte,myPen)
    umringen(distanz_grosser, r_grosser, x1, y1,anzahl_grosser)
    zeichneKreis(x2,y2,r_mitte,Farbe_mitte,myPen)
    umringen(distanz_kleiner, r_kleiner, x2, y2, anzahl_kleiner)
    
    
    
