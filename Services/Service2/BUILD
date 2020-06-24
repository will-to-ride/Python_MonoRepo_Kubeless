load("@pip_service2//:requirements.bzl", "requirement")



load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "Service2",
    srcs = ["src/handler.py", "src/src2_interface.py","src/main2.py", "src/__init__.py",],
    visibility = ["//visibility:public",],
    deps = [requirement("numpy"),
            requirement("pandas"),
            requirement("pytz"),
            requirement("python-dateutil"),
            "//Services/Service1:Service1",
    ]
)

py_binary(
    name = "main",
    srcs = [
      "src/main2.py",
    ],
    deps = [requirement("numpy"),
            requirement("pandas"),
            requirement("pytz"),
            requirement("python-dateutil"),
            ":Service2",
           ],
    imports = [
        "..", "./src",
    ],
    main = "src/main2.py",
)

py_test(
    name = "test_interface",
    srcs = ["test/test_interface.py"],
    python_version = "PY3",
    legacy_create_init = False,
    data = ["test/test_input_2.json"],
    imports=[ "..", "./src", "./test"],
    deps = [":Service2",
            "//Services/Service1:Service1"
    ],
)