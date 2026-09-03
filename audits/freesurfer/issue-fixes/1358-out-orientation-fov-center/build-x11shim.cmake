# Build-environment shim (not part of the fix): the in-tree cmake/FindX11.cmake
# does not create the X11::X11 imported target that the system VTK 9.1 config
# references, so define it here right after project().
if(NOT TARGET X11::X11)
  add_library(X11::X11 INTERFACE IMPORTED)
  set_target_properties(X11::X11 PROPERTIES
    INTERFACE_LINK_LIBRARIES "/usr/lib/x86_64-linux-gnu/libX11.so"
    INTERFACE_INCLUDE_DIRECTORIES "/usr/include")
endif()
