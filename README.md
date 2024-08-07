# MatplotSlime
Slime Mold simulation Hosted within a matplot to show the animated movement of the slime mold in an attempt to mimic the physical counterpart ("Physarum")

## Prototypes For This Project

### Stages of the Process
Stages of the process involved in this project were mapped out within the folder contained within this branch, versions along the way of the mold simulation were incorporated into the folder with each subsequent step of the unfinalized copies

### General Explanation of Prototypes (As of 7/29/2024)
1. The original mold simulation with simplified movement rules with an automatic result as the last plot
2. The original mold incorporating frame animation showing the start and finish movement
   
<p align="center">
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/V2_BaseCode_Animated.gif" width=40% height=40% />
</p>

3. Food added to the grid to later have features added besides visible indicators
4. Movement further incorporated into the slime particles to have preference for food with random motion outside of a range
5. Food can now be added via mouse-clicks and the slime particles now reproduce when eating the food
   
<p align="center">
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/V4_neural_worms.gif" width=33% height=33% />
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/V5_Reproducing_Particles.gif" width=33% height=33% />
</p>

6. Clustering behavior is now added so that the slime particles do not stray away and instead prefer colonies. Clustering levels portrayed from high (2 units) ,medium (10 units) and low (20 units)(left to right respectively)
<p align="center">
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/High_Cluster_2Units.gif" width=33% height=33% />
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/V7_Physarum_eating.gif" width=33% height=33% />
<img src="https://github.com/JustinVeerasami/MatplotSlime/blob/Prototypes/Prototype_Gifs/Low_Clustering_20Units.gif" width=33% height=33% />
</p>

9. Animation can now be played "endlessly" based off a computers own specs, further comments are now added to help with clarity of functions
