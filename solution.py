import os
import uuid

class VsSolution:
    config='''
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio 15
VisualStudioVersion = 15.0.28307.168
MinimumVisualStudioVersion = 10.0.40219.1
{}
Global
    GlobalSection(SolutionConfigurationPlatforms) = preSolution
        Debug|Any CPU = Debug|Any CPU
        Debug|Mixed Platforms = Debug|Mixed Platforms
        Debug|Win32 = Debug|Win32
        Release|Any CPU = Release|Any CPU
        Release|Mixed Platforms = Release|Mixed Platforms
        Release|Win32 = Release|Win32
    EndGlobalSection
    GlobalSection(ProjectConfigurationPlatforms) = postSolution
        {}
    EndGlobalSection
    GlobalSection(SolutionProperties) = preSolution
        HideSolutionNode = FALSE
    EndGlobalSection
    GlobalSection(ExtensibilityGlobals) = postSolution
        SolutionGuid = {{{}}}
    EndGlobalSection
EndGlobal'''

    platform='''
    {{{0}}}.Debug|Any CPU.ActiveCfg = Debug|Win32
    {{{0}}}.Debug|Any CPU.ActiveCfg = Debug|Win32
    {{{0}}}.Debug|Mixed Platforms.ActiveCfg = Debug|Win32
    {{{0}}}.Debug|Mixed Platforms.Build.0 = Debug|Win32
    {{{0}}}.Debug|Win32.ActiveCfg = Debug|Win32
    {{{0}}}.Debug|Win32.Build.0 = Debug|Win32
    {{{0}}}.Release|Any CPU.ActiveCfg = Release|Win32
    {{{0}}}.Release|Mixed Platforms.ActiveCfg = Release|Win32
    {{{0}}}.Release|Mixed Platforms.Build.0 = Release|Win32
    {{{0}}}.Release|Win32.ActiveCfg = Release|Win32
    {{{0}}}.Release|Win32.Build.0 = Release|Win32'''

    def __init__(self):
        self.uuid = uuid.uuid4();
        self.solution_guid = uuid.uuid4()
        self.projects = {}  # key 工程名，value 工程唯一标识

    def add_project(self, name, identify):
        self.projects[name] = identify

    def remove_project(self, name):
        assert isinstance(name, object)
        del self[name]

    def save2file(self):
        projects = ""
        config = ""
        for key in self.projects.keys():
            values = {"uuid": self.uuid, "project": key, "identify": self.projects[key]}
            item = "Project(\"{{{uuid}}}\") = \"{project}\", \"{project}\{project}.vcxproj\", \"{{{identify}}}\"\nEndProject"
            projects = "{0}{1}\n".format(projects, item.format(**values))

            config="{0}{1}".format(config, self.platform.format(self.projects[key]))

        buff = self.config.format(projects.strip(), config.strip(), self.solution_guid)
        print(buff)



