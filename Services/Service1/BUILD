load("@pip_service1//:requirements.bzl", "requirement")



load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "Service1",
    srcs = ["src/handler.py", "src/src1_interface.py", "src/__init__.py",],
    visibility = ["//visibility:public"],
    deps = [requirement("numpy"),
    ]
)

py_test(
    name = "test_interface",
    srcs = ["test/test_interface.py"],
    python_version = "PY3",
    legacy_create_init = False,
    data = ["test/test_input_1.json"],
    imports=[ "..", "./src", "./test"],
    deps = [":Service1"],
)
