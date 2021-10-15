---
title: Convert/Run Qt5 app into/as a ROS2 package
layout: post
sidebar_link: true
tags:
- ROS2
- Qt
- CMake
- Software
---

So you want to run your Qt5 app as a ros2 node?, Here we go


### Step - 1: Build the Qt5 App


The first thing you need to do is to convert your Qt5 app to a ros2 package so that you can build it using: `ament build`.

Let's make an example Qt5 app to showcase this!

After installing Qt creator we get two types of Qt Quick apps we can make. They differ on the build system they use:

- qmake apps
- cmake apps

Let's have a look at how to make each one of them:

- This is the qmake build system app -
![Qt5 qmake app](/images/qt5_qmake_app.gif)

- This is the cmake build system app -
![Qt5 cmake app](/images/qt5_cmake_app.gif)

### Step - 2: Depending on the build format, create/extend CMakeLists.txt






- Here we have two different steps for the Qt5 app depending on the build system you chose, you'll get these directory structures:
```bash
- CMake:
.
├── CMakeLists.txt
├── CMakeLists.txt.user
├── main.cpp
├── main.qml
├── Page1Form.ui.qml
├── Page2Form.ui.qml
├── qml.qrc
└── qtquickcontrols2.conf
0 directories, 8 files
```

```bash
- qmake:
.
├── demo.pro
├── demo.pro.user
├── main.cpp
├── main.qml
├── Page1Form.ui.qml
├── Page2Form.ui.qml
├── qml.qrc
└── qtquickcontrols2.conf
0 directories, 8 files

```
- Smply open the CMakeLists.txt to edit and in the case of a qmake build create `CMakeLists.txt`, make it look like this:

```cmake
cmake_minimum_required(VERSION 3.5)
project(demo)

set (CMAKE_CXX_STANDARD 14)
if(NOT WIN32)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Wall -Wextra -fPIC")
endif()

IF (NOT DEFINED BUILD_VERSION)
	SET(BUILD_VERSION "not set")
ENDIF()
ADD_DEFINITIONS(-DBUILD_VERSION="${BUILD_VERSION}")

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rmw_implementation REQUIRED)
find_package(std_msgs REQUIRED)
find_package(Qt5Core REQUIRED)
find_package(Qt5Quick REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)


include_directories(
	${rclcpp_INCLUDE_DIRS}
	${std_msgs_INCLUDE_DIRS}
	${Qt5Core_INCLUDE_DIRS}
	${Qt5Quick_INCLUDE_DIRS}
	)

file(GLOB SOURCE_FILES
	"src/*.cpp"
	)

add_executable(${PROJECT_NAME} ${SOURCE_FILES} "src/qml.qrc")

ament_target_dependencies(${PROJECT_NAME}
	rclcpp
	std_msgs
	rmw_implementation
	)
target_link_libraries(${PROJECT_NAME}
	Qt5::Core
	Qt5::Quick
	)

install(TARGETS ${PROJECT_NAME} DESTINATION bin)

ament_package()
```

### Step - 3: Create a `package.xml` and add it to project
- ROS2 needs a package.xml to find build and execution dependencies and to state metadata.


- A simple package.xml looks like this:
```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format2.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="2">
	<name>demo</name>
	<version>0.0.1</version>
	<description>A demo app for the blog</description>
	<maintainer email="nope@notgoogle.com">Amar Lakshya</maintainer>
	<license>Apache License 2.0</license>

	<buildtool_depend>ament_cmake</buildtool_depend>

	<build_depend>rclcpp</build_depend>
	<build_depend>std_msgs</build_depend>

	<build_depend>qtbase5-dev</build_depend>
	<build_depend>qt5-qmake</build_depend>

	<exec_depend>libqt5-core</exec_depend>
	<exec_depend>rclcpp</exec_depend>
	<exec_depend>std_msgs</exec_depend>

	<export>
		<build_type>ament_cmake</build_type>
	</export>
</package>
```

### Step - 4: Let's restructure the directory to clean everything.

- First, create an `src` directory and move everything in it as a ROS2 package ( let's say `demo`) . Now, create an `src` directory and move all the `qml`, `cpp`, `qml.qrc` and `conf` files in that directory. Now your project folder should look something like this:
```bash
.
└── src
    └── demo
        ├── CMakeLists.txt
        ├── demo.pro
        ├── demo.pro.user
        ├── package.xml
        └── src
            ├── main.cpp
            ├── main.qml
            ├── Page1Form.ui.qml
            ├── Page2Form.ui.qml
            ├── qml.qrc
            └── qtquickcontrols2.conf

3 directories, 10 files
```

### Step - 5: All set, time to build the package!

- Now, source your ROS2 workspace and run: `ament build`.

Doing these steps, you should get a ROS2 Qt5 app package called `demo`.

### Step - 6: running the package in qtcreator!

- Note that you will be easily able to run the package using ros2 commandline options, however, It would make our lives
   incredibly easy to run and build our Qt5 app in the Qt Creator.
	 
	 For that, first install the RTPS middleware system-wide by following directions on their project page: 
	 [RTPS Build instructions](https://github.com/eProsima/Fast-RTPS#installation-from-source)
	 
	 and that's it! Now source your ROS2 workspace and go to your Qt5 app folder and just run `qtcreator`!
	 
	 You will now be able to develop Qt5 apps with ROS2 in the Qt Creator

**TIP**: Here is the git-hosted [sample project](https://github.com/amar-laksh/ros2qt_demo).






