rules_python_external_version = "{COMMIT_SHA}"

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_federation",
    url = "https://github.com/bazelbuild/bazel-federation/releases/download/0.0.1/bazel_federation-0.0.1.tar.gz",
    sha256 = "506dfbfd74ade486ac077113f48d16835fdf6e343e1d4741552b450cfc2efb53",
)

load("@bazel_federation//:repositories.bzl", "rules_python_deps", "rules_python")

rules_python()
load("@bazel_federation//setup:rules_python.bzl",  "rules_python_setup")
rules_python_setup(use_pip=True)

load("@rules_python//python:pip.bzl", "pip_import")

# Create a central repo that knows about the dependencies needed for
# requirements.txt.
pip_import(   # or pip3_import
   name = "pip_service1",
   requirements = "//Services/Service1:requirements.txt",
)

# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
load("@pip_service1//:requirements.bzl", service1_pip_install = "pip_install")
service1_pip_install()   

# Import pip dependencies of all our components.

pip_import(
    name = "pip_service2",
    requirements = "//Services/Service2:requirements.txt",
)
load("@pip_service2//:requirements.bzl", service2_pip_install = "pip_install")
service1_pip_install()