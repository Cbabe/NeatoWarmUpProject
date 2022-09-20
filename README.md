For each behavior, describe the problem at a high-level. Include any relevant diagrams that help explain your approach. Discuss your strategy at a high-level and include any tricky decisions that had to be made to realize a successful implementation.

How was your code structured? Make sure to include a sufficient detail about the object-oriented structure you used for your project.

# Computational Robotics Warmup

This is a demonstration of basic robotic capabilities in ROS2 using a Neato robot. The six following projects each represent important aspects of robotics software development.

- Teleoperation
- 1m x 1m square navigation
- Wall following
- Obstacle avoidance
- Person (or object) following
- Finite State control

## Teleoperation

The purpose of this portion of the warm up is to build a ros publisher and subscriber that allow the user to control the direction of the robot using their keyboard. The user can control the Neato using WASD, where W is forwards, S is backwords, A is rotate left, and D is rotate Right. The command is then communicated to the Neato via WiFi.

[![Teleoperation](https://img.youtube.com/vi/WBagvIFqbAY/hqdefault.jpg)](https://youtu.be/WBagvIFqbAY "Teleoperation")
https://youtu.be/WBagvIFqbAY

## Square Navigation

This portion of the warmup demonstrated our ability to program a predetermined set of commands that the robot would execute autonomously. The main control scheme here is altering the robots linear velocity in the x direction (which is always directly forwards or backwards) and the angular velocity in the z direction (the rotation of the robot).

With these controls we are able to create a basic control loop that uses set speeds and set durations to execute driving forward 1 meter, and turning 90 degrees clockwise 4 times to complete a full square.

[![Square](https://img.youtube.com/vi/3zHx5tMEdHs/hqdefault.jpg)](https://youtu.be/3zHx5tMEdHs "Square")
https://youtu.be/3zHx5tMEdHs

## Wall Following

![Wall Following](./Imgs/Neate%20Wall%20Follower.jpg)
The wall following code commands the robot to drive forward until it is within range of a wall, turn to the left and enter wall following mode.

Wall following mode consists of collecting LiDAR data and measuring the distance from the robot to the wall at 45 degrees in-front and behind the robot. based on this difference, the robot executes a proportional change in the angular velocity of the the robot and continues forward.
[![Wall Following](https://img.youtube.com/vi/vsICfEMpKOg/hqdefault.jpg)](https://youtu.be/vsICfEMpKOg "Wall Following")
https://youtu.be/vsICfEMpKOg

## Obstacle Avoidance

The Obstacle Avoidance code intrepts LiDAR scan data from the Neato and then navigates around approaching objects. LiDAR scan data is first taken for the front 60 degrees of the Neato, then of this scan data the minimum distance is found. If the minium distance is below 2.5 meters the Neato randomly selects one of four possible turns, -120, -90, 90 or 120 to compete based using a constant angular velocity and varible time. After the Neato completes the turn it resumes driving straight. Orginally we had more complex programs using obsical identifcation, but we found that the LiDAR data from the Neato is not always accurate and commonly returns 0.0 floats indicates it could not make a reading even with objects in front of it. Therefor everywhere a 0.0 float was returned we changed it to 10 meters to avoid having issues finding the minimum value in our LiDAR scans.
[![Obstacle Avoidance](https://img.youtube.com/vi/ZM5VmYwmeHI/hqdefault.jpg)](https://youtu.be/ZM5VmYwmeHI "Obstacle Avoidance")
https://youtu.be/ZM5VmYwmeHI

## Person (or object) following

The Person Following code uses LiDAR scan data from the front 90 degrees of the Neato to follow a moving person and keep a set distance from said person. First all 0.0 Meter float values in the LiDAR data were replaced with 10 meters similar to the Obstacle Avoidance Code. Then we find the angle of the closest LiDAR point to get an intended direction to the person. The Neato then turns until it reaches the angle of the person using a constant angular velocity and varying the amount of time. Then Neato then goes forwards a set distance then checks whether it is within 0.2 meters of the person which was the follow distance we selected. The Neato repeats these actions until it is within 0.2 meters of the person, then it stops.
[![Person (or object) following](https://img.youtube.com/vi/oMyMJkR8LuE/hqdefault.jpg)](https://youtu.be/oMyMJkR8LuE "Person (or object) following")
https://youtube.com/shorts/oMyMJkR8LuE?feature=share

## Finite State Control

![Finite State Control](./Imgs/Finite%20State%20Controller%20Comprobo.jpg)
The finite state controller has two states, teleop and Square drive. In the teleop state the Neato can be remotely controlled throught the keyboard using WASD, the user can change to Square Drive state by pressing "0". The square drive state the Neato drives in a square using dead reckoning, after the Neato has finished driving the square the Neato changes back to the teleop state.
[![Finite State control](https://img.youtube.com/vi/47JogZiDUis/hqdefault.jpg)](https://youtu.be/47JogZiDUis "Finite State control")
https://youtube.com/shorts/47JogZiDUis?feature=share

## Challenges

What if any challenges did you face along the way?

## Improvements

What would you do to improve your project if you had more time?

## Key Takeaways

What are the key takeaways from this assignment for future robotic programming projects? For each takeaway, provide a sentence or two of elaboration.
