from conan import ConanFile
from conan.tools.cmake import CMakeToolchain

class PrometheusCpp(Conanfile):
    def build_requirements(self):
        self.build_requires("benchmark/1.7.1")
        self.build_requires("civetweb/1.15")        
        self.build_requires("libcurl/7.86.0")        
        self.build_requires("gtest/1.12.1")        
        self.build_requires("zlib/1.2.13")        

    def generate(self):
        tc = CMakeToolchain(self)
        #tc.variables["MYVAR"] = "MYVAR_VALUE"
        #tc.preprocessor_definitions["MYDEFINE"] = "MYDEF_VALUE"
        tc.generate()