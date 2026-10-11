from langgraph.graph import StateGraph, END

from src.state import CareerState

from src.agents.nodes import (
    resume_analysis_node,
    jd_analysis_node,
    gap_analysis_node,
    risk_level_node,
    improvement_node,
    final_report_node,
)

from src.agents.router import (
    route_by_risk,
)


def build_career_graph():

    graph = StateGraph(CareerState)

    # Nodes
    graph.add_node(
        "resume_analysis",
        resume_analysis_node,
    )

    graph.add_node(
        "jd_analysis",
        jd_analysis_node,
    )

    graph.add_node(
        "gap_analysis",
        gap_analysis_node,
    )

    graph.add_node(
        "risk_level",
        risk_level_node,
    )

    graph.add_node(
        "improvement",
        improvement_node,
    )

    graph.add_node(
        "final_report",
        final_report_node,
    )

    # Starting point
    graph.set_entry_point(
        "resume_analysis"
    )

    # Normal edges
    graph.add_edge(
        "resume_analysis",
        "jd_analysis",
    )

    graph.add_edge(
        "jd_analysis",
        "gap_analysis",
    )

    graph.add_edge(
        "gap_analysis",
        "risk_level",
    )

    # Conditional routing
    graph.add_conditional_edges(
        "risk_level",
        route_by_risk,
        {
            "improvement":
                "improvement",

            "final_report":
                "final_report",
        },
    )

    # Final paths
    graph.add_edge(
        "improvement",
        "final_report",
    )

    graph.add_edge(
        "final_report",
        END,
    )

    return graph.compile()