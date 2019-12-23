#include <string>
#include <pybind11/stl.h>
#include <torch/extension.h>
#include <vector>
#include <pybind11/stl_bind.h>
#include "RVO.h"
//using namespace std;
//using namespace torch;
using namespace RVO;

namespace py = pybind11;


int Blocks ();


PYBIND11_MAKE_OPAQUE(std::vector<Vector2>);

PYBIND11_MODULE(pyorca, m){
    m.def("Blocks", &Blocks);

    // py::class_<Pet>(m, "Pet")
    //    .def(py::init<const std::string &, int>())
    //    .def("set", (void (Pet::*)(int)) &Pet::set, "Set the pet's age")
    //    .def("set", (void (Pet::*)(const std::string &)) &Pet::set, "Set the pet's name");

    py::class_<RVOSimulator>(m, "RVOSim")
        .def(py::init<>())
        .def("setTimeStep", &RVOSimulator::setTimeStep)
        .def("setAgentDefaults", &RVOSimulator::setAgentDefaults)
        .def("addAgent", (size_t (RVOSimulator::*)(const Vector2 &)) &RVOSimulator::addAgent)
        .def("addObstacle", &RVOSimulator::addObstacle)
        .def("doStep", &RVOSimulator::doStep)
        .def("processObstacles", &RVOSimulator::processObstacles)
        .def("getNumAgents", &RVOSimulator::getNumAgents)
        .def("getGlobalTime", &RVOSimulator::getGlobalTime)
        .def("getAgentPosition", &RVOSimulator::getAgentPosition)
        .def("setAgentPrefVelocity", &RVOSimulator::setAgentPrefVelocity)
        .def("getAgentPrefVelocity", &RVOSimulator::getAgentPrefVelocity)
        ;

    py::class_<Vector2>(m, "Vector2")
        .def(py::init<float, float>())
        .def(py::init<>())
        .def(py::self + py::self)
        .def(py::self - py::self)
        .def(py::self * float())
        .def(float() * py::self)
        .def(py::self += py::self)
        .def("x", &Vector2::x)
        .def("y", &Vector2::y)
        ;

    m.def("absSq", &absSq);
    m.def("normalize", &normalize);

    py::bind_vector<std::vector<Vector2>>(m, "V_Vec2");
}
