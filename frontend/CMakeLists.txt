cmake_minimum_required(VERSION 3.0)
project(frontend)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "D:/Qt/6.11.0/mingw_64/lib/cmake")

find_package(Qt6 COMPONENTS
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
        api/ApiObject.h)
target_link_libraries(frontend
        Qt6::Core
        Qt6::Gui
        Qt6::Widgets
)

