cmake_minimum_required(VERSION 4.0)
project(frontend)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt5 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(frontend main.cpp
        api/Emergency.cpp
        api/Emergency.h
        api/Block.cpp
        api/Block.h
        api/Event.cpp
        api/Event.h
        api/ApiObject.cpp
        api/ApiObject.h)
target_link_libraries(frontend
        Qt5::Core
        Qt5::Gui
        Qt5::Widgets
)

