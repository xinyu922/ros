#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class MoveItIkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)
        
        # 初始化ROS节点
        rospy.init_node('moveit_ik_demo')
                
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
                
        # 获取终端link的名称
        end_effector_link = arm.get_end_effector_link()
                        
        # 设置目标位置所使用的参考坐标系
        reference_frame = 'base_link'
        arm.set_pose_reference_frame(reference_frame)
                
        # 当运动规划失败后，允许重新规划
        arm.allow_replanning(True)
        
        # 设置位置(单位：米)和姿态（单位：弧度）的允许误差
        arm.set_goal_position_tolerance(0.05)
        arm.set_goal_orientation_tolerance(0.1)
        
        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
	#arm.set_named_target('forward')
        arm.go()
        rospy.sleep(1)
               
        # 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
        # 姿态使用四元数描述，基于base_link坐标系
        target_pose = PoseStamped()
        target_pose.header.frame_id = reference_frame
        target_pose.header.stamp = rospy.Time.now()     
	
	##可以成功，几率小        
	#target_pose.pose.position.x = 0.266597
        #target_pose.pose.position.y = -0.107097
        #target_pose.pose.position.z = 0.337546
        #target_pose.pose.orientation.x = -0.736811
        #target_pose.pose.orientation.y = 0.323324
        #target_pose.pose.orientation.z = -0.308519
        #target_pose.pose.orientation.w = 0.507333
        
        #target_pose.pose.position.x = 0.281336
        #target_pose.pose.position.y = 0.0039
        #target_pose.pose.position.z = 0.316819
        #target_pose.pose.orientation.x = 0.935367
        #target_pose.pose.orientation.y = 0.129954
        #target_pose.pose.orientation.z = 0.0110977
        #target_pose.pose.orientation.w = 0.328752

        #target_pose.pose.position.x = -0.19359
        #target_pose.pose.position.y = 0.222843
        #target_pose.pose.position.z = 0.298393
        #target_pose.pose.orientation.x = 0.0616661
        #target_pose.pose.orientation.y = 0.861045
        #target_pose.pose.orientation.z = 0.502023
        #target_pose.pose.orientation.w = 0.0526431

        target_pose.pose.position.x = 0.184348
        target_pose.pose.position.y = 0.226549
        target_pose.pose.position.z = 0.290655
        target_pose.pose.orientation.x = 0.925905
        target_pose.pose.orientation.y = -0.0941516
        target_pose.pose.orientation.z = -0.0370091
        target_pose.pose.orientation.w = -0.363958
        # 设置机器臂当前的状态作为运动初始状态
        arm.set_start_state_to_current_state()
        
        # 设置机械臂终端运动的目标位姿
        arm.set_pose_target(target_pose, end_effector_link)
        
        # 规划运动路径
        traj = arm.plan()
        
        # 按照规划的运动路径控制机械臂运动
        arm.execute(traj)
        rospy.sleep(1)
         
        # 控制机械臂终端向右移动5cm
        #arm.shift_pose_target(2, -0.05, end_effector_link)
        #arm.go()
        #rospy.sleep(1)
  
        # 控制机械臂终端反向旋转90度
        #arm.shift_pose_target(3, -1.57, end_effector_link)
        #arm.go()
        #rospy.sleep(1)
           
        # 控制机械臂回到初始化位置
        #arm.set_named_target('home')
        #arm.go()

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    MoveItIkDemo()

    
    
