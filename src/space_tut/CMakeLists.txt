cmake_minimum_required(VERSION 2.8.3)
project(space_tut)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg message_generation)

add_message_files(
  FILES
  Num.msg
)

#catkin_install_python(PROGRAMS script/faxer.py
  #DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

## Declare a catkin package
catkin_package()

## Build printer
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(printer src/printer.cpp)
target_link_libraries(printer ${catkin_LIBRARIES})
add_dependencies(printer tutorial_space_generate_messages_cpp)
