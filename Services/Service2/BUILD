load("@my_deps//:requirements.bzl", "requirement")



load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
  name = "handler",
  srcs = ["src/handler.py", "src/src2_interface.py"],
)

py_library(
    name = "handler_lib",
    srcs = ["src/handler.py", "src/src2_interface.py"],
    imports=["."],
    deps = [
    ]
)

py_test(
    name = "test_interface",
    srcs = ["test/test_interface.py"],
    python_version = "PY3",
    legacy_create_init = False,
    data = ["test/test_input_2.json"],
    imports=["./src", "./test"],
    deps = [":handler"],
)