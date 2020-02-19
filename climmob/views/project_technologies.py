from .classes import privateView
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..processes import (
    projectExists,
    projectTechnologyExists,
    searchTechnologies,
    searchTechnologiesInProject,
    addTechnologyProject,
    deleteTechnologyProject,
    AliasSearchTechnology,
    AliasSearchTechnologyInProject,
    AliasExtraSearchTechnologyInProject,
    AddAliasTechnology,
    deleteAliasTechnology,
    addTechAliasExtra,
    findTechAlias,
    numberOfCombinationsForTheProject,
    numberOfAliasesInTechnology,
    getAliasExtra,
)


class projectTecnologies_view(privateView):
    def processView(self):

        # self.needJS("prjtechnologies")
        # self.needJS("datatables")
        # self.needJS("icheck")
        # self.needCSS("icheck")
        # self.needCSS('datatables')

        projectid = self.request.matchdict["projectid"]

        if not projectExists(self.user.login, projectid, self.request):
            raise HTTPNotFound()
        else:
            if self.request.method == "POST":
                if "btn_save_technologies" in self.request.POST:
                    postdata = self.getPostDict()

                    if postdata["txt_technologies_included"] != "":

                        part = postdata["txt_technologies_included"][:-1].split(",")

                        for element in part:
                            attr = element.split("_")
                            if attr[2] == "new":
                                addTechnologyProject(
                                    self.user.login, projectid, attr[1], self.request
                                )
                    if postdata["txt_technologies_excluded"] != "":

                        part = postdata["txt_technologies_excluded"][:-1].split(",")

                        for element in part:
                            attr = element.split("_")
                            if attr[2] == "exists":
                                deleteTechnologyProject(
                                    self.user.login, projectid, attr[1], self.request
                                )

            return {
                "activeUser": self.user,
                "projectid": projectid,
                "TechnologiesUser": searchTechnologies(
                    self.user.login, projectid, self.request
                ),
                "TechnologiesInProject": searchTechnologiesInProject(
                    self.user.login, projectid, self.request
                ),
                "project_numcom": numberOfCombinationsForTheProject(
                    self.user.login, projectid, self.request
                ),
            }


class prjTechAliases_view(privateView):
    def processView(self):

        # self.needJS("prjtechaliases")
        # self.needJS("datatables")
        # self.needJS("icheck")
        # self.needCSS("icheck")
        # self.needCSS('datatables')

        error_summary = {}
        dataworking = {}
        projectid = self.request.matchdict["projectid"]
        technologyid = self.request.matchdict["tech_id"]

        if not projectTechnologyExists(
            self.user.login, projectid, technologyid, self.request
        ):
            raise HTTPNotFound()
        else:
            if self.request.method == "POST":
                if "btn_save_technologies_alias" in self.request.POST:
                    postdata = self.getPostDict()
                    if postdata["txt_technologies_included"] != "":

                        part = postdata["txt_technologies_included"][:-1].split(",")

                        for element in part:
                            attr = element.split("_")
                            if attr[2] == "new":
                                dataworking["user_name"] = self.user.login
                                dataworking["project_cod"] = projectid
                                dataworking["tech_id"] = technologyid
                                dataworking["alias_id"] = attr[1]

                                add, message = AddAliasTechnology(
                                    dataworking, self.request
                                )
                                if not add:
                                    error_summary = {"dberror": message}
                    if postdata["txt_technologies_excluded"] != "":
                        part = postdata["txt_technologies_excluded"][:-1].split(",")
                        for element in part:
                            attr = element.split("_")
                            # print "*************************88"
                            # print attr
                            # print "*************************88"
                            # if attr[2] == 'extra':
                            delete, message = deleteAliasTechnology(
                                self.user.login,
                                projectid,
                                technologyid,
                                attr[1],
                                self.request,
                            )
                            if not delete:
                                error_summary = {"dberror": message}

            return {
                "activeUser": self.user,
                "dataworking": dataworking,
                "error_summary": error_summary,
                "AliasTechnology": AliasSearchTechnology(
                    technologyid, self.user.login, projectid, self.request
                ),
                "AliasTechnologyInProject": AliasSearchTechnologyInProject(
                    technologyid, self.user.login, projectid, self.request
                ),
                "AliasExtraTechnologyInProject": AliasExtraSearchTechnologyInProject(
                    technologyid, self.user.login, projectid, self.request
                ),
                "projectid": projectid,
                "techid": technologyid,
                "project_numcom": numberOfCombinationsForTheProject(
                    self.user.login, projectid, self.request
                ),
                "count": numberOfAliasesInTechnology(
                    self.user.login, projectid, technologyid, self.request
                ),
            }


class prjTechAliasDelete_view(privateView):
    def processView(self):
        error_summary = {}
        projectid = self.request.matchdict["projectid"]
        technologyid = self.request.matchdict["tech_id"]
        aliasid = self.request.matchdict["alias_id"]

        if not projectTechnologyExists(
            self.user.login, projectid, technologyid, self.request
        ):
            raise HTTPNotFound()
        else:
            if self.request.method == "POST":
                if "btn_deleteAlias" in self.request.POST:
                    delete, message = deleteAliasTechnology(
                        self.user.login, projectid, technologyid, aliasid, self.request
                    )
                    if not delete:
                        error_summary = {"dberror": message}
                    else:
                        self.returnRawViewResult = True
                        return HTTPFound(
                            location=self.request.route_url(
                                "prjtechaliases",
                                projectid=projectid,
                                tech_id=technologyid,
                            )
                        )

        return {
            "activeUser": self.user,
            "error_summary": error_summary,
            "projectid": projectid,
            "tech_id": technologyid,
            "alias_id": aliasid,
            "data": getAliasExtra(
                technologyid, self.user.login, projectid, aliasid, self.request
            ),
        }


class prjTechAliasAdd_view(privateView):
    def processView(self):
        error_summary = {}
        dataworking = {}
        projectid = self.request.matchdict["projectid"]
        technologyid = self.request.matchdict["tech_id"]

        if not projectTechnologyExists(
            self.user.login, projectid, technologyid, self.request
        ):
            raise HTTPNotFound()
        else:
            if self.request.method == "POST":
                if "btn_add_alias" in self.request.POST:
                    tdata = self.getPostDict()
                    alias_name = tdata["txt_add_alias"]
                    if alias_name != "":
                        # add the object
                        dataworking["user_name"] = self.user.login
                        dataworking["project_cod"] = projectid
                        dataworking["tech_id"] = technologyid
                        dataworking["alias_name"] = alias_name
                        # verify that there is no
                        existAlias = findTechAlias(dataworking, self.request)
                        if existAlias == False:
                            # add the alias
                            added, message = addTechAliasExtra(
                                dataworking, self.request
                            )
                            if not added:
                                # capture the error
                                error_summary = {"dberror": message}
                            else:
                                # show success message
                                self.returnRawViewResult = True
                                return HTTPFound(
                                    location=self.request.route_url(
                                        "prjtechaliases",
                                        projectid=projectid,
                                        tech_id=technologyid,
                                    )
                                )
                        else:
                            # error
                            error_summary = {
                                "exists": self._(
                                    "This alias already exists in the technology"
                                )
                            }
                    else:
                        # error
                        error_summary = {
                            "nameempty": self._("The name of the alias cannot be empy")
                        }
        return {
            "activeUser": self.user,
            "error_summary": error_summary,
            "data": self.decodeDict(dataworking),
            "projectid": projectid,
            "tech_id": technologyid,
        }
