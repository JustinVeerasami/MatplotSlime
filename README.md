# MatplotSlime
Slime Mold simulation hosted within a matplot to show the animated movement of the slime mold in an attempt to mimic the physical counterpart ("Physarum"). 

<p align="center">
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/MatplotSlime_PixelArt.png" width=33% height=33%>
</p>

The completed code for this project is able to successfully run on Visual Studio Code (ver: 1.92) using the python add-on.


## Results
The final simulation results (varied decay amounts are shown for the sake of configuration of the mold sizing / clustering)
<p align="center">
<img src=https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/Final_Results.gif width=100% height=100%>
</p>

## Installation
Steps to run the simulation:

1. Clone the github repository:
    ```bash
    git clone -b main https://github.com/JustinVeerasami/MatplotSlime.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MatplotSlime
    ```

3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
## Run The Simulation (defaults to indefinite animation)
```bash
python main.py
```

## Possible Future Steps
Applying a mean curvature blur as a post-processing step to the program would produce simulation results with an improved realism while maintaining the initial particle simulation. Sample below using a filter applied via GIMP to the GIF layers produced by the simulation (v7 and final models pictured respectively)
<p align="center">
<img src=https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/v7_meancurvature_blur.gif width=45% height=45%>
<img src=https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/Final_MeanCurvatureBlur.gif width=45% height=45%>
</p>

## References
Special thanks to Rishit Katiyar for his baseline of the graph system. It is thanks to this initial repository that I was able to find a starting point to start building my simulation.
- https://github.com/Rishit-katiyar/physarum-bio-simulation/tree/main
