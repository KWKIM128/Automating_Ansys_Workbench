# Automating_Ansys_Workbench

**This script will increase the force by 0.01 in Ansys Workbench, until the component fails**

**Step 1:** Apply approperiate boundary conditions to the model

**Step 2:** Apply approperiate mesh on the model

**Step 3:** Right click "model" to insert the "Named Selection" tool as shown in figure below
<p align="center">
  <img src="https://user-images.githubusercontent.com/115262940/221674291-1ff1236a-5995-416d-a8b3-ac16ad530af2.png" />
</p>


**Step 4:** Select the face of the area where force will be applied at. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/115262940/221677337-2a26fe01-bc08-4d85-b737-8bc9f7945c98.png" />
</p>


**Step 5:** Name the selected face to "Load". Make sure to change it to "Load". If you use a diffent name, the script won't run.
<p align="center">
  <img src="https://user-images.githubusercontent.com/115262940/221677795-d988f898-94e2-4074-bfc5-c131d17e86a8.png" />
</p>


**Step 6:** Go to the "Automation" tab, and select "Scripting"
<p align="center">
  <img src="https://user-images.githubusercontent.com/115262940/221678150-7e54334f-2182-4337-9c12-ee93dcd44785.png" />
</p>


**Step 7:** Copy paste the script into the editor, and change the value of "Force" to the force your group has decided.

**Step 8:** Run the program 
