#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String::ConstPtr& msg) //function called when message arrive, store message
   {
     ROS_INFO("Message received: %s", msg->data.c_str());
   }

int main(int argc, char **argv) //char **argv = pointer to a char pointer
{ //argument count (argc) is number of strings pointer to by argument vector (argv)
    ros::init(argc, argv, "printer"); //initialize node and name it
    ros::NodeHandle n; //variable access to the node
    ros::Subscriber sub = n.subscribe("pigeon",10, chatterCallback);
    
    ros::spin(); //loops and calls message callbacks as fast as possible

    return 0;
}

