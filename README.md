# Computational Robotics Warmup

This is a demonstration of basic robotic capabilities in ROS2 using a Neato robot. The six following projects each represent important aspects of robotics software development.

- Teleoperation
- 1m x 1m square navigation
- Wall following
- Obstacle avoidance
- Person (or object) following
- Finite State control

## Teleoperation

The purpose of this portion of the warm up is to build a ros publisher and subscriber that allow the user to control the direction of the robot using their keyboard. The user can control the Neato using WASD, where W is forwards, S is backwards, A is rotated left, and D is rotate Right. The command is then communicated to the Neato via WiFi.  
[![Teleoperation](https://img.youtube.com/vi/WBagvIFqbAY/hqdefault.jpg)](https://youtu.be/WBagvIFqbAY "Teleoperation")  
https://youtu.be/WBagvIFqbAY

## Square Navigation

This portion of the warmup demonstrated our ability to program a predetermined set of commands that the robot would execute autonomously. The main control scheme here is altering the robot's linear velocity in the x direction (which is always directly forwards or backwards) and the angular velocity in the z direction (the rotation of the robot).

With these controls we are able to create a basic control loop that uses set speeds and set durations to execute driving forward 1 meter, and turning 90 degrees clockwise 4 times to complete a full square.  
[![Square](https://img.youtube.com/vi/3zHx5tMEdHs/hqdefault.jpg)](https://youtu.be/3zHx5tMEdHs "Square")  
https://youtu.be/3zHx5tMEdHs

## Wall Following

![Wall Following](./Imgs/Neate%20Wall%20Follower.jpg)
The wall following code commands the robot to drive forward until it is within range of a wall, turn to the left and enter wall following mode.

Wall following mode consists of collecting LiDAR data and measuring the distance from the robot to the wall at 45 degrees in-front and behind the robot. Based on this difference, the robot executes a proportional change in the angular velocity of the robot and continues forward.  
[![Wall Following](https://img.youtube.com/vi/vsICfEMpKOg/hqdefault.jpg)](https://youtu.be/vsICfEMpKOg "Wall Following")  
https://youtu.be/vsICfEMpKOg

## Obstacle Avoidance

The Obstacle Avoidance code intrepts LiDAR scan data from the Neato and then navigates around approaching objects. LiDAR scan data is first taken for the front 60 degrees of the Neato, then from this scan data the minimum distance is found. If the minimum distance is below 2.5 meters the Neato randomly selects one of four possible turns, -120, -90, 90 or 120 to compete based using a constant angular velocity and variable time. After the Neato completes the turn it resumes driving straight. Originally we had more complex programs using obstacle identification, but we found that the LiDAR data from the Neato is not always accurate and commonly returns 0.0 floats indicating it could not make a reading even with objects in front of it. Therefore everywhere a 0.0 float was returned we changed it to 10 meters to avoid having issues finding the minimum value in our LiDAR scans.  
[![Obstacle Avoidance](https://img.youtube.com/vi/ZM5VmYwmeHI/hqdefault.jpg)](https://youtu.be/ZM5VmYwmeHI "Obstacle Avoidance")  
https://youtu.be/ZM5VmYwmeHI

## Person (or object) following

The Person Following code uses LiDAR scan data from the front 90 degrees of the Neato to follow a moving person and keep a set distance from said person. First all 0.0 Meter float values in the LiDAR data were replaced with 10 meters similar to the Obstacle Avoidance Code. Then we find the angle of the closest LiDAR point to get an intended direction to the person. The Neato then turns until it reaches the angle of the person using a constant angular velocity and varying the amount of time. Then Neato then goes forwards a set distance then checks whether it is within 0.2 meters of the person which was the following distance we selected. The Neato repeats these actions until it is within 0.2 meters of the person, then it stops.  
[![Person (or object) following](https://img.youtube.com/vi/oMyMJkR8LuE/hqdefault.jpg)](https://youtu.be/oMyMJkR8LuE "Person (or object) following")  
https://youtube.com/shorts/oMyMJkR8LuE?feature=share

## Finite State Control

![Finite State Control](./Imgs/Finite%20State%20Controller%20Comprobo.jpg)
The finite state controller has two states, teleop and Square drive. In the teleop state the Neato can be remotely controlled through the keyboard using WASD, the user can change to Square Drive state by pressing "0". The square drive states that the Neato drives in a square using dead reckoning, after the Neato has finished driving the square the Neato changes back to the teleop state.  
[![Finite State control](https://img.youtube.com/vi/47JogZiDUis/hqdefault.jpg)](https://youtu.be/47JogZiDUis "Finite State control")  
https://youtube.com/shorts/47JogZiDUis?feature=share

## Challenges

We faced a great deal of challenges when it came to complexity and LiDAR accuracy. On the complexity front, our original plan for the obstacle avoidance was to implement a system that found the "most free" pathway and head in that direction. Ultimately this did not work because the first "most free" path to be found was always too close to an obstacle and despite trying to create a buffer system or shift how the path was chosen we would ultimately run into something. We eventually decided to have the robot drive forward until it saw something within 45 degrees of the front on either side and rotate at least 90 degrees away from it.

As for the LiDAR troubles, we found that until the scan data populated completely with values we would receive lots of 0 values. We solved this by replacing them with the maximum range of the LiDAR at 10 meters. We also had issues with "ghost objects" where the LiDAR would read distances much higher or lower than were accurate. This issue was best solved with the averaging of several LiDAR points.

## Improvements

If we had more time, we would have liked to implement RANSAC into most of our programs that involved obstacle detection. We would do this primarily so the system could make more accurate assumptions of the environment and therefore navigate more precisely. This would let us hopefully be able to run our programs in an area with higher densities of objects with fewer crashes.

We would have also liked to implement actual odometry in our navigation rather than basing all of our turning capabilities on timing. We spent time figuring out how long it took the neato to turn a certain amount at a specific angular velocity and used this calibration in all of our work. Odometry would have been more precise and computationally sound.

## Key Takeaways

- Relying on a single sensor is not sound robotics engineering. In a system that is meant to navigate on its own, a single point of failure for the sensing system exposes the system to a great deal of risk. It is best to use multiple sensors and do as much sensor fusion and processing as is computationally feasible.

- Building your systems on top of programs already built has both benefits and disadvantages. It is always best to avoid reinventing the wheel when it comes to programming, especially if you have written a particular function in a different part of the same project. One thing to keep in mind is that as code becomes more complicated it can often feel like a patchwork system that lacks coherence, things can make troubleshooting difficult and results in needing to start at ground zero anyway.
