import ezdxf

doc = ezdxf.readfile("./resources/ptycz.dxf");

msp = doc.modelspace()

polyline_points = [];

#definiujemy funkcje wydruku i dodanie elementow do polyline_points

def print_entity(e):
    print("POLILINE on layer: %s\n" % e.dxf.layer)
    # print("start point: %s\n" % e.dxf.x)
    # print("end point: %s\n" % e.dxf.y)
    for line in e:
        print("x of line: %s\n" % line[0])
        print("y of line: %s\n" % line[1])
        polyline_points.append([(line[0], line[1])])

#oska musi byc na warstwie "os" i byc poliline
for e in msp:
    if e.dxftype() == 'LWPOLYLINE' and e.dxf.layer == "os":
        print_entity(e)

#wydruka arraya ze wszystkimi punktami lini
print(polyline_points)
# for e in msp.query('LWPOLYLINE'):
#     print_entity(e)

