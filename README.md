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
## References
Special thanks to Rishit Katiyar for his baseline of the graph system. It is thanks to this initial repository that I was able to find a starting point to start building my simulation.
- https://github.com/Rishit-katiyar/physarum-bio-simulation/tree/main
