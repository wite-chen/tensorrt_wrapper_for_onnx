project(test_json)
cmake_minimum_required(VERSION 3.0)
find_package(OpenCV REQUIRED)
find_package(CUDA)
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(/home/xj-zjd/TensorRT-7.0.0.11/include)
include_directories(${PROJECT_BINARY_DIR}/../ ${PROJECT_BINARY_DIR}/../jsoncpp-00.11.0/include)
include_directories(${PROJECT_BINARY_DIR}/../node_info)
include_directories(${PROJECT_BINARY_DIR}/../node_create)
include_directories(${PROJECT_BINARY_DIR}/../cuda_impl)
include_directories(${PROJECT_BINARY_DIR}/../node_info/plugin)
include_directories(/usr/local/cuda-10.0/include)
include_directories(${PROJECT_BINARY_DIR}/../cub-1.8.0)

link_directories(/home/xj-zjd/TensorRT-7.0.0.11/lib)
link_directories(/usr/local/cuda-10.0/lib64)
link_directories(${PROJECT_BINARY_DIR}/../jsoncpp-00.11.0/build-shared/)
add_compile_options(-std=c++11 -w)
set(CUDA_NVCC_FLAGS "${CUDA_NVCC_FLAGS} -std=c++11 -w" )
file(GLOB CUDA_SRC_FILES ${PROJECT_BINARY_DIR}/../cuda_impl/*.cu)
file(GLOB EXAMPLE_FILES ${PROJECT_BINARY_DIR}/../example/*.cpp)
file(GLOB COMMON_FILES ${PROJECT_BINARY_DIR}/../*.cpp)
file(GLOB NODE_CREATE_FILES ${PROJECT_BINARY_DIR}/../node_create/*.cpp)
file(GLOB NODE_INFO_FILES ${PROJECT_BINARY_DIR}/../node_info/*.cpp)

cuda_add_library(tensorrtWrapper ${COMMON_FILES} ${NODE_CREATE_FILES} ${NODE_INFO_FILES} ${CUDA_SRC_FILES})

foreach(example_file IN LISTS EXAMPLE_FILES)
    get_filename_component(target_file ${example_file} NAME_WE)
    # cuda_add_executable(${target_file} ${example_file} ${COMMON_FILES} ${NODE_CREATE_FILES} ${NODE_INFO_FILES} ${CUDA_SRC_FILES})
    cuda_add_executable(${target_file} ${example_file})
    target_link_libraries(${target_file} tensorrtWrapper)
    target_link_libraries(${target_file} jsoncpp)
    target_link_libraries(${target_file} nvinfer)
    target_link_libraries(${target_file} cudart)
    target_link_libraries(${target_file} ${OpenCV_LIBS})
endforeach(example_file)
