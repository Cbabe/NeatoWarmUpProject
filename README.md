
    For each behavior, describe the problem at a high-level. Include any relevant diagrams that help explain your approach.  Discuss your strategy at a high-level and include any tricky decisions that had to be made to realize a successful implementation.
   
    How was your code structured? Make sure to include a sufficient detail about the object-oriented structure you used for your project.
    

   


# Computational Robotics Warmup 

This is a demonstration of basic robotic capabilities in ROS2 using a Neato robot. The six following projects each represent important aspects of robotics software development.

* Teleoperation
* 1m x 1m square navigation
* Wall following
* Obstacle avoidance
* Person (or object) following
* Finite State control

##  Teleoperation

The purpose of this portion of the warm up is to build a ros publisher and subscriber that allow the user to control the direction of the robot using their keyboard. The control scheme is communicated to the robot via network connectivity

**  more to add **

## Square Navigation

This portion of the warmup demonstrated our ability to program a predetermined set of commands that the robot would execute autonomously. The main control scheme here is altering the robots linear velocity in the x direction (which is always directly forwards or backwards) and the angular velocity in the z direction (the rotation of the robot). 

With these controls we are able to create a basic control loop that uses set speeds and set durations to execute driving forward 1 meter, and turning 90 degrees clockwise 4 times to complete a full square.

** Add pictures and such **

## Wall Following

The wall following code commands the robot to drive forward until it is within range of a wall, turn to the left and enter wall following mode.

Wall following mode consists of collecting LiDAR data and measuring the distance from the robot to the wall at 45 degrees in-front and behind the robot. based on this difference, the robot executes a proportional change in the angular velocity of the the robot and continues forward.

## Obstale Avoidance
## Person (or object) following
## Finite State control
For the finite state controller, what was the overall behavior. What were the states? What did the robot do in each state? How did you combine and how did you detect when to transition between behaviors?  Consider including a state transition diagram in your writeup.

## Challenges
What if any challenges did you face along the way?
## Improvements
What would you do to improve your project if you had more time?
## Key Takeaways
What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.

