# LULC-Dynamic-World-Constructing-Polygons
Generating polygons of green pixels for community mapping at Village Level

## Steps to follow:
1. Use the file ```create_tiles.py``` to create **4 hectare boxes** that cover the selected village. Update the variable ```coordi``` with the boundary coordinates of the desired village. Can adjust the variable ```cover_frac``` as per requirements. After running this script we get the polygon cooridinates of all the tiles. The selected tiles placed on village boundary looks like the following:  
<p align="center">
<img width="586" alt="Screenshot 2023-01-06 at 11 22 38 PM" src="https://user-images.githubusercontent.com/57101022/211069958-fe05857c-8827-45f5-85ef-f22e49aac87b.png">
</p>    
2. Update the ```startDate```, ```endDate``` & ```geometry```(based on polygon coordinates of tiles obtained in previous steps) in the ```Dynamic_world_cover.js``` file. Execute the sciprt on GEE to obatian a csv that contains fraction of green pixels in each tile. The **Grass**, **Flooded Vegetation** & **Crops** classes of dynamic were considered as green pixels.  

3. Use to script ```select_tile.py``` to obtain the required tiles. Threshold for the acceptable greenary pixels can be adjusted. 
