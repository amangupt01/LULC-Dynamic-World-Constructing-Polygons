from shapely import geometry, ops

cordi = [ [ 85.89091999981855, 22.420810000259269 ], [ 85.891650000208045, 22.4211899997965 ], [ 85.893259999810425, 22.422539999998548 ], [ 85.893649999809014, 22.422099999492897 ], [ 85.894449999829178, 22.421889999701111 ], [ 85.895840000077868, 22.421780000024135 ], [ 85.897030000096649, 22.421359999541263 ], [ 85.898010000323708, 22.420819999819912 ], [ 85.899730000501904, 22.419649999824102 ], [ 85.901280000035115, 22.418640000012211 ], [ 85.903459999842781, 22.417730000315128 ], [ 85.90581000029556, 22.417149999648217 ], [ 85.908159999849076, 22.417039999971088 ], [ 85.908790000123517, 22.416879999787088 ], [ 85.90981999995833, 22.415660000183628 ], [ 85.910450000232728, 22.415069999955193 ], [ 85.911540000136597, 22.415019999447864 ], [ 85.911800000435477, 22.415019999447832 ], [ 85.912349999718643, 22.415019999447729 ], [ 85.91269000010945, 22.414699999979277 ], [ 85.913149999738664, 22.413360000237979 ], [ 85.91353999973721, 22.412779999571462 ], [ 85.913490000129428, 22.412779999571466 ], [ 85.912640000501256, 22.411709999691009 ], [ 85.911090000068555, 22.410690000317761 ], [ 85.909940000095531, 22.409460000253524 ], [ 85.909600000603973, 22.408609999726458 ], [ 85.908569999869485, 22.406789999433869 ], [ 85.907299999758507, 22.405159999809257 ], [ 85.907260000611871, 22.405179999832235 ], [ 85.906430000107477, 22.405179999832388 ], [ 85.905429999857304, 22.404449999443361 ], [ 85.905360000226537, 22.404310000181844 ], [ 85.904669999883197, 22.405340000016562 ], [ 85.903869999863048, 22.40624999971342 ], [ 85.902440000467834, 22.407419999709173 ], [ 85.902440000467848, 22.407550000308262 ], [ 85.902440000467905, 22.40790000026076 ], [ 85.902490000076099, 22.411589999554792 ], [ 85.902200000192707, 22.413619999639309 ], [ 85.901740000563436, 22.415059999495519 ], [ 85.901110000289037, 22.415910000022702 ], [ 85.89984999974024, 22.416819999719635 ], [ 85.898990000550413, 22.417300000271371 ], [ 85.897840000577574, 22.417459999556119 ], [ 85.89618000046822, 22.417940000107997 ], [ 85.894810000242586, 22.418359999691528 ], [ 85.894380000197984, 22.418640000013369 ], [ 85.892800000180671, 22.419699999433085 ], [ 85.89091999981855, 22.420810000259269 ] ]
print(len(cordi), len(cordi[0]))
x_ = []
y_ = []
for i in cordi:
    x_.append(i[0])
    y_.append(i[1])
print("X Coordinate Ananlysis")
print("Max: ", max(x_))
print("Min: ", min(x_))
print("Span: ", max(x_) - min(x_))
min_x = min(x_)
max_x = max(x_)

print("Y Coordinate Ananlysis")
print("Max: ", max(y_))
print("Min: ", min(y_))
print("Span: ", max(y_) - min(y_))
min_y = min(y_)
max_y = max(y_)

grid_size = 0.002
cover_frac = 0.3
grid = []

curr_x = min_x
curr_y = min_y
while curr_x <= max_x:
    while curr_y <= max_y:
        grid.append([[curr_x, curr_y], [curr_x + grid_size, curr_y] , [curr_x + grid_size, curr_y + grid_size], [curr_x, curr_y + grid_size], [curr_x, curr_y]])
        curr_y += grid_size
    curr_y = min_y
    curr_x += grid_size

# print(grid[0])


poly = geometry.Polygon(cordi)

# import matplotlib.pyplot as plt

# x,y = poly.exterior.xy
# plt.plot(x,y)
#save the plot



# dump cordi and box in grid as geojson
# import json
import geojson
from geojson import Feature, FeatureCollection, Polygon

features = []
# features.append(Feature(geometry=Polygon([cordi]), properties={"name": "poly1", "fill": "#FF0000"}))
# for box in grid:
#     features.append(Feature(geometry=Polygon([box])))
#     # print(box)
#     # print("
#     # ")
#     # print(geometry.Polygon(box))
#     # print("
#     # ")

# feature_collection = FeatureCollection(features)
# with open('grid2.geojson', 'w') as f:
#     geojson.dump(feature_collection, f)







final_grid = []
poly2 = geometry.Polygon(cordi)
#print("Area: ",poly2.area, poly2.is_valid)
count = 0
for box in grid:
    # Area intersection of two polygons
    poly1 = geometry.Polygon(box)
    #print("Area: ",poly1.area, poly1.is_valid)
    # point1 = geometry.Point(box[0][0], box[0][1])
    # point2 = geometry.Point(box[2][0], box[2][1])
    intersection = poly2.intersection(poly1)
    
    # print(intersection.area, cover_frac*grid_size*grid_size)
    if poly1.within(poly2) or intersection.area >= cover_frac*grid_size*grid_size:
        features.append(Feature(geometry=Polygon([box])))
        final_grid.append(box)
        count += 1
        # x,y = poly1.exterior.xy
        # plt.plot(x,y)

# write list to a file
with open('grid_bara_bardadih.txt', 'w') as f:
    for item in final_grid:
        f.write("%s" % item)

# dump list to a pickle file
import pickle
with open('grid_bara_bardadih.pkl', 'wb') as f:
    pickle.dump(final_grid, f)


feature_collection = FeatureCollection(features)
with open('grid_bara_bardadih.geojson', 'w') as f:
    geojson.dump(feature_collection, f)
    
#save the plot
# plt.savefig("polygon.png")

print(len(grid), count)
# print(final_grid)
