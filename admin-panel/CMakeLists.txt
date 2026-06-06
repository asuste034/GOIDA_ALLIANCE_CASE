cmake_minimum_required(VERSION 3.31)
project(admin-panel)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(admin-panel main.cpp)
target_link_libraries(admin-panel
        Qt6::Core
        Qt6::Gui
        Qt6::Widgets
)

